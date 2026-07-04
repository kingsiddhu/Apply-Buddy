#from langgraph.graph import StateGraph, END
#from langchain_ollama import OllamaLLM
from typing import TypedDict
import Scripts
import asyncio
import os, json
settings_loaded = False

version = 0
if "settings.json" in os.listdir():
    with open("settings.json") as settingsFile:
        data = json.loads(settingsFile.read())
        if version<=data.get("version",-1):

            settings_loaded = True


candidate_servers = [
    "http://localhost:8080",       # your local Docker instance
    "https://skedaddle-cannabis-unnerving.ngrok-free.dev", #My personal Server
    "https://latex.ytotech.com",   # public fallback
]

server = Scripts.latex.get_working_server(candidate_servers)

#Server Failure
if server is None:
    print("No servers reachable.")
    raise Scripts.latex.requests.exceptions.InvalidURL

Scripts.debug.logger(f"Using server: {server}")

#Get base temps
templates=[]
for i in os.listdir("Data"):
    ix = i.split(".")
    print(i)
    if ix[-1]=="tex":
        templates.append(i[0:-4])

#TUI 
print("Choose template")
for i in range(len(templates)):
    print(str(i+1)+".\t"+templates[i])

ch = int(input(">>> "))-1

#Get the tex data
with open("Data/"+templates[ch]+".tex") as f:
    base = f.read()

#Find the placeholders

place_holders = Scripts.latex.get_placeholders_tex(base)
replacing_data = {}

#getting data from user. will replace with AI someday fs. prob not tho
for i in place_holders:
    replacing_data[i] = input(f"Replacing text for {i}: ")

#I could just combine but meh for ease to read. (says the guy who wrote some devious lines)
for i in replacing_data:
    base = base.replace("[["+i+"]]", replacing_data[i])
print(base)
#TESTING
payload = {
    "compiler": "lualatex",
    "resources": [
        {
            "main": "true",
            "content":base
        }
    ]
}
with open("Data/"+templates[ch]+".json") as f:
    payload["resources"].extend(Scripts.parsejson.parse_response(f.read()))
#https://github.com/kingsiddhu/Apply-Buddy/raw/refs/heads/main/Data/SourceSansPro-SemiBold.otf
#TESTING DATA
#{
#    "compiler": "lualatex",
#    "resources": [
#        {
#            "main": "true",
#            "content": "\\documentclass{article}\n \\\usepackage{graphicx}\n  \\\begin{document}\n Hello World\\\\\n \\includegraphics[height=2cm,width=7cm,keepaspectratio=true]{logo.png}\n \\include{page2}\n \\end{document}"
#        },
#        {
#            "path": "logo.png",
#            "url": "https://www.ytotech.com/images/ytotech_logo.png"
#        },
#        {
#            "path": "page2.tex",
#            "file": "VGhpcyBpcyB0aGUgc2Vjb25kIHBhZ2UsIHdoaWNoIHdhcyBwYXNzZWQgYXMgYSBiYXNlNjQgZW5jb2RlZCBmaWxl"
#        }
#    ]
#}"""
#
#"""{
#    "compiler": "pdflatex",
#    "resources": [
#        {
#            "main": True,
#            "content": 
#                "\\documentclass{article}\n\\\begin{document}\nHello World\n\\end{document}",
#            
#        }
#    ],
#}"""

Scripts.latex.compile_latex_to_pdf(server, payload, "testing.pdf")

