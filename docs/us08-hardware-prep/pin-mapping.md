# Pemetaan Pin US-08

ESP32 yang dipakai: DevKit V1 (WROOM-32), logika 3,3 V.

| Sambungan | Pin ESP32 | Alasan |
|---|---|---|
| INA219 SDA | GPIO 21 | pin I2C default |
| INA219 SCL | GPIO 22 | pin I2C default |
| INA219 VCC | 3V3 | mengikuti level logika ESP32 |
| Sensor hujan D0 (digital) | GPIO 27 | pin bebas, bukan strapping pin, mendukung pull-up |
| Sensor hujan AO (analog, opsional) | GPIO 34 | pin input-only, pas untuk ADC |

Alur daya: TEG -> INA219 -> TP4056 -> LiPo 3,7 V -> DC-DC boost -> 5 V ke ESP32 VIN.
TEG ditempel di dinding boiler, sisi dinginnya ke heatsink.

## VCC dan GND

- Semua modul (INA219, sensor hujan) disuplai dari pin 3V3 ESP32, bukan 5V.
- Semua GND digabung jadi satu: ESP32, INA219, sensor hujan, dan TP4056 OUT-.

## Aman untuk GPIO 3,3 V

- GPIO ESP32 hanya tahan 3,3 V, makanya semua modul diberi suplai 3V3 supaya output-nya ikut 3,3 V.
- Sensor hujan D0 jadi aman di GPIO 27 karena modulnya tidak diberi 5 V.
- 5 V cuma masuk lewat pin VIN (dari DC-DC boost), tidak ada yang masuk ke GPIO.
- INA219 tahan sampai 26 V, jadi aman walaupun tegangan TEG naik.