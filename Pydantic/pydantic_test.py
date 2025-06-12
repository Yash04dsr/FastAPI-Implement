from pydantic import BaseModel
from typing import List,Dict,Optional #(jis inpout ko optional karna tha)

#pydantic model/class
class Patient (BaseModel):
    name:str
    age:int
    weight:float
    allergies:Optional[List[str]]
    contact_details:dict[str,str]

def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('object added')


patient_info={'name':'Yash','age':100,'weight':78,'allergies':['abc','pqr'],'contact_details':{'email':'abc@c.com','contact':'123456'}} #hona hi tha 
# patient_info={'name':'Yash','age':'100',} # even this is string is converted to integer -> the power of pydantic 


#pydantic object which  is required to create the pydantic schema
patient1=Patient(**patient_info)

insert_patient(patient1)