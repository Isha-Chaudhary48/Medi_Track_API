from pydantic import BaseModel,ConfigDict

class Create_Patient(BaseModel):
        name:str
        age :int
        gender:str
        phone_number: str
        address :str
        blood_group:str

class Patient_info_response(Create_Patient):
        patient_id : int
        model_config = ConfigDict(
                from_attributes = True
        )

    
class Create_Med_Records(BaseModel):
        symptoms :str
        disease:str
        prescription:str

class Med_Records_response(Create_Med_Records):
        record_id:int
        patient_id : int
        model_config=ConfigDict(
                from_attributes=True
        )