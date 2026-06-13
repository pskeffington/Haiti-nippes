"""In-memory Meshtastic transport for tests and examples."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class MemoryTransport:
    """A test transport that records messages without touching radio hardware."""

    sent_messages: list[str] = field(default_factory=list)

    def send_text(self, text: str) -> None:
        """Record a message without touching radio hardware."""
        self.sent_messages.append(text)
