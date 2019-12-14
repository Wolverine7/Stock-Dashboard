<template>
<v-app>
    <Home/>

    <v-content>
        <!--<v-container>-->
            <v-row class = 'mb-3'>
                <Charting/>
                <Api></Api>
                <Table/>
            </v-row>
            <v-row class="mb-3" no-gutters>
                 <trendline/>
                <Trendlinem/>
            </v-row>
        <!--</v-container>-->
    </v-content>

</v-app>

</template>

<script>
import Api from './Api';
import router from "../router";
import Home from './Home'
import Trendline from './Trendline'
import Table from './Table'
import Trendlinem from './Trendlinem'
import Charting from './Charting'

export default {
  name: 'Dashboard',

  components: {
      Api,
      Home,
      Trendline,
      Table,
      Trendlinem,
      Charting
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