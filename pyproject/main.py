"""Entry point the fast api"""
from enum import Enum

from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from transformers import T5ForConditionalGeneration, T5Tokenizer

from .core.config import router
from .schemes.translate import translate_text

app = FastAPI()
app.include_router(router)


tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)


class T5ModelLanguages(str, Enum):
    """Enumerating languages supported by T5-base model"""

    ENGLISH = "English"
    FRENCH = "French"
    ROMANIAN = "Romanian"
    GERMAN = "German"


@app.get("/", include_in_schema=False)
async def root():
    """Default root for the application where users get redirected to /doc"""
    return RedirectResponse(url="/docs")


@app.post(
    "/translate",
    status_code=status.HTTP_200_OK,
    response_description="Text Translated",
)
async def translate(
    source_language: T5ModelLanguages,
    destination_language: T5ModelLanguages,
    input_text,
):
    """Get the text from the user and translate to desired language"""
    if source_language == destination_language:
        return input_text
    texts = translate_text(
        model, tokenizer, source_language, destination_language, input_text
    )
    if texts == "":
        return "can not be translated"
    return texts
