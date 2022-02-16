import java.io.*;
import java.util.*;

public class main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        FileWriter fout = null;

        int c;

        try {

            fout = new FileWriter("c:\\Temp\\Test.txt"); // 파일과 연결된 출력 문자 스트림 생성

            while(true) {

                String line = scanner.nextLine(); // 빈칸을 포함하여 한 줄 읽기

                if(line.length() == 0) // 한 줄에 <Enter>키만 입력한 경우
                    
                    break;

                fout.write(line, 0, line.length()); // 읽은 문자열을 파일에 저장
                fout.write("\r\r", 0, 2); // 한 줄 띄기 위해 \r\r을 파일에 저장

            }

            fout.close();

        } catch (IOException e) {

            System.out.println("입출력 오류");

        }

        scanner.close();

    }

}