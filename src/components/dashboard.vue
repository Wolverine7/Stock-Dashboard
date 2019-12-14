<template>
<v-app>
    <Home/>

    <v-content>
        <v-container>
            <v-row class = 'mb-6' no-gutters>
            <CommitChart id="chart"></CommitChart>
            <Api></Api>
            <Table/>
            </v-row>
            <trendline/>
        </v-container>
    </v-content>

</v-app>

</template>

<script>
import CommitChart from '../js/CommitChart';
import Api from './Api';
import router from "../router";
import Home from './Home'
import Trendline from './Trendline'
import Table from './Table'

export default {
  name: 'Dashboard',

  components: {
      CommitChart,
      Api,
      Home,
      Trendline,
      Table
    },

    data: () => ({

    }),
    methods: ({
        checkLoggedIn() {
            this.$session.start();
            if (!this.$session.has("token")) {
                router.push("/auth");
            }
        },

    }),
    mounted(){
      this.checkLoggedIn()
    }

    };
</script>

<style>
    #chart{
       width: 500px;
       height: 500px;
    }
</style>