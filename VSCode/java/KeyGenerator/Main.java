public class Main {
    public static void main(String[] argss) {
        String str = "Linxi";
        KeyGenerator keygen = new KeyGenerator(str);
        keygen.keyGo(0, 0);
    }

}

class KeyGenerator {

    private String seedStr = "";
    private String key = "";
    private char arraySeedStr[] = {0};
    private int sumOfSeedStr = 0;

    // // Radomly constructor
    // public void keyGeneretor() {

    // }

    // Hand-drive constructor
    public void keyGenerartor(String str) {
        setSeedStr(str);
        setArraySeedStr(str);
    }

    public String keyGo(int start, int end) {
        for (int i = 0; i < this.arraySeedStr.length; i++) {
            this.setNumOfStr((int)this.arraySeedStr[i], getPower((int)this.arraySeedStr[i]));
        }
        return this.key;
    }

    private int getPower(int baseNum) {
        int tmp = 0;
        while ((baseNum /= 10) != 0) {
            tmp++;
        }
        return tmp;
    }

    // setters
    public void setNumOfStr(int newValue, int power) {
        this.sumOfSeedStr = this.sumOfSeedStr * (int) Math.pow((double) 10, (double) power) + newValue;
    }

    public void setSeedStr(String newSeedStr) {
        this.seedStr = newSeedStr;
    }

    public void setArraySeedStr(String seedStr) {
        this.arraySeedStr = seedStr.toCharArray();
    }


    //getters
    public String getSeedStr() {
        return this.seedStr;
    }

    public String getKey() {
        return this.key;
    }

    public char[] getArraySeedStr() {
        return this.arraySeedStr;
    }

    public int getSumOfSeedStr() {
        return this.sumOfSeedStr;
    }
}