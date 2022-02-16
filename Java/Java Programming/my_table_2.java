public class main {

    public static void main(String[] args) {

        int i, j, k;

        k = 0;

        for(i = 1; i < 6; i++) {

            for(j = 1; j <= i; j++) {

                k++;

                System.out.print(k+" ");

            }

            System.out.println();

        }

    }

}