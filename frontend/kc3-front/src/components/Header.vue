<script setup lang="ts">
import { ref } from "vue";
</script>

<template>
  <header>
    <v-app-bar app color="green" dark>
      <v-app-bar-title>
        <router-link to="/" class="header">
          Shelfie
        </router-link>
      </v-app-bar-title>
    </v-app-bar>
  </header>
</template>

<style scoped>
.header {
  text-decoration: none;
  color: inherit;
  font-size: 30px;
  margin-left: 2%;
}
</style>
