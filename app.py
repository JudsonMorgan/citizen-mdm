from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List, Optional

# Database connection parameters
DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "citizen_mdm"

# PostgreSQL connection URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI app
app = FastAPI()

# Pydantic model for response
class Citizen(BaseModel):
    citizen_id: int
    name: str
    dob: str
    health_status: str
    school_name: str

    class Config:
        orm_mode = True

# Function to get all citizens with pagination
def get_all_citizens(limit: int = 10, offset: int = 0):
    session = SessionLocal()
    query = text("SELECT * FROM merged_citizens LIMIT :limit OFFSET :offset")
    result = session.execute(query, {"limit": limit, "offset": offset}).fetchall()
    session.close()
    return result

# FastAPI route to get merged citizen data by citizen_id
@app.get("/citizens/{citizen_id}", response_model=Citizen)
def get_citizen(citizen_id: int):
    citizen = get_citizen_by_id(citizen_id)
    if citizen is None:
        raise HTTPException(status_code=404, detail="Citizen not found")
    
    return Citizen(
        citizen_id=citizen["citizen_id"],
        name=citizen["name"],
        dob=citizen["dob"],
        health_status=citizen["health_status"],
        school_name=citizen["school_name"]
    )

# FastAPI route to get all merged citizens with pagination
@app.get("/citizens", response_model=List[Citizen])
def list_citizens(limit: Optional[int] = Query(10, ge=1), offset: Optional[int] = Query(0, ge=0)):
    citizens = get_all_citizens(limit=limit, offset=offset)
    if not citizens:
        raise HTTPException(status_code=404, detail="No citizens found")
    
    return [Citizen(
        citizen_id=c["citizen_id"],
        name=c["name"],
        dob=c["dob"],
        health_status=c["health_status"],
        school_name=c["school_name"]
    ) for c in citizens]
