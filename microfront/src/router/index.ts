import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'; // Add missing import statement

import HomeView from '../views/Home.vue'
import SensorView from '../views/Sensor.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView // Remove the type assertion
    },
    {
      path: '/',
      name: 'sensor',
      component: SensorView // Remove the type assertion
    },

  ]
})

export default router
