import pytest
from app.storage import Storage
from app.models import Prompt

@pytest.fixture
def storage():
    return Storage()

def test_create_prompt(storage):
    prompt = Prompt(title="Test", content="This is a test.")
    storage.create_prompt(prompt)
    assert prompt.id in storage._prompts

def test_get_prompt(storage):
    prompt = Prompt(title="Test", content="This is a test.")
    storage.create_prompt(prompt)
    retrieved_prompt = storage.get_prompt(prompt.id)
    assert retrieved_prompt == prompt

def test_delete_prompt(storage):
    prompt = Prompt(title="Test", content="This is a test.")
    storage.create_prompt(prompt)
    storage.delete_prompt(prompt.id)
    assert storage.get_prompt(prompt.id) is None

def test_data_persistence(storage):
    prompt = Prompt(title="Test", content="This is a test.")
    storage.create_prompt(prompt)
    # Simulate end of session
    storage.clear()
    persisted_prompt = storage.get_prompt(prompt.id)
    assert persisted_prompt is None

def test_delete_nonexistent_prompt(storage):
    result = storage.delete_prompt("nonexistent-id")
    assert not result  # deletion should fail gracefully