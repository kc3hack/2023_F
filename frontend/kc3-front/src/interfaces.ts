export interface Book {
  isbn: number;
  title?: string;
  count?: number;
  date: Date;
  latest_num?: number;
  image_url?: string;
}
