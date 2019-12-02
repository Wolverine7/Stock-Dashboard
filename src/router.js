import Auth from './components/Auth'
import Dashboard from "./components/dashboard";
import Home from "./components/Home";
import VueRouter from 'vue-router';
import Vue from 'vue'

Vue.use(VueRouter)

const router =  new VueRouter({

    mode: 'history',
    base: process.env.BASE_URL,
    routes:
    [

        {
            path: '',
            name: 'Home',
            component: Home
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
