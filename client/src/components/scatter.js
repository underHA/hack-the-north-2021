import React, { useState } from 'react';
import { Scatter } from 'react-chartjs-2';

const ScatterChart = ({ clickbait }) => {
  const rand = () => Math.round(Math.random() * 20 - 10);
  const data = {
    datasets: [
      {
        label: 'A dataset',
        data: [
          // x: clickbait[0], y: clickbait[1]
          { x: 0.1, y: 0.2 },
          { x: 0.3, y: 0.4 },
          { x: 0.4, y: 0.5 },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
          //   { x: rand(), y: rand() },
        ],
        backgroundColor: 'rgba(255, 99, 132, 1)',
      },
    ],
  };

  const options = {
    scales: {
      y: {
        min: -1,
        max: 1,
      },
      x: {
        min: -1,
        max: 1,
      },
    },
  };
  return (
    <div>
      <div className="header">
        <h1 className="title">Scatter Chart</h1>
      </div>
      <Scatter data={data} options={options} />
    </div>
  );
};

export default ScatterChart;
