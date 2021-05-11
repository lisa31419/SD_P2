// import BootstrapVue from 'bootstrap-vue'
import '@/../bootstrap/css/bootstrap.css'
import Vue from 'vue'
import App from './App.vue'
// import router from './router'
import VueRouter from 'vue-router'

import Shows from './components/Shows'
import Login from './components/Login.vue'

Vue.use(VueRouter)
Vue.config.productionTip = false

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', name: 'Shows', component: Shows },
    { path: '/userlogin/', name: 'Login', component: Login }
  ]
})

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
