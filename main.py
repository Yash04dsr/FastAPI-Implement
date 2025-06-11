from fastapi import FastAPI
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

    
    





