from flask import Flask
from extension import db, cors
from config import settings
from backend.views.data_show import ds
from backend.views.frontend_get import fg
from backend.views.comparison import cp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(ds, url_prefix='/dataShow')
app.register_blueprint(fg, url_prefix='/dataGet')
app.register_blueprint(cp, url_prefix='/comparison')

app.config.from_object(settings)
db.init_app(app)
cors.init_app(app)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
