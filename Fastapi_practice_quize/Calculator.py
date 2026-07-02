
from fastapi import FastAPI ,HTTPException, Path
import json
from typing import Annotated

app = FastAPI()
@app.get('/add/{a}/{b}')
def addor(a:int,b:int):
    return f'Sum is : {a+b}'

@app.get('/sub/{a}/{b}')
def difference(a:int,b:int):
    c=a-b 
    if c<0:
        c*=-1
    return f"Difference : {c}"

#SQUARE 
@app.get('/square/{number}')
def squaring(number :int):
    return f"Number : {number}\nSquare : {number*number}"

#EVEN ODD VALIDATOR
@app.get('/evenodd/{num}')
def odd_even_checker(num:int):
    if num%2==0:
        return {
            "Number :{num} ",
            "Type : Even"
            }
    return {
        "Number :{num} ,"
        "Type : Odd"
        }