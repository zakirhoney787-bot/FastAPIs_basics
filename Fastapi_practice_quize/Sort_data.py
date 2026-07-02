from fastapi import FastAPI , HTTPException
from typing import Annotated 
import json 
app=FastAPI()


def load_data():
    with open('Data/Patient_data.json','r') as f:
        data=json.load(f)
        return data
    
data=load_data()

@app.get('patients/{sort_by}/{order}')
def data_sorter(sort_by : str, order :str):

    fields=['number']

    if order not in fields:
        raise HTTPException( status_code=404, detail='this Order is not available !')
    
    sort_order = True if order == 'desc' else False
        

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
