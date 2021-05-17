import '@/../bootstrap/css/bootstrap.css'
import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSweetalert2 from 'vue-sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'
import Shows from './components/Shows'
import Login from './components/Login.vue'
import AddEvent from './components/AddEvent.vue'

Vue.config.productionTip = false
Vue.use(VueSweetalert2)
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', name: 'Shows', component: Shows },
    { path: '/userlogin/', name: 'Login', component: Login },
    { path: '/addEvent/', name: 'AddEvent', component: AddEvent }
  ]
})

new Vue({
  router,
  render: (h) => h(App)
}).$mount('#app')
