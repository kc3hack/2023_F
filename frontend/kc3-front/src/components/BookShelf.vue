<script setup lang="ts">
import { ref } from "vue";
import BookComponent from "./BookComponent.vue";
import type {Book} from "@/interfaces"

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

const bookList = ref(bookListInit);

</script>

<template>
  <v-container class="wood_outline">
    <v-row class="bg none_books" dense>
      <BookComponent
        v-for="[id, book] in bookList"
        :key="id"
        :isbn="book.isbn"
        :title="book.title"
        :count="book.count"
        :date="book.date"
        :latest_num="book.latest_num"
        :image_url="book.image_url"
      ></BookComponent>
    </v-row>

    <h2 class="wood_line p-3"></h2>

    <v-row class="bg none_books" dense>
      <BookComponent
        v-for="[id, book] in bookList"
        :key="id"
        :isbn="book.isbn"
        :title="book.title"
        :count="book.count"
        :date="book.date"
        :latest_num="book.latest_num"
        :image_url="book.image_url"
      ></BookComponent>
    </v-row>

    <h2 class="wood_line"></h2>

    <v-row class="bg none_books" dense>
      <BookComponent
        v-for="[id, book] in bookList"
        :key="id"
        :isbn="book.isbn"
        :title="book.title"
        :count="book.count"
        :date="book.date"
        :latest_num="book.latest_num"
        :image_url="book.image_url"
      ></BookComponent>
    </v-row>

    <h2 class="wood_line"></h2>

    <v-row class="bg none_books" dense>
      <BookComponent
        v-for="[id, book] in bookList"
        :key="id"
        :isbn="book.isbn"
        :title="book.title"
        :count="book.count"
        :date="book.date"
        :latest_num="book.latest_num"
        :image_url="book.image_url"
      ></BookComponent>
    </v-row>

    <h2 class="wood_line"></h2>

    <v-row class="bg" dense>
      <BookComponent
        v-for="[id, book] in bookList"
        :key="id"
        :isbn="book.isbn"
        :title="book.title"
        :count="book.count"
        :date="book.date"
        :latest_num="book.latest_num"
        :image_url="book.image_url"
      ></BookComponent>
    </v-row>
  </v-container>
</template>

<style scoped>
.bg {
  background-image: url("@/assets/wood-texture_00016.jpg");
}

.wood_line {
  background-image: url("@/assets/wood-texture_00011.jpg");
  padding: 0.6rem 0;
}

.wood_outline {
  border: 7px solid;
  border-image: url("@/assets/wood-texture_00011.jpg");
  border-image-width: 20px;
  border-image-slice: 100 250 250 250;
}

h2 {
  width: 101%;
  margin-left: -0.3%;
  box-shadow: 0px -10px 5px brown;
}

.none_books {
  min-height: 150px;
}
</style>
