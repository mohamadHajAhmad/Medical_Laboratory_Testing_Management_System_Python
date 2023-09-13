from ast import List
from datetime import datetime
from abc import ABCMeta , abstractmethod

class DataOperationABC(metaclass = ABCMeta):
    @staticmethod
    @abstractmethod
    def Export(Object):
        pass
    
    @staticmethod
    @abstractmethod
    def PrintMedicalTestPriceAt(Object):
        pass
    
    @staticmethod
    @abstractmethod
    def PrintPatientNameAt(Object):
        pass
    
    
    @staticmethod
    @abstractmethod
    def PrintPatientNameAtMonth(Object):
        pass

class DataOperationABC(DataOperationABC):
    def Export(Object):
        file  = open(r"")
    
    def PrintMedicalTestPriceAt(Object):
        pass
    
    def PrintPatientNameAt(Object):
        pass
    
    def PrintPatientNameAtMonth(Object):
        pass


class MedicalTest :
    NewId = 0
    def __init__(self , PatientId : int , TestId : int , DateTime : datetime , Price : int, DoctorId : int ) -> None:
        self.Id = MedicalTest.NewId
        self.PatientId = PatientId
        self.TestId = TestId
        self.DateTime = DateTime
        self.Price = Price
        self.DoctorId = DoctorId
        MedicalTest.NewId +=  1


    def __str__(self) -> str:
        return (f"{self.Id} - {self.PatientId} - {self.TestId} - {self.DoctorId} - {self.DateTime}")



class TestType :
    NewId = 0
    def __init__(self , Type ,  MedicalTests : List[MedicalTest]) -> None:
        self.Id = TestType.NewId
        self.Type = Type
        self.MedicalTests = MedicalTests
        TestType.NewId += 1


    def __str__(self) -> str:
        return (f"{self.Id} - {self.Type} - {self.MedicalTests} ")



class patient :
    NewId = 0
    def __init__(self , PatientName : str , BirthDay : datetime , MedicalTests : List[MedicalTest]) -> None:
        self.Id = patient.NewId
        self.patientName = PatientName
        self.BirthDay = BirthDay
        self.MedicalTests = MedicalTests
        patient.NewId += 1


    def __str__(self) -> str:
        return (f"{self.Id} - {self.patientName} - {self.BirthDay} - {self.MedicalTests} ")


class Doctor :
    NewId = 0
    def __init__(self , DoctorName  : str , MedicalTests : List[MedicalTest]) -> None:
        self.Id = Doctor.NewId
        self.DoctorName = DoctorName
        self.MedicalTests = MedicalTests
        Doctor.NewId += 1
        
        
    def __str__(self) -> str:
        return (f"{self.Id} - {self.DoctorName} - {self.MedicalTests}")
