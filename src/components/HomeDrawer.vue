<template>
    <v-navigation-drawer
            v-model="drawer"
            app
            dark
            clipped
    >
        <v-list dense>
            <v-list-item link  @click="goHome()">
                <v-list-item-action>
                    <v-icon>mdi-home</v-icon>
                </v-list-item-action>

                <v-list-item-content>
                    <v-list-item-title>Home</v-list-item-title>
                </v-list-item-content>
            </v-list-item>


            <v-list-item link  @click="tologin()">
                <v-list-item-action>
                    <v-icon>mdi-contact-mail</v-icon>
                </v-list-item-action>

                <v-list-item-content>
                    <v-list-item-title>Log in</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-list-item link @click="goToDashboard()">
                <v-list-item-action>
                    <v-icon>mdi-view-dashboard</v-icon>
                </v-list-item-action>

                <v-list-item-content>
                    <v-list-item-title >My Dashboard</v-list-item-title>
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
</template>

<script>
    import router from '../router'

    export default {
        name: "HomeDrawer",

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
    }

</script>

<style scoped>

</style>