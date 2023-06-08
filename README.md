# Python Question Prompter using OpenAI GPT-4

This Python script interacts with the OpenAI GPT-4 API to help you rephrase a question to get better results from the model. It takes a question from the command line, sends it to the OpenAI API, and prints out the model's suggestion on how to rephrase the question.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages. In your terminal, navigate to the repository's directory and run:
    ```
    pip install -r requirements.txt
    ```
3. Get your OpenAI API key from the [OpenAI API Dashboard](https://platform.openai.com/account/api-keys) (you'll need to create an account if you don't have one).
4. Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`. This can be done in the terminal session where you're running your script:
    - On Unix/Linux/macOS:
        ```
        export OPENAI_API_KEY='your-api-key'
        ```
    - On Windows:
        ```
        set OPENAI_API_KEY=your-api-key
        ```

## Usage

In your terminal, navigate to the directory of the script and run: 
```
python proompter.py "your question here"
```
Replace `"your question here"` with the question you want to ask.
