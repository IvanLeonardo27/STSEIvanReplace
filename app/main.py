from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPLACED_CHARS_FILE = os.path.join(BASE_DIR, "replaced_chars.txt")


class TextRequest(BaseModel):
    text: str


def load_replaced_chars():
    replace_dict = {}
    with open(REPLACED_CHARS_FILE, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.strip().split("=")
                replace_dict[key] = value
    return replace_dict


def replace_chars(text: str, replace_dict: dict) -> str:
    result = ""

    for char in text:
        if char.lower() in replace_dict:
            result += replace_dict[char.lower()]
        else:
            result += char

    return result


@app.post("/replace")
def replace_endpoint(req: TextRequest):
    replace_dict = load_replaced_chars()
    return {"result": replace_chars(req.text, replace_dict)}
