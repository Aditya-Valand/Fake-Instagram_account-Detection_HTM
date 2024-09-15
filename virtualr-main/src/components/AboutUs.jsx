import React from 'react';

function AboutUs() {
  return (
    <div>
      <div className="max-w-screen-lg mx-auto p-6 pt-32">
        <h1 className="text-4xl font-bold text-white-800 mb-6">About Us</h1>
        <p className="text-lg text-white-600 leading-relaxed mb-4">
          Sniffect is an AI-driven platform that helps users detect fake Instagram accounts with ease. By analyzing data and patterns, Sniffect provides a probability score to indicate how likely an account is fake. Our goal is to foster a safer social media experience, giving users the confidence to navigate Instagram without fear of fraud or deception.
        </p>
        <p className="text-lg text-white-600 leading-relaxed mb-4">
          Our platform offers:
          <ul className="list-disc pl-6 mt-2">
            <li><strong>Fake Account Detection:</strong> Paste any Instagram account link, and our system analyzes it to give you the likelihood of it being fake.</li>
            <li><strong>AI-Powered Analysis:</strong> We utilize machine learning to ensure accurate and efficient results.</li>
            <li><strong>Detailed Reports:</strong> Get a comprehensive statistical breakdown of suspicious account activities.</li>
            <li><strong>Secure & Confidential:</strong> All user queries are handled with the utmost privacy and data protection.</li>
          </ul>
        </p>
        <p className="text-lg text-white-600 leading-relaxed mb-4">
          At Sniffect, we aim to revolutionize how people detect fake social media accounts, creating a more trustworthy online environment. Our tools are easy to use, fast, and reliable, making the process seamless for everyone.
        </p>
      </div>
    </div>
  );
}

export default AboutUs;
