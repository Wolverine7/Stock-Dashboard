import Vue from 'vue'
import Router from 'vue-router'
import Auth from '../components/Auth'
import Dashboard from "../components/Dashboard";
import HomePage from "../HomePage";


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [

    // Home Path
    {
      path: '/',
      name: 'HomePage',
      component:HomePage
    },

    //  Dash Board Path
    {
      path:'/dashboard',
      name:'Dashboard',
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
