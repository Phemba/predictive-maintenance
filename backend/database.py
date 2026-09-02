from sqlalchemy import create_engine, Column, Integer,Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///database.db")

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    air_temperature = Column(Float)
    process_temperature = Column(Float)
    rotational_speed = Column(Float)
    torque = Column(Float)
    tool_wear = Column(Float)
    risk = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    
Base.metadata.create_all(engine)
    
SessionLocal = sessionmaker(bind=engine)
    