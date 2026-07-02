from fastapi import FastAPI
import json 

app=FastAPI()

def load_data():
    with open('Marks_std.json') as file:
        return json.load(file) 

data= load_data()
students_name=[]

@app.get('/student')
def student_inf():
    for i in data:
        students_name.append(i['student'])

    return {
        "These are all students ":
        students_name
        }
#RETURN ONE STUDENT ACCORDING TO HIS NAME 
@app.get('/student/{name}')
def searcher(name:str):
    for i in data:
        if name == i['student']:
            return  f'the student {name} found in records'
    else:
        return f"none student named {name}"