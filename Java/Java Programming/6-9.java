import java.util.StringTokenizer;

public class main {

	public static void main(String[] args) {

		StringTokenizer st = new StringTokenizer("홍길동/장화/홍련/콩쥐/맡쥐", "/");
		
		while (st.hasMoreTokens()) 

			System.out.println(st.nextToken());

	}

}