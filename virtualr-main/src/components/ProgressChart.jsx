import React from "react";
import { Doughnut } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

// Register necessary components
ChartJS.register(ArcElement, Tooltip, Legend);

// Define the ProgressChart component
const ProgressChart = ({
  prediction,
  color = "#36A2EB", // Default progress color
  backgroundColor = "#E0E0E0", // Default background color
}) => {
  // Convert prediction to percentage
  const progress = prediction * 100;

  // Define the data for the Doughnut chart
  const data = {
    datasets: [
      {
        data: [progress, 100 - progress], // The progress and remaining
        backgroundColor: [color, backgroundColor], // Colors for the chart
        borderWidth: 0, // No border
      },
    ],
  };

  // Define the options for the Doughnut chart
  const options = {
    cutout: "70%", // Adjust the cutout size for the center
    responsive: true,
    plugins: {
      legend: {
        display: false, // Hide the legend
      },
      tooltip: {
        enabled: false, // Disable tooltips
      },
    },
  };

  return (
    <div className="flex items-center justify-center"> {/* Centering */}
      <div className="relative w-48 h-48">
        <Doughnut data={data} options={options} />
        <div className="absolute inset-0 flex items-center justify-center">
          <span className="text-2xl font-bold">{`${progress.toFixed(1)}%`}</span>
        </div>
      </div>
    </div>
  );
};

export default ProgressChart;