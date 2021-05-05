// import BootstrapVue from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import Vue from 'vue'
import App from './App.vue'
// import router from './router'
import VueRouter from 'vue-router'

import Cart from './components/Cart'
import Shows from './components/Shows'

Vue.use(VueRouter)
Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', name: 'ShowsPage', component: Shows },
    { path: '/cart/', name: 'CartPage', component: Cart }
  ]
})

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
