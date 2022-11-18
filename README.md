# side stacker game

This is essentially connect-four, but the pieces stack on either side of the board instead of bottom-up.
Two players see a board, which is a grid of 7 rows and 7 columns. They take turn adding pieces to a row, on one of the sides. The pieces stack on top of each other, and the game ends when there are no spaces left available, or when a player has four consecutive pieces on a diagonal, column, or row.


## Installation

to install we have to options normal pip installation and docker installation:

with docker its easy just navigate to the root dir of the project and run the following:

```bash
docker compose up
```

for normal installation a venv is preferred so all you need to do is to make sure you have python 3.10 installed

clone this repository and run the following in the base dir

```bash
python -m venv <venv_name>
```

activate your venv

#### windows

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


#### mac or linux

```bash
source venv/bin/activate
```

finally run the following to install the requirements make sure you are in the project base dir

```bash
pip install -r requirments.txt
```

```bash
python manage.py runserver
```

## usage and testing
for testing run the following command 

```bash
python manage.py test
```

result should look like 

```bash
......
----------------------------------------------------------------------
Ran 6 tests in 0.008s

OK
```

## storage

this project uses PostgreSQL for its DB because its utilizing JSONField
so make sure you have a running PostgreSQL server with 

create a DB 

add your DB information to the .env file
along with your secret please check example .env file

## to Install the Front end

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

## for more infor please check the DOC.MD file 
## License
[by khaled yasser](kikokhaled.u@gmail.com)
