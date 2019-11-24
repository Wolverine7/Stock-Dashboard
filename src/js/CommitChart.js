import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'Open',
          backgroundColor: 'rgba(71, 183,132,.5)',
          data: ["144.2600", "139.6600", "136.6100", "137.0000", "136.6300", "123.8500", "130.5300", "118.9500", "112.8900", "103.7750", "99.5500", "107.9000"],
        },
          {
          label: 'Close',
          backgroundColor: '#f87979',
          data: ["149.9700", "143.3700", "139.0300", "137.8600", "136.2700", "133.9600", "123.6800", "130.6000", "117.9400", "112.0300", "104.4300", "112.0300",],
        },
      ]
    })
  }
}