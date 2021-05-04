import Vue from 'vue'
import Router from 'vue-router'
import Shows from '@/components/Shows'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Shows',
      component: Shows
    }
  ]

})