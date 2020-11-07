from lib.filters import empty_filters


class State:
    """
    A DTO encapsulating the program state.
    
    Initialized to contain no data and no filters.
    """

    def __init__(self):
        self.raw_data = None
        self.filtered_data = None

        self.filters = empty_filters()