```
public class PalindromeImpl {


	public static void main(String[] args) {
 
   String input = "abcba";
   //"112311"; "abccba"; "112211";
   
   int start = 0;
	 int end = input.length() - 1;
   
   //we can also use while(true) instead of for
   for(;;) {			
			if (input.charAt(start) == input.charAt(end)) {
				start++;
				end--;
			}else {
				System.out.println("false");
				break;
			}
			
			if(start>end) {
				System.out.println("true");
				break;
			}
		}
    ```
