from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def static_root():
    return {'Zakir':'good boy'}

@app.get('/items/{item_id}/{name}')
def read_item(item_id: int, name:str):
    return {'Item_id':item_id ,'Name': name }
    
@app.get('/add/{a}/{b}')
def addor(a:int,b:int):
    return f'Sum is : {a+b}'

@app.get('/sub/{a}/{b}')
def difference(a:int,b:int):
    c=a-b 
    if c<0:
        c*=-1
    return f"Difference : {c}" 
    
@app.get('/profile/{name}/{id}/{cls}')
def profile(name:str , id:int , cls:str):
    return f"Name : {name},\nid : {id},\nclass : {cls}"

