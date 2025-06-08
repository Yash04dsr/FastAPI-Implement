from fastapi import FastAPI

app = FastAPI() #Create an instance of FastAPI


#Survers se data lena chahte ho -> get request
#Survers pe data bhejna chahte ho -> post request

@app.get("/") #Define a route for the root URL
def ji():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return{"message":"Teri Ma ki Jay"} #Define a route for the /hello URL