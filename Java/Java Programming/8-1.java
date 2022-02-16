// FileReader로 텍스트 파일 열기

import java.io.*;

public class main {

    public static void main(String[] args) {

        FileReader fin = null;

        try {
            
            fin = new FileReader("c:\\windows\\system.ini");
        
        int c;

        while ((c = fin.read()) != -1) { // 한 문자씩 파일 끝까지 읽는다.
        
            System.out.print((char)c);

        }

        fin.close();

    }

    catch (IOException e) {

        System.out.println("입출력 오류");

    }

}
}
