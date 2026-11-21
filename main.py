from fastapi import FastAPI,Depends,HTTPException
from schemas import Create_Patient,Patient_info_response,Create_Med_Records,Med_Records_response
from sqlalchemy.orm import Session
from database import Base, SessionLocal,engine
import models


app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def Title():
    return {"message":"Patient Management System API"}

@app.post('/patient',response_model=Patient_info_response)
def create_patient(obj:Create_Patient,db:Session=Depends(get_db)):
    patient_info = models.patientinfo(name = obj.name,age=obj.age,gender=obj.gender,phone_number = obj.phone_number,address = obj.address,blood_group = obj.blood_group)
    print(patient_info)
    db.add(patient_info)
    db.commit()
    db.refresh(patient_info)
    return patient_info

@app.get('/info',response_model=list[Patient_info_response])
def get_all_patients(db:Session = Depends(get_db)):
    objs = db.query(models.patientinfo).all()
    if not objs:
        raise HTTPException(status_code=404,detail="no get all patient found")
    return objs

@app.get('/info/{id}',response_model=Patient_info_response)
def get_by_id(id:int,db:Session=Depends(get_db)):
    obj = db.query(models.patientinfo).filter(models.patientinfo.patient_id == id).first()
    if obj == None:
        raise HTTPException(status_code=404,detail='Patient detail not found')
    return obj

@app.patch('/info/{id}',response_model=Patient_info_response)
def update_detail(id:int,obj:Create_Patient,db:Session=Depends(get_db)):
    new_info = db.query(models.patientinfo).filter(models.patientinfo.patient_id == id).first()
    if new_info == None:
        raise HTTPException(status_code=404,detail="No id found to update")
    new_info.name = obj.name
    new_info.age = obj.age
    new_info.gender = obj.gender
    new_info.address = obj.address
    new_info.phone_number = obj.phone_number
    new_info.blood_group = obj.blood_group
    db.commit()
    db.refresh(new_info)
    return new_info
@app.delete('/info/{id}')
def delete_patient(id=int,db:Session=Depends(get_db)):
    patientno= db.query(models.patientinfo).filter(models.patientinfo.patient_id == id).first()
    if patientno == None:
        raise HTTPException(status_code=404,detail="No id found to delete")
    db.delete(patientno)
    db.commit()
    return {"message":"Patient info is deleted successfully"}


@app.post('/patient_record/{id}',response_model=Med_Records_response)
def add_patient_data(id:int,obj:Create_Med_Records,db:Session=Depends(get_db)):
    check_id = db.query(models.patientinfo).filter(models.patientinfo.patient_id==id).first()
    if check_id == None:
        raise HTTPException(status_code=404,detail="Patient id not found so you need to first register")
    patient_rec = models.medicalrecords(patient_id = id,symptoms=obj.symptoms,disease=obj.disease,prescription=obj.prescription)
    print(patient_rec)
    db.add(patient_rec)
    db.commit()
    db.refresh(patient_rec)
    return patient_rec

@app.get('/get_history_patient/{id}',response_model=list[Med_Records_response])
def get_history_patient(id:int,db:Session=Depends(get_db)):
    check_id = db.query(models.medicalrecords).filter(models.medicalrecords.patient_id == id).all()
    if not check_id:
            raise HTTPException(status_code=404,detail="No patient exist to get its history")
    return check_id
    
    

@app.get('/get_all_records',response_model=list[Med_Records_response])
def get_all_records(db:Session=Depends(get_db)):
    patient_info = db.query(models.medicalrecords).all()
    if not patient_info:
        raise HTTPException(status_code=404,detail='patients not found')
    return patient_info

@app.patch('/update_records/{rec_id}',response_model=Med_Records_response)
def update_records(rec_id : int,obj:Create_Med_Records,db:Session=Depends(get_db)):
    patient_rec = db.query(models.medicalrecords).filter(models.medicalrecords.record_id == rec_id).first()
    if patient_rec == None:
        raise HTTPException(status_code=404,detail="Cannot Update")
    patient_rec.symptoms = obj.symptoms
    patient_rec.disease = obj.disease
    patient_rec.prescription = obj.prescription
    db.commit()
    db.refresh(patient_rec)
    return patient_rec
@app.delete('/delete_rec/{id}')
def delete_rec(id:int,db:Session=Depends(get_db)):
    patient_rec = db.query(models.medicalrecords).filter(models.medicalrecords.record_id == id).first()
    if patient_rec == None:
        raise HTTPException(status_code=404,detail="Cannot Delete")
    db.delete(patient_rec)
    db.commit()
    return {"message":"patient record deleted successfully"}

    
@app.delete('/delete_all_records')
def delete_all_records(db:Session=Depends(get_db)):
    db.query(models.medicalrecords).delete()
    db.commit()
    return {"message":"all medical records deleted successfully"}
    






