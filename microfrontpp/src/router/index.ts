import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router';

import HomeView from '../views/Home.vue'
import SensorView from '../views/Sensor.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/sensor',
    name: 'sensor',
    component: SensorView,
    props: (route) => ({ name: route.query.name })
  },
  // ... other routes
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
