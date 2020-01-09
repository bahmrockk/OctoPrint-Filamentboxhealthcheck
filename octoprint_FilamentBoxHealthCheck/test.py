# coding=utf-8

import time
import bme280
import smbus2

bus = smbus2.SMBus(1)
address = 0x76
data = bme280.sample(bus, address, bme280.load_calibration_params(bus, address))
print(data)


message = dict(
    humidity=data.humidity,
    temperature=data.temperature,
    pressure=data.pressure 
    )

print("SENSOR DATA\n")
print("Humidity: ", message["humidity"])
print("Humidity: " , data.humidity)
