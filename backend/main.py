from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sensors import get_temperature, detect_sound, get_light_status

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/status")
def get_status():
    return {
        "temperature": get_temperature(),
        "baby_crying": detect_sound(),
        "light": get_light_status()
    }

@app.post("/api/toggle-light")
def toggle_light():
    return {"status": "Light toggled!"}