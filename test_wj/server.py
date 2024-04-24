import pyrebase

config = {
    "apiKey": "AIzaSyAEiuF044Rb24Lhkh8xwYZf6MFlDkIleNk",
    "authDomain": "suhwa-mbc.firebaseapp.com",
    "databaseURL": "https://console.firebase.google.com/u/0/project/suhwa-mbc/database/suhwa-mbc-default-rtdb/data/~2F",
    "storageBucket": "suhwa-mbc.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Retrieve data from Firebase
sensor_data = db.child("suhwa_data").get()
for data in sensor_data.each():
    print(data.val())
