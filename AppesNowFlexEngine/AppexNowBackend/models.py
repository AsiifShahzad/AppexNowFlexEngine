from pydantic import BaseModel, Field

# Input model (matches the frontend form data structure)
class EmployeeInput(BaseModel):
    employeeId: str  # Changed from employee_id to employeeId to match frontend
    currentSalary: float = Field(gt=0)  # currentSalary from frontend
    yearsExperience: float = Field(ge=0)  # yearsExperience from frontend
    performanceScore: float = Field(ge=0, le=5)  # performanceScore from frontend
    jobRole: str  # jobRole from frontend
    location: str  # location from frontend

# Output model (what will be sent back to frontend)
class ResultOutput(BaseModel):
    employeeId: str  # Changed to match the frontend expected key
    raiseAmount: float
    bonusAmount: float
    totalNewSalary: float
