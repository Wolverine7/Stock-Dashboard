<template>
        <v-app-bar
                dark
                app
                clipped-left
        >
            <v-toolbar-title>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <router-link to="" tag="span" style="cursor: pointer">MavStocks</router-link>
            </v-toolbar-title>


            <v-spacer></v-spacer>

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
                    <v-list-item
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
            </v-menu>
        </v-app-bar>
</template>

<script>
import router from '../router'

    export default {
        name: "HomeNav",

        data () {
          return {
              drawer: null,
          }
    },

        methods: ({
            tologin() {
                router.push('/auth')
            },
            logout(){
                localStorage.removeItem('token')
                localStorage.removeItem('isAuthenticates')
                localStorage.removeItem('log_user')
            }
        }),

    }
</script>

<style scoped>

</style>