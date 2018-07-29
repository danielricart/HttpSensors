import Adafruit_DHT
sensor_args = {
        '11': Adafruit_DHT.DHT11,
        '22': Adafruit_DHT.DHT22,
        '2302': Adafruit_DHT.AM2302
        }
def read_value(sensor, pin):
    if sensor in sensor_args:
        humidity, temperature = Adafruit_DHT.read_retry(sensor_args[sensor], pin)
    else:
        raise Exception
    return temperature, humidity
