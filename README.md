# Knowli

# Overview

Knowli made for CS50 is a demo project of a webapp that i want to develop in the future.
Main goal of Knowli is to allow young polish people to learn maths in a free, easy and engaging way.

# Distinctiveness and Complexity

My app is meant to be easy to navigate for young users, while hiding the complexity under the hood.
In my django project I created two apps: **learn** and **account**. First one is made to serve the main utilities of the site, such as learning, taking tests ets. Second one is made to serve as an authentication tool.

In settings I made some changes to better support the projects nationality, changing the language and timezone to polish. I also changed requirements to the password validation during registration, added email backend support to allow for password change in the console, email login authentication specified in authentication.py and made some other small tweaks.
I also included option for logging in with Google, but it won't work as expected, because only my email is permitted to log-in. It is more as a showcase of future developement possibilities and my abilities of setting that up in settings.py.

I used django's build in login views to make process of working with data as secure as possible. It is used in addition to forms I created in account/forms.py to support the process of exchanging data between the server and users. It required me to make html templates in templates/registration/ supported by base.html to change the user interface from basic django styles to clean UI stored in static/css/base.css. 
I created model Profile that is related as OneToOne with user model, that expands on the User and adds option to change the photo of the profile(thanks to Pillow) and specify education level.


# How to run

1.
Add to the file hosts in C:\Windows\System32\Drivers\etc(PC) or /etc/host(MAC) this line:
127.0.0.1 knowli.pl
[host conf.](image.png)

2.
Create and open a python venv

3.
Install requirements.txt by typing in console:
'pip install -r requirements.txt'