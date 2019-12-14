<template>
    <div id="table">
         <v-data-table :headers="headers" :items="desserts" :items-per-page="5" class="elevation-1"></v-data-table>
    </div>
</template>

<script>
  export default {
    data () {
      return {
        response:'',
        headers: [
          {
            text: 'Name',
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Symbol', value: 'symbol'},
          { text: 'Currency', value: 'currency'},
          { text: 'Match Score', value: 'matchScore'},
        ],
        desserts: [],
      }
    },
      mounted(){
        const axios = require('axios')
        axios.get('http://localhost:8000/portfolio/api/table').then(
                    response => {
                        this.response = response.data["bestMatches"]
                        console.log(this.response)
                        for(var i in this.response){
                            this.desserts.push({symbol: this.response[i]["1. symbol"], currency: this.response[i]["8. currency"], name: this.response[i]["2. name"],matchScore: this.response[i]["9. matchScore"]})
                        }
                    }
        ).catch(e => {
              console.log(e)
        })

      }
  }
</script>


<style>
    #table{
        width: 700px;
        height: 400px;
        padding-left: 100px;
    }
</style>