"""Optional Meshtastic Python transport adapter.

This adapter imports the official Meshtastic Python package only at runtime so
base tests do not require the dependency or live hardware.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class MeshtasticDependencyError(RuntimeError):
    """Raised when the optional Meshtastic Python package is unavailable."""


@dataclass(slots=True)
class MeshtasticPythonTransport:
    """Send text through an already-open Meshtastic interface object.

    A future factory can create serial, TCP, or BLE interfaces. This class keeps
    the first implementation narrow: it accepts an injected interface object with
    a `sendText` method, matching the public Meshtastic Python API convention.
    """

    interface: Any
    destination_id: str | None = None
    channel_index: int | None = None

    @staticmethod
    def ensure_dependency() -> None:
        """Verify that the optional Meshtastic package can be imported."""
        try:
            import meshtastic  # noqa: F401
        except ImportError as exc:
            raise MeshtasticDependencyError(
                "Install the optional mesh dependency before using live Meshtastic transports."
            ) from exc

    def send_text(self, text: str) -> None:
        """Send text through the injected Meshtastic interface."""
        if not hasattr(self.interface, "sendText"):
            raise TypeError("interface must provide a sendText method")
        kwargs: dict[str, Any] = {}
        if self.destination_id:
            kwargs["destinationId"] = self.destination_id
        if self.channel_index is not None:
            if self.channel_index < 0:
                raise ValueError("channel_index must be non-negative")
            kwargs["channelIndex"] = self.channel_index
        self.interface.sendText(text, **kwargs)
