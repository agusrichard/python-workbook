import logging

logger = logging.getLogger(__name__)
# logger.propagate = False
# logger.info('Hello from helper')

# Create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./file.log')

# level and the format
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug('Sekardayu Hana Pradiani')
logger.error('Saskia Nurul Azhima')