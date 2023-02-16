<script setup lang="ts">
import { ref } from 'vue';
import html2canvas from 'html2canvas';

const drawer = ref(false);
const menuItems = [
    {
        name: '本棚',
        url: '/'
    },
    {
        name: 'ISBN登録',
        url: '/search'
    },
    {
        name: '書籍確認',
        url: '/stock'
    }
];

function openSNS(){
  drawer.value = false;
  
  setTimeout(async () => {
    console.log("screen shot");
    let image;
    //TODO 画面スクショ↓
    html2canvas(document.querySelector('#book-origin'),{proxy: "true", useCORS: true}).then((canvas) => {
        const link = document.createElement('a');//aタグ追加
        link.href = canvas.toDataURL();//base64形式で画像url生成
        //image = canvas.toDataURL();
        link.download = `export_image.png`;//画像ダウンロード設定
        link.click();//ダウンロード
      });
    
    //TODO Twitterへ飛ぶ↓
	  /*let s = "自分だけの本棚を公開しました!";
		//投稿画面を開く
		let url = "https://twitter.com/intent/tweet?url=" + "&text=" + s +"%20pic.twitter.com/"+image;
		window.open(url,"_blank","width=1000,height=500");*/

  }, 1000)
}
</script>

<template>
    <div class="menu">
    <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
    
    <v-navigation-drawer location="end" v-model="drawer" fixed temporary>
        <v-list nav dense>
          <v-list-item-group>
            <v-list-item>
              <v-list-item-title v-for="(menuItem, index) in menuItems" :key="index">
                <div class="mt-16">
                <RouterLink :to="menuItem.url" style="text-decoration: none; color: inherit">{{ menuItem.name }}</RouterLink>
                </div>
              </v-list-item-title>
              <button class="mt-16" @click="openSNS">本棚公開</button>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </div>
</template>

<style>
.menu{
  padding: 4px;
}
</style>
