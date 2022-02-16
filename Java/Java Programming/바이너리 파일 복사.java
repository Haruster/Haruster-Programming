// 바이너리 파일 복사

import java.io.*;

public class main {

    public static void main(String[] args) {

        File src = new File("c:\\Windows\\Web\\Wallpaper\\Theme1\\img1.jpg"); // 원본 파일 경로명

        // 윈도우 7에서는 File("C:\\Users\\Public\\Picture\\Sample Pictures\\desert.jpg");를 사용하면 된다.

        File dest = new File("c:\\Temp\\copyimg.jpg"); // 복사 파일 경로명

        int c; 

        try {

            FileInputStream fi = new FileInputStream(src); // 파일 입력 바이트 스트림 생성
            FileOutputStream fo = new FileOutputStream(dest); // 파일 출력 바이트 스트림 생성

            while((c = fi.read()) != -1) {

                fo.write((byte)c);

            }

            fi.close();
            fo.close();

            System.out.println(src.getPath() + "를 " + dest.getPath() + "로 복사하였습니다.");

        } catch(IOException e) {

            System.out.println("파일 복사 오류");

        }

    }

}