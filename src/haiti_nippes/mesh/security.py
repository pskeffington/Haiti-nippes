"""Public-safe security planning objects for Meshtastic operations."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class SecurityIncidentFlag(StrEnum):
    """Incident categories that may require communications review."""

    LOST_DEVICE = "lost_device"
    UNUSUAL_TRAFFIC = "unusual_traffic"
    UNAUTHORIZED_USER = "unauthorized_user"
    MISCONFIGURED_NODE = "misconfigured_node"
    KEY_ROTATION_DUE = "key_rotation_due"
    TRAINING_NEEDED = "training_needed"


@dataclass(frozen=True, slots=True)
class ChannelPolicy:
    """A public-safe description of a channel's intended use.

    This object deliberately stores policy labels only. It must not store real
    channel keys, QR codes, live channel names, or operational secrets.
    """

    policy_id: str
    purpose: str
    allowed_roles: tuple[str, ...]
    message_rules: tuple[str, ...]
    rotation_interval_days: int
    emergency_use: bool = False

    def validate(self) -> None:
        """Validate policy constraints."""
        if self.rotation_interval_days <= 0:
            raise ValueError("rotation interval must be positive")
        if not self.allowed_roles:
            raise ValueError("at least one allowed role is required")


@dataclass(frozen=True, slots=True)
class KeyRotationRecord:
    """Metadata-only record of a key-rotation event.

    Never store the key itself. Record only dates, reason labels, and public-safe
    administrative metadata.
    """

    policy_id: str
    rotated_on: str
    reason: str
    authorized_by_role: str
    next_rotation_due: str

    def validate_public_safe(self) -> None:
        """Reject accidental key material in metadata fields."""
        joined = " ".join(
            [
                self.policy_id,
                self.rotated_on,
                self.reason,
                self.authorized_by_role,
                self.next_rotation_due,
            ]
        ).lower()
        blocked_terms = ("key=", "aes", "password", "secret", "private")
        if any(term in joined for term in blocked_terms):
            raise ValueError("rotation record appears to contain sensitive material")
