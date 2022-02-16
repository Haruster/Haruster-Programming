import java.io.*;
import java.util.*;
import java.io.IOException;

public class main {

    public static void main(String[] args) {

        Vector<String> vector = new Vector<String>(1);

        int n = 0;

        System.out.println("<< File Data를 읽어 Vector에 저장하고 화면으로 출력하기 >> \n");
        System.out.println("File로부터 Data를 읽어 Vector에 저장하고 화면으로 출력");

        try {

            File file = new File("c:\\test\\test.txt");

            FileReader fileReader = new FileReader(file);

            BufferedReader bufferedReader = new BufferedReader(fileReader);
            
            String line = "";
            
            while ((line = bufferedReader.readLine()) != null) {
                
                vector.addElement(new String(line));
                
                System.out.println("\t(" + n + ".번째 vector 데이터) - " + line);
                
                n++;
                
            }
            
            bufferedReader.close();

        } catch(FileNotFoundException e) {
        } catch(IOException e) {
            
            System.out.println(e);
            
        }
        
        System.out.println("vector에 저장된 Data를 화면으로 출력");
        
        vector.sort(null);
        
        for (n = 0; n < vector.size(); n++) {
            
            System.out.println("\t(" + n + "번째 vector 데이터) - " + vector.elementAt(n));
            
        }
        
        System.out.println("Vector Data를 array에 저장하고 화면으로 출력");
        
        Object[] array = vector.toArray();
        
        for (n = 0; n < array.length; n++) {
            
            System.out.println("\t(" + n + " 번째 array 데이터) - " + array[n]);
            
        }

    }
}