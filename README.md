
# Django Studybud
---
## A functional practice project written with the DjangoREST framework
---
The thought of learning  **DjangoREST**  was a big challenge, so I got some simplified tutorials from TraversyMedia (https://www.youtube.com/@TraversyMedia).
This project is a community study platform just like Discord but for programmers, where users can create profiles, topics, and rooms. Comments and messages can be made in rooms.
***


## Features:
+ **User Authentication**: Users can register an account and login to the app.
+ **Room creation** : Users can create rooms and comment in rooms when logged in.
+ **User profile**: Users can update profile information and check other people's profiles.
+ **CRUD functionality**: Users can create, enter, and read messages in rooms, but only delete and update messages and rooms if they are the creators of such messages or rooms.
---

## How to run a project locally/clone


1. Clone the repo using git clone using git clone:
`git clone https://github.com/titobzzz/DjangoBase.git`
2. Create a virtual environment in the cloned repo directory with `python -m venv env`.
3. Activate the virtual environment using `env\Scripts\activate`
4. Install the dependencies `pip install -r requirements.txt`
5. Run `python manage.py migrate` to setup the database.
6. Run the server from the command line (in the project directory) with `python manage.py runserver`.
7. Lastly, navigate to http://127.0.0.1:8000/ in your web browser.


---
## Note
The majority of the branches were made to store the source codes with errors and bugs I encountered while building the project, such as **No Reverse match**,**value error at ..**  and many more :smiley: Thanks to @hephhay and @olaniyigeorge for the help.

## App preview 
### Rooms
[![Room](https://ibb.co/4RYygxx)]
### feeds
[![feeds](https://ibb.co/TWJTy4p)]