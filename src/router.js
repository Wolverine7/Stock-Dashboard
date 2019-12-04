import Auth from './components/Auth'
import Dashboard from "./components/dashboard";
import Drawer from './components/HomeDrawer';
import VueRouter from 'vue-router';
import Vue from 'vue'

Vue.use(VueRouter)

export default new VueRouter({

    mode: 'history',
    // base: process.env.BASE_URL,
    base: 'localhost:8000',
    routes:
        [

            {
                path: '',
                name: 'Drawer',
                component: Drawer,
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
