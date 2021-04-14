"""
    Configuration variables
"""

import json
import configparser

import __root__

# Root path
root_path = __root__.path()

# Properties file
CONFIGURATION_FILE = "config/settings.conf"

# Config file parser
parser = configparser.RawConfigParser()

parser.read(CONFIGURATION_FILE)

# Service host
service_host = parser.get("SERVICE", "service_host")

# Service port number
service_port = int(parser.get("SERVICE", "service_port"))

# Resources
resources = parser.get("SERVICE", "resources")

# Log
LOG_BASE_PATH = parser.get('LOG', 'base_path')
LOG_LEVEL = parser.get('LOG', 'log_level')
FILE_NAME = LOG_BASE_PATH + parser.get('LOG', 'file_name')
LOG_HANDLERS = json.loads(parser.get('LOG', 'handlers'))

# DEPLOYMENT
deployment_environment = int(parser.get("DEPLOYMENT", "env"))

