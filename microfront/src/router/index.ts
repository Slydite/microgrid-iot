import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router';


import SensorView from '../views/Sensor.vue'
import HomeView from '../views/Home.vue'
const routes: Array<RouteRecordRaw> = [

    {
        path: '/home', // Added this line to handle '/home' path
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
