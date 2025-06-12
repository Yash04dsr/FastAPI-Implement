from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    #IMPLEMenting field validator (like specifically checking some field ka part according to our use cases)

    #1. use that validate the field required
    @field_validator('email') #defining the method od validatio n using validator woth on which part is applicable
    @classmethod
    def email_validater(cls,value):
        valid_dom=['hdfc.com','icici.com']

        domain=value.split('@')[-1]
        if domain not in valid_dom:
            raise ValueError('Not a Valid Email with Valid Domain')
        
        return value
    
    # 2. Perform some transformations such as Capitalisation of the Name

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    """ 2 type of actions of filed validator 
      a. Before
      b. After
      
      this is one more parameter definied as mode in the field validator which tells us when the field validator should work 
      should it work before type coersion or after the coersion 

      # by default it is set as after (pahle type change hoga if required and then field validator start to work)

      Let see bye an example
    """
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        
        if 0<value<100:
            return value
        else:
            raise ValueError ('The age is not in defined range of 0 and 100')



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@hdfc.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)