from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successesfuly", "developer": developer}

@app.post("/projects/")
def create_project(project: Project):
    return{"message": "Project created successfully", "Project": project}

@app.get("/projects/")
def get_project():
    sample_project = Project(
        title = "Sample Project",
        description = "this is a sample Project",
        language = ["python", "JavaScript"],
        lead_developer = Developer(name="John Doe", experience=5)
    )
    return {"Projects": [sample_project]}