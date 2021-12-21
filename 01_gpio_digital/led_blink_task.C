#include <wiringPi.h>
int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (11, OUTPUT) ;
  pinMode (9, OUTPUT) ;
  pinMode (10, OUTPUT) ;
  digitalWrite(11, HIGH); delay(2000);
  digitalWrite(11,LOW);
  digitalWrite(9,HIGH); delay(2000);
  digitalWrite(9,LOW);
  digitalWrite(10,HIGH); delay(2000);
  digitalWrite(10,LOW);
  pinMode(11,INPUT);
  pinMode(9,INPUT);
  pinMode(10,INPUT);


  return 0 ;
}