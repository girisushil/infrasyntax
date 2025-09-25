import React, { useState } from 'react';
import { searchApi } from './services/api';
import { ResultItem } from './components/ResultItem';
import './App.css';

function App() {
const [query, setQuery] = useState('');
const [results, setResults] = useState([]);
const [loading, setLoading] = useState(false);
const [error, setError] = useState('');
const [searched, setSearched] = useState(false);

const handleSearch = async (e) => {
e.preventDefault();
if (!query.trim()) return;

setLoading(true);
setError('');
setResults([]);
setSearched(true);

try {
  const response = await searchApi.search(query);
  setResults(response.data.results);
} catch (err) {
  setError('Failed to fetch results. Please ensure the backend is running and reachable.');
  console.error(err);
} finally {
  setLoading(false);
}
};

return (
<div className="container">
<header>
<h1>InfraSyntax ⚙️</h1>
<p>Your production-ready search engine for configuration files.</p>
</header>

  <form onSubmit={handleSearch} className="search-form">
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="e.g., redirect http to https in nginx"
    />
    <button type="submit" disabled={loading}>
      {loading ? 'Searching...' : 'Search'}
    </button>
  </form>

  <div className="results-area">
    {loading && <div className="spinner"></div>}
    {error && <p className="error">{error}</p>}
    {!loading && searched && results.length === 0 && (
      <p className="no-results">No results found. Try a different query!</p>
    )}
    <div className="results-container">
      {results.map((result, index) => (
        <ResultItem key={`${result.source_repository}-${index}`} result={result} />
      ))}
    </div>
  </div>
</div>
);
}

export default App;
