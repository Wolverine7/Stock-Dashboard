<template>

    <v-app>
        <v-img src="../assets/image4.jpeg" aspect-ratio="3.7">
            <v-menu
                    center
            >
                <template v-slot:activator="{ on }">
                    <v-btn v-on="on">
                        Explore More
                    </v-btn>
                </template>

                <v-list>
                    <v-list-item
                            @click="tologin()"
                    >
                        <v-icon>mdi-account</v-icon>
                        <v-list-item-title>Log In</v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-icon>mdi-account</v-icon>
                        <v-list-item-title>Sign Up</v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                    <v-icon>mdi-email</v-icon>
                    <v-list-item-title>Contact Us</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-img>
    </v-app>
</template>

<script>

    import router from '../router'

    export default {
        name: "landinPage",

        components: {},

        methods: ({
            goHome() {
                router.push('/home');
            },

            tologin() {
                router.push('/auth');
            },


        }),
    }
</script>

<style scoped>

</style>