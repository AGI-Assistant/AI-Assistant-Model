# AGI Assistant
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
  - [AGI-Assistant-Backend](#agi-assistant-backend)
  - [AGI-Assistant-Model](#agi-assistant-model)
  - [AGI-Assistant-Frontend](#agi-assistant-frontend)
- [References](#references)
  - [Lucidchart](#lucidchart)

## Installation
Since this repository contains multiple models, the installation process is
split into multiple parts. <br>
Depending on which model you want to use, you need to follow the corresponding installation guide. <br>

### Installing the OpenAI Models locally
1. To use the OpenAI API, you need to create an account and get an API key. <br>
2. Use the .env.example file to create a .env file. <br>
3. Add your API keys to the .env file (Backend & OpenAi). <br>
4. Install the requirements.txt file. <br>
```bash
pip install -r requirements.txt
```
5. To start the application locally, you run the src_openai/main.py file. <br>
```bash
src_openai/main.py
```

### Building the Docker Image for the OpenAI Models
...

### Llama Models
...

### Building the Docker Image for the Llama Models
...

## Usage
...

## Project Structure
### AGI-Assistant-Backend
This repository handles the data traffic and connects all the different components. <br>
### AGI-Assistant-Frontend
This repository holds everything required to run the frontend of the application. <br>
### AGI-Assistant-Model
This repository holds everything required to run the machine learning model. <br>

## References
### Repositories
Backend:   https://github.com/Knaeckebrothero/AGI-Assistant-Backend <br>
Frontend:  https://github.com/Knaeckebrothero/AGI-Assistant-Frontend <br>
Model:     https://github.com/Knaeckebrothero/AGI-Assistant-Model <br>

### Google Drive
https://drive.google.com/drive/folders/1Y2YULB6s9xqoHco0fPvO1QiQ1kFSJ2QU?usp=sharing

### Lucidchart
https://lucid.app/documents#/documents?folder_id=336580960 <br>
