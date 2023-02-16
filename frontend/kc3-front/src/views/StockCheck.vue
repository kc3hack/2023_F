<script setup lang="ts">
import { ref } from "vue";
import type { Book } from "@/interfaces";
import { useUsersStore } from "@/stores/users";

const userStore = useUsersStore();

const bookListInit = userStore.getBooks;

const books = ref(bookListInit);

const headersInit = [
  {
    text: "サムネ",
    value: "image_url",
  },
  {
    text: "タイトル",
    value: "title",
  },
  {
    text: "持っている本の数",
    value: "count",
  },
  {
    text: "登録日",
    value: "date",
  },
  {
    text: "所持している最新刊",
    value: "latest_num",
  },
];

const headers = ref(headersInit);
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-table fixed-header height="800px">
          <thead>
            <tr>
              <th v-for="(header, index) in headers" :key="index">
                {{ header.text }}
              </th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="[id, book] in books" :key="id">
              <td>
                <v-avatar size="80">
                  <v-img :src="book.image_url"></v-img>
                </v-avatar>
              </td>
              <td>{{ book.title }}</td>
              <td>{{ book.count }}冊</td>
              <td>{{ book.date.toLocaleDateString() }}</td>
              <td>{{ book.latest_num }}巻</td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
    </v-row>
  </v-container>
</template>
