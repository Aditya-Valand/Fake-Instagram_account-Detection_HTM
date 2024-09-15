import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const AccountStatsDashboard = ({ stats }) => {
  const data = [
    { name: 'Posts', value: stats.posts },
    { name: 'Followers', value: stats.followers },
    { name: 'Following', value: stats.following },
  ];

  return (
    <div className="mt-8">
      <h3 className="text-xl font-semibold mb-4">Account Statistics</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AccountStatsDashboard;