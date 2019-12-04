<template>
    <v-app id="inspire">
        <Navbar/>
        <Home/>



<!--        <v-app-bar-->
<!--                app-->
<!--                color="cyan"-->
<!--                dark-->
<!--        >-->
<!--            <v-toolbar-title>HOME</v-toolbar-title>-->
<!--            <v-img :src="require('./assets/bull.svg')" height="50" padding-right="80" contain-->
<!--                   class="cyan darken-5"></v-img>-->

<!--            <v-spacer/>-->

<!--            <v-toolbar-title>ACTIONS</v-toolbar-title>-->


<!--        </v-app-bar>-->


        <!--Page Body-->
        <v-content>
            <router-view/>
        </v-content>

        <v-footer
                color="cyan"
                app
        >
            <v-spacer/>

            <span class="white--text">&copy; 2019</span>
        </v-footer>
    </v-app>
</template>

<script>
    import router from './router'
    import Navbar from './components/Navbar'
    import Home from './components/Home'

    export default {
        name: '#app',

        components: {
            Navbar,
            Home,
        },

        data: () => ({
            authenticated: false,
        }),

        methods: ({
            tologin() {
                router.push('/auth');
            },

            logout() {
                localStorage.removeItem('isAuthenticates');
                localStorage.removeItem('log_user');
                localStorage.removeItem('token');
                this.authenticated = false;
                window.location = ""
            },


            goHome() {
                router.push('');
            },

            goToDashboard() {
                router.push('/dashboard');
            },
        }),
    };
</script>

<style>

</style>