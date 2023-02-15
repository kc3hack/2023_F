import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";
import AppSearch from "@/views/AppSearch.vue";
//import Apphoge from"@/views/AppHoge.vue";

const routeSettings: RouteRecordRaw[] = [
  {
    path: "/",
    name: "AppTop",
    component: AppTop,
  },
  {
    path: "/search",
    name: "AppSearch",
    component: AppSearch,
  },
  /*
  {
    path: "/hoge",
    name: "AppHoge",
    component: AppHoge,
  },*/
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routeSettings,
});

export default router;
