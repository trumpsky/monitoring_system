from flask import Flask
from extension import db
from config import settings
from backend.views.data_show import *

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(ds, url_prefix = '/dataShow' )

app.config.from_object(settings)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
