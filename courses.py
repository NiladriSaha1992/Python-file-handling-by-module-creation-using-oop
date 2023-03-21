class Courses:
    def __init__(self, cID, cName, cDuration, cCost):
        self.course_ID = cID
        self.course_name = cName
        self.course_duration = cDuration
        self.course_cost = cCost

    def saveCourseInfo(self):
        info = f"Course ID: {self.course_ID}\nName: {self.course_name}\nDuration: {self.course_duration}\nCost (in rupee): {self.course_cost}\n\n"
        try:
            f = open("coursesinfo.txt", "a")
            try:
                f.write(info)
                return "Success: data saved into the 'coursesinfo.txt' file successfully!"
            except:
                return "Error: unable to save data into the 'coursesinfo.txt' file!"
            finally:
                f.close()
        except:
            return "Error: unable to open the 'coursesinfo.txt' file!"
