import React, { useRef, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

function Graph() {
    const data = {
        labels: ['January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [
            {
                label: 'Focus %',
                data: [50, 88, 25, 50, 88, 33, 35, 66, 70, 85, 90, 95],
                borderColor: 'rgba(75,192,192,1)',
                borderWidth: 1,
            },
        ],
    };
    const options = {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Month',
                },
            },
            y: {
                title: {
                    display: true,
                    text: 'Focus',
                },
            },
        },
        plugins: {
            legend: {
                display: true,
            },
            tooltip: {
                callbacks: {
                    label: (tooltipItem) => `Focus: ${tooltipItem.raw}`,
                },
            },
        },
    };

    return (
        <div style={{ width: '100%', height: '700px', margin: '0 auto' }} className="fluid-container centred">
            <Line data={data} options={options} />
        </div>
    );
}

export default Graph;