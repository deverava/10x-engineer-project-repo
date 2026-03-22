import { apiRequest } from "./client";

export async function getCollections() {
  return apiRequest("/collections");
}

export async function createCollection(data) {
  return apiRequest("/collections", {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function deleteCollection(id) {
  return apiRequest(`/collections/${id}`, {
    method: "DELETE",
  });
}