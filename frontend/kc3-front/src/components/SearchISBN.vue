<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

let isbn = ref("");
let image = ref("");
let title = ref("");
let volume = ref("");
let registerDate = ref("");

function searchISBN() {
  let query = isbn.value.split(" ").join("+");
  // APIを取得
  const url = "https://api.openbd.jp/v1/get?isbn=" + query + "&pretty";
  //json
  fetch(url)
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      //表紙
      image.value = data[0].summary.cover;
      document.getElementById("thumbnail")?.setAttribute("src", image.value);

      let group = title_separete(data[0].summary.title);
      //タイトル
      title.value = group[1].replace("（", "").replace("(", "");
      if(title.value === "タイトルを取得できませんでした") title.value = data[0].summary.title;
      //巻数
      volume.value = group[2];
      //登録日
      let origin = new Date();
      let year = origin.getFullYear();
      let month = origin.getMonth() + 1;
      let day = origin.getDate();
      registerDate.value = year + "/" + month + "/" + day;
    })
    .catch((e) => {
      alert("ISBNが存在しません.");
    });
}

function title_separete(title: string): string[] {
  let group: string[] = title.match(/(\S*)\s?.*([0-9]|[０-９]).*/) ?? [
    "情報の取得に失敗",
    "タイトルを取得できませんでした",
    "巻数を取得できませんでした",
  ];
  return group;
}

async function addBook() {
  const authorization =
    "Bearer " + JSON.parse(sessionStorage.getItem("user")).token;
  const header = {
    headers: {
      accept: "application/json",
      Authorization: authorization,
      "Content-Type": "application/json",
    },
  };

  await axios
    .post(
      "/api/books/create",
      {
        title:
          title.value === "タイトルを取得できませんでした" ? null : title.value,
        have_books: 0,
        resist_date: registerDate.value,
        new_books: Number(volume.value), // よくわからない項目
        image_url: image.value,
      },
      header
    ) //テストurl
    .then((response) => {
      //BEから データを受け取ったときにやる処理
      console.log(response.data); //テスト
    })
    .catch((e) => {
      console.log(e);
      alert("登録エラーが起こりました.");
    });
}
</script>

<template>
  <div class="background">
    <div class="outside">
      <div class="search-area">
        ISBN13:<input v-model="isbn" autofocus placeholder=" ISBN" />
        <v-btn @click="searchISBN">書籍情報取得</v-btn>
      </div>

      <div class="result-area">
        <img src="" id="thumbnail" />
        <p>タイトル:<input v-model="title" placeholder="title" /></p>
        <p>巻数:<input v-model="volume" placeholder="volume" /></p>
        <p>
          登録日:<input v-model="registerDate" placeholder="registerDate" />
        </p>
      </div>

      <v-btn
        class="search-button"
        @click="addBook"
        style="background-color: yellow"
        >本を追加</v-btn
      >
    </div>
  </div>
</template>

<style>
.background {
  padding: 150px;
}

.outside {
  background-color: #e7d0a9;
  margin-left: auto;
  margin-right: auto;
  padding: 30px;
  height: 600px;
  width: 600px;
  text-align: center;
  border: thick double;
  border-radius: 10px;
}

.search-area {
  background-color: lightgray;
  border: solid;
}

.result-area {
  background-color: lightgray;
  border: solid;
}

input {
  margin: 5px;
}

.search-button {
  border-radius: 10px;
  padding: 4px;
  margin: 50px;
}
</style>
