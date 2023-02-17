import { defineStore } from "pinia";
import type { Book, User } from "@/interfaces";
import axios from "axios";

interface State {
  userStore: User;
}

export const useUsersStore = defineStore({
  id: "users", //ストアを特定するための名称
  state: (): State => {
    //データ本体
    return {
      userStore: { token: "", authUser: "", books: new Map<number, Book>() },
    };
  },
  getters: {
    // データの加工処理
    getBooks: (state): Map<number, Book> => {
      return state.userStore.books;
    },
  },
  actions: {
    //データの変更処理
    Init() {
      let user;
      const userJSONStr = sessionStorage.getItem("user");
      if (userJSONStr != undefined) {
        const userJSON = JSON.parse(userJSONStr);
        user = userJSON;
        this.userStore = user;
        this.userStore.books = bookListInit; //あとでけす
      }
    },
    addBook(book: Book): void {
      this.userStore.books.set(book.isbn, book);
    },
    async signup(address: string, password: string) {
      await axios
        .post("/api/users/create", {
          name: address,
          password: password,
        })
        .then((response) => {
          //BEから データを受け取ったときにやる処理
          console.log("新規登録成功");
          this.userStore.authUser = address;
          this.userStore.token = response.data.access_token;

          const userJSONStr = JSON.stringify(this.userStore);
          sessionStorage.setItem("user", userJSONStr);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
});

const bookListInit = new Map<number, Book>();

bookListInit.set(11111111111, {
  isbn: 11111111111,
  title: "sample",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088825656.jpg",
});
bookListInit.set(2222222222222, {
  isbn: 2222222222222,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784040646176.jpg",
});
bookListInit.set(2222222222223, {
  isbn: 2222222222223,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088917191.jpg",
});
bookListInit.set(2222222222224, {
  isbn: 2222222222224,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784088904320.jpg",
});
bookListInit.set(2222224222223, {
  isbn: 2222224222223,
  title: "test",
  count: 1,
  date: new Date(2023, 2, 12),
  latest_num: 1,
  image_url: "https://cover.openbd.jp/9784041011102.jpg",
});
