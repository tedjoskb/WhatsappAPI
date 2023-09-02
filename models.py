from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, TIMESTAMP, func


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)
    role = Column(String)

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True,index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    reciever_no = Column(String)
    message_text = Column(Text, nullable=True)
    sent_at= Column(TIMESTAMP, nullable=False,server_default=func.now())


# class Address(Base):
#     __tablename__='address'
#     id = Column(Integer, primary_key=True,index=True)
#     address1 = Column(String)
#     address2 = Column(String)
#     city = Column(String)
#     state = Column(String)
#     country = Column(String)
#     postalcode = Column(String)
#     apt_num = Column(Integer)
#     user_address = relationship("Users",back_populates="address")

    