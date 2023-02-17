<script setup lang="ts">
import { ref, computed } from "vue";
import BookComponent from "./BookComponent.vue";
import { useUsersStore } from "@/stores/users";
import type { Book } from "@/interfaces";

const userStore = useUsersStore();
const test = userStore.userStore.authUser;
const a = ref(test);
userStore.Init();

const bookList = computed((): Map<number, Book> => {
  return userStore.getBooks;
});
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
