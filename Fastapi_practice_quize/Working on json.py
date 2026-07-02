from fastapi import FastAPI ,HTTPException, Path
import json
from typing import Annotated

app = FastAPI()

#PATIENT DATA ACCESSOR
def load_data():
    with open('Data/Patient_data.json','r') as f:
        data=json.load(f)
        return data
    
@app.get('/view/{patient_id}')
def view(patient_id :str=Path(..., title='Enter the ID of patient ' , examples=["p1"]) ):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")