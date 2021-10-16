import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int month = 0;
        int day = 0;

        System.out.print("태어난 월을 입력해주세요 : ");
        
        month = scanner.nextInt();

        System.out.print("태어난 일을 입력해주세요 : ");

        day = scanner.nextInt();

        switch(month) {
            case 1:
                if (day >= 20) {
                    System.out.println("물병자리");
                }
                else {
                    System.out.println("염소자리");
                }
                
                break;

            case 2:
                if(day >= 19) {
                    System.out.println("물고기자리");
                }
                else {
                    System.out.println("물병자리");
                }

                break;

                case 3:
                if(day >= 21) {
                    System.out.println("양자리");
                }
                else {
                    System.out.println("물고기자리");
                }

                break;

                case 4:
                if(day >= 20) {
                    System.out.println("황소자리");
                }
                else {
                    System.out.println("양자리");
                }

                break;

                case 5:
                if(day >= 21) {
                    System.out.println("쌍둥이자리");
                }
                else {
                    System.out.println("황소자리");
                }

                break;

                case 6:
                if(day >= 21) {
                    System.out.println("게자리");
                }
                else {
                    System.out.println("쌍둥이자리");
                }

                break;

                case 7:
                if(day >= 21) {
                    System.out.println("사자자리");
                }
                else {
                    System.out.println("게자리");
                }

                break;

                case 8:
                if(day >= 21) {
                    System.out.println("처녀자리");
                }
                else {
                    System.out.println("사자자리");
                }

                break;

                case 9:
                if(day >= 21) {
                    System.out.println("천칭자리");
                }
                else {
                    System.out.println("처녀자리");
                }

                break;

                case 10:
                if(day >= 21) {
                    System.out.println("전갈자리");
                }
                else {
                    System.out.println("천칭자리");
                }

                break;

                case 11:
                if(day >= 21) {
                    System.out.println("사수자리");
                }
                else {
                    System.out.println("전갈자리");
                }

                break;

                case 12:
                if(day >= 21) {
                    System.out.println("염소자리");
                }
                else {
                    System.out.println("사수자리");
                }

                break;

            
        }
    }
}