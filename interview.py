import os
import openai
from dotenv import load_dotenv
from parse import parseFromFile
from user import User

class Interviewer:
    def __init__(self, user: User):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError('OPENAI_API_KEY not found in .env file')
        self.client = openai.OpenAI(api_key=self.api_key)
        self.user = user
        self.history = []

    def ask_openai(self, prompt, stop=None):
        response = self.client.chat.completions.create(
            model="gpt-4.1",
            messages=prompt,
            stop=stop
        )
        return response.choices[0].message.content.strip()

    def start_interview(self):
        print("Welcome to the Resume Grill! Type 'exit' to quit, or 'idk' for an example answer.\n")
        # Updated system prompt for bullet-point-specific questions
        system_prompt = (
            "You are a tough technical interviewer, and a senior software engineer with 10+ years of experiences. "
            "Ask detailed, challenging questions about the candidate's resume, "
            "focusing on specific bullet points from their experience or projects. "
            "Reference the bullet point in your question (quote or paraphrase it). "
            "Ask one question at a time, wait for the candidate's answer before asking a follow-up. "
            "If the candidate says 'idk', provide a model answer based on their resume, then ask two follow-up questions about the same or related bullet points."
        )
        prompt = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here is my resume: {self.user.to_text()}"}
        ]
        first_question = True
        while True:
            if first_question:
                question = self.ask_openai(prompt + self.history + [{"role": "assistant", "content": "Ask a resume grill question about a specific bullet point."}])
                print(f"\nInterviewer: {question}\n")
                self.history.append({"role": "assistant", "content": question})
                first_question = False
            answer = input("You: ")
            if answer.lower() == 'exit':
                print("Interview ended.")
                break
            elif answer.lower() == 'idk':
                # Generate a model answer
                model_answer = self.ask_openai(prompt + self.history + [{"role": "user", "content": "idk"}, {"role": "assistant", "content": "Provide a model answer based on the resume."}])
                print(f"\nExample answer: {model_answer}\n")
                self.history.append({"role": "user", "content": model_answer})
                # Ask two follow-up questions
                for i in range(2):
                    followup = self.ask_openai(prompt + self.history + [{"role": "assistant", "content": "Ask a follow-up resume grill question about a specific bullet point or related detail."}])
                    print(f"\nInterviewer: {followup}\n")
                    self.history.append({"role": "assistant", "content": followup})
                    answer = input("You: ")
                    if answer.lower() == 'exit':
                        print("Interview ended.")
                        return
                    self.history.append({"role": "user", "content": answer})
                # After two follow-ups, continue to next main question
                first_question = True
                continue
            self.history.append({"role": "user", "content": answer})
            # Generate a follow-up question
            followup = self.ask_openai(prompt + self.history + [{"role": "assistant", "content": "Ask a follow-up resume grill question about a specific bullet point or related detail."}])
            print(f"\nInterviewer: {followup}\n")
            self.history.append({"role": "assistant", "content": followup})
            answer = input("You: ")
            if answer.lower() == 'exit':
                print("Interview ended.")
                break
            self.history.append({"role": "user", "content": answer})
            # After one follow-up, continue to next main question
            first_question = True