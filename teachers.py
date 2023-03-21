class Teachers:
    def __init__(self, tname, tdob, tgend, tqlf, texp, tadd, tphn, teml, tpsw):
        self.name = tname
        self.dob = tdob
        self.gender = tgend
        self.qualification = tqlf
        self.experience = texp
        self.address = tadd
        self.phone = tphn
        self.email = teml
        self.password = tpsw

    def saveTeachersInfo(self):
        info = f"Teacher's name: {self.name}\nDate of birth: {self.dob}\nGender: {self.gender}\nQualification: {self.qualification}\nPrev. experience (in years): {self.experience}\nAddress: {self.address}\nPhone no.: {self.phone}\nEmail ID: {self.email}\nPassword: {hash(self.password)}\n\n"
        try:
            f = open('teachersinfo.txt', 'a')
            try:
                f.write(info)
                return "Success: data saved into the 'teachersinfo.txt' file successfully!"
            except:
                return "Error: unable to save data into the 'teachersinfo.txt' file!"
            finally:
                f.close()
        except:
            return "Error: unable to open the 'teachersinfo.txt' file!"
