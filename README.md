
# how to set up Virtual  enviornemnt in project:

source venv/bin/activate 

# How to run app using Uvicorn
uvicorn app.main:app --reload

# Why we use Schame
To set boundaries for front end. We will use pydantic library in that project

# with out using Scheme or pydantic lib how things will work, Pydantic provide base model to parse.

body is fastapi libraray get body from postman and convert into dict
def create_posts(payload:dict =Body(...)):

# Order of ROute (posts/id) or post(posts/lastest) really matter. try to focus on that
most commonly get(posts/id)

# Http Execption
We shouls use proper Http exception with the help of https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

# bad way and good way to raise Exception
    Bad way:

    response.status_code=status.HTTP_404_NOT_FOUND
    return {"Message:":f"Post with {id} not found"}

    Good way:

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} not found")

# DBMS(Database management system )
We dont interact with database directly , we use DBMS
For example: SQL, Mongo etc

# how to open PostgreSql in linux 
srevice postgresql(status, start)
sudo su - postgres

# command to make connection
 psql -h localhost -p 5432 -U muhammad -d test


the we can type command to play with database.

# URL will change in Enviornemnt put in Varaible 
 
# put token in enviornemnt vaiable  using this command Open Tests an write below command
(pm.eviornment.set("JWT".pm.response.json().access_token)

acess token is get from response variable for login

# ALembic 

1. PIP Install Alembic (Initialize the Alembic in project just like git)
2.alembic init (directory name) -> this will create folder and alembic.ini file 
3. We will play with almebic folder inside there is (env.py) file that is main file.
4. Alembic works with models , we will make sure that it will have connection with base

# Errors:
Address already in use - FastAPI (sudo lsof -t -i tcp:8000 | xargs kill -9)


