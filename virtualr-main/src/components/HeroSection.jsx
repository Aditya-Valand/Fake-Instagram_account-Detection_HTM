import video1 from "../assets/video1.mp4";
import video2 from "../assets/video2.mp4";
import Textlink from "./Textarea";

const HeroSection = () => {
  return (
    <div className="flex flex-col items-center mt-6 lg:mt-20">
      <h1 className=" font-poppins text-4xl sm:text-6xl lg:text-7xl text-center tracking-wide">
      Sniffect - Unmasking Fake Accounts 
        <span className="bg-gradient-to-r from-[#00DBDE] to-[#FC00FF] text-transparent bg-clip-text">
          {" "}
          with Precision
        </span>
      </h1>
      <p className="mt-10 text-lg text-center text-neutral-500 max-w-4xl">
      Paste the link, get the truth. Sniffect makes detecting fake Instagram accounts effortless.
      </p>
      {/* <div className="flex justify-center my-10">
        <a
          href="#"
          className="bg-gradient-to-br from-[#FF057C] via-[#8D0B93] to-[#321575] py-3 px-4 mx-3 rounded-md"
        >
          Start for free
        </a>
        <a href="#" className="py-3 px-4 mx-3 rounded-md border">
          Documentation
        </a>
      </div> */}
      {/* <Textlink/> */}
      {/* <div className="flex mt-10 justify-center">
        <video
          autoPlay
          loop
          muted
          className="rounded-lg w-1/2 border border-orange-700 shadow-sm shadow-orange-400 mx-2 my-4"
        >
          <source src={video1} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <video
          autoPlay
          loop
          muted
          className="rounded-lg w-1/2 border border-orange-700 shadow-sm shadow-orange-400 mx-2 my-4"
        >
          <source src={video2} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div> */}
    </div>
  );
};

export default HeroSection;
