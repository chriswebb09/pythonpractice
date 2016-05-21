from abc import ABCMeta
class BaseQuery(object):
    __metaclass__ = ABCMeta
    def __init__(self, search_term):
        self.search_term = search_term

    def get_results(self):
        raise Exception('Not implemented')

