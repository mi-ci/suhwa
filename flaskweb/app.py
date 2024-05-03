from flask import Flask, render_template, request, Response, redirect, jsonify, send_file
import random
import pyrebase
import mediapipe as mp
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import io
import pymysql
global score1, score2

score1 = 0
score2 = 0

app = Flask(__name__)


config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "suhwa-mbc.firebaseapp.com",
    "databaseURL": "https://suhwa-mbc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "suhwa-mbc.appspot.com"
}
last_frame = None
last_frame2 = None
model = None
actions = ['bathroom', 'scissors', 'rainbow', 'ginseng', 'mountain', 'girl', 'sometimes', 'nineteen', 'remote', 'reject']
def load_resources():
    global model
    model = load_model('best.keras')

    # MediaPipe hands model
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    return mp_drawing, hands, mp_hands

mp_drawing, hands, mp_hands = load_resources()

global seq, action_seq, seq_length, firebase, db
seq = []
action_seq = []
seq_length = 30
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/words")
def words():  
    return render_template("words.html")   

@app.route("/help")
def help():  
    return render_template("help.html")     

@app.route("/main")
def main():
    quizlist = ['bathroom', 'scissors', 'rainbow', 'ginseng', 'mountain', 'girl', 'sometimes', 'nineteen', 'remote', 'reject']
    global quiz
    quiz = random.choice(quizlist)
    return render_template("main.html", value2=score1, value3=score2, value6=quiz)

# =========================================여기서부터 정답비교==================================
@app.route("/check_answer", methods=["POST"])
def check_answer():
    global score1, score2, quiz
    player1_data = db.child("suhwa_data").get()
    player1 = player1_data[-1].val()
    player2_data = db.child("suhwa_data2").get()
    player2 = player2_data[-1].val()
    if quiz == player1:
        score1 += 1
    if quiz == player2:
        score2 += 1
    return jsonify({"score1": score1, "score2": score2, "quiz": quiz, "player1" : player1, "player2" : player2})


# =========================================여기서부터 비디오==================================

@app.route('/video_feed', methods=['POST'])
def video_feed():
    global last_frame

    img_bytes = request.files['frame'].read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 4))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

            # Compute angles between joints
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3] # Child joint
            v = v2 - v1 # [20, 3]
            # Normalize v
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # Get angle using arcos of dot product
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

            angle = np.degrees(angle) # Convert radian to degree

            d = np.concatenate([joint.flatten(), angle])

            seq.append(d)

            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

            if len(seq) < seq_length:
                continue

            input_data = np.expand_dims(np.array(seq[-seq_length:], dtype=np.float32), axis=0)

            y_pred = model.predict(input_data, verbose=0).squeeze()

            i_pred = int(np.argmax(y_pred))
            conf = y_pred[i_pred]

            if conf < 0.5:
                continue

            action = actions[i_pred]
            action_seq.append(action)

            if len(action_seq) < 3:
                continue

            # this_action = ''
            this_action = action
            # if action_seq[-1] == action_seq[-2] == action_seq[-3]:
            #     this_action = action
            if this_action != '' :
                db.child("suhwa_data").push(this_action)
                print("Data Sent", this_action)

            cv2.putText(img, f'{this_action.upper()}', org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)
    last_frame = img
    return Response("Frame received", status=200)

@app.route('/video_feed2', methods=['POST'])
def video_feed2():
    frame = request.files['frame'].read()
    global last_frame2
    last_frame2 = frame
    return Response("Frame received", status=200)

@app.route('/current_frame')
def current_frame():
    _, buffer = cv2.imencode('.jpg', last_frame)
    return send_file(io.BytesIO(buffer), mimetype='image/jpeg')

@app.route('/current_frame2')
def current_frame2():
    global last_frame2
    return Response(last_frame2, mimetype='image/jpeg')

# =========================================여기서부터 게시판==================================

@app.route('/qna')
def qna():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password='1234', db='project', charset='utf8')
    cur = conn.cursor()
    cur.execute("select * from qna order by no desc")
    data = cur.fetchall()
    print(type(data))
    conn.commit()
    conn.close()
    return render_template("qna.html", rows=data)

@app.route('/content', methods=['GET'])
def content():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password='1234', db='project', charset='utf8')
    cur = conn.cursor()
    id = request.args.get('id')
    cur.execute(f"select * from qna where no={id}")
    data = cur.fetchall()
    print(type(data))
    conn.commit()
    conn.close()
    return render_template("content.html", content=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
