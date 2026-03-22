import { useEffect, useState } from "react";
import { getPrompts } from "../../api/prompts";

function PromptList() {
  const [prompts, setPrompts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchPrompts() {
      try {
        const data = await getPrompts();
        setPrompts(data.prompts || []);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchPrompts();
  }, []);

  if (loading) return <p>Loading prompts...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error}</p>;

  return (
    <div>
      <h2>Prompts</h2>
      {prompts.length === 0 ? (
        <p>No prompts found</p>
      ) : (
        prompts.map((prompt) => (
          <div key={prompt.id} style={{ marginBottom: "16px" }}>
            <h3>{prompt.title}</h3>
            <p>{prompt.content}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default PromptList;