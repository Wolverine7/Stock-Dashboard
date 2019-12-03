<template>
<v-app>
    <router-view/>
    <Navbar/>
    <Drawer/>
    <v-content>
        <CommitChart id="chart"></CommitChart>
        <Api></Api>
    </v-content>


</v-app>

</template>

<script>
import Navbar from './Navbar';
import Drawer from './Drawer';
import CommitChart from '../js/CommitChart';
import Api from './Api';
import router from "../router";

export default {
  name: 'Dashboard',
  components: {
      Navbar,
      Drawer,
      CommitChart,
      Api,
    },

    data: () => ({

    }),
    method:() => ({
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