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
                        console.log(response.data)
                    }).catch(e => {
              console.log(e)
            })

        }

    }
</script>

<style>
    #line{
        width: 1000px;
        height: 1000px;
    }
</style>