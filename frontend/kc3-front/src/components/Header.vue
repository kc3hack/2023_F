<script setup lang="ts">
import { ref } from "vue";
</script>

<template>
  <header>
    <v-app-bar app color="blue" dark>
      <v-app-bar-title>
        <router-link to="/" style="text-decoration: none; color: inherit">
          書籍管理アプリ(仮)
        </router-link>
      </v-app-bar-title>
    </v-app-bar>
  </header>
</template>
