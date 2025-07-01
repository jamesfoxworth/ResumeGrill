class Education:
    def __init__(self, school, date, degree, gpa=None, coursework=None):
        self.school = school
        self.date = date
        self.degree = degree
        self.gpa = gpa
        self.coursework = coursework if coursework is not None else []
    
    
    def asDict(self):
        return {
            "school": self.school,
            "date": self.date,
            "degree": self.degree,
            "gpa": self.gpa,
            "coursework": self.coursework
        }
    
    def __repr__(self):
        return f"Education(school={self.school}, date={self.date}, degree={self.degree}, gpa={self.gpa}, coursework={self.coursework})" 