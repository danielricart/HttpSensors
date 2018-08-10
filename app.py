from TemperatureHumidity.TemperatureHumidity import read_value
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
    resp = {}
    data = read_temperature()
    addTimestamp(data)
    resp = jsonify(data)
    resp.status_code = 200
    #    data.pop('timestamp')
    return resp

def read_temperature():
    data1, data2 = read_value('11', 4)
    data = {"temperature": "{}".format(data1), "humidity": "{}".format(data2)}
    logging.debug(json.dumps(data))
    return data

def addTimestamp(data):
    data['timestamp'] = datetime.strftime(datetime.now(), datetime_format)
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG', False))
