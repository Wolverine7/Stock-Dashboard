<template>
<v-app>
    <Home/>

    <v-content>
        <CommitChart id="chart"></CommitChart>
        <Api></Api>
    </v-content>

</v-app>

</template>

<script>
import CommitChart from '../js/CommitChart';
import Api from './Api';
import router from "../router";
import Home from './Home'

export default {
  name: 'Dashboard',

  components: {
      CommitChart,
      Api,
      Home,
    },

    data: () => ({

    }),
    methods: ({
        checkLoggedIn() {
            this.$session.start();
            if (!this.$session.has("token")) {
                router.push("/auth");
            }
        }
    })

    };
</script>

<style>
    #chart{
       width: 500px;
       height: 500px;
    }
</style>