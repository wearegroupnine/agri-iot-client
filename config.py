from configparser import ConfigParser
#from lib.logger_opt import *

config_file = './config.ini'
config = ConfigParser()
config.read(config_file)

version = ''

path_save_raw_dir = ''
path_save_ai_dir = ''

api_camera_service = None 
api_ai_service_obj = None 

def get_version():
    return version

def check_config_section():
    if not config.has_section('common'):
        config.add_section('common')

    if not config.has_section('path'):
        config.add_section('path')

    if not config.has_section('api'):
        config.add_section('api')

    config.write(open(config_file, 'w'))

def get_config():
    global version, path_save_raw_dir, path_save_ai_dir, api_camera_service, api_ai_service_obj
    try:
        version = config.get('common', 'version')
    except Exception as e:
        logger.warning(e)
        version = ''

    try:
        path_save_raw_dir = config.get('path', 'save_raw_dir')
    except Exception as e:
        logger.warning(e)
        path_save_raw_dir = ''

    try:
        path_save_ai_dir = config.get('path', 'save_ai_dir')
    except Exception as e:
        logger.warning(e)
        path_save_ai_dir = ''

    try:
        api_camera_service = config.get('api', 'camera_service')
    except Exception as e:
        logger.warning(e)
        api_camera_service = ''

    try:
        api_ai_service_obj= config.get('api', 'ai_service_obj')
    except Exception as e:
        logger.warning(e)
        api_ai_service_obj = ''

def reload_config():
    check_config_section()
    get_config()

if __name__ == '__main__':
    reload_config()
