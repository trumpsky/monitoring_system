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
      component: () => import('@/pages/Home'),
      children: [
        {
          path: "/menu/1-1",
          component: () => import('@/pages/SystemInformation')
        },{
          path: "/menu/1-2",
          component: () => import('@/pages/Help')
        },{
          path: "/menu/1-3",
          component: () => import('@/pages/Team')
        },
        {
          path: "/menu/2-1",
          component: () => import('@/pages/ClusterLevel')
        },
        {
          path: "/menu/2-2",
          component: () => import('@/pages/ClusterLevel')
        },
        {
          path: "/menu/2-3",
          component: () => import('@/pages/NodeMultipleLevel')
        },
        {
          path: "/menu/3-1",
          component: () => import('@/pages/Product')
        },
        {
          path: "/menu/3-2",
          component: () => import('@/pages/Product')
        },
        {
          path: "/menu/3-3",
          component: () => import('@/pages/Product')
        }
      ]
    }
  ]
})
