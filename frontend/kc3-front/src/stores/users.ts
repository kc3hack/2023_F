import { defineStore } from "pinia";
import type { Book, User } from "@/interfaces";
import axios from "axios";
import router from "@/router";

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
        this.getUserHasBooks();
      }
    },
    addBook(book: Book): void {
      this.userStore.books.set(book.isbn, book);
    },
    async getUserHasBooks() {
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
        .get(
          "/api/books/all",
          header
        )
        .then((response) => {
          return response.data;
        })
        .then((data) => {
          const max = data.length > 25 ? 25 : data.length;
          const bookList = new Map<number, Book>();
          for (let i = 0; i < max; i++) {
            bookList.set(i, data[i]);
          }
          return bookList;
        })
        .then((bookList) => {
          this.userStore.books = bookList;
        })
        .catch((e) => {
          console.log(e);
        });
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

          router.push({ path: "/" });
        })
        .catch((e) => {
          console.log(e);
        });
    },
    async login(address: string, password: string) {
      const headers = {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      };

      await axios
        .post(
          "/api/auth/token",
          {
            username: address,
            password: password,
          },
          headers
        )
        .then((response) => {
          console.log("ログイン成功");
          this.userStore.authUser = address;
          this.userStore.token = response.data.access_token;

          const userJSONStr = JSON.stringify(this.userStore);
          sessionStorage.setItem("user", userJSONStr);

          router.push({ path: "/" });
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
});
