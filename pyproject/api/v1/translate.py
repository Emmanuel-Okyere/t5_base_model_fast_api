from fastapi import APIRouter, status
from pyproject.translate_service import translate_text
from pyproject.schemes.translate import Translations
from transformers import T5ForConditionalGeneration, T5Tokenizer

router = APIRouter(prefix="/api/v1")


tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base", return_dict=True)


@router.post(
    "/translate",
    status_code=status.HTTP_200_OK,
    response_description="Text Translated",
    tags=["Language Translate"],
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
