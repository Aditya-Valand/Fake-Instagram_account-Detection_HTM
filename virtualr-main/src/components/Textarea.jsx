import React, { useState } from 'react';
import axios from 'axios';
import ProgressChart from './ProgressChart';
import AccountStatsDashboard from './AccountStatsDashboard';
import EngagementRateCalculator from './EngagementRateCalculator';

const Textlink = () => {
  const [link, setLink] = useState('');
  const [error, setError] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const isValidInstagramLink = (url) => {
    try {
      const parsedUrl = new URL(url);
      return parsedUrl.hostname === 'www.instagram.com' || parsedUrl.hostname === 'instagram.com';
    } catch {
      return false;
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setAnalysis(null);
  
    if (!link.trim()) {
      setError('Please enter an Instagram account link.');
      return;
    }
    if (!isValidInstagramLink(link)) {
      setError('Please enter a valid Instagram account link.');
      return;
    }
  
    setIsLoading(true);
  
    try {
      const token = localStorage.getItem('token'); // Get the JWT token from localStorage
  
      const response = await axios.post(
        'http://localhost:3001/analyze/account', 
        { profile_link: link },
        {
          headers: {
            'Authorization': `Bearer ${token}` // Include the JWT token in the request headers
          }
        }
      );
      
      setAnalysis(response.data);
    } catch (error) {
      setError(error.response?.data?.error || 'An error occurred during analysis');
    } finally {
      setIsLoading(false);
    }
  };
  

  return (
    <div className="max-w-4xl mx-auto p-4">
      <form onSubmit={handleSubmit} className="space-y-2 mb-8">
      <div className="flex flex-col items-center space-y-4">
        
        <input
          type="text"
          value={link}
          onChange={(e) => setLink(e.target.value)}
          placeholder="Paste Instagram account link here"
          className="w-1/2 p-2 border rounded text-sm"
          />
        <button 
          type="submit" 
          className="w-64 bg-gradient-to-br from-[#FF057C] via-[#8D0B93] to-[#321575] text-white p-2 rounded hover:bg-blue-600 text-sm"
          disabled={isLoading}
          >
          {isLoading ? 'Analyzing...' : 'Check Account'}
        </button>
          </div>
      </form>
      {error && (
        <div className="mt-2 p-2 bg-red-100 border border-red-400 text-red-700 rounded text-sm">
          {error}
        </div>
      )}
      {analysis && (
        <div className="mt-4">
          <div className="text-center mb-8">
            <ProgressChart prediction={analysis.prediction} />
            <p className="mt-2 text-lg font-semibold">{analysis.message}</p>
            <p className="text-sm text-gray-600">Prediction Score: {(analysis.prediction * 100).toFixed(2)}%</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <AccountStatsDashboard stats={analysis.accountStats} />
            {/* <EngagementRateCalculator posts={analysis.recentPosts} followers={analysis.accountStats.followers} /> */}
          </div>
        </div>
      )}
    </div>
  );
};

export default Textlink;