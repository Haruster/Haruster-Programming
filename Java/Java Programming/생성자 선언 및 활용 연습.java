public class Book {

    String title;
    String author;

    public Book(String t) { // 생성자

        title = t;
        author = "작자미상";

    }

    public Book(String t, String a) { // 생성자

        title = t;
        author = a;

    }

    public static void main(String[] args) {

        Book littleprince = new Book("어린왕자", "생텍쥐페리"); // 생성자 Book(String t, String a) 호출

        Book loveStory = new Book("춘향전"); // 생성자 Book(String t) 호출

        System.out.println(littleprince.title + " " + littleprince.author);
        System.out.println(loveStory.title + " " + loveStory.author);

    }

}