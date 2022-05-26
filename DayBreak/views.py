from django.shortcuts import render
import pyrebase

# # Import the functions you need from the SDKs you need
#     #import { initializeApp } from "firebase/app";
#     #import { getAnalytics } from "firebase/analytics";
# # TODO: Add SDKs for Firebase products that you want to use
# # [https://firebase.google.com/docs/web/setup#available-libraries](https://firebase.google.com/docs/web/setup#available-libraries)

# Your web app's Firebase configuration
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
config = {
    "apiKey": "AIzaSyC5Z2nGqsojfXtRvaHLOruyICxjQhveE9A",
    "authDomain": "daybreak-website.firebaseapp.com",
    "databaseURL": "https://daybreak-website-default-rtdb.firebaseio.com",
    "projectId": "daybreak-website",
    "storageBucket": "daybreak-website.appspot.com",
    "messagingSenderId": "1065770096905",
    "appId": "1:1065770096905:web:8e7baf36ce0e559399dbd8",
    "measurementId": "G-VNHQ70WCKE"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def home(request):
    #Marcus = database.child('Data').child('Name').child('1').get().val()
    #Chad = database.child('Data').child('Name').child('2').get().val()
    #Ilan = database.child('Data').child('Name').child('3').get().val()
    #Age = database.child('Data').child('Age').get().val()
    #Height = database.child('Data').child('Height').get().val()
    return render(request, "index.html") #{"Name": [Marcus, Chad, Ilan], "Age": Age, "Height": Height})

def postsign(request):
    pass

def form(request):
    return render(request, "form.html")
