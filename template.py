# Automating the project's folder structure

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'pneuDetection'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "app.py",
    "main.py",
    "setup.py",
    "research/trials.ipynb", # notebook experiments
    "requirements.txt",
    "Dockerfile",
    "templates/index.html" # necc for Flask web-app
]

for filepath in list_of_files:
    filepath = Path(filepath) # handling Windows filepath issues
    filedir, filename = os.path.split(filepath) # establishing folder + file
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    
    else:
        logging.info(f"{filename} already exists.")