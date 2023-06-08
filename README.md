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
# python proompter.py "your question here"

Replace `"your question here"` with the question you want to ask.

## Add to PATH

To be able to run this script from anywhere, add it to your system's PATH. The method for doing this will vary depending on your operating system.

### Unix/Linux/macOS

1. Open your terminal.
2. Open your shell's profile script (.bashrc, .bash_profile, .zshrc, etc.) with your preferred text editor (like nano, vim, etc.). For example:
    ```
    nano ~/.bashrc
    ```
3. Add the following line at the end of the file:
    ```
    export PATH=$PATH:/path/to/directory
    ```
    Replace `/path/to/directory` with the path to the directory that contains the `proompter.py` script.
4. Save and exit the text editor.
5. To make the changes take effect immediately, source your profile script:
    ```
    source ~/.bashrc
    ```
6. Now you should be able to just use the command `proompter.py` from anywhere in the terminal.

### Windows

1. Right-click on 'Computer' and click on 'Properties'.
2. Click on 'Advanced system settings'.
3. In the System Properties window, click on the 'Environment Variables' button.
4. In the Environment Variables window, select 'Path' in the user variables section and click 'Edit'.
5. In the Edit Environment Variable window, add the full path to the directory containing `proompter.py` at the end of the 'Variable value' field, preceded by a semicolon (`;`).
6. Click OK in each window to close it.
7. You may need to restart your command prompt or computer for the changes to take effect.

After adding the script to your PATH, you can run it from anywhere using the command `proompter.py`.
