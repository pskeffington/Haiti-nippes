"""Device inventory records for public-safe mesh planning."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class DeviceStatus(StrEnum):
    """Lifecycle state for planned or issued devices."""

    PLANNED = "planned"
    CONFIGURED = "configured"
    ISSUED = "issued"
    IN_SERVICE = "in_service"
    MAINTENANCE = "maintenance"
    LOST = "lost"
    RETIRED = "retired"


@dataclass(frozen=True, slots=True)
class DeviceInventoryRecord:
    """A non-sensitive device custody and readiness record."""

    asset_id: str
    node_id: str
    status: DeviceStatus
    hardware_model: str = ""
    firmware_version: str = ""
    assigned_role: str = ""
    assigned_site_label: str = ""
    last_check_label: str = ""
    notes: str = ""

    def needs_attention(self) -> bool:
        """Return True when the record should be reviewed by a maintainer."""
        return self.status in {
            DeviceStatus.MAINTENANCE,
            DeviceStatus.LOST,
            DeviceStatus.RETIRED,
        }

    def validate_public_safe(self) -> None:
        """Reject obvious sensitive values in public inventory records."""
        joined = " ".join(
            [
                self.asset_id,
                self.node_id,
                self.hardware_model,
                self.firmware_version,
                self.assigned_role,
                self.assigned_site_label,
                self.last_check_label,
                self.notes,
            ]
        ).lower()
        blocked_terms = ("patient", "private key", "channel key", "password")
        if any(term in joined for term in blocked_terms):
            raise ValueError("inventory record appears to contain sensitive content")
