from fastapi import APIRouter, Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas,models,utilis,oauth2
router=APIRouter(
    tags=['AUthentication']

)

@router.post('/login',response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
   
#def login(user_credentials:schemas.UserLogin,db: Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'invalid credentials')
    if not utilis.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'invalid credentials')
    acces_token=oauth2.create_access_token(data={"user_id":user.id})
    #create a token and return 
    return{"access_token" : acces_token,"token_type":"bearer"}
