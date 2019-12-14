<template>
    <v-app>
<!--        <HomeNav/>-->

        <!--Page Body-->
        <v-content>
            <router-view/>
        </v-content>

    </v-app>
</template>

<script>

// import HomeNav from "./components/HomeNav";

    export default {
        name: 'App',

        components: {
           // HomeNav,
        },

        data:() => ({
            authenticated: false,
            return:{
                drawer: null,
            },
        }),

        methods: ({}),
    };
</script>

<style>
    /*html{*/
      /*overflow-y: hidden;*/
    /*}*/
</style>