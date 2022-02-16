public class Book {

    String title;
    String author;

    void show() { System.out.println(title + " " + author);}

    public Book() {

        this("", "");

        System.out.println("생성자 호출됨");

    }

    public Book(String title) {

        this(title, "작자미상");

    }

    public Book(String title, String author) {

        this.title = title;
        this.author = author;

    }

    public static void main(String[] args) {

        Book littlePrince = new Book("어린왕자", "생텍쥐페리");
        Book lovestory = new Book("춘향전");
        Book emptyBook = new Book();

        lovestory.show();

    }

}