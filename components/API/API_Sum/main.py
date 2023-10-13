from fastapi import FastAPI
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to your frontend's domain during production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/calculate")
def calculate(x1: float, x2: float):
    y = x1+x2
    return {"y": y}