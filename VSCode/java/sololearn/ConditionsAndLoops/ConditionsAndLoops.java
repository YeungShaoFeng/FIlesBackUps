public class ConditionsAndLoops
{
    public static void main(String[] args)
    {
        String text = "This is about conditions and loops. ";
        System.out.println(text);
    }
}

class IfCondition
{
    public static void main(String[] args)
    {
        int x, y;
        x = 3; y = 18;
        if (x < y) {
            System.out.println("x(3) is smaller than y(18). ");
        } else {
            System.out.println("Hell No!!!!!!!!!!!!!!!!!!!!!");
        }
        /**
         * Any of the following comparsion operators may be used to form the condition
         *  < less than
         *  > greater than
         *  != not equal to
         *  == equal to
         *  <= less than or equal to
         *  >= greater than or equal to
         */

        // This is a nested if statement
        int age = 24;
        if (age > 0) {
            if (age > 16) {
                System.out.println("Welcome!");
            } else {
                System.out.println("Too Young");
            }
        } else {
            System.out.println("ErrOr>_< ");
        }

        /**
         * Instead of using nested if-else statements, 
         * you can use the else if statement to check multiple conditions
         * For example:
         */
        if (age <= 0) {
            System.out.println("ErrOr>_< ");
        } else if (age <= 16) {
            System.out.println("Too Young");
        } else if (age < 120) {
            System.out.println("Welcome! ");
        } else {
            System.out.println("REALLy? ");
        }
        // You can include as many else if statement as you want. 
    }
}

class LogicalStatement
{
    public static void main(String[] args)
    {
        int age = 22;
        int money = 800;
        
        if (age > 18) {
            if (money > 500) {
                System.out.println("Welcome!");
            }
        }
        System.out.println();
        //It is better in this way
        // The AND(&&) logical opetator
        if (age > 18 && money > 500) {
            System.out.println("Welcome! ");
        }

        // The OR(||) logical opetator
        if (age > 18 || money > 500) {
            System.out.println("Welcome! ");
        }

        // The NOT(!) logical operator
        if (!(age > 18)) { // !(age > 18) reads as "if age is NOT greater than 18".
            System.out.println("Too Young! ");
        } else {
            System.out.println("Welcome! ");
        }
    }
}

class SwitchStatement
{
    public static void main(String[] args)
    {
        int day = 3;

        switch(day)
        {
            case 1:
             System.out.println("Monday");
             break;
            case 2:
             System.out.println("Tuseday");
             break;
            case 3:
             System.out.println("Wednesday");
             break;
            default:
             System.out.println("No matches.");
        }
    }
}

class WhileLoops
{
    public static void main(String[] args)
    {
        int x = 3;

        while(x > 0) {
            System.out.println(x);
            x--;
        }
        System.out.println();
        /**
         * Outpus
         *  3
         *  2
         *  1
         * 
         */

        x = 6;
        while( x < 10 )
        {
          System.out.println(x);
          x++;
        }
        System.out.println("Loop ended");
        
        /*
        6
        7
        8
        9
        Loop ended
        */
    }
}

class ForLoops
{
    public static void main(String[] args)
    {
        for(int x = 1; x <=5; x++) {
            System.out.println(x);
        }
        System.out.println(); 
        /* Outputs
        1
        2
        3
        4
        5

        */
        // The example bleow prints only the even values between 0 and 10;
        for(int x=0; x<=10; x=x+2) {
            System.out.println(x);
        }
        /*
        0
        2
        4
        6
        8
        10
        */
    }
}

class DoWhileLoops
{
    public static void main(String[] args)
    {
        int x = 1;
        do {
            System.out.println(x);
            x++;
        } while(x < 5);
        /**
         * Notice that the condition appears at the end of the loop, 
         * so the statements in the loop execute once before it is tested.
         */
        System.out.println();
        /*
        1
        2
        3
        4

        */
        //Even with a false condition, the code will run once. Example:
        x = 1;
        do {
            System.out.println(x);
            x++;
        } while (x < 0);
        //Outputs 1

        /**
         * The break and continue statements change the loop's execution flow.
         * The break statement terminates the loop 
         * and transfers execution to the statement immediately following the loop.
         * Example:
         */
        while(x > 0) {
            System.out.println(x);
            if (x == 4) {
                break;
            }
            x++;
        }
        System.out.println();
        /**
         * Outputs
         *  1
         *  2
         *  3
         *  4

         */
        /**
         * The continue statement causes the loop to skip the remainder of its body 
         * and then immediately retest its condition prior to reiterating. 
         * In other words, it makes the loop skip to its next iteration.
         * Example:
         */
        for(x=10; x<=40; x=x+10) {
            if(x == 30) {
              continue;
            }
            System.out.println(x);
        }
        /* Outputs
        10
        20
        40
        */
    }
}