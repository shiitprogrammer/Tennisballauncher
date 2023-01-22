void setup() {
  // put your setup code here, to run once:
pinMode(3, OUTPUT);
pinMode(5, OUTPUT);
Serial.begin(9600);
int speed = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
int motor = 3;
if ( Serial.available())
  {
  int rpm = Serial.readString().toInt();
   
  if( rpm >= 500 && rpm <= 4000)
    {
      Serial.println(rpm); 
      Serial.println(rpm / 8);
      int speed = int(map(rpm, 0,4000,0,255));
      analogWrite(motor, speed);
      
    }
  }
  
}
