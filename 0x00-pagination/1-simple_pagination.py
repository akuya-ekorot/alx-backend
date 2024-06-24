#!/usr/bin/env python3

"""Server class"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Returns the appropriate page"""

        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start, end = self.index_range(page, page_size)

        return self.dataset()[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Returns a tuple of size two containing the start and end index_range
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters
        """

        end_index = page_size * page
        start_index = end_index - page_size

        return start_index, end_index
