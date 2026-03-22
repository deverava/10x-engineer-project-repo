import { apiRequest } from "./client";

export async function getPrompts({ collectionId = "", search = "" } = {}) {
  const params = new URLSearchParams();

  if (collectionId) {
    params.append("collection_id", collectionId);
  }

  if (search) {
    params.append("search", search);
  }

  const query = params.toString();
  return apiRequest(`/prompts${query ? `?${query}` : ""}`);
}

export async function getPrompt(id) {
  return apiRequest(`/prompts/${id}`);
}

export async function createPrompt(data) {
  return apiRequest("/prompts", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function updatePrompt(id, data) {
  return apiRequest(`/prompts/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
  });
}

export async function deletePrompt(id) {
  return apiRequest(`/prompts/${id}`, {
    method: "DELETE",
  });
}