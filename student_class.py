class Student:
    def __init__(self, school_name, department, dean_name, student_name, student_id, address, credits, gpa):
        # 初始化學生物件屬性
        self.school_name = school_name  # 學校名稱
        self.department = department  # 科系名稱
        self.dean_name = dean_name  # 系主任姓名
        self.student_name = student_name  # 學生姓名
        self.student_id = student_id  # 學生學號(ID)
        self.address = address  # 個人通訊地址
        self.credits = credits  # 已取得學分數
        self.gpa = gpa  # 成績GPA

    
    def getSchoolName(self):
        return self.school_name

    def setSchoolName(self, school_name):
        self.school_name = school_name

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department

    def getDeanName(self):
        return self.dean_name

    def setDeanName(self, dean_name):
        self.dean_name = dean_name

    def getStudentName(self):
        return self.student_name

    def setStudentName(self, student_name):
        self.student_name = student_name

    def getStudentID(self):
        return self.student_id

    def setStudentID(self, student_id):
        self.student_id = student_id

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getCredits(self):
        return self.credits

    def setCredits(self, credits):
        self.credits = credits

    def getGPA(self):
        return self.gpa

    def setGPA(self, gpa):
        self.gpa = gpa

# Example usage:
student = Student("STUST", "資訊工程系", "李宗儒博士", "LEO", "4b0g0118", "123 Main St", 120, 3.8)
print(student.getSchoolName())
student.setSchoolName("南台科大")
print(student.getSchoolName())
