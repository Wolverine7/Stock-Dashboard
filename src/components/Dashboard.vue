<template>
    <v-app>
    <Navbar/>
    <Drawer></Drawer>
    <v-content>
        <CommitChart id="chart"></CommitChart>
        <canvas id="radar-chart" width="800" height="600"></canvas>
        <Api></Api>
    </v-content>


</v-app>
</template>

<script>
    // import Drawer from './components/Drawer';
import Navbar from './Navbar';
import Drawer from './Drawer';
import CommitChart from '../js/CommitChart';
import Api from './Api';

export default {
  name: 'Dashboard',
  components: {
      Navbar,
      Drawer,
      CommitChart,
      Api,
    }
}
</script>

<style>

</style>