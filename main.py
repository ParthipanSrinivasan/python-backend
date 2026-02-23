from fastapi import FastAPI, Form
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://192.168.1.6:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "postgresql://weather_app_projects_user:1WqSXc5pDAodgXq8BObeRGBsObpW0pMm@dpg-d685cm0boq4c73csfu7g-a.oregon-postgres.render.com/weather_app_projects"

engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}

@app.get("/users")
def get_users():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM users"))
            users = [dict(row._mapping) for row in result]
            return users
    except Exception as e:
        return {"error": str(e)}

@app.get("/categories")
def developer():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM categories"))
            categories = [dict(row._mapping) for row in result]
            return categories
    except Exception as e:
        return {"error": str(e)}
@app.get("/order")
def order_deatils():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM orders"))
            orders = [dict(row._mapping) for row in result]
            return orders
    except Exception as e:
        return {"error": str(e)}
@app.get("/product")
def product_details():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM products"))
            products = [dict(row._mapping) for row in result]
            return products
    except Exception as e:
        return {"error": str(e)}

class User(BaseModel):
    name: str
    email: str

# @app.post("/users")
# def create_user(name: str, email: str):
#         try:
#             with engine.connect() as conn:
#                query = text("INSERT INTO users (name, email)  VALUES (:name, :email)")
#                conn.execute(query, {"name": name, "email": email})
#                conn.commit()
#             return {"message": "User Created Succesfully"}
#         except Exception as e:
#             return {"error": str(e)}

@app.post("/users")
def create_user(
    name: str = Form(...),
    email: str = Form(...)
):
    try:
        with engine.connect() as conn:
            query = text("INSERT INTO users (name, email)  VALUES (:name, :email)")
            conn.execute(query, {"name":name, "email":email})
            conn.commit()
        return {"message": "User Created Succesfully"}
    except Exception as e:
        return {"error": str(e)}