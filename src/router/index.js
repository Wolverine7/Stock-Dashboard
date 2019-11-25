import Vue from 'vue'
import Router from 'vue-router'
import Auth from '../components/Auth'
import App from "../App";
import Dashboard from "../components/Dashboard";

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [

    // Home Path
    {
      path: '/',
      name: 'Dashboard',
      component:Dashboard
    },
    //  Authentication Path
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})
