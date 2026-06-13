"""Guarded Meshtastic CLI transport.

This adapter is intentionally conservative. It can be wired to the installed
`meshtastic` CLI later, but callers must opt in to execution. Tests should not
require the CLI or radio hardware.
"""

from __future__ import annotations

from dataclasses import dataclass
import shutil
import subprocess


@dataclass(frozen=True, slots=True)
class MeshtasticCliTransport:
    """Send text through the Meshtastic CLI when explicitly enabled."""

    executable: str = "meshtastic"
    destination: str | None = None
    channel_index: int | None = None
    dry_run: bool = True

    def build_command(self, text: str) -> list[str]:
        """Build a conservative CLI command without executing it."""
        command = [self.executable, "--sendtext", text]
        if self.destination:
            command.extend(["--dest", self.destination])
        if self.channel_index is not None:
            if self.channel_index < 0:
                raise ValueError("channel_index must be non-negative")
            command.extend(["--ch-index", str(self.channel_index)])
        return command

    def send_text(self, text: str) -> None:
        """Send text through the CLI, or validate command shape in dry-run mode."""
        command = self.build_command(text)
        if self.dry_run:
            return
        if shutil.which(self.executable) is None:
            raise RuntimeError(f"Meshtastic CLI executable not found: {self.executable}")
        subprocess.run(command, check=True)
