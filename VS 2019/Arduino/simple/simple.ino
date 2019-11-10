
int value = 0;

void setup() {
    Serial.begin(115200);
    pinMode(PB0, INPUT_ANALOG);
    pinMode(PB1, OUTPUT);
}

void loop() {
    value = analogRead(PB0);
    Serial.println(value); 
    delay(300);
}