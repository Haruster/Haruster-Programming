// 3개의 버튼 컴포넌트를 가진 스윙 프레임 만들기

import javax.swing.*;
import java.awt.*;

public class ContenePaneEx extends JFrame {

    public ContenePaneEx() {

        setTitle("ContentPane과 JFrame"); // 프레임 타이틀 달기
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 프레임 윈도우를 닫으면 프로그램을 종료하도록 설정

        Container contentPane = getContentPane(); // 컨텐트 팬을 알아낸다.

        contentPane.setBackground(Color.ORANGE); // 컨텐트팬의 색을 오렌지색으로
        contentPane.setLayout(new FlowLayout()); // 컨텐트팬에 FlowLayout 배치관리자 달기

        contentPane.add(new JButton("OK")); // OK 버튼 달기
        contentPane.add(new JButton("Cancel")); // Cancel 버튼 달기
        contentPane.add(new JButton("Ignore")); // Ignore 버튼 달기

        setSize(300, 150); // 프레임 크기 300 x 150 설정
        setVisible(true);


    }

    public static void main(String[] args) {

        new ContenePaneEx();

    }

}