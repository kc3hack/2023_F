<script setup lang="ts">
import { ref } from "vue";

const dialog = ref(false);

const props = withDefaults(defineProps<Props>(), {
  title: "タイトルの取得に失敗",
  detail: "詳細の取得に失敗",
  count: 0,
  latest_num: 0,
  image_url: "/src/assets/noimage.png",
});

interface Props {
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
        <v-card-text>
          {{ detail }}
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" block @click="dialog = false">
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