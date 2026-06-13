"""Create a synthetic metadata-only Meshtastic packet log CSV.

This demo writes public-safe synthetic records only. It does not connect to live
Meshtastic hardware and does not store patient data, keys, private channel names,
or exact field coordinates.
"""

from __future__ import annotations

from pathlib import Path

from haiti_nippes.mesh import PacketLogRecord, write_packet_log_csv


DEFAULT_OUTPUT = Path("outputs/mesh_packet_log_demo.csv")


def build_demo_records() -> list[PacketLogRecord]:
    """Build synthetic packet observations for documentation and tests."""
    return [
        PacketLogRecord(
            observed_at="2026-06-13T14:00:00Z",
            source_node="NIP-TRAIN-001",
            destination_node="NIP-TRAIN-002",
            channel_label="training",
            message_kind="training",
            priority="routine",
            payload_summary="synthetic training check-in",
            hop_limit=3,
            rssi=-78.0,
            snr=8.25,
        ),
        PacketLogRecord(
            observed_at="2026-06-13T14:05:00Z",
            source_node="NIP-TRAIN-002",
            destination_node="NIP-TRAIN-001",
            channel_label="training",
            message_kind="training",
            priority="routine",
            payload_summary="synthetic receipt confirmation",
            hop_limit=3,
            rssi=-81.5,
            snr=6.75,
        ),
    ]


def main() -> None:
    """Write the synthetic packet log demo CSV."""
    records = build_demo_records()
    write_packet_log_csv(DEFAULT_OUTPUT, records)
    print(f"Wrote synthetic packet log: {DEFAULT_OUTPUT}")


if __name__ == "__main__":
    main()
