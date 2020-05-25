import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/home/Home.vue'
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '/',
        name: 'DefaultHome',
        component: () => import('@/home/components/Table.vue')
      },
      {
        path: '/controlCenter',
        name: 'ControlCenter',
        component: () => import('@/home/components/ControlCenter.vue')
      },
      {
        path: '/table',
        name: 'Table',
        component: () => import('@/home/components/Table.vue')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
