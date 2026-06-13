"""Interface boundary for Meshtastic-compatible transports."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .message import FieldMessage


class MeshTransport(Protocol):
    """Protocol for transport adapters."""

    def send_text(self, text: str) -> None:
        """Send a text payload through a Meshtastic-compatible transport."""


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
