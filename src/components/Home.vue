<template>
    <div>
        <v-navigation-drawer
                v-model="drawer"
                app
                dark
                clipped
                temporary
        >

            <v-list dense>
                <v-list-item
                        v-for="item in items"
                        :key="item.title"
                        :to="item.link"
                >
                    <v-list-item-action>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>
                            {{ item.title }}
                        </v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar
                dark
                app
                clipped-left
        >
            <v-toolbar-title>
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
                <router-link to="/" tag="span" style="cursor: pointer">MavStocks</router-link>
            </v-toolbar-title>

            <v-spacer> <v-img :src="require('../assets/bull.svg')" height="70" contain /></v-spacer>

            <v-menu
                    left
                    top
            >
                <template v-slot:activator="{ on }">
                    <v-btn icon v-on="on">
                        <v-icon>mdi-dialpad</v-icon>
                    </v-btn>
                </template>

                <v-list>
                    <v-list-item v-if="authenticated === false"
                            @click="tologin()"
                    >
                        <v-icon>mdi-account</v-icon>
                        <v-list-item-title>Log In</v-list-item-title>
                    </v-list-item>

                    <v-list-item

                    >
                        <v-icon>mdi-account</v-icon>
                        <v-list-item-title>Sign Up</v-list-item-title>
                    </v-list-item>
                </v-list>
                  <v-list-item @click="logout" v-if="authenticated===true">
                        <v-icon>mdi-account</v-icon>
                        <v-list-item-title>Log Out</v-list-item-title>
                    </v-list-item>
            </v-menu>
        </v-app-bar>
    </div>
</template>

<script>
    import router from '../router'

    export default {
        name: "Home",


        data: () => ({
            drawer: null,
            items: [
                {icon: 'mdi-view-dashboard', title: 'My Dashboard', link: '/dashboard'},
                {icon: 'mdi-account', title: 'My Profile'},
                {icon: 'mdi-settings', title: 'Change My Password'},
            ],
            authenticated:''
        }),

        methods: ({

            tologin() {
                router.push('/auth');
            },

            logout() {
                localStorage.removeItem('isAuthenticates');
                localStorage.removeItem('log_user');
                localStorage.removeItem('token');
                 this.$session.destroy();
                router.push('/auth')
            },
            checkLogin(){
              if (this.$session.has("token")) {
                    console.log('hello')
                  this.authenticated = true
                }
            },
            goHome() {
                router.push('/home');
            },

            goToDashboard() {
                router.push('/dashboard');
            },
        }),
        mounted(){
            this.checkLogin()
        }
    }
</script>

<style scoped>

</style>