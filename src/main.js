import Vue from 'vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router';
import { routes } from './router/index';
import Home from "./Home";


Vue.use(VueRouter)

const router = new VueRouter({
  routes
});

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h=>h(Home)
}).$mount('#app')


// new Vue({
//   vuetify,
//   router: routes,
//   render: h => h(Dashboard)
// }).$mount('#app')
