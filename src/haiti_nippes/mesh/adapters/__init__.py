"""Transport adapters for Meshtastic-facing code.

Adapters isolate live hardware or CLI behavior from public-safe message objects
and tests. The default test path should keep using MemoryTransport.
"""

from .memory import MemoryTransport
from .meshtastic_cli import MeshtasticCliTransport
from .meshtastic_python import MeshtasticPythonTransport, MeshtasticDependencyError

__all__ = [
    "MemoryTransport",
    "MeshtasticCliTransport",
    "MeshtasticDependencyError",
    "MeshtasticPythonTransport",
]
