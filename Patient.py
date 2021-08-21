class PatientEntity:
    name =''
    age=''
    gender=''
    mobile=0
    bloodGroup=''
    bill =0
    disease=''
    admission=''
    def __init__(self,name,age,mobile,disease,admission,gender,blood,bill):
        self.name=name
        self.age=age
        self.gender=gender
        self.mobile=mobile
        self.bloodGroup=blood
        self.disease=disease
        self.bill=bill
        self.admission=admission

    def getName(self):
        return  self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def getMobile(self):
        return self.mobile
    def getBlood(self):
        return self.bloodGroup
    def getBill(self):
        return self.bill
    def getDisease(self):
        return self.disease
    def getAdmission(self):
        return self.admission;