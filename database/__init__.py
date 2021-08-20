import mysql.connector
from Patient import PatientEntity

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
    def getPatientDetail(self):
        str="select * from patient";
        mycursor=self.myDatabase.cursor()
        mycursor.execute(str)
        a= mycursor.fetchall();
        print(a)
        return a;

    def insertPatientDetail(self,patientEntity):
        sql = "INSERT INTO patient (name,age,PhoneNo,Diesease,AdmissionDate,Gender,BloodGroup,bill) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
        val=(patientEntity.getName(),patientEntity.getAge(),patientEntity.getMobile(),patientEntity.getDisease(),'sysdate',patientEntity.getGender(),patientEntity.getBlood(),patientEntity.getBill())
        mycursor = self.myDatabase.cursor()
        a=mycursor.execute(sql,val)
        self.myDatabase.commit()

        print(mycursor.lastrowid)
        return mycursor.lastrowid