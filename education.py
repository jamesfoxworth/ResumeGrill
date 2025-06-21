class Education:
    def __init__(self, school, date, degree, gpa=None, coursework=None):
        self.school = school
        self.date = date
        self.degree = degree
        self.gpa = gpa
        self.coursework = coursework if coursework is not None else []
    
    def format(self):
        # Format as in TeX
        coursework_text = ""
        if self.coursework:
            coursework_text = f"\n    \\resumeItem{{Relevant Coursework: {', '.join(self.coursework)}}}"
        
        gpa_text = f"GPA: {self.gpa}" if self.gpa else ""
        
        section = f"""
    \\resumeSubheading
      {{{self.school}}}{{{self.date}}}
      {{{self.degree}}}{{{gpa_text}}}{coursework_text}"""
        return section
    
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