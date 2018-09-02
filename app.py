from TemperatureHumidity.TemperatureHumidity import read_value
from HumidexTemperature.HumidexTemperature import dewpoint, humidex
from flask_caching import Cache
from datetime import datetime
from flask import Flask
from flask import jsonify
import json
import logging
import os

cache_time = int(os.getenv('CACHE_TIME', 300))
datetime_format = '%d/%m/%Y %H:%M:%S'
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


@app.route("/temperaturehumidity")
@cache.cached(timeout=cache_time)
def temperaturehumidity():
    data = read_temperature()
    addTimestamp(data)
    addId(data)
    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route("/humidex")
@cache.cached(timeout=cache_time)
def humidextemperature():
    source_data = read_temperature()
    humidx = humidex(float(source_data['temperature']), float(source_data['humidity']))
    data = {"temperature": humidx, "type": "humidex"}
    addTimestamp(data)
    addId(data)
    logging.debug(data)
    resp = jsonify(data)
    resp.status_code = 200
    return resp


@app.route("/dewpoint")
@cache.cached(timeout=cache_time)
def dewpointtemperature():
    source_data = read_temperature()
    dewpt = dewpoint(float(source_data['temperature']), float(source_data['humidity']))
    data = {"temperature": dewpt, "type": "dewpoint"}
    addTimestamp(data)
    addId(data)
    logging.debug(data)
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route("/")
@cache.cached(timeout=cache_time)
def root():
    source_data = read_temperature()
    dewpt = dewpoint(float(source_data['temperature']), float(source_data['humidity']))
    humidx = humidex(float(source_data['temperature']), float(source_data['humidity']))
    data = source_data
    data['humidex'] = humidx
    data['dewpoint'] = dewpt
    addTimestamp(data)
    addId(data)
    logging.debug(data)
    resp = jsonify(data)
    resp.status_code = 200
    return resp
    


def read_temperature():
    logging.debug("read temperature from sensor")
    data1, data2 = read_value('11', 4)
    data = {"temperature": "{}".format(data1), "humidity": "{}".format(data2)}
    logging.debug(json.dumps(data))
    return data

def addTimestamp(data):
    data['timestamp'] = datetime.strftime(datetime.now(), datetime_format)
    pass


def addId(data):
    data['id'] = str(datetime.now().timestamp()).replace(".","_")
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG', False))
