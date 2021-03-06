import { Bar } from 'react-chartjs-2';
import { defaults } from 'react-chartjs-2';
import { useEffect, useState, useRef } from 'react';

const Bargraph = () => {
  const data = {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    datasets: [
      {
        label: '# of times clickbait was caught',
        data: [4, 5, 6, 7, 8],
        backgroundColor: [
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 99, 132, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(54, 162, 235, 0.2)',
        ],
        borderColor: [
          'rgba(255, 159, 64, 1)',
          'rgba(255, 99, 132, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(54, 162, 235, 1)',
          // 'rgba(255, 206, 86, 1)',
          // 'rgba(75, 192, 192, 1)',
        ],
        borderRadius: 3,
        borderWidth: 1,
      },
    ],
  };

  const graphOptions = {
    scales: {
      x: {
        ticks: {
          font: {
            family: 'Quicksand',
            size: 20,
          },
        },
      },
      y: {
        ticks: {
          font: {
            family: 'Quicksand',
            size: 15,
          },
        },
      },
    },
  };

  return (
    <div>
      <div className="bar-graph-container">
        <h2>Clickbait detector</h2>
        <Bar data={data} options={graphOptions} />
      </div>
    </div>
  );
};

export default Bargraph;
