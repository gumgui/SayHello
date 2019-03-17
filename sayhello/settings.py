import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
# 设置数据库路径
dev_db = 'sqlite:///'+ os.path.join(basedir,'data.db')
# 设置密钥
SECRET_KEY = os.getenv('SECTRRT_KEY','secret string')
# 初始化数据库
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',dev_db)
# 使用本地bootstrap文件
BOOTSTRAP_SERVE_LOCAL = True
# flask-debugtoolbar 是否拦截重定向
DEBUG_TB_INTERCEPT_REDIRECTS = False