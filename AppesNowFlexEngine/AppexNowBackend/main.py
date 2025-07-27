from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EmployeeInput, ResultOutput
from calculate import calculate_raise_bonus

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate", response_model=ResultOutput)
def calculate_salary(data: EmployeeInput):
    result = calculate_raise_bonus(data)
    return {
        "employeeId": data.employeeId,
        **result
    }
