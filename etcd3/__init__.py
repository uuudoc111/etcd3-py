# -*- coding: utf-8 -*-
# flake8: noqa
"""Top-level package for etcd3-py."""
import six

from .version import __version__, __author__, __email__

__all__ = ['__version__', '__author__', '__email__']

from .client import Client

AioClient = None
if six.PY3:  # pragma: no cover
    from .aio_client import AioClient

__all__.extend([
    'Client',
    'AioClient'
])

from .stateful import Txn
from .stateful import Watcher
from .stateful import Lease
from .stateful import Lock

from .stateful.watch import EventType

__all__.extend([
    'Txn',
    'Watcher',
    'Lease',
    'Lock',
    'EventType'
])
