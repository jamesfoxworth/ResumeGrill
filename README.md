# ResumeGrill

A Python tool for practicing technical interviews based on your own resume.

ResumeGrill simulates a tough, senior software engineer interviewer who asks you detailed, challenging questions about your actual experience and projects. If you get stuck, it can provide model answers and keep the conversation going with follow-up questions.

---


## Usage

The tool supports automatic parsing for the popular "Jake's Resume" template, written in LaTex.
Copy the LaTex code into a text file, and pass it as an argument to main.

```bash
python main.py --resume my_resume.txt
```

During the interview:
- Type your answers and press Enter.
- Type `idk` to see a model answer and get two follow-up questions.
- Type `exit` to quit the session.

---

