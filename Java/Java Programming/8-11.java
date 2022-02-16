// 블록 단위로 바이너리 파일 고속 복사

import java.io.*;

public class main {

    public static void main(String[] args) {

        File src = new File("c:\\Windows\\Web\\Wallpaper\\Theme1\\img1.jpg"); // 원본 파일 경로명

        // 윈도우 7에서는 File("c:\\Users\\Public\\Pictures\\Sample pictures\\desert.jpg")를 사용하면 된다.

        File dest = new File("c:\\Temp\\desert.jpg"); // 복사 파일

        try {

            FileInputStream fi = new FileInputStream(src); // 파일 입력 바이트 스트림
            FileOutputStream fo = new FileOutputStream(dest); // 파일 출력 바이트 스트림

            byte [] buf = new byte [1024 * 10]; // 10KB 버퍼

            while(true) {

                int n = fi.read(buf); // 버퍼 크기만큼 읽기, n은 실제 읽은 바이트

                fo.write(buf, 0, n);

                if(n < buf.length)

                    break; // 버퍼 크기보다 작게 읽었기 때문에 파일 끝에 도달. 복사 종료

            }

            fi.close();
            fo.close();

            System.out.println(src.getPath() + "를 " + dest.getPath() + "로 복사하였습니다.");

        } catch (IOException e) { System.out.println("파일 복사 오류");}



    }

}
