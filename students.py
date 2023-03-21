class Students:
    def __init__(self, sname, sdob, sgend, slqlf, sgrd, sadd, sphn, seml, spsw):
        self.name = sname
        self.dob = sdob
        self.gender = sgend
        self.last_qualification = slqlf
        self.guardian = sgrd
        self.address = sadd
        self.phone = sphn
        self.email = seml
        self.password = spsw

    def saveStudentsInfo(self):
        info = f"Student's name: {self.name}\nDate of birth: {self.dob}\nGender: {self.gender}\nQualification: {self.last_qualification}\nGuardian's name: {self.guardian}\nAddress: {self.address}\nPhone no.: {self.phone}\nEmail ID: {self.email}\nPassword: {hash(self.password)}\n\n"
        try:
            f = open('studentsinfo.txt', 'a')
            try:
                f.write(info)
                return "Success: data saved into the 'studentsinfo.txt' file successfully!"
            except:
                return "Error: unable to save data into the 'studentsinfo.txt' file!"
            finally:
                f.close()
        except:
            return "Error: unable to open the 'studentsinfo.txt' file!"
