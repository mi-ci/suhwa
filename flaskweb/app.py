from flask import Flask, render_template,request,Response, render_template_string
import random
import pygame
import pyrebase
import time
import winsound


score1=0
score2=0
config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "suhwa-mbc.firebaseapp.com",
    "databaseURL": "https://suhwa-mbc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "suhwa-mbc.appspot.com"
}


app=Flask(__name__)

@app.route("/")
def intro():
  return render_template("intro.html")


@app.route("/main")
def main():
  firebase = pyrebase.initialize_app(config)
  db = firebase.database()

  # Retrieve data from Firebase
  player1_data = db.child("suhwa_data").get()
  player2_data = db.child("suhwa_data2").get()




  quizlist=["화장실", "가위","무지개","인삼","산","여자","가끔","열아홉","리모컨","싫다"]
  quiz = random.choice(quizlist)
  
 


  player1 = player1_data[-1].val()
  player2 = player2_data[-1].val()

  global score1
  global score2

  if quiz == player1 :
    result1 = "정답입니다"
    pygame.mixer.init()
    pygame.mixer.music.load("player1.mp3")
    pygame.mixer.music.play()
    score1=score1+1
    return render_template("main.html")

  else:
    result1="땡!"


  if quiz == player2 :
    result2 = "정답입니다"
    pygame.mixer.init()
    pygame.mixer.music.load("player2.mp3")
    pygame.mixer.music.play()
    score2=score2+1  
  
  else:
    result2="땡!"

  if quiz!=player1 and quiz!=player2 :
    winsound.Beep(370,500)


  return render_template("main.html", value1=result1, value2=score1, value3=score2, value4=player1, value5=player2, value6=quiz, value7=result2)
  
# 화면송출
@app.route('/video_feed', methods=['POST'])
def video_feed():
    frame = request.files['frame'].read()
    # Storing the frame in a global variable is typically not a good practice and can lead to race conditions.
    # Here it's done just for demonstration; consider using better state management or streaming directly.
    global last_frame
    last_frame = frame
    return Response("Frame received", status=200)

@app.route('/video')
def index():
    # Continuously reload the image to display the video stream
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Video Stream</title>
    </head>
    <body>
        <h1>Video Stream from Raspberry Pi</h1>
        <img src="/current_frame" alt="Video stream" id="videoframe">
        <script>
            var img = document.getElementById('videoframe');
            setInterval(function(){
                img.src = "/current_frame?" + new Date().getTime();
            }, 100); // Reloads the image every 100 milliseconds
        </script>
    </body>
    </html>
    ''')

@app.route('/current_frame')
def current_frame():
    global last_frame
    return Response(last_frame, mimetype='image/jpeg')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, threaded=True)
  