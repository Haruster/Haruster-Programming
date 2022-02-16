public class main {

	public static void main(String[] args) {

		System.out.println("2021E7334 정준영");

		String a = new String(" C#");
		String b = new String(",C++ ");
		
		System.out.println(a + "의 길이는  " + a.length()); 
		System.out.println(a.contains("#"));
		
		a = a.concat(b); 
	
		System.out.println(a);

		a = a.trim(); 
	
		System.out.println(a);
		
		a = a.replace("C#","Java");
	
		System.out.println(a);

		String s[] = a.split(","); 
	
		for (int i = 0; i < s.length; i++)
	
			System.out.println("분리된 문자열" + i + ": " + s[i]);
		
		a = a.substring(5); 
		
		System.out.println(a);
		
		char c = a.charAt(2);
		
		System.out.println(c);
	}

}
