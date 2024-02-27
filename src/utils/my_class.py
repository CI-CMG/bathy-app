import logging


class MyClass:
    var1 = 'STATIC'
    logger = logging.getLogger(__name__)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    def __init__(self, value):
        self.var2 = value

    def testme(self):
        self.logger.warning(self.var2)
        self.logger.warning(self.var1)
