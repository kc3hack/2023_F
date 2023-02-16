<script setup lang="ts">
import { ref } from "vue";
import type { Book } from "@/interfaces";

const bookListInit = new Map<number, Book>();

bookListInit.set(11111111111, {
  isbn: 11111111111,
  title: "sample",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088825656.jpg",
});
bookListInit.set(2222222222222, {
  isbn: 2222222222222,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784040646176.jpg",
});
bookListInit.set(2222222222223, {
  isbn: 2222222222223,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088917191.jpg",
});
bookListInit.set(2222222222224, {
  isbn: 2222222222224,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088904320.jpg",
});
bookListInit.set(2222224222223, {
  isbn: 2222224222223,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

bookListInit.set(2222224222223, {
  isbn: 2222224222223,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

bookListInit.set(2222224222225, {
  isbn: 2222224222225,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

bookListInit.set(2222224222226, {
  isbn: 2222224222226,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

bookListInit.set(2222224222229, {
  isbn: 2222224222229,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

bookListInit.set(2222224222296, {
  isbn: 2222224222296,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

bookListInit.set(2222224232296, {
  isbn: 2222224222296,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

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
