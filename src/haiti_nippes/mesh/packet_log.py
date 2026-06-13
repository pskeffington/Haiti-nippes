"""Packet log records for non-sensitive Meshtastic test data."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class PacketLogRecord:
    """A compact metadata-only packet log record.

    Store metadata and sanitized summaries only. Do not store patient data,
    encryption keys, precise private coordinates, or sensitive field identities.
    """

    observed_at: str
    source_node: str
    destination_node: str
    channel_label: str
    message_kind: str
    priority: str
    payload_summary: str
    hop_limit: int | None = None
    rssi: float | None = None
    snr: float | None = None

    def to_row(self) -> dict[str, Any]:
        """Return a dictionary suitable for CSV or SQLite insertion."""
        self.validate_public_safe()
        return asdict(self)

    def validate_public_safe(self) -> None:
        """Reject obvious sensitive payloads before writing logs."""
        joined = " ".join(
            [
                self.source_node,
                self.destination_node,
                self.channel_label,
                self.message_kind,
                self.priority,
                self.payload_summary,
            ]
        ).lower()
        blocked_terms = (
            "dob",
            "date of birth",
            "patient name",
            "private key",
            "channel key",
            "password",
        )
        if any(term in joined for term in blocked_terms):
            raise ValueError("packet log appears to contain sensitive content")
