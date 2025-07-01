class Project:
    def __init__(self, name, tools, bullets):
        self.name = name
        self.tools = tools
        self.bullets = bullets
        
    def asDict(self):
        return {
            "name": self.name,
            "tools": self.tools,
            "bullets": self.bullets
        }
    
    def __repr__(self):
        return f"Project(name={self.name}, tools={self.tools}, bullets={self.bullets})"