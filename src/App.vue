<template>
    <v-app>
        <v-navigation-drawer
                v-model="drawer"
                app
                right
        >
            <v-list dense>
                <v-list-item link>
                    <v-list-item-action>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-action>

                    <v-list-item-content>
                        <v-list-item-title v-on:click="goHome">Home</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>


                <v-list-item link>
                    <v-list-item-action>
                        <v-icon>mdi-contact-mail</v-icon>
                    </v-list-item-action>

                    <v-list-item-content>
                        <v-list-item-title @click="tologin">Log in</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link>
                    <v-list-item-action>
                        <v-icon>mdi-contact-mail</v-icon>
                    </v-list-item-action>

                    <v-list-item-content>
                        <v-list-item-title @click="goToDashboard()">My Dashboard</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link>
                    <v-list-item-action>
                        <v-icon>mdi-contact-mail</v-icon>
                    </v-list-item-action>

                    <v-list-item-content>
                        <v-list-item-title>Meet Our Team</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

            </v-list>
        </v-navigation-drawer>

        <v-app-bar
                app
                color="cyan"
                dark
        >
            <v-toolbar-title>HOME</v-toolbar-title>
            <v-img :src="require('./assets/bull.svg')" height="50" padding-right="80" contain
                   class="cyan darken-5"></v-img>

            <v-spacer/>

            <v-toolbar-title>ACTIONS</v-toolbar-title>

            <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
        </v-app-bar>


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

    export default {
        name: '#app',

        data: () => ({
            authenticated: false,
        }),

        methods: ({
            tologin() {
                router.push('/auth');
            },

            logout: function () {
                localStorage.removeItem('isAuthenticates');
                localStorage.removeItem('log_user');
                localStorage.removeItem('token');
                this.authenticated = false;
                window.location = ""
            },


            goHome: function () {
                router.push('');
            },

            goToDashboard: function () {
                router.push('/dashboard');
            },
        }),
    };
</script>

<style>

</style>