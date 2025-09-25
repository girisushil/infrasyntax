import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';

const getLanguage = (fileType) => {
if (!fileType) return 'bash';
const ft = fileType.toLowerCase();
if (ft.includes('yml') || ft.includes('yaml')) return 'yaml';
if (ft.includes('dockerfile')) return 'dockerfile';
if (ft.includes('.conf')) return 'nginx';
if (ft.includes('.tf')) return 'terraform';
return 'bash';
};

export const ResultItem = ({ result }) => {
return (
<div className="result-item">
{result.associated_comments && <p className="comment">{result.associated_comments}</p>}
<div className="code-block">
<SyntaxHighlighter language={getLanguage(result.file_type)} style={vscDarkPlus} showLineNumbers>
{result.raw_code_snippet}
</SyntaxHighlighter>
</div>
<div className="metadata">
<span>⭐ {result.repository_stars}</span>
<a href={result.source_repository} target="_blank" rel="noopener noreferrer">
{result.source_repository.replace('https://github.com/', '')}
</a>
</div>
</div>
);
};
