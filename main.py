from enum import Enum

from fastapi import FastAPI

# 
# IDEA: get the features for each class 
#

class ClassName(str, Enum):
    bard = "bard"
    alchemist = "alchemist"
    warrior = "warrior"

app = FastAPI()

@app.get("/classes/{class_name}")
async def get_class(class_name: ClassName):
    if class_name == '':
        return {"Classes are: alchemist, bard, warrior"}
    
    if class_name is ClassName.bard:
        return {"class_name": class_name, "message": "Bard features"}

    if class_name is ClassName.warrior:
        return {"class_name": class_name, "message": "Warrior features"}

    if class_name is ClassName.alchemist:
        return {"class_name": class_name, "message": "Alchemist features"}

@app.get("/classes")
async def fetch_classes():
    return {"Classes are: alchemist, bard, warrior"}