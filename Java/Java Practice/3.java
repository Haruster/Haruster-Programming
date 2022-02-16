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

        RCNT--;

        // 이름순으로 정렬하기
        System.out.println("array Data를 이름 순으로 정렬하기");

        for (int NN = 0; NN < RCNT; NN++) {

            for(int N = 0; N < (RCNT - NN); N++) {
                
                if (array[N][0].compareTo(array[N + 1][0]) > 0) {
                    
                    for (int R = 0; R < 5; R++) {
                        
                        String X = array[N][R];
                        
                        array[N][R] = array[N + 1][R];
                        array[N + 1][R] = X;
                        
                    }
                    
                }
                
            }

        }
        
        RCNT++;
    
        System.out.println("정렬된 array Data 출력하기");
        
        for (int N = 0; N < RCNT; N++) {
            
            System.out.println("\t(" + N + "번째 array 데이터) - ");
            
            for (int j = 0; j < 5; j++) {
                
                System.out.print(" " + array[N][j]);
                
            }
            
            System.out.println();
            
        }
    }
    
}