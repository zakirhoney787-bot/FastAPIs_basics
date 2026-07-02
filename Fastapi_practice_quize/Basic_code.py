from fastapi import FastAPI ,HTTPException, Path
import json
from typing import Annotated

app = FastAPI()

#BASICS
@app.get('/')
def static_root():
    return {'Zakir':'good boy'}

#OR
@app.get('/hello/{name}')
def greetor(name : str= Path(..., openapi_examples={
                    "default_name ":{
                    "summary": "Standard Name",
                    "value": "ZAKIR SAHAB"}})
                    ):
    return f"hello {name.upper()}"

#FOR PRINTING DETAILS
@app.get('/items/{item_id}/{name}')
def read_item(item_id: int, name:str):
    return {'Item_id':item_id ,'Name': name }

