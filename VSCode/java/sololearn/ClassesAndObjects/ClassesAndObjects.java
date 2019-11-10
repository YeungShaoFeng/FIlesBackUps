public class ClassesAndObjects {
    private static String text = "This is about Classes and Objects. ";
    public static void main(String[] args) {
        System.out.println(text);
        sayHelloTo("there");
        System.out.println(sum(1, 2));
        Dog dog = new Dog();
        dog.bark();
    }

    // Method with parameter
    public static void sayHelloTo(String name) {
        System.out.println("Hello " + name + "!");
    }

    // Method with return type and paremeters
    static int sum(int val1, int val2) {
        return val1 + val2;
    }
}
/**
 * Access Modifiers:[default, public, protected, private]
 *  For Classes:
 *      public: The class is accessible by any other class.
 *      default: The class is accesible only by classes in the same package.
 *  For Attributes and Methods:
 *      default: A variable or method declared with on access control modifier
 *               is available to any other class in the same package.
 *      public: Accessible for any other class.
 *      protected: Provides the same access as the default access modifier, with
 *              the addition that subclasses can access protected methods and
 *              variables of the superclass.
 *      private: Accessible only within the declared class itself.
 *              
 */
class Dog {
    public void bark() {
        System.out.println("Woof-Woof...");
    }
}