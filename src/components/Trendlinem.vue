<template>
    <div id="line-multiple">
        <canvas id="line-multiple-chart">

        </canvas>
    </div>
</template>

<script>


    export default {
        name: 'Trendline',
         data: () => ({
            response: null,
            symbol1:'',
            symbol2:'',
            sybmol3:'',
            labels:[],
            msft_data: [],
            goog_data: [],
            tsla_data: [],
            msft_data_graph: [],
            goog_data_graph: [],
            tsla_data_graph: [],

        }),
        mounted(){
            const axios = require('axios')
            const Chart = require('chart.js');
            axios.get('http://localhost:8000/portfolio/api/mutipledata').then(
                    response => {
                        this.msft_data = response.data["msft_json_data"]["Time Series (Daily)"]
                        this.goog_data = response.data["goog_json_data"]["Time Series (Daily)"]
                        this.tsla_data = response.data["tsla_json_data"]["Time Series (Daily)"]

                        this.symbol1 = response.data["msft_json_data"]["Meta Data"]["2. Symbol"]
                        this.symbol2 = response.data["goog_json_data"]["Meta Data"]["2. Symbol"]
                        this.symbol3 = response.data["tsla_json_data"]["Meta Data"]["2. Symbol"]


                        for(var i in this.msft_data){
                           this.msft_data_graph.push(this.msft_data[i]["1. open"])
                        }

                        for(var ii in this.goog_data){
                            this.goog_data_graph.push(this.goog_data[ii]["1. open"])
                        }

                        for(var iii in this.tsla_data){
                           this.tsla_data_graph.push(this.tsla_data[iii]["1. open"])
                        }

                        console.log(this.tsla_data_graph)


                        var ctx = document.getElementById('line-multiple-chart').getContext('2d');

                        var chart = new Chart(ctx, {
                            // The type of chart we want to create
                            type: 'bar',

                        // The data for our dataset
                        data: {
                            labels: this.labels,
                            datasets: [
                                {
                                    label: this.symbol1,
                                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                                    pointBackgroundColor: 'white',
                                    borderWidth:1,
                                    borderColor: 'rgba(54, 162, 235, 1)',
                                    pointBorderColor: 'white',
                                    data: this.msft_data_graph
                                },
                                {
                                    label: this.symbol2,
                                    backgroundColor: 'rgba(141, 216, 190, 1)',
                                    pointBackgroundColor: 'white',
                                    borderWidth:1,
                                    borderColor: 'rgba(54, 162, 235, 1)',
                                    pointBorderColor: 'white',
                                    data: this.goog_data_graph
                                },
                                {
                                    label: this.symbol3,
                                    backgroundColor: 'rgba(218, 233, 165, 1)',
                                    pointBackgroundColor: 'white',
                                    borderWidth:1,
                                    borderColor: 'rgba(54, 162, 235, 1)',
                                    pointBorderColor: 'white',
                                    data: this.tsla_data_graph
                                }

                            ]
                        },

                        // Configuration options go here
                            options: {}
                        });

                    }).catch(e => {
              console.log(e)
            })

        }

    }
</script>

<style>
    #line-multiple{
        width: 800px;
        height: 800px;
    }
</style>