import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Test',
      component: () => import('@/pages/Test')
    },
    {
      path: '/clutter',
      name: 'Clutter',
      component: () => import('@/pages/ClutterLevel')
    },
  ]
})
