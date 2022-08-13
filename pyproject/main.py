from enum import Enum
from fastapi import FastAPI
from .core.config import router

app = FastAPI()
app.include_router(router)


class T5_ModelLanguages(str, Enum):
    ENGLISH = "English"
    FRENCH = "French"
    ROMANIAN = "Romanian"
    GERMAN = "German"


@app.post("/translate")
def root(source_language: T5_ModelLanguages, destination_language: T5_ModelLanguages):
    return {
        "source_language": source_language,
        "destination_language": destination_language,
    }
