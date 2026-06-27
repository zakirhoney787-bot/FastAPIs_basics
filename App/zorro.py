from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

#BASICS
@app.get('/')
def static_root():
    return {'Zakir':'good boy'}

@app.get('/items/{item_id}/{name}')
def read_item(item_id: int, name:str):
    return {'Item_id':item_id ,'Name': name }

#CALCULATOR 
@app.get('/add/{a}/{b}')
def addor(a:int,b:int):
    return f'Sum is : {a+b}'

@app.get('/sub/{a}/{b}')
def difference(a:int,b:int):
    c=a-b 
    if c<0:
        c*=-1
    return f"Difference : {c}" 

#PROFILE VIEWER  
# @app.get('/profile/{name}/{id}/{cls}')
# def profile(name:str= Path(max_length=50, title="User Name",examples=["JohnDoe"]) ,
#             id :int=Path(ge=1, title="User ID") ,
#             cls:str=Path(title="Class Code") ):
#     return f"Name : {name},\nid : {id},\nclass : {cls}"

#PATIENT DATA ACCESSOR
BASE_DIR = Path(__file__).parent

def load_data():
    file_path = BASE_DIR / "Patient_data.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data=json.load(f)
        return data
    
@app.get('/view/{patient_id}')
def view():
    data = load_data()

    if id in data:
        return data['patient_id']
    return {'Error' :"The id doesn't found  "}