from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, TIMESTAMP, func


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    user_phone_number = Column(String, unique=True, index=True)
    whatsapp_credentials = relationship("WhatsAppCredential", back_populates="users")
    message = relationship("Message", back_populates="user")


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    reciever_no = Column(String)
    message_text = Column(Text, nullable=True)
    sent_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    user = relationship("Users", back_populates="message")


class WhatsAppCredential(Base):
    __tablename__ = 'whatsapp_credentials'

    id = Column(Integer, primary_key=True, index=True)
    api_token = Column(String, unique=True, index=True)
    phone_number = Column(String, ForeignKey("users.user_phone_number"), unique=True, index=True)
    users = relationship("Users", back_populates="whatsapp_credentials")


    