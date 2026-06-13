"""Interface stubs for future Meshtastic device integration.

The real Meshtastic Python dependency is intentionally not imported here yet so
this repository can remain lightweight while the programming matrix matures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from .message import FieldMessage


class MeshTransport(Protocol):
    """Protocol for transport adapters implemented later."""

    def send_text(self, text: str) -> None:
        """Send a text payload through a Meshtastic-compatible transport."""


@dataclass(slots=True)
class MemoryTransport:
    """A test transport that records messages in memory."""

    sent_messages: list[str] = field(default_factory=list)

    def send_text(self, text: str) -> None:
        """Record a message without touching radio hardware."""
        self.sent_messages.append(text)


@dataclass(slots=True)
class MeshInterface:
    """Small wrapper around a Meshtastic-compatible transport."""

    transport: MeshTransport

    def send_field_message(self, message: FieldMessage) -> str:
        """Validate, render, and send a structured field message."""
        message.validate_public_safe()
        text = message.to_text()
        self.transport.send_text(text)
        return text
