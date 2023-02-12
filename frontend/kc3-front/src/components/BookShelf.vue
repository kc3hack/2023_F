<script setup lang="ts">
import { ref } from "vue";

const bookListInit = new Map<number, Book>();
bookListInit.set(11111111111, {
  isbn: 11111111111,
  title: "sample",
  detail: "hoge",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088825656.jpg",
});

bookListInit.set(2222222222222, {
  isbn: 2222222222222,
  title: "test",
  detail: "aaaaaaa",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784040646176.jpg",
});

bookListInit.set(2222222222223, {
  isbn: 2222222222223,
  title: "test",
  detail: "aaaaaaa",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088917191.jpg",
});

bookListInit.set(2222222222224, {
  isbn: 2222222222224,
  title: "test",
  detail: "aaaaaaa",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088904320.jpg",
});

bookListInit.set(2222224222223, {
  isbn: 2222224222223,
  title: "test",
  detail: "aaaaaaa",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});

const bookList = ref(bookListInit);
console.log(bookList);

interface Book {
  isbn: number;
  title: string;
  detail: string;
  count?: number;
  date: Date;
  latest_num?: number;
  image_url?: string;
}
</script>

<template>
  <v-container class="wood_outline">
    <v-row class="bg" dense>
      <v-col
        v-for="[id, book] in bookList"
        :key="id"
        cols="3.5"
        class="mr-n16 mt-3"
      >
        <v-img
          :src="book.image_url"
          class="white-text align-end hover_anim"
          aspect-ratio="1.5"
        ></v-img>
      </v-col>
    </v-row>

    <h2 class="wood_line p-3"></h2>

    <v-row class="bg" dense>
      <v-col
        v-for="[id, book] in bookList"
        :key="id"
        cols="3.5"
        class="mr-n16 mt-3"
      >
        <v-img
          :src="book.image_url"
          class="white-text align-end hover_anim"
          aspect-ratio="1.5"
        ></v-img>
      </v-col>
    </v-row>

    <h2 class="wood_line"></h2>

    <v-row class="bg" dense>
      <v-col
        v-for="[id, book] in bookList"
        :key="id"
        cols="3.5"
        class="mr-n16 mt-3"
      >
        <v-img
          :src="book.image_url"
          class="white-text align-end hover_anim"
          aspect-ratio="1.5"
        ></v-img>
      </v-col>
    </v-row>

    <h2 class="wood_line"></h2>

    <v-row class="bg" dense>
      <v-col
        v-for="[id, book] in bookList"
        :key="id"
        cols="3.5"
        class="mr-n16 mt-3"
      >
        <v-img
          :src="book.image_url"
          class="white-text align-end hover_anim"
          aspect-ratio="1.5"
        ></v-img>
      </v-col>
    </v-row>

    <h2 class="wood_line"></h2>

    <v-row class="bg" dense>
      <v-col v-for="[id, book] in bookList" :key="id" cols="3.5" class="mr-n16">
        <v-img
          :src="book.image_url"
          class="white-text align-end hover_anim"
          aspect-ratio="1.5"
        ></v-img>
      </v-col>
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

.hover_anim {
  transition-duration: 0.3s;
}

.hover_anim:hover {
  transform: scale(1.1);
}
</style>
