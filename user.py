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
    
    def format(self):
        """
        Converts the User object back into the original LaTeX resume format.
        """
        # Header section
        header = f"""%-------------------------
% Resume in Latex
% Author : Jake Gutierrez
% Based off of: https://github.com/sb2nov/resume
% License : MIT
%------------------------

\\documentclass[letterpaper,11pt]{{article}}

\\usepackage{{latexsym}}
\\usepackage[empty]{{fullpage}}
\\usepackage{{titlesec}}
\\usepackage{{marvosym}}
\\usepackage[usenames,dvipsnames]{{color}}
\\usepackage{{verbatim}}
\\usepackage{{enumitem}}
\\usepackage[hidelinks]{{hyperref}}
\\usepackage{{fancyhdr}}
\\usepackage[english]{{babel}}
\\usepackage{{tabularx}}
\\input{{glyphtounicode}}


%----------FONT OPTIONS----------
% sans-serif
% \\usepackage[sfdefault]{{FiraSans}}
% \\usepackage[sfdefault]{{roboto}}
% \\usepackage[sfdefault]{{noto-sans}}
% \\usepackage[default]{{sourcesanspro}}
% \\usepackage[sfdefault]{{carlito}}
\\usepackage[scaled]{{berasans}}

% serif
% \\usepackage{{CormorantGaramond}}
% \\usepackage{{charter}}
% \\usepackage{{palatino}}


\\pagestyle{{fancy}}
\\fancyhf{{}} % clear all header and footer fields
\\fancyfoot{{}}
\\renewcommand{{\\headrulewidth}}{{0pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}

% Adjust margins
\\addtolength{{\\oddsidemargin}}{{-0.5in}}
\\addtolength{{\\evensidemargin}}{{-0.5in}}
\\addtolength{{\\textwidth}}{{1in}}
\\addtolength{{\\topmargin}}{{-.5in}}
\\addtolength{{\\textheight}}{{1.0in}}

\\urlstyle{{same}}

\\raggedbottom
\\raggedright
\\setlength{{\\tabcolsep}}{{0in}}

% Sections formatting
\\titleformat{{\\section}}{{
  \\vspace{{-4pt}}\\scshape\\raggedright\\large
}}{{}}{{0em}}{{}}[\\color{{black}}\\titlerule \\vspace{{-5pt}}]

% Ensure that generate pdf is machine readable/ATS parsable
\\pdfgentounicode=1

%-------------------------
% Custom commands
\\newcommand{{\\resumeItem}}[1]{{
  \\item\\small{{
    {{#1 \\vspace{{-2pt}}}}
  }}
}}

\\newcommand{{\\resumeSubheading}}[4]{{
  \\vspace{{-2pt}}\\item
    \\begin{{tabular*}}{{0.97\\textwidth}}[t]{{l@{{\\extracolsep{{\\fill}}}}r}}
      \\textbf{{#1}} & #2 \\\\
      \\textit{{\\small#3}} & \\textit{{\\small #4}} \\\\
    \\end{{tabular*}}\\vspace{{-7pt}}
}}

\\newcommand{{\\resumeSubSubheading}}[2]{{
    \\item
    \\begin{{tabular*}}{{0.97\\textwidth}}{{l@{{\\extracolsep{{\\fill}}}}r}}
      \\textit{{\\small#1}} & \\textit{{\\small #2}} \\\\
    \\end{{tabular*}}\\vspace{{-7pt}}
}}

\\newcommand{{\\resumeProjectHeading}}[2]{{
    \\item
    \\begin{{tabular*}}{{0.97\\textwidth}}{{l@{{\\extracolsep{{\\fill}}}}r}}
      \\small#1 & #2 \\\\
    \\end{{tabular*}}\\vspace{{-7pt}}
}}

\\newcommand{{\\resumeSubItem}}[1]{{\\resumeItem{{#1}}\\vspace{{-4pt}}}}

\\renewcommand\\labelitemii{{$\\vcenter{{\\hbox{{\\tiny$\\bullet$}}}}$}}

\\newcommand{{\\resumeSubHeadingListStart}}{{\\begin{{itemize}}[leftmargin=0.15in, label={{}}]}}
\\newcommand{{\\resumeSubHeadingListEnd}}{{\\end{{itemize}}}}
\\newcommand{{\\resumeItemListStart}}{{\\begin{{itemize}}}}
\\newcommand{{\\resumeItemListEnd}}{{\\end{{itemize}}\\vspace{{-5pt}}}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\\begin{{document}}

%----------HEADING----------
\\begin{{center}}
    \\textbf{{\\Huge \\scshape {self.name}}} \\\\ \\vspace{{1pt}}
    \\small {self.phone} $|$ \\href{{mailto:{self.email}}}{{\\underline{{{self.email}}}}} $|$ 
    \\href{{{self.linkedin}}}{{\\underline{{linkedin.com/in/{self.linkedin.split('/')[-1]}}}}} $|$
    {{{self.location}}} $|$
    {{U.S. Citizen}}
\\end{{center}}

"""

        # Education section
        education_section = """%-----------EDUCATION-----------
\\section{Education}
  \\resumeSubHeadingListStart
"""
        
        for edu in self.education:
            education_section += edu.format()
        
        education_section += """
  \\resumeSubHeadingListEnd

"""

        # Experience section
        experience_section = """%-----------EXPERIENCE-----------
\\section{Experience}
  \\resumeSubHeadingListStart

"""
        
        for experience in self.experiences:
            experience_section += experience.format()
        
        experience_section += """
  \\resumeSubHeadingListEnd

"""

        # Projects section
        projects_section = """%-----------PROJECTS-----------
\\section{Projects}
    \\resumeSubHeadingListStart
"""
        
        for project in self.projects:
            projects_section += project.format()
        
        projects_section += """
    \\resumeSubHeadingListEnd

"""

        # Technical Skills section
        languages_str = ", ".join(self.languages)
        dev_tools_str = ", ".join(self.devTools)
        frameworks_str = ", ".join(self.frameworks)
        
        skills_section = f"""%
%-----------PROGRAMMING SKILLS-----------
\\section{{Technical Skills}}
 \\begin{{itemize}}[leftmargin=0.15in, label={{}}]
    \\small{{\\item{{
     \\textbf{{Languages}}{{: {languages_str}}} \\\\
     \\textbf{{Developer Tools}}{{: {dev_tools_str}}} \\\\
     \\textbf{{Frameworks}}{{: {frameworks_str}}}
    }}}}
 \\end{{itemize}}


"""

        # Footer
        footer = """%-------------------------------------------
\\end{document}"""

        return header + education_section + experience_section + projects_section + skills_section + footer