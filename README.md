# GIL

Gemini Integrated Linux is an innovative CLI AI agent designed to automate Linux commands. It translates human-readable language into executable Linux commands, streamlining development and operational workflows.

## Key Features:
- **Natural Language Processing**: Understands and processes human language to generate precise Linux commands.
- **Automation**: Automates routine and complex Linux tasks, reducing manual effort and potential errors.
- **Gemini API Powered**: Leverages the powerful Gemini API for its advanced language understanding and generation capabilities.

## How it Works:
Users provide natural language instructions, which GIL processes using the Gemini API. The AI agent then translates these instructions into the a bash script, executing them securely and efficiently within the target environment.

## Setup and Usage:

1. Clone the repository
```
git clone <This repo>
```
2. Move into the repo and create a **.env** file with the following variables
```
GEMINI_API_KEY=<Gemini API key>
MODEL=<Model name>
``` 
3. You may tweak the **config.json** file to ypur liking (Optional)
```
{
    "saveScripts":true, (With this true, the executed scripts will be saved in the history)
    "historyStorage":"./history", (Path to the folder you may want to store the scripts)
    "scriptReview":true (This will make the tool ask confirmation before running the script. Will also display the script.)
}

```
5. Create the history folder
```
mkdir history
```
4. Setup the python virtual env
```
python3 venv gilVenv
source gilVenv/bin/activate
pip3 install -r requirements.txt
```
5. Usage is simple
```
python3 gil.py <Task...for eg. display the storage>
```

---
Still under development...
