from flask import Flask, render_template, request, Response, render_template_string, redirect
import random
import pygame
import pyrebase
import winsound
import webbrowser
import time


score1 = 0
score2 = 0
config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "suhwa-mbc.firebaseapp.com",
    "databaseURL": "https://suhwa-mbc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "suhwa-mbc.appspot.com"
}

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/main")
def main():
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    player1_data = db.child("suhwa_data").get()
    player2_data = db.child("suhwa_data2").get()

    quizlist = ['bathroom', 'scissors', 'rainbow', 'ginseng', 'mountain', 'girl', 'sometimes', 'nineteen', 'remote', 'reject']
    quiz = random.choice(quizlist)

    player1 = player1_data[-1].val() if player1_data else ""
    player2 = player2_data[-1].val() if player2_data else ""

    global score1, score2

    if quiz == player1:
        pygame.mixer.init()
        pygame.mixer.music.load("player1.mp3")
        pygame.mixer.music.play()
        score1 += 1
        

        
    
    elif quiz == player2:
        pygame.mixer.init()
        pygame.mixer.music.load("player2.mp3")
        pygame.mixer.music.play()
        score2 += 1
        
    
    if quiz != player1 and quiz != player2:
        winsound.Beep(370, 500)

    if quiz == player1 or quiz == player2:
        return redirect("localhost:5000/main")
        




    return render_template("main.html", value2=score1, value3=score2, value4=player1, value5=player2, value6=quiz)





@app.route('/video_feed', methods=['POST'])
def video_feed():
    frame = request.files['frame'].read()
    global last_frame
    last_frame = frame
    return Response("Frame received", status=200)

@app.route('/video_feed2', methods=['POST'])
def video_feed2():
    frame = request.files['frame'].read()
    global last_frame2
    last_frame2 = frame
    return Response("Frame received", status=200)

# @app.route('/video')
# def index():
#     return render_template_string('''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Video Stream</title>
#     </head>
#     <body>
#         <h1>Video Stream from Raspberry Pi</h1>
#         <div id="timer"></div>
#         <img src="/current_frame" alt="Video stream" id="videoframe">
#         <script>
#             var img = document.getElementById('videoframe');
#             setInterval(function(){
#                 img.src = "/current_frame?" + new Date().getTime();
#             }, 100); // Reloads the image every 100 milliseconds
#         </script>
#     </body>
#     </html>
#     ''')

@app.route('/current_frame')
def current_frame():
    global last_frame
    return Response(last_frame, mimetype='image/jpeg')
@app.route('/current_frame2')
def current_frame2():
    global last_frame2
    return Response(last_frame2, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)