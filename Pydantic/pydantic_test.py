from pydantic import BaseModel

#pydantic model/class
class Patient (BaseModel):
    name:str
    age:int

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('object added')


# patient_info={'name':'Yash','age':100} #hona hi tha 
patient_info={'name':'Yash','age':'100'} # even this is string is converted to integer -> the power of pydantic 


#pydantic object which  is required to create the pydantic schema
patient1=Patient(**patient_info)

insert_patient(patient1)