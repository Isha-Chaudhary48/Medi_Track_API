from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from database import Base
class patientinfo(Base):
    __tablename__='patient_info'
    patient_id = Column(Integer,primary_key=True,index = True)
    name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    gender = Column(String)
    phone_number = Column(String,nullable=False)
    address = Column(String)
    blood_group = Column(String)

class medicalrecords(Base):
    __tablename__="medical_records"
    record_id =Column(Integer,primary_key=True,index = True)
    patient_id = Column(Integer,ForeignKey("patient_info.patient_id"),nullable=False)
    symptoms = Column(String)
    disease= Column(String)
    prescription=Column(String)



