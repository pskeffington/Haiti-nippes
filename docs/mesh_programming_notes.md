# Mesh programming notes

Maintainer: Paul Skeffington, MS, MPH  
Project: Haiti Nippes rural and remote healthcare communications  
Last updated: 2026-06-13

## Purpose

This note defines the first programming path for Meshtastic-related work in the Haiti Nippes repository. The repository is currently public, so all implementation work must remain limited to public-safe scaffolding, generalized examples, and non-sensitive test data.

Do not commit live encryption keys, private channel names, exact field coordinates, real healthcare-worker identities, patient information, private messages, deployment schedules, or access credentials.

## Current object layer

The first mesh object layer lives under:

```text
src/haiti_nippes/mesh/
```

Current objects:

- `FieldMessage`: compact operational text message object.
- `MessageKind`: check-in, clinic-status, logistics, referral, security, training, weather, and WASH categories.
- `MessagePriority`: routine, priority, urgent, and emergency levels.
- `MeshNode`: public-safe node planning record.
- `NodeRole`: field-worker, clinic-fixed, relay, gateway, training, and test roles.
- `DeviceInventoryRecord`: device custody and readiness record.
- `DeviceStatus`: planned, configured, issued, in-service, maintenance, lost, and retired states.
- `PacketLogRecord`: metadata-only packet log object.
- `ChannelPolicy`: public-safe channel-use policy object.
- `KeyRotationRecord`: metadata-only key-rotation record. Never stores key material.
- `TrainingDrill`: short training-channel exercise object.
- `MeshInterface`: adapter boundary for future Meshtastic transports.
- `MemoryTransport`: local test transport that records sent messages in memory.

## Test command

After installing the package in editable mode with test tooling, run:

```bash
python -m pytest tests/test_mesh_objects.py
```

## Example command

Run the first safe training check-in example with:

```bash
python examples/mesh_training_checkin.py
```

Expected message:

```text
ROUTINE / TRAINING / CHW-00 / training-site / test check-in no patient data / REQ confirm receipt
```

## Next implementation layer

The next pass should add a real Meshtastic adapter while preserving the existing interface boundary.

Recommended path:

```text
src/haiti_nippes/mesh/adapters/
├── __init__.py
├── memory.py
├── meshtastic_cli.py
└── meshtastic_python.py
```

The `memory.py` adapter should move the existing `MemoryTransport` into an adapters namespace. The `meshtastic_cli.py` adapter should shell out to the installed `meshtastic` CLI only after command structure and safety checks are stable. The `meshtastic_python.py` adapter should import the official Meshtastic Python library only when that optional dependency is installed.

## Programming rules

1. Keep transport logic separate from message objects.
2. Keep live hardware interaction behind adapters.
3. Keep tests runnable without radio hardware.
4. Keep packet logs metadata-only unless the repository is made private and a formal data-protection rule is added.
5. Keep patient-facing traffic coded, minimized, and operational.
6. Treat Meshtastic as a communications layer, not a clinical record system.
7. Keep all field examples synthetic until a private operational repository is established.

## First hardware-facing proof of concept

The first hardware-facing proof of concept should connect to a local Meshtastic device, send a single synthetic training message, subscribe to incoming text events, and record metadata-only packet observations.

Synthetic test payload:

```text
ROUTINE / TRAINING / CHW-00 / training-site / test check-in no patient data / REQ confirm receipt
```

The proof of concept should not send patient information, real site coordinates, live keys, private channel names, or deployment-sensitive identifiers.
