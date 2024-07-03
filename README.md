# Knowli

# Overview

Knowli made for CS50 is a demo project of a webapp that I want to develop further in the future.
Main goal of Knowli is to allow young polish people to learn maths for free in an easy and engaging way.

# Distinctiveness and Complexity

My app is meant to be easy to navigate for young users, while hiding the complexity under the hood.
In my django project I created two apps: **learn** and **account**. First one is made to serve the main purpose of the site, learning, taking tests etc. Second one is made to serve as an authentication tool.

In settings I made some changes to better support the projects nationality, changing the language and timezone to polish. I also changed requirements to the password validation during registration, added email backend support to allow for password change in the console, email login authentication specified in authentication.py and made some other small tweaks.
I also included option for logging in with Google, but it won't work as expected, because only my email is permitted to log-in. It is more as a showcase of future developement possibilities and my abilities of setting that up in settings.py.

First lets talk about account app.I used django's build in login views to make process of working with data as secure as possible. It is used in addition to forms I created in account/forms.py to support the process of exchanging data between the server and users. It required me to make html templates in templates/registration/ supported by base.html to change the user interface from basic django styles to clean UI with styles stored in static/css/base.css. 
I created model Profile that is related as OneToOne with User model, that expands on the User and adds option to change the photo of the profile (in the future) and specify education level. Profile model is later registered in admin.py to make it easy to interact with using the panel.
In account I also created a UserRegistrationForm that:
    -checks for correct password
    -checks if passwords are the same
    -checks for correct, only once used email
I wrote authentication method to allow users to log in with their emails in authentication.py and allowed it to work in settings.
Then in static I have some messy CSS and in templates all of the .html.
My urls are straight forward here thanks to django.contrib.auth.

In learn app I created 3 models.
    -MathTest, that has a title, slug, to later use with urls, description and one of the levels
    -MathTask, that is connected to a MathTest. It has a question and between 2 to 4 answers, where only one is correct
    -Score, that connects to MathTest and User
Only form here is made to display questions, admin registers created models.
My views have three functions. First one renders index, second one lists all the tests in a level, that it gets from the template.

Third one works when taking the test. It checks if the test exists, fetches the object based on a slug, that it gets from the url and retrieves all tasks for this test.
It handles POST request, for submitting the test with the use of JS.
It than checs if there is a existing high score, and if its beaten, that it changes that to the new one.
It hanldes GET with the help of the form created earlier.
If the POST is sent, it renders a score page with a name of a test, current score and highest score.

My urls here are a little bit more complicated, as beside index, 'take_test' needs slug of a taken test and 'test_list' needs level of a test to display it in a correct category.
I made some CSS in static and templates for index and tests logic.
learn_base.html template uses JS to show avaliable courses after clicking "Kursy"
take_test.html template uses JS to mark only one answer in a question at the time and than send answers to the views POST.

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

4.
Go to Knowli\knowli

5. 
Type:
'python manage.py runserver_plus --cert-file cert.crt'
in your console.

6.
Go to 
https://127.0.0.1:8000/learn/ (for standard login)
or 
https://knowli.pl:8000/learn/ (if you want to check google login)


You should see /learn/ landing page with some text, in the top right you can se login/register button. 
The site is almost empty because of the requirement to log-in.
Click it, than  click "Założ konto!" to register.
Nazwa użytkownika = username
Hasło =  password
"Stopień nauki" allows users to pick a type of school they attend to and is ment to collect data about the users.

After registering you can click "zalogować" to log-in.
(If you want to, you can check the password reset option, using "Zresetuj hasło" at the bottom of log-in form)
Now you see two additional nav-bars at the top.
Click on "Kursy" to pick a course. Right now there is a different test in each one of them.

Let's click on the "Egzamin ósmoklasisty" and then "Liczby naturalne klasa 8".
You will get 3 questions.
Answer:
-a
-d
-c

You should see the score in Twój wynik: 2
and the highest score (Twój najwyższy wynik) of 2

Now click "Spróbuj jeszcze raz" as retake the test and don't click any answers.
You should see the score of 0 with a highest score of 2.

If you will you can check other test in Kursy > Matura or try to break the site.

