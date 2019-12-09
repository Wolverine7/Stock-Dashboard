import Vue from 'vue';
import vuetify from './plugins/vuetify';
import router from './router';
import App from "./App";
import VueSession from 'vue-session';


Vue.use(VueSession)

Vue.config.productionTip = false

new Vue({
  el: "#app",
  vuetify,
  router,
  render: h=>h (App),
}).$mount('#app')


// new Vue({
//   el:"#home",
//   vuetify,
//   router,
//   render: h => h(Home)
// })
