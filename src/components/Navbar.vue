<template>
    <v-app-bar
            app
            color="cyan"
            dark
    >
        <v-toolbar-title>HOME</v-toolbar-title>
        <v-img :src="require('../assets/bull.svg')" height="50" padding-right="80" contain
               class="cyan darken-5"></v-img>

        <v-spacer/>

        <v-toolbar-title>ACTIONS</v-toolbar-title>

        <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
    </v-app-bar>
</template>

<script>

</script>

<style>

</style>