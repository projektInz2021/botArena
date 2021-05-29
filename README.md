# botArena - battling bots webapp
University group project. Web application where you can create your own bot, battle with other bots and become AI warriors master!

## Table of contents
* [Demo](#demo)
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## Demo
You can find working demo at link (#tbd)

## General info
Use botArena API and our in-app editor to program your bot's behaviour and let it be the winner of the turn-based, Tron-alike game! Send your script and start competing with other user's bots. Analyse battles, improve and become a leader of botArena!

## Technologies
Project is created with:
* AWS Web Services
* Flask
* Vue.js (Vue Material Dashboard)
	
## Setup
Setup information (#tbd)
### Frontend setup
To run frontend application locally:
* Clone therepository
* Change directory to _frontend_ using
```
cd frontend
```
*  Install dependencies
```
npm install
```
* Run the local development server
```
npm run dev
```
### Backend setup
To run backend application locally:
* Clone therepository
* Change directory to _botArena_ using
```
cd botArena
```
*  Install dependencies
```
pip install Flask Flask-Login Flask-Cors passlib Flask-Sqlalchemy
```
* Initialize and run migrations
```
python manage.py db init
python manage.py db upgrade
```
* Run app
```
python app.py
```
For more information and UI kit documentation visit https://demos.creative-tim.com/vue-material-dashboard/documentation/ 
