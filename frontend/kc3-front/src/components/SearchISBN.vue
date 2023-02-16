<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

const isbn = ref("");

async function searchISBN() {
  await axios
    .get("https://jsonplaceholder.typicode.com/users") //テストurl
    .then((response) => {
      //BEから データを受け取ったときにやる処理
      console.log(response.data);
      console.log(isbn.value); //テスト
    })
    .catch((e) => {
      console.log(e);
    });
}
</script>

<template>
  <div class="background">
    <div class="outside">
      <div class="search-area">
        <label for="message">ISBNを入力(ハイフンなし): </label>
        <input v-model="isbn" type="text" placeholder=" ISBNコード" /><br />
      </div>

      <button class="search-button" @click="searchISBN">本を検索・追加</button>
    </div>
  </div>
</template>

<style>
.background {
  padding: 250px;
}
.outside {
  background-color: #e7d0a9;
  margin-left: auto;
  margin-right: auto;
  padding: 30px;
  height: 180px;
  width: 600px;
  text-align: center;
  border: thick double;
  border-radius: 10px;
}
.search-area {
  background-color: lightgray;
  border: solid;
}
.search-button {
  background-color: yellow;
  border: solid;
  border-radius: 10px;
  padding: 4px;
  margin: 50px;
}
</style>
