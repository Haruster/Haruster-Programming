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
        System.out.println("번호를 입력해주세요");
        System.out.println("1. 추가, 2. 수정 3. 삭제");

        int Number = scanner.nextInt();


        if (Number == 1) {

            try {

                System.out.println("추가할 데이터의 <이름> <학기> <전공> <교양> <시사> 과목의 점수를 입력해주세요 : (종료를 원하신다면 '.' Enter을 눌러주세요)");

                fout = new FileWriter("c:\\test\\test.txt");

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

            System.out.println("총" + cnt + "개의 데이터를 File에 저장하였습니다.");

        }

        else if (Number == 2) {

            File file = new File("c:\\test\\test.txt");

            if(file.exists() == false) {

                // 파일이 존재하지 않을 경우 새로운 파일을 생성
                try {

                    System.out.println("추가할 데이터의 <이름> <학기> <전공> <교양> <시사> 과목의 점수를 입력해주세요 : (종료를 원하신다면 '.' Enter을 눌러주세요)");

                    fout = new FileWriter("c:\\test\\test.txt");

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

                } System.out.println("데이터 입력을 완료하였습니다.~");

                    fout.close();

                } catch (IOException e) {

                    System.out.println("입출력 오류가 발생하였습니다.");

                }

                System.out.println("총" + cnt + "개의 데이터를 File에 저장하였습니다.");


            }

            System.out.println("파일의 내용을 추가하는 수정을 하시려면 1번을, 파일의 내용을 삭제하는 수정을 하시려면 2번을 눌러주세요 : ");

            int Key = scanner.nextInt();

            if (Key == 1) {

                try {

                    System.out.println("추가할 데이터의 <이름> <학기> <전공> <교양> <시사> 과목의 점수를 입력해주세요 : (종료를 원하신다면 '.' Enter을 눌러주세요)");

                    fout = new FileWriter("c:\\test\\test.txt");

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

                System.out.println("총" + cnt + "개의 데이터를 File에 저장하였습니다.");

            }


            if (Key == 2) {

                // 파일 열어서 삭제하는 로직
                String dummy = "";
                try {
                    BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file)));

                    // 삭제하고자 하는 position 이전까지는 이동하며 dummy에 저장
                    String line;
                    
                    System.out.println("삭제할 데이터의 Position을 입력해주세요 : ");
                    
                    int position = scanner.nextInt();
                    
                    for(int i=0; i<position; i++) {
                        line = br.readLine(); //읽으며 이동
                        dummy += (line + "\r\n" );
                    }

                    // 삭제하고자 하는 데이터는 건너뛰기
                    String delData = br.readLine();

                    // 삭제하고자 하는 position 이후부터 dummy에 저장
                    while((line = br.readLine())!=null) {

                        dummy += (line + "\r\n" );

                    }

                    // FileWriter를 이용해서 덮어쓰기
                    FileWriter fw = new FileWriter("c:\test\test.txt");
                    fw.write(dummy);

                    //bw.close();
                    fw.close();
                    br.close();

                } catch (Exception e) {

                    e.printStackTrace();

                }

            }


        }

        else if (Number == 3) {

            // 파일 열어서 삭제하는 로직
            File file = new File("c:\\test\\test.txt");
            String dummy = "";
            try {
                BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file)));

                // 삭제하고자 하는 position 이전까지는 이동하며 dummy에 저장
                String line;

                System.out.println("삭제할 데이터의 Position을 입력해주세요 : ");

                int position = scanner.nextInt();
                
                for(int i=0; i<position; i++) {
                    line = br.readLine(); //읽으며 이동
                    dummy += (line + "\r\n" );
                }

                // 삭제하고자 하는 데이터는 건너뛰기
                String delData = br.readLine();
                
                // 삭제하고자 하는 position 이후부터 dummy에 저장
                while((line = br.readLine())!=null) {

                    dummy += (line + "\r\n" );

                }

                // FileWriter를 이용해서 덮어쓰기
                FileWriter fw = new FileWriter("c:\test\test.txt");
                fw.write(dummy);

                //bw.close();
                fw.close();
                br.close();

            } catch (Exception e) {

                e.printStackTrace();

            }


        }

        else {

            System.out.println("올바른 번호를 입력해주세요!!");

        }

        scanner.close();


    }

}