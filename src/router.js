import Auth from './components/Auth'
import Dashboard from "./components/dashboard";
import Home from './components/Home';
import LandingPage from './components/landinPage';
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
              path: '/',
              name: 'LandingPage',
              component: LandingPage,
            },

            {
                path: '/home',
                name: 'Home',
                component: Home,
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
            },
        ]
})
