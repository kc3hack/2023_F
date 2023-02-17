<script setup lang="ts">
import { ref } from "vue";
import { useUsersStore } from "@/stores/users";

const userStore = useUsersStore();

const address = ref("");
const password = ref("");

const isNew = ref(false);
function toggle() {
  isNew.value = !isNew.value;
}

async function newForm() {
  //新規登録
  await userStore.signup(address.value, password.value);
}

async function existForm() {
  //ログイン
  await userStore.login(address.value, password.value);
}
</script>

<template>
  <div class="login-background">
    <h1 class="greeting">書籍管理へようこそ</h1>
    <div class="login-block">
      <button class="toggle" @click="toggle">
        {{ isNew ? "ログインする方はこちら" : "新規登録の方はこちら" }}
      </button>
      <div>
        <div class="form">
          <label for="message">メールアドレス: </label>
          <input v-model="address" type="text" placeholder=" address" /><br />
          <label for="message">パスワード: </label>
          <input
            v-model="password"
            type="password"
            placeholder=" password"
          /><br />
          <button @click="newForm" v-if="isNew" class="submit">新規登録</button>
          <button @click="existForm" v-else class="submit">ログイン</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.login-background {
  padding: 280px;
}
.greeting {
  padding: 4px;
  text-align: center;
  font-family: serif;
  color: white;
}
.login-block {
  margin-left: auto;
  margin-right: auto;
  background-color: #e7d0a9;
  height: 180px;
  width: 600px;
  padding: 10px;
  border: thick double;
  border-radius: 10px;
}
.toggle {
  background-color: lightgray;
  border: solid;
  border-radius: 5px;
  padding: 4px;
}
.form {
  text-align: center;
  margin: 10px;
}
.submit {
  margin: 15px;
  padding: 4px;
  border: solid;
  border-radius: 10px;
  background-color: yellow;
}
</style>
