export const planetChartData = {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        dataset: [
            {
                label: 'Open',
                data: ["144.2600", "139.6600", "136.6100", "137.0000", "136.6300", "123.8500", "130.5300", "118.9500", "112.8900", "103.7750", "99.5500", "107.9000"],
                backgroundColor: [
                    'rgba(54,73,93,.5)', // Blue
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)',
                    'rgba(54,73,93,.5)'
                ],
                borderColor: [
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                    '#36495d',
                ],
                borderWidth: 3
            },
            {
                label: 'Close',
                data: ["149.9700", "143.3700", "139.0300", "137.8600", "136.2700", "133.9600", "123.6800", "130.6000", "117.9400", "112.0300", "104.4300", "112.0300",],
                backgroundColor: [
                   'rgba(71, 183,132,.5)'
                 ],
                 borderColor: [
                  '#47b784',
                ],
                borderWidth: 3
            }

        ]
    },
    options: {
    responsive: true,
    lineTension: 1,
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          padding: 25,
        }
      }]
    }
  }
};

export default planetChartData