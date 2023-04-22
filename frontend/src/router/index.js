import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'Test',
      component: () => import('@/pages/Test')
    },
    {
      path: '/',
      name: 'Home',
      component: () => import('@/pages/Home')
    },
    {
      path: '/clutter',
      name: 'Clutter',
      component: () => import('@/pages/ClutterLevel')
    },
  ]
})
