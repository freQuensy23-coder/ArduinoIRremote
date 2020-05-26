

int SPEED = 9600;
int lamp_pin = 11;
int reciver_pin = 3;
  
bool recieve(){
    wait = true;
    delay_time = 1000;
    //*****************************************
    while (wait){

      
        time_start = millis()
        sgn = digitalRead(reciver_pin);
        if (sgn == 0){
          return true;
          wait = false
        }
        else{
          if (time_start - millis() < delay_time){
            return false;
            wait = false;
          }
        }
      
          
      }
    //*****************************************  
  }

  
void transmit_bool(bool sgn){
    int a = 1;
  }
  
void setup() {
  // put your setup code here, to run once:
  Serial.begin(SPEED);

  pinMode(lamp_pin, OUTPUT);
  pinMode(reciver_pin, INPUT);
  

}

void loop() 
{ 
   
}
