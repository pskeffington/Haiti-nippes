"""Structured field-message objects for Meshtastic healthcare operations."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Final


MAX_TEXT_LENGTH: Final[int] = 220


class MessagePriority(StrEnum):
    """Operational priority levels for short mesh messages."""

    ROUTINE = "routine"
    PRIORITY = "priority"
    URGENT = "urgent"
    EMERGENCY = "emergency"


class MessageKind(StrEnum):
    """High-level message categories for the Nippes communications model."""

    CHECK_IN = "check_in"
    CLINIC_STATUS = "clinic_status"
    LOGISTICS = "logistics"
    REFERRAL = "referral"
    SECURITY = "security"
    TRAINING = "training"
    WEATHER = "weather"
    WASH = "wash"


@dataclass(frozen=True, slots=True)
class FieldMessage:
    """A short, non-sensitive operational message.

    The object is designed for healthcare coordination without patient-level
    identifiers. It should be used to format short text payloads for training,
    field check-ins, clinic status, supply requests, and emergency coordination.
    """

    sender: str
    location_label: str
    kind: MessageKind
    priority: MessagePriority
    summary: str
    request: str = ""
    timestamp_label: str = ""

    def to_text(self) -> str:
        """Render the message as a compact field-safe text payload."""
        parts = [
            self.priority.value.upper(),
            self.kind.value.upper(),
            self.sender.strip(),
            self.location_label.strip(),
            self.summary.strip(),
        ]
        if self.request.strip():
            parts.append(f"REQ {self.request.strip()}")
        if self.timestamp_label.strip():
            parts.append(self.timestamp_label.strip())
        text = " / ".join(part for part in parts if part)
        if len(text) > MAX_TEXT_LENGTH:
            raise ValueError(
                f"message exceeds {MAX_TEXT_LENGTH} characters; shorten payload"
            )
        return text

    def validate_public_safe(self) -> None:
        """Reject obvious patient-identifying patterns before test use."""
        text = self.to_text().lower()
        blocked_terms = ("dob", "date of birth", "patient name", "ssn")
        if any(term in text for term in blocked_terms):
            raise ValueError("message appears to contain patient-identifying content")
