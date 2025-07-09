import argparse
from dotenv import load_dotenv
import os
import google.generativeai as genai
import subprocess
import json
from datetime import datetime

load_dotenv()
PROMPT= "You are a linux system assistant, your job is totake a task given by the user," \
    " generate a shell script for that specific task and if its not possible or is not something you should do as a system assistant, return the words NOT POSSIBLE." \
    " When returning the script, dont return anything other than just the plain bash script.Dont even format the script with ```, " \
    "just the raw text. If the task is an error sent by the user, ONLY return a minor explaination explaining the error, not more than one paragraph  .Here is the task given by the user : "
    
SCRIPTREVIEW=True
HISTORYPATH=None
SAVESCRIPT=True

APIKEY=os.getenv("GEMINI_API_KEY")
MODEL=os.getenv("MODEL")
if not APIKEY:
    print("Invalid env")
    exit(1)

genai.configure(api_key=APIKEY)
model = genai.GenerativeModel(MODEL)

def config_load():
    global SCRIPTREVIEW
    global HISTORYPATH
    global SAVESCRIPT
    with open ("./config.json","r") as f:
        if f==None:
            print("Config not found")
            exit(1)
        config = json.load(f)
        SCRIPTREVIEW=config.get("scriptReview",True)
        HISTORYPATH=config.get("historyStorage",None)
        SAVESCRIPT=config.get("saveScripts",False)

        if(SAVESCRIPT==True and HISTORYPATH==None):
            print("Invalid History path")
            exit(1)
       
def script_save(script):
    timestamp = datetime.now().strftime("%Y-%M-%d_%H-%M-%S")
    fileName = f"{HISTORYPATH}/{timestamp}.sh"
    try:
        with open(fileName,"w") as f:
            f.write(script)
    except:
        print("Error saving the script...")

def script_gen(task):
    compiledPrompt = PROMPT + task
    print("please stand by...")
    APIResponse = model.generate_content(compiledPrompt)

    return APIResponse.text


def main():
    config_load()
    parser = argparse.ArgumentParser(description="Gemini Integrated Linux Assistant")
    parser.add_argument("task",type=str,nargs="+",help="Task to be performed")
    args = parser.parse_args()

    task = " ".join(args.task)

    response = script_gen(task)
    if "NOT POSSIBLE" in response:
        print("The task is out of the agent's scope")
        exit(1)
    if SCRIPTREVIEW==True:
        print("======[Task script]======")
        print(response)
        print("======[xxxxxxxxxxx]======")
        confirmation = input("continue?[y/n]")
        if confirmation.lower() not in ["yes","y"]:
            print("Aborted")
            exit(0)

    subprocess.run(response,shell=True,executable="/bin/bash")
    
    if SAVESCRIPT==True:
        script_save(response)


if __name__ == "__main__":
    main()
    
    
    