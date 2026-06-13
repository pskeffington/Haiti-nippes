# Meshtastic hardware proof-of-concept plan

Maintainer: Paul Skeffington, MS, MPH  
Project: Haiti Nippes rural and remote healthcare communications  
Last updated: 2026-06-13

## Purpose

This document defines the first safe path from memory-only testing toward a live Meshtastic hardware proof of concept. The goal is to validate programming interfaces, message formatting, and basic operational workflow before any rural healthcare deployment planning depends on live radio behavior.

The repository is currently public. This plan must remain generic and non-sensitive. Do not commit live encryption keys, exact field coordinates, private channel names, patient data, healthcare-worker identities, operational schedules, or access credentials.

## Proof-of-concept phases

### Phase 0: Memory-only validation

Status: active.

Purpose: confirm that message objects, safety checks, training drills, packet metadata objects, and adapter boundaries work without hardware.

Commands:

```bash
python -m pytest tests/test_mesh_objects.py
python examples/mesh_training_checkin.py
```

Expected synthetic payload:

```text
ROUTINE / TRAINING / CHW-00 / training-site / test check-in no patient data / REQ confirm receipt
```

### Phase 1: CLI dry-run validation

Status: active.

Purpose: confirm that the repository can build a Meshtastic CLI command without executing it.

Command:

```bash
python examples/mesh_cli_dry_run.py
```

Expected behavior: the script prints a command shape and explicitly states that no message was transmitted.

### Phase 1A: Packet-log dry-run validation

Status: active.

Purpose: confirm that the repository can generate a metadata-only packet-log CSV from synthetic observations.

Command:

```bash
python examples/mesh_packet_log_demo.py
```

Expected behavior: the script writes `outputs/mesh_packet_log_demo.csv` with synthetic packet metadata only. Review `docs/mesh_packet_log_schema.md` before using this format for bench or field data.

### Phase 2: Local single-device CLI validation

Status: planned.

Purpose: validate that the installed Meshtastic CLI can detect one local device and send one synthetic training message on a controlled training channel.

Requirements:

- One local Meshtastic device.
- Meshtastic CLI installed in the active Python environment.
- Device connected by USB, Bluetooth, or another supported local method.
- Training-only channel configuration.
- No patient data, real deployment data, live operational keys, or private field identifiers.

Synthetic message only:

```text
ROUTINE / TRAINING / CHW-00 / training-site / cli hardware test no patient data / REQ confirm receipt
```

### Phase 3: Two-node bench test

Status: planned.

Purpose: validate message send, receive acknowledgement, and metadata-only observation between two nearby devices before any range testing.

Minimum success criteria:

- Device A sends synthetic training message.
- Device B receives the message.
- Operator records timestamp, source label, destination label, channel label, RSSI/SNR if available, and short sanitized payload summary.
- Packet observations follow `docs/mesh_packet_log_schema.md`.
- No live patient or deployment-sensitive information is transmitted.

### Phase 4: Local range and obstruction test

Status: planned.

Purpose: characterize message reliability under short local range, building obstruction, and antenna placement changes before considering field geography.

Minimum success criteria:

- Test route is documented generically.
- No exact private coordinates are committed.
- Packet metadata is recorded without sensitive payload content.
- Any observed dead zones are described at a non-sensitive planning level.

### Phase 5: Nippes planning translation

Status: planned.

Purpose: convert bench and local range lessons into a Nippes-specific deployment model for clinic nodes, relay nodes, field-worker devices, and training procedures.

Outputs:

- Candidate node-role table.
- Training-channel procedure.
- Device custody checklist.
- Metadata-only packet log template.
- Public-safe coverage assumptions.
- Private operational annex if the repository is made private.

## Field safety rules

1. Use synthetic messages until a formal data-protection policy exists.
2. Keep the training channel separate from operational channels.
3. Do not use real patient names, full birth dates, home addresses, or clinical histories.
4. Do not commit live keys, QR codes, channel files, private channel names, or device secrets.
5. Do not commit exact coordinates for clinics, relays, residences, storage sites, or healthcare workers in a public repository.
6. Keep live hardware interaction behind adapters.
7. Keep tests runnable without hardware.
8. Treat Meshtastic as operational communications support, not a clinical record system.

## MacBook terminal setup

```bash
git clone https://github.com/pskeffington/Haiti-nippes.git
cd Haiti-nippes
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[test]"
python -m pytest tests/test_mesh_objects.py
python examples/mesh_training_checkin.py
python examples/mesh_cli_dry_run.py
python examples/mesh_packet_log_demo.py
```

For live Meshtastic Python work later:

```bash
python -m pip install -e ".[mesh,test]"
```

## Next programming step

Add a bench-test checklist and a CSV review checklist so generated packet logs can be inspected before any artifact is committed.
