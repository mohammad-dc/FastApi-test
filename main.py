from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'date': {'name': 'Mohammad'}}


@app.get('/about')
def about():
    return {'data': 'about page'}
