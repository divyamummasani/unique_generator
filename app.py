from flask_cors import CORS
import traceback
from flask import Flask
# from flask import g
from common import AppConfigurations
from scripts.services import blueprint

app = Flask(__name__)


app.register_blueprint(blueprint)


CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

# CORS(app, origins="*", allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
# supports_credentials=True, intercept_exceptions=False)
@app.route('/healthcheck')
def healthcheck():
    return 'success'


service_port = AppConfigurations.service_port
service_host = AppConfigurations.service_host

if __name__ == '__main__':
    try:
        print(('Starting service @ port ' + str(service_port)))
        app.run(host=str(service_host), port=int(service_port), debug=True, threaded=True, use_reloader=False)
    except:
        traceback.print_exc()

