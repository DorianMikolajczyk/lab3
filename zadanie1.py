import logging

def show_logs(level, format):
    logging.basicConfig(level=level, format=format)
    logging.debug('Pokazuje logi na poziomie DEBUG')
    logging.info('Pokazuje logi na poziomie INFO')
    logging.warning('Pokazuje logi na poziomie WARNING')
    logging.error('Pokazuje logi na poziomie ERROR')
    logging.critical('Pokazuje logi na poziomie CRITICAL')


show_logs(logging.DEBUG, '%(levelname)s: %(message)s')
