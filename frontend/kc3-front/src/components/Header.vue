<script setup lang="ts">
import {ref} from "vue";

const drawer = ref(false);
const group_init: string[] = [
  "タイトル",
  "持っている本の数",
  "登録日",
  "今持っている最新刊",
];
const group = ref([group_init]);
</script>

<template>
  <header>
    <v-app-bar app color="blue" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-app-bar-title>書籍管理アプリ(仮)</v-app-bar-title>

      <v-navigation-drawer v-model="drawer" absolute temporary>
          <v-list>
              <v-list-group v-model="group">
                  <v-list-item>
                    <v-list-item-title>aaa</v-list-item-title>
                  </v-list-item>
              </v-list-group>
          </v-list>
      </v-navigation-drawer>
    </v-app-bar>
  </header>
</template>
