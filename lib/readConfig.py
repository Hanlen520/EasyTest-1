# coding:utf-8import osimport configparserimport logginglog = logging.getLogger('log')# 配置文件路径# configPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\lib' + '\\config' + '\\cfg.ini'configPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/lib' + '/config' + '/cfg.ini'conf = configparser.ConfigParser()conf.read(configPath, encoding='utf-8')MySQL_host = conf.get('MySQL', 'MySQL_host')MySQL_user = conf.get('MySQL', 'MySQL_user')MySQL_pwd = conf.get('MySQL', 'MySQL_pwd')MySQL_database = conf.get('MySQL', 'MySQL_database')MySQL_port = conf.get('MySQL', 'MySQL_port')MySQL_host_job = conf.get('MySQL', 'MySQL_host_job')MySQL_user_job = conf.get('MySQL', 'MySQL_user_job')MySQL_pwd_job = conf.get('MySQL', 'MySQL_pwd_job')MySQL_database_job = conf.get('MySQL', 'MySQL_database_job')MySQL_port_job = conf.get('MySQL', 'MySQL_port_job')