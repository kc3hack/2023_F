import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";

const routeSettings: RouteRecordRaw[] = [
  {
    path: "/",
    name: "AppTop",
    component: AppTop,
  },
  {
    path: "/login",
    name: "login",
    component: () => {
      return import("@/views/AppLogin.vue");
    }
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routeSettings,
});

export default router;
