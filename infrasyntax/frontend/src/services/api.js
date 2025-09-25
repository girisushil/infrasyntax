import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const apiClient = axios.create({
baseURL: API_URL,
headers: {
'Content-Type': 'application/json',
},
});

export const searchApi = {
search: (query) => {
return apiClient.get('/api/search', { params: { q: query } });
},
};
