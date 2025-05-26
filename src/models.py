from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)

class InPatient(Patient):
    __tablename__ = 'inpatients'
    id = Column(Integer, primary_key=True)

class OutPatient(Patient):
    __tablename__ = 'outpatients'
    id = Column(Integer, primary_key=True)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True)