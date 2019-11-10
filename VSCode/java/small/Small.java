import java.util.Scanner;

public class Small {
    public static void main(String[] args) {
        String plainText = javaIn("Plain text: ", 0, 0);
        String password = javaIn("Password: ", 0, 0);
        String cipher = smallIn(plainText, password);
        System.out.println(cipher);
    }

    public static String smallIn(String plainText, String password) {
    	return smallOn(plainText, password, 1);
    }
    
    public static String smallOut(String plainText, String password) {
    	return smallOn(plainText, password, 0);
    }
    
    private static String smallOn(String text, String password, int mode) {
        int[] length = {0, 0};
        length[0] = text.length();
        length[1] = password.length();
    	
        char[] textArray = text.toCharArray();
        char[] passwordArray = password.toCharArray();

        if (length[0] > length[1]) {
        	int tmp = length[0];
        	length[0] = length[1];
        	length[1] = tmp;
            for (int i = 0; i < length[1]; i++) {
                textArray[i] = (char)((int)textArray[i] + (int)passwordArray[i%length[0]]);
            }
        } else {
            for (int i = 0; i < length[0]; i++) {
                textArray[i] = (char)((int)textArray[i] + (int)passwordArray[i]);
            }
        }
        return String.valueOf(textArray);
    }


    static String javaIn(String pmt, int start, int end) {
        Scanner sc = new Scanner(System.in);
        System.out.print(pmt);
        String input = sc.nextLine();
//         sc.close();
        return (start > 0 || end > 0) ? input.substring(start, end) : input;
    }
}

class Test {
    public static void main(String[] args) {
        String str = "How are you today?";
        System.out.println(str.length());
        char[] arr = str.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            // System.out.print(String.valueOf(arr[i]));
            arr[i] = (char) ((int) arr[i] + 1);
        }
        System.out.println(arr);

    }
}