#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, TypedDict


class HyperIndexDict(TypedDict):
    index: int
    next_index: int
    page_size: int
    data: List[List[str]]


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(
                    len(dataset),
                )
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int | None = None,
        page_size: int = 10,
    ) -> HyperIndexDict:
        dataset_len = len(self.dataset())

        assert isinstance(index, int)
        assert index >= 0 and index < dataset_len

        return {"index": -1, "next_index": -1, "page_size": -1, "data": []}
