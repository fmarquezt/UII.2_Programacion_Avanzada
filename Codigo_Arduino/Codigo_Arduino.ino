//Programa realizado en Aruidno para el trabajo del Ingeniero Arzabala.
//IMEC91N
//-Fernando Alberto Marquez Torres
//-Dilan Rojas
//-Aaron Garcia
//-Oscar Vazquez
//-Jason Robledo



//Profesor, sobrescriba el numero de las siguientes variables
//con el # de pines que usara como LEDS de salida

int Pin_Salida_Digital_1 = 2;
int Pin_Salida_Digital_2 = 3;

//Profesor, Sobrescriba el valor, con el # de Pin analogico que usted usara
int Pin_Entrada_Analogica = A0;


char dato;
void setup() {
  // put your setup code here, to run once:
  pinMode (Pin_Salida_Digital_1,OUTPUT);
  pinMode (Pin_Salida_Digital_2,OUTPUT);
  pinMode (Pin_Entrada_Analogica,INPUT);

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
    int Lectura_Serial = analogRead(Pin_Entrada_Analogica);
  float Lectura_Serial_float = (5.0/1023)*Lectura_Serial;
  Serial.println(Lectura_Serial_float);
  delay(500);

  if (Serial.available()>0)
  {
    dato=Serial.read();
    if(dato == '1')
    {
      digitalWrite(Pin_Salida_Digital_1,HIGH);
    }
    if(dato == 'A')
    {
      digitalWrite(Pin_Salida_Digital_2,HIGH);
    }
    if(dato == '2')
    {
      digitalWrite(Pin_Salida_Digital_1,LOW);
    }
    if(dato == 'B')
    {
      digitalWrite(Pin_Salida_Digital_2,LOW);
    }
  }


}
