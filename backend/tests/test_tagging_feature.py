def test_create_prompt_with_tags(client):
    response = client.post(
        "/prompts",
        json={
            "title": "Docker Prompt",
            "content": "Explain Docker",
            "description": "Testing tags",
            "tags": ["docker", "devops"]
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert "tags" in data
    assert data["tags"] == ["docker", "devops"]


def test_update_prompt_tags(client):
    create_response = client.post(
        "/prompts",
        json={
            "title": "Update Tags",
            "content": "Before update",
            "tags": ["old"]
        }
    )

    prompt_id = create_response.json()["id"]

    update_response = client.put(
        f"/prompts/{prompt_id}",
        json={
            "title": "Update Tags",
            "content": "After update",
            "tags": ["new", "updated"]
        }
    )

    assert update_response.status_code == 200
    data = update_response.json()

    assert data["tags"] == ["new", "updated"]


def test_filter_prompts_by_tag(client):
    client.post(
        "/prompts",
        json={
            "title": "Docker Prompt",
            "content": "Docker content",
            "tags": ["docker"]
        }
    )

    client.post(
        "/prompts",
        json={
            "title": "AWS Prompt",
            "content": "AWS content",
            "tags": ["aws"]
        }
    )

    response = client.get("/prompts?tag=docker")

    assert response.status_code == 200
    data = response.json()

    assert len(data["prompts"]) == 1
    assert data["prompts"][0]["title"] == "Docker Prompt"