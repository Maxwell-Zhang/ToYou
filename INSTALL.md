登陆服务器，进入自己的账户目录下
cd ~/ToYou
### 只用执行一次 ###
sudo apt-get install libmysqlclient-dev
pip install virtualenv #安装virtualenv
virtualenv venv #新建env 环境
### *********** ###

. env/bin/activate #启动env
pip install flask
pip install tornado
pip install flask-sqlalchemy
pip install flask-mysqldb
pip install flask-script
pip install redis
### 配置完成 ###
python setup_database.py 数据库建表
运行 python runserver.py 启动服务器（端口号目前设为 5001）

### 客户端测试 ###
在本机电脑浏览器输入
http://111.231.110.120:5001/User/Login?name=hhh

可以再返回页面得到服务器返回的字符串
