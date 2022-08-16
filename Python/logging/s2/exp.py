import logging.config

logging.config.fileConfig(fname='log.conf')
logger = logging.getLogger('root')

for _ in range(100000):
    logger.info('This is an information message')
    logger.error('This is an information message')
    logger.warning('This is an information message')
