import { useEffect, useMemo, useState } from "react";
import {
  createPrompt,
  deletePrompt,
  getPrompts,
  updatePrompt,
} from "./api/prompts";
import {
  createCollection,
  deleteCollection,
  getCollections,
} from "./api/collections";
import "./styles/global.css";

const emptyPromptForm = {
  title: "",
  content: "",
  description: "",
  collection_id: "",
};

const emptyCollectionForm = {
  name: "",
  description: "",
};

function App() {
  const [prompts, setPrompts] = useState([]);
  const [collections, setCollections] = useState([]);
  const [selectedCollectionId, setSelectedCollectionId] = useState("");
  const [selectedPrompt, setSelectedPrompt] = useState(null);

  const [search, setSearch] = useState("");
  const [loadingPrompts, setLoadingPrompts] = useState(true);
  const [loadingCollections, setLoadingCollections] = useState(true);
  const [submittingPrompt, setSubmittingPrompt] = useState(false);
  const [submittingCollection, setSubmittingCollection] = useState(false);

  const [error, setError] = useState("");
  const [promptFormError, setPromptFormError] = useState("");
  const [collectionFormError, setCollectionFormError] = useState("");

  const [promptForm, setPromptForm] = useState(emptyPromptForm);
  const [collectionForm, setCollectionForm] = useState(emptyCollectionForm);

  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    loadCollections();
  }, []);

  useEffect(() => {
    loadPrompts();
  }, [selectedCollectionId]);

  const filteredPrompts = useMemo(() => {
    if (!search.trim()) return prompts;

    const term = search.toLowerCase();
    return prompts.filter((prompt) => {
      return (
        prompt.title.toLowerCase().includes(term) ||
        prompt.content.toLowerCase().includes(term) ||
        (prompt.description || "").toLowerCase().includes(term)
      );
    });
  }, [prompts, search]);

  async function loadPrompts() {
    setLoadingPrompts(true);
    setError("");

    try {
      const data = await getPrompts({
        collectionId: selectedCollectionId,
      });
      const promptItems = data.prompts || [];
      setPrompts(promptItems);

      if (promptItems.length > 0) {
        if (!selectedPrompt) {
          setSelectedPrompt(promptItems[0]);
        } else {
          const updatedSelected = promptItems.find(
            (item) => item.id === selectedPrompt.id
          );
          setSelectedPrompt(updatedSelected || promptItems[0]);
        }
      } else {
        setSelectedPrompt(null);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoadingPrompts(false);
    }
  }

  async function loadCollections() {
    setLoadingCollections(true);

    try {
      const data = await getCollections();
      setCollections(data.collections || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoadingCollections(false);
    }
  }

  function handlePromptFormChange(event) {
    const { name, value } = event.target;
    setPromptForm((prev) => ({ ...prev, [name]: value }));
  }

  function handleCollectionFormChange(event) {
    const { name, value } = event.target;
    setCollectionForm((prev) => ({ ...prev, [name]: value }));
  }

  function startCreatePrompt() {
    setPromptForm({
      ...emptyPromptForm,
      collection_id: selectedCollectionId || "",
    });
    setPromptFormError("");
    setIsEditing(false);
  }

  function startEditPrompt(prompt) {
    setPromptForm({
      title: prompt.title || "",
      content: prompt.content || "",
      description: prompt.description || "",
      collection_id: prompt.collection_id || "",
    });
    setPromptFormError("");
    setIsEditing(true);
    setSelectedPrompt(prompt);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  async function handlePromptSubmit(event) {
    event.preventDefault();
    setPromptFormError("");

    if (!promptForm.title.trim() || !promptForm.content.trim()) {
      setPromptFormError("Title and content are required.");
      return;
    }

    setSubmittingPrompt(true);

    const payload = {
      title: promptForm.title.trim(),
      content: promptForm.content.trim(),
      description: promptForm.description.trim() || null,
      collection_id: promptForm.collection_id || null,
      tags: [],
    };

    try {
      let savedPrompt;

      if (isEditing && selectedPrompt) {
        savedPrompt = await updatePrompt(selectedPrompt.id, payload);
      } else {
        savedPrompt = await createPrompt(payload);
      }

      await loadPrompts();
      await loadCollections();
      setSelectedPrompt(savedPrompt);
      setPromptForm({
        ...emptyPromptForm,
        collection_id: selectedCollectionId || "",
      });
      setIsEditing(false);
    } catch (err) {
      setPromptFormError(err.message);
    } finally {
      setSubmittingPrompt(false);
    }
  }

  async function handleDeletePrompt(id) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this prompt?"
    );

    if (!confirmed) return;

    try {
      await deletePrompt(id);
      await loadPrompts();
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleCollectionSubmit(event) {
    event.preventDefault();
    setCollectionFormError("");

    if (!collectionForm.name.trim()) {
      setCollectionFormError("Collection name is required.");
      return;
    }

    setSubmittingCollection(true);

    try {
      await createCollection({
        name: collectionForm.name.trim(),
        description: collectionForm.description.trim() || null,
      });

      setCollectionForm(emptyCollectionForm);
      await loadCollections();
    } catch (err) {
      setCollectionFormError(err.message);
    } finally {
      setSubmittingCollection(false);
    }
  }

  async function handleDeleteCollection(id) {
    const confirmed = window.confirm(
      "Delete this collection? Prompts will remain but be unassigned."
    );

    if (!confirmed) return;

    try {
      await deleteCollection(id);

      if (selectedCollectionId === id) {
        setSelectedCollectionId("");
      }

      await loadCollections();
      await loadPrompts();
    } catch (err) {
      setError(err.message);
    }
  }

  function getCollectionName(collectionId) {
    if (!collectionId) return "Unassigned";
    const match = collections.find((collection) => collection.id === collectionId);
    return match ? match.name : "Unknown Collection";
  }

  return (
    <div className="page">
      <aside className="sidebar">
        <div className="brand">
          <span className="brand-icon">🚀</span>
          <div>
            <h1>PromptLab</h1>
            <p>Prompt workspace</p>
          </div>
        </div>

        <div className="sidebar-section">
          <div className="section-title-row">
            <h2>Collections</h2>
          </div>

          {loadingCollections ? (
            <p className="muted">Loading collections...</p>
          ) : (
            <div className="collection-list">
              <button
                className={`collection-item ${
                  selectedCollectionId === "" ? "active" : ""
                }`}
                onClick={() => setSelectedCollectionId("")}
              >
                <span>All Prompts</span>
              </button>

              {collections.map((collection) => (
                <div
                  key={collection.id}
                  className={`collection-item ${
                    selectedCollectionId === collection.id ? "active" : ""
                  }`}
                >
                  <button
                    className="collection-main"
                    onClick={() => setSelectedCollectionId(collection.id)}
                  >
                    <span>{collection.name}</span>
                  </button>
                  <button
                    className="icon-button danger-text"
                    onClick={() => handleDeleteCollection(collection.id)}
                    title="Delete collection"
                  >
                    ✕
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="sidebar-section">
          <h2>New Collection</h2>

          <form onSubmit={handleCollectionSubmit} className="stack-form">
            <label>
              <span>Name</span>
              <input
                type="text"
                name="name"
                value={collectionForm.name}
                onChange={handleCollectionFormChange}
                placeholder="DevOps"
              />
            </label>

            <label>
              <span>Description</span>
              <textarea
                name="description"
                rows="3"
                value={collectionForm.description}
                onChange={handleCollectionFormChange}
                placeholder="Optional description"
              />
            </label>

            {collectionFormError ? (
              <p className="error-text">{collectionFormError}</p>
            ) : null}

            <button className="primary-button" disabled={submittingCollection}>
              {submittingCollection ? "Creating..." : "Create Collection"}
            </button>
          </form>
        </div>
      </aside>

      <main className="main-content">
        <header className="topbar">
          <div>
            <h2>Prompt Dashboard</h2>
            <p>Manage prompts, collections, and search quickly.</p>
          </div>

          <div className="topbar-actions">
            <input
              className="search-input"
              type="text"
              placeholder="Search prompts..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
            <button className="primary-button" onClick={startCreatePrompt}>
              New Prompt
            </button>
          </div>
        </header>

        {error ? <div className="alert error-alert">{error}</div> : null}

        <section className="form-card">
          <div className="card-header">
            <h3>{isEditing ? "Edit Prompt" : "Create Prompt"}</h3>
            {isEditing ? (
              <button
                className="secondary-button"
                onClick={() => {
                  setIsEditing(false);
                  setPromptForm({
                    ...emptyPromptForm,
                    collection_id: selectedCollectionId || "",
                  });
                }}
              >
                Cancel Edit
              </button>
            ) : null}
          </div>

          <form onSubmit={handlePromptSubmit} className="stack-form">
            <label>
              <span>Title</span>
              <input
                type="text"
                name="title"
                value={promptForm.title}
                onChange={handlePromptFormChange}
                placeholder="Enter prompt title"
              />
            </label>

            <label>
              <span>Content</span>
              <textarea
                name="content"
                rows="5"
                value={promptForm.content}
                onChange={handlePromptFormChange}
                placeholder="Write your prompt content"
              />
            </label>

            <label>
              <span>Description</span>
              <textarea
                name="description"
                rows="3"
                value={promptForm.description}
                onChange={handlePromptFormChange}
                placeholder="Optional description"
              />
            </label>

            <label>
              <span>Collection</span>
              <select
                name="collection_id"
                value={promptForm.collection_id}
                onChange={handlePromptFormChange}
              >
                <option value="">No Collection</option>
                {collections.map((collection) => (
                  <option key={collection.id} value={collection.id}>
                    {collection.name}
                  </option>
                ))}
              </select>
            </label>

            {promptFormError ? (
              <p className="error-text">{promptFormError}</p>
            ) : null}

            <button className="primary-button" disabled={submittingPrompt}>
              {submittingPrompt
                ? isEditing
                  ? "Updating..."
                  : "Creating..."
                : isEditing
                ? "Update Prompt"
                : "Create Prompt"}
            </button>
          </form>
        </section>

        {selectedPrompt ? (
          <section className="detail-card">
            <div className="card-header">
              <div>
                <p className="eyebrow">Selected Prompt</p>
                <h3>{selectedPrompt.title}</h3>
              </div>
              <div className="detail-actions">
                <button
                  className="secondary-button"
                  onClick={() => startEditPrompt(selectedPrompt)}
                >
                  Edit
                </button>
                <button
                  className="danger-button"
                  onClick={() => handleDeletePrompt(selectedPrompt.id)}
                >
                  Delete
                </button>
              </div>
            </div>

            <p className="detail-meta">
              Collection: {getCollectionName(selectedPrompt.collection_id)}
            </p>

            {selectedPrompt.description ? (
              <p className="detail-description">{selectedPrompt.description}</p>
            ) : null}

            <pre className="prompt-preview">{selectedPrompt.content}</pre>
          </section>
        ) : null}

        <section className="list-section">
          <div className="card-header">
            <h3>All Prompts</h3>
            <span className="badge">{filteredPrompts.length}</span>
          </div>

          {loadingPrompts ? (
            <div className="empty-state">Loading prompts...</div>
          ) : filteredPrompts.length === 0 ? (
            <div className="empty-state">
              No prompts found. Create one to get started.
            </div>
          ) : (
            <div className="prompt-grid">
              {filteredPrompts.map((prompt) => (
                <article
                  key={prompt.id}
                  className={`prompt-card ${
                    selectedPrompt?.id === prompt.id ? "selected" : ""
                  }`}
                  onClick={() => setSelectedPrompt(prompt)}
                >
                  <div className="prompt-card-top">
                    <div>
                      <h4>{prompt.title}</h4>
                      <p className="prompt-collection">
                        {getCollectionName(prompt.collection_id)}
                      </p>
                    </div>
                  </div>

                  <p className="prompt-content-snippet">
                    {prompt.content.length > 140
                      ? `${prompt.content.slice(0, 140)}...`
                      : prompt.content}
                  </p>

                  <div className="prompt-card-actions">
                    <button
                      className="secondary-button small"
                      onClick={(e) => {
                        e.stopPropagation();
                        startEditPrompt(prompt);
                      }}
                    >
                      Edit
                    </button>
                    <button
                      className="danger-button small"
                      onClick={(e) => {
                        e.stopPropagation();
                        handleDeletePrompt(prompt.id);
                      }}
                    >
                      Delete
                    </button>
                  </div>
                </article>
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;