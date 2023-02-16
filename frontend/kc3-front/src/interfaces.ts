export interface Book {
  isbn: number;
  title?: string;
  count?: number;
  date: Date;
  latest_num?: number;
  image_url?: string;
  isBookshelf?: boolean;
}

export interface User {
  token: string;
  authUser: string; //address
  books: Map<number, Book>;
}
