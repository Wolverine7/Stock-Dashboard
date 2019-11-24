<template>
    <div id="template">

    </div>
</template>

<script>
    export default {
        data: function(){
            {
                return {
                    stocks_open: [],
                    stocks_close:[],
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                }
            }
        },
        mounted(){
            const axios = require('axios');
            axios.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&apikey=demo')
                .then(response => {
                    var output = response.data["Monthly Time Series"];
                    var parsedData = JSON.parse(JSON.stringify(output));

                    for(var i in parsedData){
                       this.stocks_open.push(output[i]["1. open"]);
                       this.stocks_close.push(output[i]["4. close"]);
                    }

                })
            console.log(this.stocks_open, this.stocks_close);
        }
    }
</script>

<style>

</style>