from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from calculate import calculate_raise_bonus
from supabase import create_client
import os
from dotenv import load_dotenv
import traceback

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmployeeData(BaseModel):
    employeeId: str
    currentSalary: float
    yearsExperience: float
    performanceScore: float
    jobRole: str
    location: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AppexNow Flex Backend!"}

@app.post("/calculate")
async def calculate(data: EmployeeData):
    try:
        # Calculate raise and bonus
        result = calculate_raise_bonus(data)
        
        # Insert into database
        response = supabase.table("salary_records").insert({
            "employee_id": data.employeeId,
            "current_salary": data.currentSalary,
            "years_experience": data.yearsExperience,
            "performance_score": data.performanceScore,
            "job_role": data.jobRole,
            "location": data.location,
            "raise_amount": result["raiseAmount"],
            "bonus_amount": result["bonusAmount"],
            "total_new_salary": result["totalNewSalary"]
        }).execute()

        print("Supabase response:", response)

        # Check if there was an error in the response
        if hasattr(response, 'data') and response.data is None:
            raise HTTPException(status_code=500, detail="Database insert failed")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

    return {
        "employeeId": data.employeeId,
        "raiseAmount": result["raiseAmount"],
        "bonusAmount": result["bonusAmount"],
        "totalNewSalary": result["totalNewSalary"]
    }