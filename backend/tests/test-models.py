from app.models import Prompt
from pydantic import ValidationError
import pytest

def test_prompt_model_validation():
    with pytest.raises(ValidationError):
        Prompt(title="", content="")

def test_prompt_model_default_values():
    prompt = Prompt(title="Test", content="This is a test.")
    assert prompt.created_at is not None
    assert prompt.updated_at is not None

def test_prompt_model_serialization():
    prompt = Prompt(title="Test", content="This is a test.")
    prompt_dict = prompt.dict()
    assert isinstance(prompt_dict, dict)
    assert prompt_dict["title"] == "Test"
    assert prompt_dict["content"] == "This is a test."