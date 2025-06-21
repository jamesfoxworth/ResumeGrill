class Project:
    def __init__(self, name, tools, bullets):
        self.name = name
        self.tools = tools
        self.bullets = bullets
    
    def format(self):
        # Format as in TeX
        bullets_text = ""
        for bullet in self.bullets:
            bullets_text += f"\n            \\resumeItem{{{bullet}}}"
        
        # Format tools with proper styling
        tools_formatted = f"$|$ \\emph{{ {', '.join(self.tools)}}}"
        
        section = f"""
          \\resumeProjectHeading
            {{\\textbf{{{self.name}}} {tools_formatted}}}{{}}
            \\resumeItemListStart{bullets_text}
            \\resumeItemListEnd"""
        return section
        
    def asDict(self):
        return {
            "name": self.name,
            "tools": self.tools,
            "bullets": self.bullets
        }
    
    def __repr__(self):
        return f"Project(name={self.name}, tools={self.tools}, bullets={self.bullets})"