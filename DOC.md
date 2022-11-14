# notes and documentation of this app

the_game directory  is where the magic happens  

## Installation

covered in the readme.md file 

## load testing 
load testing was done using locust.py the reports are in the root directory of this porject under the names
### "connect4 load test report.HTML" 
and 
### "connect4 load test report.csv"

you can also rerun the test but navigating to the root dir of the project and 

```bash
locust -f locust.py --host http://127.0.0.1:8080/ --users 100 --spawn-rate 50
```
## function 




## storage

I have chosen Postgres because i am using a Json field

## notes 
i used function based views  because it gives me more control and can show you my work better 

you will need a .env file which is provided via email

## License
[by khaled yasser](kikokhaled.u@gmail.com)