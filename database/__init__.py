import mysql.connector
from Patient import PatientEntity
from datetime import date

class DatabaseConnection:
    myDatabase = None

    def __init__(self):

        try:
            if self.myDatabase == None:
                print("creating databsse")
                self.myDatabase = mysql.connector.connect(
                    host="127.0.0.1",
                    database="patientmanagement",
                    user="root",
                    password="")
            else:
                print("db aready created")
        except:
            print("can't establish connection", TypeError)
        9

    def getConnection(self):
        return self.myDatabase
    def getPatientDetail(self,patientId):
        str="select * from patient where patient_id = %s"
        val=(patientId,)

        mycursor=self.myDatabase.cursor()
        mycursor.execute(str,val)
        patient= mycursor.fetchone()
        if mycursor.rowcount>0:
            return PatientEntity(patient[1],patient[2],patient[3],patient[4],patient[5],patient[6],patient[7],patient[8])
        else:
            return 0

    def insertPatientDetail(self,patientEntity):
        sql = "INSERT INTO patient (name,age,PhoneNo,Diesease,AdmissionDate,Gender,BloodGroup,bill) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
        val=(patientEntity.getName(),patientEntity.getAge(),patientEntity.getMobile(),patientEntity.getDisease(),patientEntity.getAdmission(),patientEntity.getGender(),patientEntity.getBlood(),patientEntity.getBill())
        mycursor = self.myDatabase.cursor()
        a=mycursor.execute(sql,val)
        self.myDatabase.commit()

        print(mycursor.lastrowid)
        return mycursor.lastrowid