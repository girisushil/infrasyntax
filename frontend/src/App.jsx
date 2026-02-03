import { useState } from "react";
import axios from "axios";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [auditResults, setAuditResults] = useState({});
  const [auditing, setAuditing] = useState({});

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query) return;
    setLoading(true);
    setAuditResults({});
    try {
      const response = await axios.post("http://127.0.0.1:8000/search", {
        query: query,
        num_results: 10,
      });
      setResults(response.data.results);
    } catch (error) {
      console.error("Search failed:", error);
    }
    setLoading(false);
  };

  const handleAudit = async (code, technology, index) => {
    setAuditing((prev) => ({ ...prev, [index]: true }));
    try {
      const response = await axios.post("http://127.0.0.1:8000/audit", {
        code: code,
        technology: technology,
      });
      setAuditResults((prev) => ({ ...prev, [index]: response.data }));
    } catch (error) {
      console.error("Audit failed:", error);
    }
    setAuditing((prev) => ({ ...prev, [index]: false }));
  };

  // --- NEW HELPER: Truncate at first full stop ---
  const formatDescription = (description) => {
    if (!description) return "";
    const index = description.indexOf(".");
    if (index !== -1) {
      return description.substring(0, index + 1); // Include the dot
    }
    return description;
  };

  return (
    <div className="app-container">
      <header>
        <h1>InfraSyntax 🛡️</h1>
        <p>Secure, Goal-Oriented DevOps Search</p>
      </header>

      <div className="search-section">
        <form onSubmit={handleSearch}>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g., 'terraform s3 bucket private'"
            autoFocus
          />
          <button type="submit" disabled={loading}>
            {loading ? "Searching..." : "Search"}
          </button>
        </form>
      </div>

      <div className="results-list">
        {results.map((item, index) => (
          <div
            key={index}
            className={`result-card ${
              item.is_dependency ? "dependency-card" : ""
            }`}
          >
            <div className="result-header">
              <div className="header-left">
                <span className={`badge ${item.technology}`}>
                  {item.technology}
                </span>

                {/* --- USAGE OF HELPER FUNCTION --- */}
                <h3>{formatDescription(item.description)}</h3>

                {item.is_dependency && (
                  <div className="dependency-tag">
                    🔗 Auto-detected dependency for: "{item.related_to}"
                  </div>
                )}
              </div>

              <button
                className="audit-btn"
                onClick={() => handleAudit(item.code, item.technology, index)}
                disabled={auditing[index]}
                style={{ flexShrink: 0 }}
              >
                {auditing[index] ? "Scanning..." : "🛡️ Check Security"}
              </button>
            </div>

            {/* Audit Result Display */}
            {auditResults[index] && (
              <div
                className={`audit-result ${
                  (auditResults[index]?.safety_score ?? 0) === 100
                    ? "safe"
                    : "risk"
                }`}
              >
                <div className="audit-score">
                  Safety Score:{" "}
                  <strong>{auditResults[index]?.safety_score ?? 0}/100</strong>
                </div>

                {auditResults[index]?.vulnerabilities?.length > 0 && (
                  <ul className="vuln-list">
                    {auditResults[index].vulnerabilities.map((v, i) => (
                      <li key={i}>
                        ⚠️ {v.id || "Unknown"}: {v.name || "Security Issue"}
                      </li>
                    ))}
                  </ul>
                )}

                {auditResults[index]?.safety_score === 100 && (
                  <div className="safe-msg">
                    ✅ No issues found. Safe to use.
                  </div>
                )}
              </div>
            )}

            <div className="code-block">
              <SyntaxHighlighter
                language={
                  item.technology === "terraform" ? "hcl" : item.technology
                }
                style={vscDarkPlus}
                wrapLongLines={true}
              >
                {item.code}
              </SyntaxHighlighter>
            </div>

            <div className="result-footer">
              <span className="source-file">📄 {item.source_file}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
