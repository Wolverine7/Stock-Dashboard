<template>
<v-app>
    <Navbar/>
    <Drawer></Drawer>
    <v-content>
        <CommitChart id="chart"></CommitChart>
        <Api></Api>
    </v-content>



</v-app>

</template>

<script>
import Navbar from './components/Navbar';
import Drawer from './components/Drawer';
import CommitChart from './js/CommitChart';
import Api from './components/Api';


export default {
  name: 'App',
  components: {
      Navbar,
      Drawer,
      CommitChart,
      Api,
    },

    data: () => ({

    }),
    method:() => ({})

    };
</script>

<style>
    #chart{
       width: 500px;
       height: 500px;
    }
</style>