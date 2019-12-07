import Vue from 'vue';
import vuetify from './plugins/vuetify';
import router from './router';
import App from "./App";
import VueSession from 'vue-session';
import Home from './components/Home';


Vue.use(VueSession)

Vue.config.productionTip = false

new Vue({
  router,
  el:'#app',
  vuetify,
  render: h=>h (App),
})


new Vue({
  vuetify,
  router,
  render: h=>h(Home)
})


// new Vue({
//   el:"#dashboard",
//   vuetify,
//   router,
//   render: h => h(Dashboard)
// })
