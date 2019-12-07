<template>
    <v-app>
        <HomeNav/>
        <HomeDrawer/>

        <v-content>
            <router-view/>
        </v-content>
    </v-app>
</template>

<script>
    import HomeDrawer from "./HomeDrawer";
    import HomeNav from "./HomeNav";

    export default {
        el:"#home",
        name: "Home",

        components: {
            HomeDrawer,
            HomeNav,
        },

    }
</script>

<style scoped>

</style>