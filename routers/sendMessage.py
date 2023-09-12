from typing import Annotated

from pydantic import  BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, UploadFile
import httpx
from starlette import status
from starlette.responses import JSONResponse

import models
from models import Message,WhatsAppCredential
from database import SessionLocal
from .auth import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


db_depedency = Annotated[Session, Depends(get_db)]
user_depedency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    deviceId : str
    number : str
    message : str
    imageUrl : str

    class Config:
        json_schema_extra = {
            'example': {
                'deviceId': 'db63f5inihanyakeydummycf083dd3ffd025d672e255xxxxx',
                'number': '+628975835238',
                'message': "Hello World!",
                'imageUrl': "https://app.woo-wa.com/wp-content/uploads/2018/12/Logo-Woo-WA-PNG-Berwarna-150px.png"
            }
        }

    # URL API Woowa CRM
    WOOWA_API_URL = "https://api.woo-wa.com/"

    # Kredensial atau token autentikasi
    WOOWA_API_TOKEN = "YOUR_API_TOKEN_HERE"

def get_creds(user:user_depedency,db: db_depedency):


@router.post("/send-message-and-image")
async def send_message_and_image(user:user_depedency,db: db_depedency,
                                 message: str, image: UploadFile):

    # Membaca file gambar yang diunggah
    with image.file as img_file:
        img_data = img_file.read()

    # Mengirim pesan dan gambar ke Woowa CRM
    # async with httpx.AsyncClient() as client:
    #     headers = {"Authorization": f"Bearer {WOOWA_API_TOKEN}"}
    #     data = {"message": message}
    #
    #     files = {"file": (image.filename, img_data)}
    #
    #     response = await client.post(
    #         f"{WOOWA_API_URL}/woowa-crm-send-message-and-image",
    #         headers=headers,
    #         data=data,
    #         files=files,
    #     )
    #         # Mengembalikan respons dari Woowa CRM
    #         return {"status_code": response.status_code, "response_data": response.text}