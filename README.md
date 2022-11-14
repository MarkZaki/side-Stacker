# connect 4

one app in use and it is called the_game

## Installation

to install we have to options normal pip installation and docker installation:

with docker its easy just navigate to the root dir of the project and run the following:

```bash
docker compose up
```

for normal installation a venv is preferred so all you need to do is to make sure you have python 3.10 installed

clone this repostory and run the following

```bash
python -m venv venv
```

activate your venv

windows

```bash
cd venv/Scripts/
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
./activate
```

```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```

```bash
./activate
```

on mac or linux

```bash
source venv/bin/activate
```

finally run the following to install the requirements make sure you are in the project base dir

```bash
pip install -r requirments.txt
```

```bash
python manage.py runserver 127.0.0.1:8000
```

## usage and testing

you can test with these endpoints and they have descriptions of the fields as well if you need a data representation you can also refer to [the admin panel](http://127.0.0.1:8000/admin)

## storage

postgres and the DB name is "connect4"
if you wish to change the name please refre to the config dir in a file called settings.py line 100

## to Install Front end

first you have to run

```bash
npm install
```

to install packages.

then run

```bash
npm run dev
```

to compile the frontend code

then go to 127.0.0.1:8000 and everything should be working Correctly

## License

[by khaled yasser](kikokhaled.u@gmail.com)
