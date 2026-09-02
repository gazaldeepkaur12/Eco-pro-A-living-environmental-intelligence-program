#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT22
#define SOIL_PIN A0
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  delay(1000);
  Serial.println("temp,humidity,soil");
}

void loop() {
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();
  int soilRaw = analogRead(SOIL_PIN);
  int soilPercent = map(soilRaw, 1023,0,0,100);
  soilPercent = constrain(soilPercent,0,100);


if (isnan(temp)|| isnan(humidity)) {
Serial.println("ERROR");
delay(2000);
return;
}

Serial.print(temp,1);
Serial.print(",");
Serial.print(humidity,1);
Serial.print(",");
Serial.println(soilPercent);


delay(2000);
}
