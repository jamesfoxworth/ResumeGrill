import argparse
from parse import parseFromFile
from user import User
from interview import Interviewer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resume Grill Interview Simulator")
    parser.add_argument('--resume', '-r', type=str, default='resume.txt', help='Path to the resume file')
    args = parser.parse_args()
    user = parseFromFile(args.resume)
    interviewer = Interviewer(user)
    interviewer.start_interview() 