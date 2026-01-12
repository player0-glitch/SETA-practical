from app.database import engine 

with engine.connect():
    print("Connected successfully")
