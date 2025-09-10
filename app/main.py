from fastapi import FastAPI, Form, Request
import openai
from decouple import config

from .twilio_utils import send_message, logger

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "up & running"}