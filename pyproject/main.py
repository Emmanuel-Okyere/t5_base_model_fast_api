"""Entry point the fast api"""

from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from transformers import T5ForConditionalGeneration, T5Tokenizer
from .translate_service import translate_text
from .core.config import router
from .schemes.translate import Translations


app = FastAPI()
app.include_router(router)


tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)


@app.get("/", include_in_schema=False)
async def root():
    """Default root for the application where users get redirected to /doc"""
    return RedirectResponse(url="/docs")


@app.post(
    "/translate",
    status_code=status.HTTP_200_OK,
    response_description="Text Translated",
)
async def translate(request: Translations):
    """Get the text from the user and translate to desired language"""
    source_language = request.source_language
    destination_language = request.destination_language
    input_text = request.input_text
    if source_language == destination_language:
        return input_text
    texts = translate_text(
        model, tokenizer, source_language, destination_language, input_text
    )
    if texts == "":
        return ""
    return texts
