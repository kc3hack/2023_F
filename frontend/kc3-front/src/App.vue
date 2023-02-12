<script setup lang="ts">
import Header from "@/components/Header.vue";
import { RouterView } from "vue-router";
</script>

<template>
  <div id="app" class="main-bg">
    <v-app>
      <Header></Header>
      <v-main>
        <RouterView class="py-10"></RouterView>
      </v-main>
    </v-app>
  </div>
</template>

<style scoped>
.main-bg {
  background-image: url("@/assets/main-wood.jpg");
  background-size: cover;
  background-color: rgba(255,255,255,0.25);
  background-blend-mode: lighten;
}
</style>
