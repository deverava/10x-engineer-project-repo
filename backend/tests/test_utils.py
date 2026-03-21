from app.utils import sort_prompts_by_date
from app.models import Prompt

def test_sort_prompts_by_date_empty():
    sorted_prompts = sort_prompts_by_date([])
    assert sorted_prompts == []

def test_sort_prompts_by_date_single():
    prompt = Prompt(title="Test", content="This is a test.")
    sorted_prompts = sort_prompts_by_date([prompt])
    assert sorted_prompts == [prompt]

def test_sort_prompts_by_date_multiple():
    prompt1 = Prompt(title="Test1", content="Content1")
    prompt2 = Prompt(title="Test2", content="Content2")
    prompt1.created_at = prompt1.updated_at = prompt2.created_at = prompt2.updated_at
    sorted_prompts = sort_prompts_by_date([prompt2, prompt1], descending=True)
    assert sorted_prompts == [prompt2, prompt1]

def test_sort_prompts_edge_cases():
    prompts = [
        Prompt(title="Test", content="Content"),
        Prompt(title="Another Test", content="Another Content")
    ]
    sorted_prompts = sort_prompts_by_date(prompts)
    assert len(sorted_prompts) == 2