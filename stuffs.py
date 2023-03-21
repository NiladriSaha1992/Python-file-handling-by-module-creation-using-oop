class Stuffs:
    def __init__(self, sname, sdob, sgend, sqlf, sexp, sadd, sphn, seml, spsw):
        self.name = sname
        self.dob = sdob
        self.gender = sgend
        self.qualification = sqlf
        self.experience = sexp
        self.address = sadd
        self.phone = sphn
        self.email = seml
        self.password = spsw

    def saveStuffsInfo(self):
        info = f"Stuff's name: {self.name}\nDate of birth: {self.dob}\nGender: {self.gender}\nQualification: {self.qualification}\nPrev. experience (in years): {self.experience}\nAddress: {self.address}\nPhone no.: {self.phone}\nEmail ID: {self.email}\nPassword: {hash(self.password)}\n\n"
        try:
            f = open('stuffsinfo.txt', 'a')
            try:
                f.write(info)
                return "Success: data saved into the 'stuffsinfo.txt' file successfully!"
            except:
                return "Error: unable to save data into the 'stuffsinfo.txt' file!"
            finally:
                f.close()
        except:
            return "Error: unable to open the 'stuffsinfo.txt' file!"
