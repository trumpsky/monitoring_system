# backend

> powererd by flask

## 0. 运行环境配置

1. 创建并运行虚拟环境

   ```shell
   cd backend
   virtualenv flask_env
   .\flask_env\Scripts\activate
   deactivate
   ```
2. 需要安装以下依赖

   ```python
   flask==2.2.3
   flask-script==2.0.6
   pymysql==1.0.3
   dbutils==1.3
   flask-sqlalchemy==3.0.3
   ```

   > pip install -r requirements.txt（后续添加依赖需手动写入 requirements 文件）
   >
3. 在config文件夹下创建与settings.py同级的localsettings.py文件，文件应包括数据库的配置，以下为范例

   ```python
   DB_HOST = "127.0.0.1"
   DB_USER = "oliver"
   DB_PWD = "123"
   DB_NAME = "db"
   DIALECT = 'mysql'
   DRIVER = 'pymysql'
   DB_PORT = 3306
   SECRET_KEY = "azaaaafg"
   ```

## 1. 运行步骤

1. 进入backend目录
   > cd backend
   >
2. 运行项目
   > python app.py
   >

## 2. 全局配置

1. 跨域配置
   - 暂无
2. csrf验证配置
   - 暂无
3. 数据库使用统一云数据库，详细配置请询问项目开发人员

## 5. 项目规范

1. 新建blueprint
   - 进入backend/backend/views目录
   - 参照data_show.py新建文件
   - 在model.py中新建数据表
   - 在app.py中注册蓝图实例
2. 新建接口
   - 进入新建蓝图
   - 添加接口及路由
     ```python
     @ds.route("/login", strict_slashes=False)
     def login():
         user_list = []
         users = User.query.all()
         for user in users:
             user_list.append(user.to_json())

         return jsonify(user_list=user_list)
     ```
3. 数据库操作
   - 在module_name目录下的models.py中添加数据库模型
     ```python
     class User(db.Model):
         __tablename__ = 'test_table'
         id = db.Column(db.Integer, primary_key=True)
         name = db.Column(db.String(100))
         age = db.Column(db.Integer)
     ```
