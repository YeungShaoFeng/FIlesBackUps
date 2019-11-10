import java.util.Scanner;

public class BasicConcepts
{

    public static void main(String[] args) {
        System.out.println("Hello world! ");
    }
}

class NumericalOperations
{
    public static void main(String[] args)
    {
        int x, y;
        x = 49;y = 4;
        System.out.println("          x: " + x);
        System.out.println("          y: " + y);
        System.out.println("        x/y: " + x/y);
        System.out.println("    x/y*1.0: " + x/y*1.0);
        System.out.println();

        double m, n;
        m = 49;n = 4;
        System.out.println("          n: " + n);
        System.out.println("          m: " + m);
        System.out.println("        m/n: " + m/n);
        System.out.println("        m%n: " + m%n);
        System.out.println();

        int increment = 5, decrement = 5;
        System.out.println("  increment: " + increment);
        System.out.println("  decrement: " + decrement);        
        System.out.println("++increment: " + ++increment);
        System.out.println("--decrement: " + --decrement);
        increment = 5;decrement = 5;
        System.out.println("increment++: " + increment++);
        System.out.println("decrement--: " + decrement--);
    }
}

class Comments
{

    public static void main(String[] args) {
    //  single-line commet
    
    /*  
        multi-line
        comments 
    */
    
    /** This is a documentation comment.  */
    
    /** This is also a
     *  documentation comment. 
     */
    }
}

class StringConcatenation
{
    public static void main(String[] args)
    {
        String firstName, lastName;
        firstName = "Linxi";lastName = "Yeung";

        System.out.println("Hello, my name is " + firstName + " " + lastName + ". ");
    }
}

class GetInput
{
    public static void main(String[] args)
    {
        System.out.println("Type in something below. ");
        Scanner myVar = new Scanner(System.in);
        System.out.println(myVar.nextLine());
        myVar.close(); 
        /**
         * make sure you close the new instante of the Scanner class
         * after using. otherwise it leads to Resource leak. 
         */
        
         /**
         * You can now read in diffenret kinds of input data that the user enter.
         * Here are some methods that are available through the Scanner class:
         *  Read a byte - nextByte()
         *  Read a short - nextShort()
         *  Read an int - nextInt()
         *  Read a long - nextLong()
         *  Read a float - nextFloat()
         *  Read a double - nextDouble()
         *  Read a boolean - nextBoolean()
         *  Read a complete line - nextLine()
         *  Read a word - next()
         */
    }
}
