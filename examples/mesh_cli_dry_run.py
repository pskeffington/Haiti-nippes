"""Build a Meshtastic CLI command without sending live traffic.

This example is intentionally dry-run only. It validates command construction for
future field testing without touching a radio, Bluetooth, serial, TCP, or a live
Meshtastic network.
"""

from __future__ import annotations

from haiti_nippes.mesh import FieldMessage, MeshInterface, MessageKind, MessagePriority
from haiti_nippes.mesh.adapters import MeshtasticCliTransport


def main() -> None:
    """Render a synthetic training message and show the dry-run CLI command."""
    message = FieldMessage(
        sender="CHW-00",
        location_label="training-site",
        kind=MessageKind.TRAINING,
        priority=MessagePriority.ROUTINE,
        summary="cli dry-run no patient data",
        request="confirm receipt",
    )
    transport = MeshtasticCliTransport(
        destination="!ffffffff",
        channel_index=0,
        dry_run=True,
    )
    interface = MeshInterface(transport=transport)

    sent_text = interface.send_field_message(message)
    command = transport.build_command(sent_text)

    print("Dry-run only. No message was transmitted.")
    print(" ".join(command))


if __name__ == "__main__":
    main()
