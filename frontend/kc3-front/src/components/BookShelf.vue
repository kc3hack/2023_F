<script setup lang="ts">
import { computed, ref } from "vue";
import BookComponent from "./BookComponent.vue";
import { useUsersStore } from "@/stores/users";
import type { Book } from "@/interfaces";

const userStore = useUsersStore();
userStore.Init();

const bookList = computed((): Book[][] => {
  const list = [...userStore.getBooks.values()];
  console.log(list)
  const result = [
    list.slice(0,5),
    list.slice(5,10),
    list.slice(10,15),
    list.slice(15,20),
    list.slice(20,25),
  ]
  console.log(result)
  return result;
});
</script>


<template>
  <v-container class="wood_outline" id="book-origin">
    <v-row class="bg none_books" dense>
      <BookComponent
        v-for="(book, index) in bookList[0]"
        :key="index"
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
        v-for="(book, index) in bookList[1]"
        :key="index"
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
        v-for="(book, index) in bookList[2]"
        :key="index"
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
        v-for="(book, index) in bookList[3]"
        :key="index"
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
        v-for="(book, index) in bookList[4]"
        :key="index"
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
