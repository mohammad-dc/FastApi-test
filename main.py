from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'date': {'name': 'Mohammad'}}


@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog/{id}')
def blog_details(id: int):
    return {'blog_id': id}

@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    # like http://localhost:8000/blog?limit=44&published=true
    if published:  
        return {'blog_list': f'{limit} publised blogs from DB'}
    else:
        return {'blog_list': f'{limit} blogs from DB'}


# for post requests
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}