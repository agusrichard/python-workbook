# import logging
# import traceback

# # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# # import helper
# try:
#     a = [1, 2, 3]
#     val = a[5]
# except IndexError as e:
#     # logging.error(e, exc_info=True)
#     logging.error("The error is %s", traceback.format_exc())


import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

handler = TimedRotatingFileHandler('app.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
