from fastapi import FastAPI ,Path
import json
app=FastAPI()

#MARKING TO THE STUDENTS
def load_data():
    with open('Marks_std.json') as file:
        return json.load(file) 

data= load_data()

@app.get('/{student}')
def student_inf(student:str):
    for i in data:
        if student in i.values():
            avg=(i['marks']['math']+i['marks']['english']+i['marks']['science'])/3
            if avg>=60:
                result=True               
                comment='THIS GUY IS REALLY A HERO'
                return {
                        'Comment': comment,
                        'Data':i,
                        'Pass' :result
                            } 
            else:
                comment="THIS GUY IS TOTALY FOOLISH"   
                return {
                            'Comment': comment,
                            'Data':i,
                            'Pass' :False
                            }

