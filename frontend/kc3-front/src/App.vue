<script setup lang="ts">
import Header from "@/components/Header.vue";
import { RouterView } from "vue-router";
import { useUsersStore } from "@/stores/users";

const userStore = useUsersStore();
userStore.Init();
</script>

<template>
  <div id="app">
    <v-app>
      <Header class="change-font"></Header>
      <v-main>
        <RouterView class="py-10"></RouterView>
      </v-main>
    </v-app>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Murecho:wght@500;900&display=swap");

.change-font {
  font-family: "Murecho", sans-serif;
}

.main-bg {
  background-image: url("@/assets/main-wood.jpg");
  background-size: cover;
  background-color: rgba(255, 255, 255, 0.25);
  background-blend-mode: lighten;
  height: 100%;
}
</style>
