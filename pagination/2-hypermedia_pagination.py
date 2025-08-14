#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """
    function named index_range that takes two integer
    arguments page and page_size
    """
    start: int = (page - 1) * page_size
    end: int = page_size * page
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Implement a method named get_page that takes two integer
        arguments page with default value 1 and page_size with
        default value 10
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        returns a dictionary
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages}