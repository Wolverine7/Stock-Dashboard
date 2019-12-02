<template>
<v-app>
    <Home/>
    <v-content>
    </v-content>
</v-app>

</template>

<script>
import Home from './components/Home'

export default {
  name: '#app',
  components: {
     Home,
    },

    data: () => ({
        authenticated: false,
    }),

    method:() => ({

    }),

    };
</script>

<style>

</style>