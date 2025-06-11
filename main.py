from fastapi import FastAPI,Path,HTTPException,Query
import json

#Reading the JSON file
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


app = FastAPI() #Create an instance of FastAPI

"""Info:::
#Survers se data lena chahte ho -> get request
#Survers pe data bhejna chahte ho -> post request """

@app.get("/") #Define a route for the root URL
def ji():
    return {"message": "A patient management system for doctors"} #Return a welcome message

@app.get("/about")
def about():
    return{"message":"A fully functional api to manage patients records"} #Define a route for the /hello URL

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patient(patient_id:str=Path(...,description="ID of the Required Patient from DB ",example="P001")):
    data=load_data()
    if (patient_id in data):
        return data[patient_id]
    #return {"error":"The patient with this ID Does not exist"} -this was leading to 200 responce message which not good
    raise HTTPException(status_code=404, detail="patiend not found")

    
#  ##using query parameteres in the game:   
# @app.get("/sort")
# def sort_patients(sort_by:str=Query(...,description='Sort the patients by weight/height/bmi'),order:str=Query('asc',decimal_places='Select the oder in which you want the sorted list (asc/des)')):
    
#     #manage exceptions first both the input parameter ke liye
#     valid_field=['height','weight','bmi']
#     if sort_by not in valid_field:
#         raise HTTPException(status_code=400,detail=f'The selection of sort is not from {valid_field}')
    
#     if order not in ['asc','des']:
#         raise HTTPException(status_code=400,detail="The order selection is not from asc/des")
    
#     #back to working code

#     data=load_data()

#     # if order is asc:
#     #     order_value=False
#     # else:
#     #     order_value=True

#     order_value = True if order == 'des' else  False
 
#     # writting the function for sortted data 
#     sorted_Data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=order_value)

#     return sorted_Data

##using query parameteres in the game:   
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):
     
    #manage exceptions first both the input parameter ke liye
    valid_fields = ['height', 'weight', 'bmi']
 
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
     #back to working code
    data = load_data()

    sort_order = True if order=='desc' else False
 # writting the function for sortted data 
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data

    





