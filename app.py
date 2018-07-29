from TemperatureHumidity.TemperatureHumidity import read_value

from flask import Flask
from flask import jsonify
import json
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
@app.route("/temperaturehumidity")
def temperaturehumidity():
    data1, data2 = read_value('11', 4)
    data = {"temperature": "{}".format(data1), "humidity": "{}".format(data2)}
    logging.debug(json.dumps(data))
    resp = jsonify(data)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.environ.get('DEBUG', False))
