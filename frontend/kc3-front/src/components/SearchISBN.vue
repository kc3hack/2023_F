<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

const isbn = ref("");

async function searchISBN() {
  await axios
    .get("https://jsonplaceholder.typicode.com/users") //テストurl
    .then((response) => {
      //BEから データを受け取ったときにやる処理
      console.log(response.data);//テスト
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
      ISBN13:<input value="" autofocus placeholder=" ISBN">
      <v-btn>書籍情報取得</v-btn>
      </div>

      <div class="result-area">
        <input v-model="title">
      </div>
      

      <v-btn class="search-button" @click="searchISBN" style="background-color: yellow;">本を検索・追加</v-btn>
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
  height: 500px;
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
  border-radius: 10px;
  padding: 4px;
  margin: 50px;
}
</style>
