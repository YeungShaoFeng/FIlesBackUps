public class Array {
    public static void main(String[] args) {
        String text = "This is about Arrays. ";
        System.out.println(text);
    }
}

class NewArray {
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5 };
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
        System.out.println();

        String str[] = { "Go", "Hug" };
        for (int i = 0; i < str.length; i++) {
            System.out.print(str[i]);
            System.out.print(" ");
        }
        System.out.println();
    }
}

class Summing {
    public static void main(String[] args) {
        // You can access the length of an array(the number of the elements it stores)
        // via its length property.
        int[] intArr = new int[5];
        System.out.println("The length of the intArr is: " + intArr.length);

        int sum = 0;
        for (int i = 1; i < 101; i++) {
            sum += i;
        }
        System.out.println("The sum of 1 to 100 is: " + sum);
    }
}

class EnhancedForLoop {
    public static void main(String[] args) {
        int[] A = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        for (int i : A) {// Notice the colon after the variavle in the syntax.
            System.out.print(i + "\t");
        }
        System.out.println();
        /**
         * The enhanced for loop declares a varialble of a type compatible with the
         * elements of the array being accessed. The variable will be available within
         * the for block, and its value will be the same as the current array element.
         * So, on each iteration of the loop, the variable of t will be qual to the
         * correspoding element int the array.
         */
    }
}

class MultidimensionalArray {
    public static void main(String[] args) {
        // The example bleow creats a three-dimensional array.
        // And accesses the first element in the second array.
        int[][][] sample = { { { 1, 2, 3, 7 }, { 4, 5, 6 }, { 8, 9, 0 } },
                             { { 1, 2, 3, 7 }, { 4, 5, 6 }, { 8, 9, 0 } } };
        
        for (int i = 0; i < sample.length; i++) {
            for (int j = 0; j < sample[i].length; j++) {
                for (int k = 0; k < sample[i][j].length; k++) {
                    System.out.print(sample[i][j][k] + " ");
                }
                System.out.println();                
            }
            System.out.println();
        }
    }
}
