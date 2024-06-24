#!/usr/bin/env python3

"""
    Simple helper function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing the start and end index_range
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters
    """

    end_index = page_size * page
    start_index = end_index - page_size

    return start_index, end_index
