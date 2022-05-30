from asyncio.windows_events import NULL
from django.conf import settings
from django.forms import NullBooleanField
from django.shortcuts import render
from pyparsing import nullDebugAction
import pyrebase
from django.core import mail
#from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
    # {"Name": [Marcus, Chad, Ilan], "Age": Age, "Height": Height})
    return render(request, "index.html")


def postsignUp(request):
    # getting email from the html file
    email = request.POST.get('email')
    # generating a random key that will be used as the ID
    id = database.generate_key()
    # getting all users from the database through their perspective unique IDs
    all_users = database.child("users").get()
    # setting a holder boolean statement that will be used as a check later
    tempVal = True

    try:
        # this can be updated for better efficiency later on through other search methods
        # looping through all the users in the database through a for each loop
        for user in all_users.each():
            # Same email Validation
            if(user.val()["Email"] == email):
                # changes the boolean if the email is there already
                tempVal = False
                break
    finally:
        if tempVal:
            # Data that will be put into the database
            data = {
                "Email": email
            }
            # Data inputted into the database
            database.child("users").child(id).set(data)

            # Welcome email automation
            html_render = render_to_string('Welcome.html')
            text_content = strip_tags(html_render)

            # Variables for the email automation
            subject, from_email, to = "Welcome to DayBreak", settings.EMAIL_HOST_USER, email

            # send mail
            mail.send_mail(subject, text_content, from_email,
                           [to], html_message=html_render)

            # rendering selected html file
            return render(request, "form.html")

        else:
            return render(request, "form.html")


def form(request):
    return render(request, "form.html")


def Post(self, request, format=None):
    pass
