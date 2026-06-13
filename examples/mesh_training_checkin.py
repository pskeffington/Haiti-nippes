"""Run a public-safe Meshtastic training check-in example.

This example uses MemoryTransport only. It does not connect to radio hardware,
Bluetooth, serial, TCP, or any live Meshtastic network.
"""

from __future__ import annotations

from haiti_nippes.mesh.interface import MemoryTransport, MeshInterface
from haiti_nippes.mesh.training import basic_check_in_drill


def main() -> None:
    """Render and send the first training check-in through memory transport."""
    drill = basic_check_in_drill(sender="CHW-00")
    transport = MemoryTransport()
    interface = MeshInterface(transport=transport)

    print(drill.prompt())
    sent_text = interface.send_field_message(drill.expected_message)
    print(sent_text)


if __name__ == "__main__":
    main()
