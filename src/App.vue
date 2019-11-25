<template>
<v-app>
    <router-view/>
    <!--<Navbar/>-->
    <!--<Drawer></Drawer>-->
    <!--<v-content>-->
        <!--<CommitChart id="chart"></CommitChart>-->
        <!--<Api></Api>-->
    <!--</v-content>-->


</v-app>

</template>

<script>
// import Drawer from './components/Drawer';
// import Navbar from './components/Navbar';
// import Drawer from './components/Drawer';
// import CommitChart from './js/CommitChart';
// import Api from './components/Api';
import router from "./router";
// import Dashboard from "./components/Dashboard";
export default {
  name: 'App',
  components: {
      // Navbar,
      // Drawer,
      // CommitChart,
      // Api
      // Dashboard
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