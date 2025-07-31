import logging
from logging.handlers import RotatingFileHandler

class FlaskLogger:
    def __init__(self, app=None, log_file='app.log', max_bytes=1000000, backup_count=3):
        self.logger = logging.getLogger('flask_app_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.logger.handlers = self.logger.handlers
        app.logger.setLevel(self.logger.level)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)