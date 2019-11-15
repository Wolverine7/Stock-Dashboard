<template>
  <v-app>
      <Navbar/>
      <Drawer>
      </Drawer>

  </v-app>
</template>

<script>
import Drawer from './components/Drawer';
import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: {
    Drawer,
      Navbar
  },
  data: () => ({
    //
  }),
};
</script>
