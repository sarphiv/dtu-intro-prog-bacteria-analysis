from lib.filters import empty_filters


class State:
    def __init__(self):
        self.raw_data = None
        self.filtered_data = None

        self.filters = empty_filters()