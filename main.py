from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from typing import Literal, Optional
import json 
from typing_extensions import Annotated , TypedDict , Optional
from pydantic import BaseModel, Field, computed_field

app = FastAPI()

# class of patient
class patient(BaseModel):
    
    id : Annotated[int, Field(... , description="ID of the patient in DB", example=1, gt=0)]
    name : Annotated[str, Field(... , description="Name of the patient", example="John Doe")]
    city : Annotated[str, Field(... , description="City of the patient", example="New York")]
    age : Annotated[int, Field(... , description="Age of the patient", example=30, ge=0)]
    gender : Annotated[Literal["Male", "Female", "Other"], Field(... , description="Gender of the patient", example="Male")]
    height : Annotated[float, Field(... , description="Height of the patient in cm", example=175.5, gt=0)]
    weight : Annotated[float, Field(... , description="Weight of the patient in kg", example=70.5, gt=0)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        
class PatientUpdate(BaseModel):
    name : Annotated[Optional[str], Field(None , description="Name of the patient", example="John Doe")]
    city : Annotated[Optional[str], Field(None , description="City of the patient", example="New York")]
    age : Annotated[Optional[int], Field(None , description="Age of the patient", example=30, ge=0)]
    gender : Annotated[Optional[Literal["Male", "Female ", "Other"]], Field(None , description="Gender of the patient", example="Male")]    
    height : Annotated[Optional[float], Field(None , description="Height of the patient in cm", example=175.5, gt=0)]
    weight : Annotated[Optional[float], Field(None , description="Weight of the patient in kg", example=70.5, gt=0)]    
    

# utility functions
# load data from json file
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data
# save data to json file
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
        
        
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "A fully functional API for managing patient records, appointments, and medical history."}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
def view_patient(patient_id: int = Path(..., description="ID of the patient in DB", example=1, gt=0)):
    data = load_data()
    for patient in data:
        if patient['id'] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on basis on weight , height or BMI "), order: str = Query("asc", description="sort order: asc or desc")):
    
    valid_fields = ['weight', 'height', 'BMI']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order value. Must be 'asc' or 'desc'")
    
    data = load_data()
    sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=(order == 'desc'))
    
    return sorted_data

@app.post("/create")
def create_patient(patient: patient):
    # load the existing data
    data = load_data()
    
    # check if the patient ID already exists
    for existing_patient in data:
        if existing_patient['id'] == patient.id:
            raise HTTPException(status_code=400, detail="Patient with this ID already exists")
        
    #  add new patient to the data
    data.append(patient.dict())
    
    # save the updated data back to the file
    save_data(data)
    
    return JSONResponse(status_code=201,content={"message": "Patient created successfully", "patient": patient.dict()})


# update patient record
@app.put("/update/{patient_id}")
def update_patient(patient_id: int, patient_update: PatientUpdate):

    data = load_data()

    for patient in data:
        if patient['id'] == patient_id:
            break
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_patient_info = patient

    update_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in update_patient_info.items():
        existing_patient_info[key] = value

    # Convert dict → Pydantic model
    patient_obj = patient(**existing_patient_info)

    # Convert model → dict (recalculates BMI and verdict)
    patient_dict = patient_obj.model_dump()

    data[data.index(patient)] = patient_dict

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient updated successfully",
            "patient": patient_dict
        }
    ) 