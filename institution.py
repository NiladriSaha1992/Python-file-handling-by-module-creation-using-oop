import teachers as tech
import students as stu
import stuffs as stf
import courses as crs


class Institution:
    def setCourseInfo(self, cID, cName, cDuration, cCost):
        course = crs.Courses(cID, cName, cDuration, cCost)
        return course.saveCourseInfo()

    def setTeacherInfo(self, tname, tdob, tgend, tqlf, texp, tadd, tphn, teml, tpsw):
        teacher = tech.Teachers(tname, tdob, tgend, tqlf,
                                texp, tadd, tphn, teml, tpsw)
        return teacher.saveTeachersInfo()

    def setStuffInfo(self, sname, sdob, sgend, sqlf, sexp, sadd, sphn, seml, spsw):
        stuff = stf.Stuffs(sname, sdob, sgend, sqlf,
                           sexp, sadd, sphn, seml, spsw)
        return stuff.saveStuffsInfo()

    def setStudentInfo(self, sname, sdob, sgend, slqlf, sgrd, sadd, sphn, seml, spsw):
        student = stu.Students(sname, sdob, sgend, slqlf,
                               sgrd, sadd, sphn, seml, spsw)
        return student.saveStudentsInfo()


while True:
    getOption = int(input(
        "Select an option to add data relating to it:\n1)Course, 2)Teacher, 3)Stuff, 4)Student\n"))
    match getOption:
        case 1:
            print("Enter the following details of courses:")
            while True:
                getCourseID = input("Enter course ID:\n")
                getCourseName = input("Enter course name:\n")
                getCourseDuration = int(
                    input("Enter duration (in months):\n"))
                getCourseCost = float(
                    input("Enter cost of the course (in rupee):\n"))
                instObj = Institution()
                status = instObj.setCourseInfo(
                    getCourseID, getCourseName, getCourseDuration, getCourseCost)
                print(status)
                cont = input("do you want to add more courses? (y/n)\n")
                if cont == 'y':
                    continue
                elif cont == 'n':
                    break
                else:
                    cont = input("please select a correct option (y/n)\n")

        case 2:
            print("Enter the following details of teachers:")
            while True:
                getTeachName = input("Enter name:\n")
                getTeachDob = input("Enter date of birth:\n")
                getTeachGender = input("Enter gender (M/F):\n")
                getTeachQlf = input("Enter qualification:\n")
                getTeachExperience = input(
                    "Enter working experience (in years):\n")
                getTeachAddress = input("Enter address:\n")
                getTeachPhone = input("Enter phone number:\n")
                getTeachEmail = input("Enter email ID:\n")
                getTeachPsw = input("Enter password:\n")
                instObj = Institution()
                status = instObj.setTeacherInfo(
                    getTeachName, getTeachDob, getTeachGender, getTeachQlf, getTeachExperience, getTeachAddress, getTeachPhone, getTeachEmail, getTeachPsw)
                print(status)
                cont = input("do you want to add more teachers? (y/n)\n")
                if cont == 'y':
                    continue
                elif cont == 'n':
                    break
                else:
                    cont = input("please select a correct option (y/n)\n")

        case 3:
            print("Enter the following details of stuffs:")
            while True:
                getStuffName = input("Enter name:\n")
                getStuffDob = input("Enter date of birth:\n")
                getStuffGender = input("Enter gender (M/F):\n")
                getStuffQlf = input("Enter qualification:\n")
                getStuffExperience = input(
                    "Enter working experience (in years):\n")
                getStuffAddress = input("Enter address:\n")
                getStuffPhone = input("Enter phone number:\n")
                getStuffEmail = input("Enter email ID:\n")
                getStuffPsw = input("Enter password:\n")
                instObj = Institution()
                status = instObj.setStuffInfo(getStuffName, getStuffDob, getStuffGender, getStuffQlf,
                                              getStuffExperience, getStuffAddress, getStuffPhone, getStuffEmail, getStuffPsw)
                print(status)
                cont = input("do you want to add more stuffs? (y/n)\n")
                if cont == 'y':
                    continue
                elif cont == 'n':
                    break
                else:
                    cont = input("please select a correct option (y/n)\n")

        case 4:
            print("Enter the following details of students:")
            while True:
                getStudentName = input("Enter name:\n")
                getStudentDob = input("Enter date of birth:\n")
                getStudentGender = input("Enter gender (M/F):\n")
                getStudentLastQlf = input("Enter qualification:\n")
                getStudentGuardian = input("Enter guardian's name:\n")
                getStudentAddress = input("Enter address:\n")
                getStudentPhone = input("Enter phone number:\n")
                getStudentEmail = input("Enter email ID:\n")
                getStudentPsw = input("Enter password:\n")
                instObj = Institution()
                status = instObj.setStudentInfo(getStudentName, getStudentDob, getStudentGender, getStudentLastQlf,
                                                getStudentGuardian, getStudentAddress, getStudentPhone, getStudentEmail, getStudentPsw)
                print(status)
                cont = input("do you want to add more students? (y/n)\n")
                if cont == 'y':
                    continue
                elif cont == 'n':
                    break
                else:
                    cont = input("please select a correct option (y/n)\n")

        case _:
            getOption = int(input(
                "Please select a correct option:\n1)Course, 2)Teacher, 3)Stuff, 4)Student\n"))

    cont = input("do you want to continue? (y/n)\n")
    if cont == 'y':
        continue
    elif cont == 'n':
        break
    else:
        cont = input("please select a correct option (y/n)\n")
