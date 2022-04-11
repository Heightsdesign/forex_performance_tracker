Introduction:

Quren is an online forex performance tool for traders founded by your humble and gracious host, Paul-Henri ERIC.
The point of this application is to give forex traders (on any level) more insights on their performances, 
how many positive trades do you make per day ? What is your win/loss ratio ? What is the profit coming out of it ? ect...

The goal here is to answer those questions to provide you more insight.
The idea behind this project first came up after beginning my personal journey on forex trading.
I was trying to learn what traders do and that often comes with trading.
After several days of training a thought came up. The thought that, well, I've got a vague idea of what my performances are, 
but everybody can tell if whether they're winning or not, but can have I more precise indicators ? 
Some numbers that would be more than just a balance sheet saying "hey you've won or lost this much today"? 
Something giving me a better understanding or clues on what I might doing right or what I might be doing wrong.

So whether you've been trading for a little while or you're just starting your journey 
but you feel like having more clarity on you're actions could be helpful, you're at the right place !

Installation : 

1. Download zip file from repository

2. If you do not have python 3 installed you can download it from here https://www.python.org/

3. Install the requirements:
>>> pip install -r requirements

4. Download and setup your Postgresql database : https://www.postgresql.org/.
note : You will have to set your own credentials in the "DATABASES" section of the /fpt/settings.py file
note 2: If you do not wish to use postgresql you will have to modify 
the "DATABASES" section of the /fpt/settings.py file accordingly

5. /!\ Before launching the migrations commands, in the /live/forms.py and users/forms.py files 
change the choices=get_choices() to a list such as choices=[EURUSD, GBPUSD].
You can change them back to the get choices functions after the migrations are successful.

6.Navigate to the main project directory where the manage.py file is located (/fpt_project/)and run the commands
>>> python manage.py makemigrations
>>> python manage.py migrate

7. To start a local server, run the command :
>>> python manage.py runserver 

Useful specifications:

python version : 3.9.1
django version : 4.0.0
