from flask import Flask, render_template, request, Response, redirect
import random
import pygame
import pyrebase
import winsound
import threading
import time

app = Flask(__name__)

score1 = 0
score2 = 0
last_question_time = None

config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "suhwa-mbc.firebaseapp.com",
    "databaseURL": "https://suhwa-mbc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "suhwa-mbc.appspot.com"
}

def reset_scores():
    global score1, score2
    score1 = 0
    score2 = 0

def reset_last_question_time():
    global last_question_time
    last_question_time = None

def start_timer():
    global last_question_time
    last_question_time = time.time()
    threading.Timer(60, reset_last_question_time).start()

def check_timeout():
    global last_question_time
    if last_question_time and time.time() - last_question_time > 60:
        reset_scores()

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

    check_timeout()

    global score1, score2

    if quiz == player1:
        pygame.mixer.init()
        pygame.mixer.music.load("player1.mp3")
        pygame.mixer.music.play()
        score1 += 1
        start_timer()
        return redirect("/main")

    elif quiz == player2:
        pygame.mixer.init()
        pygame.mixer.music.load("player2.mp3")
        pygame.mixer.music.play()
        score2 += 1
        start_timer()
        return redirect("/main")

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