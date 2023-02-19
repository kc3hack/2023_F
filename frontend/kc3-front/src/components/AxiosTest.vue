<script setup lang="ts">
import axios from "axios";
import { ref } from "vue";

const test = ref("");
const postes = ref("");

async function gettest() {
  await axios
    .get("/api/test", {
      params: {
        tes: "testdayo",
      },
    })
    .then((res) => (test.value = res.data))
    .catch((error) => {
      console.log(error);
    });
}

const tes = {
  isbn: 111111,
  title: "ぼっち・ざ・ろっく",
};

async function posttest() {
  await axios
    .post("/api/posttest", tes)
    .then((res) => (postes.value = res.data.title))
    .catch((error) => {
      console.log(error);
    });
}
</script>

<template>
  <v-btn @click="gettest">getてすと</v-btn>
  <p>{{ test }}</p>
  <v-btn @click="posttest">post</v-btn>
  <p>{{ postes }}</p>
</template>
