<script setup lang="ts">
import { ref } from 'vue';
const drawer = ref(false);

const menuItems = [
    {
        name: '本棚',
        url: '#'
    },
    {
        name: 'ISBN登録',
        url: '#'
    },
    {
        name: '書籍確認',
        url: '#'
    },
    {
        name: '本棚公開',
        url: '#'
    }
];
</script>

<template>
    <div class="menu">
    <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    
    <v-navigation-drawer location="end" v-model="drawer" fixed temporary>
        <v-list nav dense>
          <v-list-item-group>
            <v-list-item v-for="(menuItem, index) in menuItems" :key="index">
                <v-list-item-title>{{ menuItem.name }}</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </div>
</template>

<style>
.menu{
  padding: 4px;
}
</style>
