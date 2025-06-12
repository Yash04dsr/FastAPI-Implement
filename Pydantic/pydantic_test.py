from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

#Annotated is used to add metadata to the field like validation rules, descriptions, examples,default value etc.
#full syntac for annotated field is:
#field_name: Annotated[field_type, Field(..., title='...', description='...', examples=['...'], default=..., gt=..., lt=..., max_length=..., strict=..., etc.)]

#here strict=True means that the value must be of the specified type (float in this case) and cannot be coerced from another type (like int). pydantic ka chudap sambhal leta hai
#Field is used to add validation and metadata to the field (provides more control over the field)

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1
        max_anystr_length = 50
        use_enum_values = True
        extra = 'forbid'  # This will raise an error if extra fields are passed
        allow_mutation = True  # This allows the model to be mutable
        validate_assignment = True  # This will validate the data when assigning new values

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)