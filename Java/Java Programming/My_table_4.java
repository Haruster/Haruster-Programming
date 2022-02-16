public class main {

    public static void main(String[] args) {

        char alpha = 65;

        int i, j;

        for(i = 1; i < 6; i++) {

            for(j = 0; j < 5; j++) {

                System.out.print((char)(alpha + (j * 5 )) + " ");

            }

            alpha++;
            System.out.println();

        }

    }

}