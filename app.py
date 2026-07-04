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

if server is None:
    print("No servers reachable.")
    raise Scripts.latex.requests.exceptions.InvalidURL
else:
    print(f"Using server: {server}")

    #TESTING
    payload = {
        "compiler": "pdflatex",
        "resources": [
            {
                "main": "true",
                "content":""
            }
        ]
    }

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

