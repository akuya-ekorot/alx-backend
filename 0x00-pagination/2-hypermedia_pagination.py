#!/usr/bin/env python3

"""Server class"""

import csv
import math
from typing import List, Tuple, TypedDict


class HyperDict(TypedDict):
    page_size: int
    page: int
    data: List[List[str]]
    next_page: int | None
    prev_page: int | None
    total_pages: int


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> HyperDict:

        dataset_len = 0 if self.dataset() is None else len(self.dataset())
        total_pages = (
            math.floor(dataset_len / page_size)
            if dataset_len % page_size == 0
            else math.floor(dataset_len / page_size) + 1
        )

        data = self.get_page(page, page_size)
        page_size_result = len(data)

        return {
            "page_size": page_size_result,
            "page": page,
            "data": data,
            "next_page": None if page >= total_pages else page + 1,
            "prev_page": None if page <= 1 else page - 1,
            "total_pages": total_pages,
        }
