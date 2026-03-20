# 🚀 FastAPI Basic API Learning

## 🏥 Patient Management System API (FastAPI)

This project is a **CRUD-based REST API** built using **FastAPI** for managing patient records.  
It allows users to create, view, update, and sort patient data, along with automatic BMI calculation and health verdict.

---

## 🚀 Features

- ✅ Create new patient records  
- ✅ View all patients or a specific patient  
- ✅ Update patient details  
- ✅ Sort patients based on weight, height, or BMI  
- ✅ Automatic BMI calculation  
- ✅ Health verdict generation (Underweight, Normal, Overweight, Obese)  
- ✅ Data stored using JSON file  
- ✅ Interactive API testing using `/docs`  

---

## 🛠️ Tech Stack

- Python 🐍  
- FastAPI ⚡  
- Uvicorn 🚀  
- Pydantic 📦  
- JSON (for data storage)  

---

## 📚 What I Learned

This is a **self-learning project** where I explored:

- Installing and setting up FastAPI  
- Creating REST APIs using:
  - `@app.get()`
  - `@app.post()`
  - `@app.put()`  
- Using Pydantic models for validation  
- Working with Path & Query parameters  
- Handling errors using `HTTPException`  
- Building computed fields like BMI using `@computed_field`  
- Testing APIs using Swagger UI (`/docs`)  
- Managing data using JSON files  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
