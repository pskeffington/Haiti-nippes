"""Training helpers for Meshtastic healthcare communications."""

from __future__ import annotations

from dataclasses import dataclass

from .message import FieldMessage, MessageKind, MessagePriority


@dataclass(frozen=True, slots=True)
class TrainingDrill:
    """A short training-channel exercise for new users."""

    drill_id: str
    title: str
    objective: str
    expected_message: FieldMessage

    def prompt(self) -> str:
        """Return a concise trainer prompt."""
        return f"{self.drill_id}: {self.title} - {self.objective}"


def basic_check_in_drill(sender: str = "CHW-00") -> TrainingDrill:
    """Create the first standard non-sensitive check-in drill."""
    message = FieldMessage(
        sender=sender,
        location_label="training-site",
        kind=MessageKind.TRAINING,
        priority=MessagePriority.ROUTINE,
        summary="test check-in no patient data",
        request="confirm receipt",
    )
    return TrainingDrill(
        drill_id="TRN-001",
        title="Basic training-channel check-in",
        objective="User connects phone to node, sends a test message, and receives confirmation.",
        expected_message=message,
    )
