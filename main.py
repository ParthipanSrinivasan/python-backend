from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

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