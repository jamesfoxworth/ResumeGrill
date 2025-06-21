import re
from project import Project
from experience import Experience

def preprocess_tex(lines):
    """
    Preprocess LaTeX lines to handle commands that span multiple lines.
    Returns a new list of lines with multi-line commands combined.
    """
    result = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('%'):
            i += 1
            continue
        # If line starts with a command that may span multiple lines
        if line.startswith('\\resumeSubheading') or line.startswith('\\resumeProjectHeading'):
            combined = line
            close_brace_count = line.count('}')
            i += 1
            # Keep adding lines until we've seen 4 closing braces
            while close_brace_count < 4 and i < len(lines):
                next_line = lines[i].strip()
                combined += ' ' + next_line
                close_brace_count += next_line.count('}')
                i += 1
            result.append(combined)
        else:
            result.append(line)
            i += 1
    return result

def parseFromText(text, verbose=False):
    """
    Parses a resume from the given format into Projects and Experiences.
    """
    
    lines = text.strip().split('\n')
    # Preprocess lines to handle multi-line LaTeX commands
    lines = preprocess_tex(lines)
    
    if verbose:
        print("Preprocessed lines:")
        for i, line in enumerate(lines[:20]):  # Show first 20 lines
            print(f"{i}: {line}")
        print("...")
        print("\nAll lines starting with \\resumeSubheading or \\resumeProjectHeading:")
        for line in lines:
            if line.startswith('\\resumeSubheading') or line.startswith('\\resumeProjectHeading'):
                print(line)
    
    result = {
        "Experience": [],
        "Projects": []
    }
      
    current_section = None
    current_project = None
    current_experience = None
    
    # Regular expressions for parsing different sections
    section_pattern = re.compile(r'\\section\{(.*?)\}')
    project_heading_pattern = re.compile(r'\\resumeProjectHeading\s*\{\\textbf\{(.*?)\}\s*\$\|\$\s*\\emph\{\s*(.*?)\}\}\{\}')
    experience_heading_pattern = re.compile(r'\\resumeSubheading\s*\{(.*?)\}\{(.*?)\}\s*\{(.*?)\}\{(.*?)\}')
    resume_item_pattern = re.compile(r'\\resumeItem\{(.*?)\}')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        section_match = section_pattern.search(line)
        if section_match:
            current_section = section_match.group(1)
            if verbose:
                print(f"Found section: {current_section}")
            i += 1
            continue
            
        # Parse Projects section
        if current_section == "Projects":
            # Check for project heading
            if verbose and "resumeProjectHeading" in line:
                print(f"Checking project regex on: {line}")
                match = project_heading_pattern.search(line)
                print(f"Project regex match: {match is not None}")
                
            project_match = project_heading_pattern.search(line)
            if project_match:
                # Save previous project if exists
                if current_project:
                    result["Projects"].append(Project(
                        current_project["name"], 
                        current_project["tools"], 
                        current_project["bullets"]
                    ))
                
                # Start new project
                project_name = project_match.group(1).strip()
                tools_str = project_match.group(2).strip()
                tools = [tool.strip() for tool in tools_str.split(',')]
                current_project = {
                    "name": project_name,
                    "tools": tools,
                    "bullets": []
                }
                if verbose:
                    print(f"Found project: {project_name} with tools {tools}")
            
            # Check for resume items/bullets
            item_match = resume_item_pattern.search(line)
            if item_match and current_project:
                bullet = item_match.group(1)
                current_project["bullets"].append(bullet)
                if verbose:
                    print(f"Added bullet to project: {bullet[:50]}...")
        
        # Parse Experience section
        elif current_section == "Experience":
            # Check for experience heading
            if verbose and "resumeSubheading" in line:
                print(f"Checking experience regex on: {line}")
                match = experience_heading_pattern.search(line)
                print(f"Experience regex match: {match is not None}")
                
            experience_match = experience_heading_pattern.search(line)
            if experience_match:
                # Save previous experience if exists
                if current_experience:
                    result["Experience"].append(Experience(
                        current_experience["company"],
                        current_experience["title"],
                        current_experience["location"],
                        current_experience["bullets"],
                        current_experience["start_date"],
                        current_experience["end_date"]
                    ))
                
                # Start new experience
                title = experience_match.group(1).strip()
                date_range = experience_match.group(2).strip()
                # Parse date range to extract start_date and end_date
                date_parts = date_range.split('–')  # Note: this is an en dash, not a hyphen
                if len(date_parts) == 1:
                    date_parts = date_range.split('--')  # Try double hyphen as fallback
                
                start_date = date_parts[0].strip()
                end_date = date_parts[1].strip() if len(date_parts) > 1 else "Present"
                
                company = experience_match.group(3).strip()
                location = experience_match.group(4).strip()
                
                current_experience = {
                    "company": company,
                    "title": title,
                    "location": location,
                    "bullets": [],
                    "start_date": start_date,
                    "end_date": end_date
                }
                if verbose:
                    print(f"Found experience: {title} at {company}")
            
            # Check for resume items/bullets
            item_match = resume_item_pattern.search(line)
            if item_match and current_experience:
                bullet = item_match.group(1)
                current_experience["bullets"].append(bullet)
                if verbose:
                    print(f"Added bullet to experience: {bullet[:50]}...")
        
        i += 1
    
    # Add the last project if any
    if current_project:
        result["Projects"].append(Project(
            current_project["name"], 
            current_project["tools"], 
            current_project["bullets"]
        ))
    
    # Add the last experience if any
    if current_experience:
        result["Experience"].append(Experience(
            current_experience["company"],
            current_experience["title"],
            current_experience["location"],
            current_experience["bullets"],
            current_experience["start_date"],
            current_experience["end_date"]
        ))
    
    if verbose:
        print(f"Parsed {len(result['Projects'])} projects and {len(result['Experience'])} experiences.")
        
        for project in result["Projects"]:
            print(f"Project: {project.name}, Tools: {project.tools}, Bullets: {project.bullets}")
        
        for experience in result["Experience"]:
            print(f"Experience: {experience.company}, Title: {experience.title}, Location: {experience.location}, Start Date: {experience.start_date}, End Date: {experience.end_date}, Bullets: {experience.bullets}")
    
    return result

def parseFromFile(file_path, verbose=False):
    """
    Parses a resume from a file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Remove any markdown code block indicators if present
    text = text.replace('```plaintext', '').replace('```', '')
    
    if verbose:
        print(f"Read {len(text)} characters from {file_path}")
    
    return parseFromText(text, verbose)
