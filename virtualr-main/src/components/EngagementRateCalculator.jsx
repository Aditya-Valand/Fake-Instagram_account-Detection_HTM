import React from 'react';

const EngagementRateCalculator = ({ posts, followers }) => {
  const calculateEngagementRate = () => {
    if (posts.length === 0 || followers === 0) return 0;

    const totalEngagements = posts.reduce((sum, post) => sum + post.likes + post.comments, 0);
    const averageEngagements = totalEngagements / posts.length;
    return (averageEngagements / followers) * 100;
  };

  const engagementRate = calculateEngagementRate();

  return (
    <div className="mt-6 p-4 bg-white shadow rounded-lg">
      <h3 className="text-lg font-semibold mb-2">Engagement Rate</h3>
      <p className="text-3xl font-bold text-blue-600">{engagementRate.toFixed(2)}%</p>
      <p className="text-sm text-gray-600 mt-1">
        Based on average likes and comments per post relative to follower count.
      </p>
    </div>
  );
};

export default EngagementRateCalculator;