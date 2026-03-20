# FastAPI_Basic_API_learning
#🏥 Patient Management System API (FastAPI)

This project is a CRUD-based REST API built using FastAPI for managing patient records.
It allows users to create, view, update, and sort patient data, along with automatic BMI calculation and health verdict.

🚀 Features

✅ Create new patient records

✅ View all patients or a specific patient

✅ Update patient details

✅ Sort patients based on weight, height, or BMI

✅ Automatic BMI calculation

✅ Health verdict generation (Underweight, Normal, Overweight, Obese)

✅ Data stored using JSON file

✅ Interactive API testing using /docs

🛠️ Tech Stack

Python 🐍

FastAPI ⚡

Uvicorn 🚀

Pydantic 📦

JSON (for data storage)

📚 What I Learned

This is a self-learning project where I explored:

Installing and setting up FastAPI

Creating REST APIs using:

@app.get()

@app.post()

@app.put()

Using Pydantic models for validation

Working with Path & Query parameters

Handling errors using HTTPException

Building computed fields like BMI using @computed_field

Testing APIs using Swagger UI (/docs)

Managing data using JSON files

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create virtual environment
python -m venv myenv

Activate it:

myenv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install fastapi uvicorn
▶️ Run the Application
uvicorn main:app --reload
🌐 API Documentation

After running the server, open:

👉 http://127.0.0.1:8000/docs

You can:

Test all APIs

Send requests

View responses

📌 API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
GET	/about	About API
GET	/view	Get all patients
GET	/view/{patient_id}	Get patient by ID
GET	/sort	Sort patients
POST	/create	Create new patient
PUT	/update/{patient_id}	Update patient
🧪 Example Request (POST /create)
{
  "id": 1,
  "name": "John Doe",
  "city": "Mumbai",
  "age": 30,
  "gender": "Male",
  "height": 175,
  "weight": 70
}
📊 Computed Fields

BMI → Automatically calculated

Verdict → Based on BMI:

Underweight

Normal weight

Overweight

Obese

💾 Data Storage

Patient data is stored in a local file:

patients.json
📈 Future Improvements

Add database (MongoDB / PostgreSQL)

Add DELETE endpoint

Add authentication (JWT)

Deploy API to cloud

Build frontend UI
