# MediTrack API

MediTrack is a patient medical records management API built using Python, FastAPI and SQLAlchemy.

I created this project to practice backend development, database operations and CRUD functionality.

## Technologies Used
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Features
- Register and manage patients.
- Add medical records for each patient.
- Store symptoms, diseases and prescriptions.
- View complete patient visit history.
- Update and delete patient records.

## API Documentation

After running the application, visit:

`http://127.0.0.1:8000/docs`

## Run Locally

```bash
git clone YOUR_REPOSITORY_URL
cd meditrack-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## What I Learned
- Building REST APIs with FastAPI.
- Database operations using SQLAlchemy.
- CRUD operations and database relationships.
- Request validation using Pydantic.

*This is a learning project developed using fictional patient data.*