from fastapi import FastAPI, Depends
from pydantic import BaseModel
import models , schemas
from DataBase.database import engine, SessionLocal
from sqlalchemy.orm.session  import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blogs")
def create(request: schemas.Blog, db: Session= Depends(get_db) ):
    new_blog= models.Blog(title= request.title, description=request.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
