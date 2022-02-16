// InputStreamReader로 한글 텍스트 파일 읽기

import java.io.*;

public class main {

    public static void main(String[] args) {

        InputStreamReader in = null;
        FileInputStream fin = null;

        try {

            fin = new FileInputStream("c:\\temp\\hangul.txt");
            in = new InputStreamReader(fin, "MS949"); // 올바른 문자 집합 저장

            int c;

            System.out.println("인코딩 문자 집합은 " + in.getEncoding());

            while ((c = in.read()) != -1) {

                System.out.print((char)c);

            }

            in.close();
            fin.close();

        } catch (IOException e) {
            System.out.println("입출력 오류");
        }

    }

}