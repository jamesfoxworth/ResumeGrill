from education import Education

class User:
    def __init__(self, name, email, location, phone, linkedin, languages, devTools, frameworks, projects, experiences, education=None):
        self.name = name
        self.email = email
        self.location = location
        self.phone = phone
        self.linkedin = linkedin
        self.languages = languages
        self.devTools = devTools
        self.frameworks = frameworks
        self.projects = projects
        self.experiences = experiences
        self.education = education if education is not None else []

    def to_text(self):
        """
        Returns a plain text summary of the user's resume for LLM prompts.
        """
        lines = []
        lines.append(f"Name: {self.name}")
        lines.append(f"Email: {self.email}")
        lines.append(f"Phone: {self.phone}")
        lines.append(f"Location: {self.location}")
        lines.append(f"LinkedIn: {self.linkedin}")
        lines.append("")
        lines.append("Education:")
        for edu in self.education:
            lines.append(f"  - {edu.school}, {edu.degree}, {edu.date} GPA: {edu.gpa if edu.gpa else ''}")
            if edu.coursework:
                lines.append(f"    Coursework: {', '.join(edu.coursework)}")
        lines.append("")
        lines.append("Experience:")
        for exp in self.experiences:
            lines.append(f"  - {exp.title} at {exp.company} ({exp.start_date} - {exp.end_date}), {exp.location}")
            for bullet in exp.bullets:
                lines.append(f"    * {bullet}")
        lines.append("")
        lines.append("Projects:")
        for proj in self.projects:
            lines.append(f"  - {proj.name} [{', '.join(proj.tools)}]")
            for bullet in proj.bullets:
                lines.append(f"    * {bullet}")
        lines.append("")
        lines.append(f"Languages: {', '.join(self.languages)}")
        lines.append(f"Developer Tools: {', '.join(self.devTools)}")
        lines.append(f"Frameworks: {', '.join(self.frameworks)}")
        return '\n'.join(lines)