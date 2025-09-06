# Accessing Database with FastAPI  

This project demonstrates how to connect and interact with a database using **FastAPI** and **SQLAlchemy ORM**. It includes basic CRUD operations (Create, Read, Update, Delete) and is structured for easy scalability.  

---

## 🚀 Features  

- FastAPI for building REST APIs  
- SQLAlchemy ORM for database interactions  
- SQLite (default) database setup (you can switch to PostgreSQL/MySQL)  
- Pydantic models for request/response validation  
- Dependency Injection for database session handling  

---

## 📂 Project Structure  

project/
│── main.py # FastAPI entry point
│── models.py # SQLAlchemy models (tables)
│── schemas.py # Pydantic schemas (validation)
│── DataBase/
│ └── database.py # DB connection and session
│── requirements.txt # Python dependencies

yaml
Copy code

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the repository  

git clone https://github.com/JawadSaghir/FastAPI.git
cd Accessing-Database-with-FastAPI
2️⃣ Create and activate a virtual environment
bash
Copy code
# Create virtual environment  
python -m venv venv  

# Activate (Windows)  
venv\Scripts\activate  

# Activate (Mac/Linux)  
source venv/bin/activate  
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the FastAPI server
bash
Copy code
uvicorn main:app --reload
The server will start at 👉 http://127.0.0.1:8000

📌 API Endpoints
POST /blogs → Create a new blog

GET /blogs → Get all blogs

GET /blogs/{id} → Get a single blog by ID

PUT /blogs/{id} → Update a blog

DELETE /blogs/{id} → Delete a blog

🛠️ Change Database (Optional)
By default, this project uses SQLite.
To switch to PostgreSQL or MySQL, update the DATABASE_URL in DataBase/database.py:

python
Copy code
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
📖 Learn More
FastAPI Documentation

SQLAlchemy ORM

✅ You now have a working FastAPI project with database access!

yaml
Copy code

---

Do you also want me to generate the **requirements.txt** content for you, so anyone who clones your rep
