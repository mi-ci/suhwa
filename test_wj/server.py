import pyrebase

config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "project-id.firebaseapp.com",
    "databaseURL": "https://project-id.firebaseio.com",
    "storageBucket": "project-id.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Retrieve data from Firebase
sensor_data = db.child("suhwa_data").get()
for data in sensor_data.each():
    print(data.val())
