import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";
import AppTop from "@/views/AppTop.vue";
import AppSearch from "@/views/AppSearch.vue";
import { useUsersStore } from "@/stores/users";
//import Apphoge from"@/views/AppHoge.vue";

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
    },
  },
  {
    path: "/stock",
    name: "stock",
    component: () => {
      return import("@/views/StockCheck.vue");
    },
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

router.beforeEach(async (to) => {
  const publicPages = ["/login"];
  const authRequired = !publicPages.includes(to.path);
  const auth = useUsersStore();
  if (authRequired && !auth.userStore.authUser) {
    console.log(authRequired);
    console.log(auth.userStore.authUser);
    return "/login";
  }
});
