"""CSV utilities for metadata-only Meshtastic packet logs."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from .packet_log import PacketLogRecord


PACKET_LOG_FIELDS = [
    "observed_at",
    "source_node",
    "destination_node",
    "channel_label",
    "message_kind",
    "priority",
    "payload_summary",
    "hop_limit",
    "rssi",
    "snr",
]


def write_packet_log_csv(path: str | Path, records: Iterable[PacketLogRecord]) -> None:
    """Write metadata-only packet records to CSV.

    Every record is validated before writing. The caller is responsible for
    keeping the destination path out of public commits if field data becomes
    sensitive.
    """
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=PACKET_LOG_FIELDS)
        writer.writeheader()
        for record in records:
            writer.writerow(record.to_row())
