public class Constructors {
    public static void main(String[] args) {
        //The constructor is called when you creat an object using the new keyword.
        Vehicle benzVehicle = new Vehicle("Blaaaaaaaaaack!");
        System.out.println("The color of the benz is: " + benzVehicle.getColor());
    }
}

class Vehicle {
    private String color;
    /**
     * Constructors:
     *  A constructor can be used to provide initial values for object attributes.
     *  - A constructor name must be the same as its class name.
     *  - A constructor must have no explicit return type.
     * @param sColor
     */
    Vehicle(String sColor) {
        color = sColor;
    }

    //getter
    public String getColor() {
        return this.color;
    }
}