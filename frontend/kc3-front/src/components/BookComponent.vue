<script setup lang="ts">
import { ref } from "vue";

const dialog = ref(false);

const props = withDefaults(defineProps<Props>(), {
  title: "タイトルの取得に失敗",
  count: 0,
  latest_num: 0,
  image_url: "/src/assets/noimage.png",
  isBookshelf: false,
});

interface Props {
  isbn: number;
  title: string;
  count?: number;
  date: Date;
  latest_num?: number;
  image_url?: string;
  isBookshelf: boolean;
}
</script>

<template>
  <v-col cols="3.5" class="mr-n16 mt-3">
    <v-img
      :src="image_url"
      class="white-text align-end hover_anim"
      aspect-ratio="1.5"
      @click="dialog = true"
    ></v-img>
  </v-col>

  <v-dialog v-model="dialog" max-width="500">
    <div class="text-center">
      <v-card>
        <v-card-title>
          {{ title }}
        </v-card-title>

        <v-divider class="mx-4 mb-1"></v-divider>

        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-card color="teal-darken-2" theme="dark" elevation="5">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="125" class="me-8">
                    <v-icon size="100">mdi-book-account</v-icon>
                  </v-avatar>
                  <div class="me-auto mt-6 ms-auto">
                    <v-card-title>持っている本の数</v-card-title>
                    <v-card-text>{{ count }}冊</v-card-text>
                  </div>
                </div>
              </v-card>
            </v-col>

            <v-col cols="12">
              <v-card color="light-green-darken-1" theme="dark">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="125" class="me-8">
                    <v-icon size="100">mdi-calendar-multiselect</v-icon>
                  </v-avatar>
                  <div class="me-auto mt-6 ms-auto">
                    <v-card-title>登録日</v-card-title>
                    <v-card-text>{{ date.toLocaleDateString() }}</v-card-text>
                  </div>
                </div>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card color="green-lighten-1" theme="dark">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="125" class="me-8">
                    <v-icon size="100">mdi-bookshelf</v-icon>
                  </v-avatar>
                  <div class="me-auto mt-6 ms-auto">
                    <v-card-title>所持している最新刊</v-card-title>
                    <v-card-text>{{ latest_num }}巻</v-card-text>
                  </div>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" block @click="dialog = false" max-width="25">
            <v-icon>mdi-close-box-multiple-outline</v-icon>
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </v-dialog>
</template>

<style scoped>
.hover_anim {
  transition-duration: 0.3s;
}

.hover_anim:hover {
  transform: scale(1.1);
}
</style>
