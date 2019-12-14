<template>
    <div id="charting">
        <canvas id="bar-chart">

        </canvas>
    </div>
</template>

<script>
    // import { Bar } from 'vue-chartjs'

export default {
    data: () => ({
        response: null,
        symbol: '',
        labels: [],
        close: [],
        open: []
    }),
    mounted() {
         const axios = require('axios')
         const Chart = require('chart.js');
         axios.get('http://localhost:8000/portfolio/api/monthly').then(
             response => {
                 this.response = response.data["Monthly Time Series"]
                 this.symbol = response.data["Meta Data"]["2. Symbol"]
                 var stop = 12;
                 var count = 0;
                 var count2 = 0;

                for(var i in this.response){
                      this.open.push(this.response[i]["1. open"])
                      count++;
                      if(stop ==count){
                          break;
                      }
                }
                for(var ii in this.response){
                      this.close.push(this.response[ii]["4. close"])
                      count2++;
                      if(stop ==count2){
                          break;
                      }
                }
                var ctx = document.getElementById('bar-chart').getContext('2d');

                  var myChart = new Chart(ctx, {
                      type: 'bar',
                      data: {
                      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                      datasets: [
                          {
                              label: 'Open',
                              data: this.open,
                              backgroundColor: 'rgba(71, 183,132,.5)',
                          },
                          {
                              label: 'Close',
                              data: this.close,
                              backgroundColor: '#f87979',
                          },
                      ]
                  }
                  }
                )
                console.log(this.open, this.close)
             }).catch(e => {
              console.log(e)
            })


    }
}

</script>

<style>
    #charting{
        width: 600px;
        height: 600px;
    }
</style>