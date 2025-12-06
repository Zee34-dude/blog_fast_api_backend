from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI() #instance

@app.get('/blog') # path decorator
def index(limit:int=10,published:bool=False,sort: Optional[str]=None): # function
    # only get 10 published blogs
    
    if published:
     return {'data':f' {limit} blog published  '}
    else:
     return  {'data':f' {limit} blog list '}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def about(id:int):
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id:int,limit=10  ):
    comments=[
        {"id":1, "comment":'yeah'},
        {"id":2, "comment":'cmoe'},
        {"id":3, "comment":'gfhsj'}
        
    ]
    for comment in comments:
        if id == comment['id']:
            return {"comment": comment['comment']}
    
      # If no comment found, return the id or message
    return {"message": f"No comment found for id {id}"}

class Blog (BaseModel):
    title: str
    body: str
    published: Optional[bool]
 
@app.post('/blog')
def create_blog(request:Blog):
    return {'data':"blog created"}


# if __name__=="__main__":
#     uvicorn.run(app, host='127.0.0.1',port=9000)
