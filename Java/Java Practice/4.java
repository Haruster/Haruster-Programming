import java.io.*;
import java.util.*;
import java.io.IOException;

public class main {

    public static void main(String[] args) {

        String[][] array = new String[11][5]; // 2차원 배열 정의

        int RCNT = 0;

        System.out.println("<< File Data를 읽어 array에 저장하고 정렬하여 출력하기 >> \n");
        System.out.println("File Data를 읽어 array에 저장하기");

        try {

            File file = new File("c:\\test\\test.txt");

            FileReader fileReader = new FileReader(file);

            BufferedReader bufferedReader = new BufferedReader(fileReader);

            String line = "";

            while((line = bufferedReader.readLine()) != null) {

                array[RCNT] = line.split(" ");

                System.out.println("\t(" + RCNT + " 번째 array 데이터) -");

                for(int j = 0; j < array[RCNT].length; j++) {

                    System.out.println("[" + RCNT + "][" + j + "] : " + array[RCNT][j]);

                }

                System.out.println();

                RCNT++;

            }

            bufferedReader.close();

        } catch (FileNotFoundException e) {
        } catch (IOException e) {

            System.out.println(e);

        }

        System.out.println("array Data를 이용하여 보고서를 작성하고 파일로 출력");

        String line;

        int SUM;

        float AVG;

        FileWriter fout = null;

        try {

            fout = new FileWriter("c:\\test\\test.out");

            fout.write("Refort##001\r\n"); // 굴림체 보통 20으로 작성
            fout.write("===============================\r\n");
            fout.write("-------\t---------\t----\t----\t----\t----\t----\t----\r\n");
            fout.write("이름\t학기\t전공\t교양\t시사\t합계\t평균\t석차\r\n");
            fout.write("-------\t---------\t----\t----\t----\t----\t----\t----\r\n");

            for(int N = 0; N < RCNT; N++) {

                line = array[N][0] + "\t" + array[N][1] + "\t" + array[N][2] + "\t" + array[N][3] + "\t" + array[N][4];

                SUM = Integer.parseInt(array[N][2]) + Integer.parseInt(array[N][3]) + Integer.parseInt(array[N][4]);
                
                AVG = SUM / 3;
                
                line = line + "\t" + SUM + "\t" + AVG;
                
                fout.write(line, 0, line.length());
                fout.write("\r\n", 0, 2);

            }

            fout.write("-------\t---------\t----\t----\t----\t----\t----\t----\r\n");
            fout.write("\r\n", 0, 2);
            
            fout.close();

        } catch (IOException e) {
            
            System.out.println("입출력 오류");
            
        }
        
        System.out.println("파일 경로에 저장된 결과 확인");
        
    }

}