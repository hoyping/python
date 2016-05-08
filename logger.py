#######################################
#File Name: logger.py
#Created Time: 2016-03-17 00:11:56
#######################################
#!/usr/bin/env python
import os
import logging
from logging import config
LOG_CONF = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_CONF)
logger = logging.getLogger('root')


if __name__ == '__main__':
    logger.info("haha")
    logger.error("How?")

