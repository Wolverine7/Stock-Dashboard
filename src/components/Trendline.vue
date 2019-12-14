<template>
    <div id="line">
        <canvas id="line-chart">

        </canvas>
    </div>
</template>

<script>


    export default {
        name: 'Trendline',
         data: () => ({
            response: null,
            symbol:'',
            labels:[],
            data: []
        }),
        mounted(){
            const axios = require('axios')
            const Chart = require('chart.js');
            axios.get('http://localhost:8000/portfolio/api/trendline').then(
                    response => {
                        this.response = response.data["Time Series (Daily)"]
                        this.symbol = response.data["Meta Data"]["2. Symbol"]
                        var stop = 20;
                        var count = 0;

                        for(var i in this.response){
                            this.labels.push(i)
                            count ++;
                            if(stop ==count){
                                break;
                            }
                        }

                        for(var ii in this.response){
                            this.data.push(this.response[ii]["1. open"])
                        }

                        console.log(this.data)

                        var ctx = document.getElementById('line-chart').getContext('2d');

                        var chart = new Chart(ctx, {
                            // The type of chart we want to create
                            type: 'line',

                        // The data for our dataset
                        data: {
                            labels: this.labels,
                            datasets: [{
                                label: this.symbol,
                                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                                pointBackgroundColor: 'white',
                                borderWidth:1,
                                borderColor: 'rgba(54, 162, 235, 1)',
                                pointBorderColor: 'white',
                                data: this.data
                            }]
                        },

                        // Configuration options go here
                            options: {}
                        });
                    }
                    ).catch(e => {
              console.log(e)
            })

        }

    }
</script>

<style>
    #line{
        width: 800px;
        height: 800px;
    }
</style>