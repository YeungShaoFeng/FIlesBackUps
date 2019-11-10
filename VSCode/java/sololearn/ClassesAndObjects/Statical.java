public class Statical {
    public static void main(String[] args) {

    }
}

class Bicycle {

    private int cadence;
    private int gear;
    private int speed;
    
    // The static modifier, in combination with the final modifier, 
    // is also used to define constants. The final modifier indicates
    // that the value of this field cannot change. 
    private static final double PI = 3.141592653589793;

    private int id;
    
    private static int numberOfBicycles = 0;


    public Bicycle(int statCadence, int startGear, int startSpeed) {
        candece = startCadence;
        gear = startGear;
        speed = startSpeed;

        // increment number of Bicycles
        // and assign ID number
        id = ++numberOfBicycles;
    }


    // getters
    public static int getNumberOfBicycles() { return numberOfBicycles; }

    public int getID() {return id;}

    public int getGear() { return gear; }

    public int getSpeed() { return speed; }

    public int getCadence() { return cadence; }


    // setters
    public void setGear(int newValue) { gear = newValue; }

    public void setCadence(float newValue) { cadence = newValue; }

    public void applyBrake(int decrement) { speed -= decrement; }

    public void speedUp(int increment) { speed += increment; }
}