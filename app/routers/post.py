from fastapi import Depends,HTTPException,status,Response,APIRouter
from .. import schemas,models
from sqlalchemy.orm import Session,join as join_
from typing import List,Optional
from ..database import get_db
from .. import oauth2
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)



@router.get("/",response_model=List[schemas.PostOut])
def  get_posts(db: Session = Depends(get_db),current_user =Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    
    # cursor.execute("""SELECT * FROM posts""")
    # posts=cursor.fetchall()
    posts=db.query(models.Post).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results=db.query(models.Post,func.count(models.Vote.post_id).label("like")).join(
        models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(
        models.Post.id).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print(results)
    results = [{**row._mapping} for row in results]
    return results


@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id:int,db: Session = Depends(get_db),current_user =Depends(oauth2.get_current_user)):

    post=db.query(models.Post).filter(models.Post.id==id).first()

    results=db.query(models.Post,func.count(models.Vote.post_id).label("like")).join(
        models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(
        models.Post.id).first()
    
    results=results._mapping
    print(results)
    
    
    # cursor.execute("""SELECT * from posts WHERE id = %s""",str(id))
    # post=cursor.fetchone()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with {id} not found")
  
    if(post.owner_id!=current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Unauthorized person to perform this action')  
    return results

@router.delete("/{id}",)
def delete_post(id:int,db: Session = Depends(get_db),current_user =Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts where id=%s RETURNING *""",str(id))
    # post=cursor.fetchone()
    # conn.commit()
    post=db.query(models.Post).filter(models.Post.id==id);
    
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id :{id} not found")
    delete_post=post.first()
    #if delete_post.owner_id!=oauth2.get_current_user.id:
    if delete_post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Unauthorized person to perform this action')
    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.put("/{id}",response_model=schemas.Post )
def update_post(id:int,post:schemas.PostCreate,db: Session = Depends(get_db),current_user =Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title=%s,content=%s,published=%s
    #                WHERE id =%s RETURNING * """,(post.title,post.content,post.published,str(id)))
    # post=cursor.fetchone()
    # conn.commit();  
    post_query=db.query(models.Post).filter(models.Post.id==id)
    check=post_query.first()
    if check==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id :{id} not found")
    
    if check.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Unauthorized person to perform this action')

    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db),current_user =Depends(oauth2.get_current_user)):
    
    
    post=post.dict()
    #post['owner_id']=current_user.id
    
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES 
    #                (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published)) 
    # new_post=cursor.fetchone()
    # conn.commit()
    
    #new_post=models.Post(**post)
    new_post=models.Post(owner_id=current_user.id,**post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post