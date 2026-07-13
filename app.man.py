from typing import TypedDict
import Scripts
import asyncio
import os, json
import random


#INIT
args = Scripts.args
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
format = []

for i in os.listdir("Data"):
    ix = i.split(".")
    if ix[-1]=="tex":
        print(i)
        templates.append(".".join(ix[0:-2]))
        format.append(ix[-2]+"latex")



ch = int(input(">>> "))-1

#AI INIT

#INIT END


#TUI 
#Get the tex data
with open(f"Data/{templates[ch]}.{format[ch][0:-5]}.tex") as f:
    base = f.read()

#Find the placeholders

place_holders = Scripts.latex.get_placeholders_tex(base)
replacing_data = {i:None for i in place_holders}

#MD Data

with open(f"Data/{templates[ch]}.md") as f:
    md = Scripts.latex.get_vars_data_md(f.read())
print(Scripts.debug.json.dumps(md, indent=4))


print(replacing_data)

#getting data from user. will replace with AI someday fs. prob not tho
for i in place_holders:
    if replacing_data[i] is None:
        replacing_data[i] = input(f"Replacing text for {i}: ")
    else:
        print(f"Replacing text for {i}: {replacing_data[i]}")




#I could just combine but meh for ease to read. (says the guy who wrote some devious lines)
for i in replacing_data:
    base = base.replace("[["+i+"]]", replacing_data[i])
base = base.replace("..", ".")
print(base)


#TESTING
payload = {
    "compiler": format[ch],
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

