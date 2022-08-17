"""Translates a given text"""

from enum import Enum
from pydantic import BaseModel


class T5ModelLanguages(str, Enum):
    """Enumerating languages supported by T5-base model"""

    ENGLISH = "English"
    FRENCH = "French"
    ROMANIAN = "Romanian"
    GERMAN = "German"


class Translations(BaseModel):
    """The request body parameter declaration"""

    source_language: T5ModelLanguages
    destination_language: T5ModelLanguages
    input_text: str
