# Code Quality Analyzer by DeepSeek

A powerful tool that leverages the `deepseek-r1:1.5b` model to analyze, summarize, suggest improvements, and offer alternative approaches for your code. This app helps developers improve code quality by providing detailed insights into code performance, structure, and optimization opportunities.

## Features

- **Code Analyzer**: Provides a detailed analysis of the code, identifying areas for improvement and offering insights on code quality.
- **Code Summary**: Summarizes the functionality and structure of your code, helping you understand the core logic at a glance.
- **Code Improvement**: Suggests optimizations and improvements to enhance code readability, efficiency, and maintainability.
- **Alternative Approach**: Offers alternative approaches or optimizations for your code, helping you explore different ways to achieve the same goal.
- **Full Code Analysis**: Runs all analysis functions at once and displays the results in tabs for easy comparison.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **DeepSeek (Ollama)**: For natural language processing, using the `deepseek-r1:1.5b` model to analyze and process code.
- **Python**: The primary programming language used to develop the app.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Streamlit
- LangChain (for integrating DeepSeek)


 Ensure you have access to the DeepSeek API via Ollama and that your environment is set up accordingly.

### Running the App

To run the application, use the following command:

```bash
streamlit run app.py


How It Works
Code Analyzer: Paste your code into the text area and click "Analyze Code" to get a breakdown of the code's functionality and areas for improvement.
Code Summary: Use the "Summarize Code" option to get a concise summary of what the code does.
Code Improvement: After pasting your code, click "Suggest Improvements" to receive recommendations on how to improve it.
Alternative Approach: This option will suggest alternative coding approaches for achieving the same task.
Full Code Analysis: This will run all the analysis processes at once and provide you with a full breakdown of your code in a tabbed interface.
