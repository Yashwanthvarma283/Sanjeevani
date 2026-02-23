from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sanjeevani AI Service is from arun's laptop"}
    # Final Git verification test