import Auth from './components/Auth'
import Dashboard from "./components/dashboard";
import App from './App'
import VueRouter from 'vue-router';
import Vue from 'vue'

Vue.use(VueRouter)

export default new VueRouter({

    mode: 'history',
    base: process.env.BASE_URL,
    routes:
        [

            {
                path: '',
                name: 'App',
                component: App
            },

            // Dashboard Path
            {
                path: '/dashboard',
                name: 'Dashboard',
                component: Dashboard
            },

            //  Authentication Path
            {
                path: '/auth',
                name: 'Auth',
                component: Auth
            }
        ]
})
