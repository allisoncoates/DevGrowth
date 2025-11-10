import { createRouter, createWebHistory } from 'vue-router'
import NewEntry from '@/pages/NewEntry.vue'
import PastEntries from '@/pages/PastEntries.vue'

const routes = [
  { path: '/', component: NewEntry },
  { path: '/pastentries', component: PastEntries },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
