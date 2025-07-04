class Experience:
    def __init__(self, company, title, location, bullets, start_date, end_date=None):
        self.company = company
        self.title = title
        self.bullets = bullets
        self.location = location
        self.start_date = start_date
        self.end_date = end_date if end_date is not None else "Present"
    
    
    def asDict(self):
        return {
            "company": self.company,
            "title": self.title,
            "bullets": self.bullets,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
    
    def __repr__(self):
        return f"Experience(company={self.company}, title={self.title}, location={self.location}, bullets={self.bullets}, start_date={self.start_date}, end_date={self.end_date})"

    

    
