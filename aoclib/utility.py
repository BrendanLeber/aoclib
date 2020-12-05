# -*- coding: utf-8 -*-

from re import findall
from typing import List, Tuple, Any, Iterable


def extract_ints(line: str) -> List[int]:
    return [int(x) for x in findall(r"-?\d+", line)]


def grouped(iterable: Iterable[Any], n: int) -> Iterable[Tuple[Any, ...]]:
    """s -> (s0, s1, s2, ..., sn-1), (sn, sn+1, sn+2, ..., s2n-1)..."""
    return zip(*[iter(iterable)] * n)


def pairwise(iterable: Iterable[Any]) -> Iterable[Tuple[Any, Any]]:
    """s -> (s0, s1), (s2, s3), (s4, s5), ..."""
    itr = iter(iterable)
    return zip(itr, itr)
