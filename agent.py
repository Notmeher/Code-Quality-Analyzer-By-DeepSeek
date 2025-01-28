import os
from langchain_community.llms import Ollama

class CallAIAgent:
    def __init__(self):
        # Initialize the Ollama LLM with deepseek-r1:1.5b model
        self.llm = Ollama(model="deepseek-r1:1.5b")

    def analyze_code(self, code_text):
        """
        Analyzes code using the deepseek-r1:1.5b model.
        """
        try:
            response = self.llm(f"Analyze the following code:\n\n{code_text}\n\nProvide a summary of the code, identify any areas for improvement, and suggest alternative approaches if any.")
            return response
        except Exception as e:
            return f"Error: {e}"

    def suggest_improvements(self, code_text):
        """
        Suggests improvements for a code snippet using the deepseek-r1:1.5b model.
        """
        try:
            response = self.llm(f"Suggest improvements for the following code:\n\n{code_text}")
            return response
        except Exception as e:
            return f"Error: {e}"

    def summarize_code(self, code_text):
        """
        Summarizes the key functionality of the provided code using the deepseek-r1:1.5b model.
        """
        try:
            response = self.llm(f"Summarize the key functionality and structure of the following code:\n\n{code_text}")
            return response
        except Exception as e:
            return f"Error: {e}"

    def suggest_alternative_approach(self, code_text):
        """
        Suggests alternative approaches for implementing the provided code.
        """
        try:
            response = self.llm(f"Suggest an alternative approach or optimization for the following code:\n\n{code_text}")
            return response
        except Exception as e:
            return f"Error: {e}"
