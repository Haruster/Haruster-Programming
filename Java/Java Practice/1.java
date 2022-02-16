import java.io.*;
import java.util.*;
import java.io.IOException;

public class main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        FileWriter fout = null;

        String NAME;

        int Semeter, Major, Refinement, PSE;
        int cnt = 0;

        System.out.println("<< Key B'd로부터 성적 Data를 입력 받아 File에 저장하기 >>\n");
        System.out.println("Key B'd로부터 성적 Data를 입력 받아 File에 저장");
        System.out.println("<이름> <학기> <전공> <교양> <시사> 과목의 점수를 입력해주세요 : (종료를 원하신다면 '.' Enter을 눌러주세요)");

        try {

            fout = new FileWriter("c\\test.txt");

            while (true) {

                System.out.print("(" + (cnt + 1) + ") -> ");

                NAME = scanner.next();

                if (NAME.compareTo(".") == 0)

                    break;

                Semeter = scanner.nextInt();
                Major = scanner.nextInt();
                Refinement = scanner.nextInt();
                PSE = scanner.nextInt();

                fout.write(NAME + " " + Semeter + " ");
                fout.write(Integer.toString(Major) + " ");
                fout.write(Integer.toString(Refinement) + " ");
                fout.write(Integer.toString(PSE) + " ");
                fout.write("\n", 0, 1);

                cnt++;

            }

            System.out.println("데이터 입력을 완료하였습니다.~");

            fout.close();

        } catch (IOException e) {

            System.out.println("입출력 오류가 발생하였습니다.");

        }

        scanner.close();

        System.out.println("총" + cnt + "개의 데이터를 File에 저장하였습니다.");

    }

}