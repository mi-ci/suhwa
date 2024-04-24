import pyrebase

config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "project-id.firebaseapp.com",
    "databaseURL": "https://project-id.firebaseio.com",
    "storageBucket": "project-id.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Data you want to send
data = {"temperature": 22.5, "humidity": 60}

# Sending data to Firebase
db.child("sensor_data").push(data)

print("Data sent to Firebase")
