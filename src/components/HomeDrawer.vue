<template>
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
          link
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              {{ item.text }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>


<!--            <v-list-item link @click="goToDashboard()">-->
<!--                <v-list-item-action>-->
<!--                    <v-icon>mdi-view-dashboard</v-icon>-->
<!--                </v-list-item-action>-->

<!--                <v-list-item-content>-->
<!--                    <v-list-item-title>My Dashboard</v-list-item-title>-->
<!--                </v-list-item-content>-->
<!--            </v-list-item>-->

<!--            <v-list-item link>-->
<!--                <v-list-item-action>-->
<!--                    <v-icon>mdi-contact-mail</v-icon>-->
<!--                </v-list-item-action>-->

<!--                <v-list-item-content>-->
<!--                    <v-list-item-title>Meet Our Team</v-list-item-title>-->
<!--                </v-list-item-content>-->
<!--            </v-list-item>-->



<script>
    import router from '../router'

    export default {
        name: "HomeDrawer",


        data :() => ({
                drawer: false,
                items: [
                    {icon: 'mdi-home', title: 'Home', link: '/home'},
                    {icon: 'mdi-dashboard', title: 'My Dashboard', link: '/dashboard'},
                    {icon: 'mdi-account', title: 'My Profile'},
                ],
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
                router.push('/home');
            },

            goToDashboard() {
                router.push('/dashboard');
            },
        }),
    }

</script>

<style scoped>

</style>