# Minnehack 2018
Our project for Minnehack 2018 focuses on the prevention of football injuries. We created a simple website for collecting football injury data and a machine learning model for predicting the number of games a player is expected to miss due to injury given their physical stats, position, training specifications, and injury history.

The project consists of a website with a form that football players can fill out to receive a prediction of their injury outlook. After a form submission, the data is added to the database on the server and is then fed into a deep neural network that predicts the number of games the player is expected to miss due to injury.

### Server running instructions
Windows: .virtualenv/Scripts/python manage.py "runserver"

Ubuntu: .virtualenv/bin/python3 manage.py "runserver"


Local website address is localhost:8000
