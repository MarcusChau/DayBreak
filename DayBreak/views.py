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
    email = request.POST.get('email')
    id = database.generate_key()
    all_users = database.child("users").get()
    tempVal = True
    try:
        for user in all_users.each():
            if(user.val()["Email"] == email):
                tempVal = False
                break
    finally:
        if tempVal:
            #id = str(email).split('@')[0]
            data = {
                "Email": email
            }
            database.child("users").child(id).set(data)

            # Welcome email
            html_render = render_to_string('Welcome.html')
            text_content = strip_tags(html_render)
            # email = EmailMultiAlternatives(
            #    "Welcome",
            #    text_content,
            #    settings.EMAIL_HOST_USER,
            #    [email]
            # )
            subject, from_email, to = "Welcome to DayBreak", settings.EMAIL_HOST_USER, email
            #email.attach_alternative(html_render, "text/html")
            # email.send()
            mail.send_mail(subject, text_content, from_email,
                           [to], html_message=html_render)

            return render(request, "form.html")

        else:
            return render(request, "form.html")


def form(request):
    return render(request, "form.html")


def Post(self, request, format=None):
    pass
