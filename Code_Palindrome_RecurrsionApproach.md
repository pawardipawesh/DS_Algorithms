```
public class PalindromeImpl {

	public static void main(String[] args) {
		String input = "112211";
    //"112311"; "abccba";"abcba";
    
    PalindromeImpl obj =  new PalindromeImpl();
		System.out.println(obj.isPalindrome(input));
 }
 
 private boolean isPalindrome(String input) {
		
		if(input.length()<=1) {
			return true;
		}
		
		if (input.charAt(0) == input.charAt(input.length()-1)) {
		  return isPalindrome(input.substring(1,input.length()-1 ));
		}else {
			return false;
		}
}
```
