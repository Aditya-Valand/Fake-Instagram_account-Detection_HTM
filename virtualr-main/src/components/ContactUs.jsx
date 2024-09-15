import React from "react";

function ContactUs() {
  return (
    <div>
      <div className="max-w-screen-lg mx-auto p-6 pt-32">
        <h1 className="text-4xl font-bold text-white-800 mb-6">Contact Us</h1>
        <p className="text-lg text-white-600 leading-relaxed mb-4">
          We'd love to hear from you! If you have any questions, feedback, or
          inquiries, please fill out the form below or reach out to us directly.
        </p>
        <form className="space-y-6">
          <div>
            <label
              className="block text-white-700 text-sm font-bold mb-2"
              htmlFor="name"
            >
              Name
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-white-700 leading-tight focus:outline-none focus:shadow-outline"
              id="name"
              type="text"
              placeholder="Your name"
            />
          </div>
          <div>
            <label
              className="block text-white-700 text-sm font-bold mb-2"
              htmlFor="email"
            >
              Email
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-white-700 leading-tight focus:outline-none focus:shadow-outline"
              id="email"
              type="email"
              placeholder="Your email"
            />
          </div>
          <div>
            <label
              className="block text-white-700 text-sm font-bold mb-2"
              htmlFor="message"
            >
              Message
            </label>
            <textarea
              className="shadow appearance-none border rounded w-full py-2 px-3 text-white-700 leading-tight focus:outline-none focus:shadow-outline"
              id="message"
              placeholder="Your message"
              rows="5"
            ></textarea>
          </div>
          <div>
            <button
              className="bg-gradient-to-br from-[#FF057C] via-[#8D0B93] to-[#321575] text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button"
            >
              Send
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default ContactUs;
