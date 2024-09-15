import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import FeatureSection from "./components/FeatureSection";
import Footer from "./components/Footer";
import Textarea from "./components/Textarea"; // Changed from Textlink to Textarea
import ProgressChart from "./components/ProgressChart";
import AboutUs from "./components/AboutUs";
import ContactUs from "./components/ContactUs";
import RegistrationForm from './components/RegistrationForm';
import LoginForm from './components/LoginForm';
const App = () => {
  const progressValue = 75;

  return (
    <Router>
      <div className="bg-gradient max-w-7xl mx-auto">
        <Navbar />
        <main className="pt-20 px-6">
          <Routes>
            <Route path="/" element={
              <>
                <HeroSection />
                <div className="text-center py-3 px-5">
                  <h2>Enter the Account Link Below</h2>
                  <Textarea />
                </div>
                {/* <ProgressChart progress={progressValue} /> */}
                <FeatureSection />
              </>
            } />
            <Route path="/about" element={<AboutUs />} />
            <Route path="/contact" element={<ContactUs />} />
            <Route path="/features" element={<FeatureSection />} />
            <Route path="/signup" element={<RegistrationForm />} />
            <Route path="/signin" element={<LoginForm />} />
            
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;