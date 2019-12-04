<template>
    <v-app>

        <HomeNav/>

        <!--Page Body-->
        <v-content>
            <router-view/>
        </v-content>


    </v-app>
</template>

<script>
    import HomeNav from './components/HomeNav';

    export default {
        name: '#app',

        components: {
             HomeNav,
        },

        data: () => ({
            authenticated: false,
        }),

        methods: ({}),
    };
</script>

<style>

</style>