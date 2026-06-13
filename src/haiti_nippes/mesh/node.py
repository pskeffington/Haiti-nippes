"""Node identity and role objects for Nippes mesh planning."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class NodeRole(StrEnum):
    """Planned operational roles for Meshtastic devices."""

    FIELD_WORKER = "field_worker"
    CLINIC_FIXED = "clinic_fixed"
    RELAY = "relay"
    GATEWAY = "gateway"
    TRAINING = "training"
    TEST = "test"


@dataclass(frozen=True, slots=True)
class MeshNode:
    """A public-safe node planning record.

    Do not store exact coordinates, live cryptographic material, private channel
    names, or healthcare-worker identities in this public repository.
    """

    node_id: str
    label: str
    role: NodeRole
    commune: str = ""
    site_label: str = ""
    hardware_model: str = ""
    firmware_version: str = ""

    def display_name(self) -> str:
        """Return a compact display name for logs and training tables."""
        role = self.role.value.replace("_", "-")
        return f"{self.node_id} {role} {self.label}".strip()

    def validate_public_safe(self) -> None:
        """Reject fields that appear to contain sensitive live deployment data."""
        joined = " ".join(
            [
                self.node_id,
                self.label,
                self.commune,
                self.site_label,
                self.hardware_model,
                self.firmware_version,
            ]
        ).lower()
        blocked_terms = ("private key", "channel key", "exact gps", "home address")
        if any(term in joined for term in blocked_terms):
            raise ValueError("node record appears to contain sensitive deployment data")
