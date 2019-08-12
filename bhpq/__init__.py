"""BHPQ - Binary Heap Priority Queue

    >>> from bhpq import BinaryHeapPriorityQueue

See https://github.com/aayushuppal/bhpq for more information
"""

from pathlib import Path
from typing import Dict

from .bhpq import BinaryHeapPriorityQueue

_p = Path(__file__)
_vf = (_p / ".." / "_version.py").resolve()

_version_info: Dict[str, str] = {}
with open(_vf) as fid:
    exec(fid.read(), _version_info)


# Version of bhpq package
__version__ = _version_info["__version__"]
