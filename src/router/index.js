import Auth from '../components/Auth'
import Dashboard from "../components/dashboard";
import Home from "../Home"

export const routes =
    // ({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes:
  [

      {
          path:'/',
          name:'Home',
          component: Home
      },

    // Dashboard Path
    {
      path: '/dashboard',
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
// })
