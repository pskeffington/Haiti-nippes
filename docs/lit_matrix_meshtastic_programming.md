# Meshtastic programming literature matrix

Maintainer: Paul Skeffington, MS, MPH  
Project: Haiti Nippes rural and remote healthcare communications  
Last updated: 2026-06-13

## Scope

This matrix tracks programming-facing Meshtastic sources for the Nippes healthcare communications program. The focus is on code, APIs, firmware, automation, configuration, telemetry, message handling, security administration, and field-operable tooling. It should remain separate from the broader humanitarian source registry until each source is converted into a formal `SourceRecord` object.

## Immediate programming direction

The first usable programming path is the official Python client/API repository. It supports scripting around Meshtastic devices, sending and receiving messages over mesh radios, accessing device operations and data, and subscribing to events through a publish-subscribe model. This makes it the best starting point for Nippes program objects such as field-message templates, device inventory checks, packet logging, telemetry review, node-health reporting, and training simulations.

## Matrix

| id | source | type | programming relevance | Nippes healthcare use | implementation notes | status |
|---|---|---|---|---|---|---|
| MESH-PROG-001 | Meshtastic Python, `meshtastic/python` | GitHub repository; Python client/API and CLI | Provides a Python library and example client for sending and receiving messages over Meshtastic mesh radios. The README describes access to device UI/application operations and event delivery through a publish-subscribe model. | Primary automation layer for a Nippes healthcare mesh: send test messages, subscribe to field events, script device checks, collect non-sensitive operational packets, and build admin dashboards. | Start with a minimal Python package under `src/haiti_nippes/mesh/` that wraps connection, message send, message receive, node inventory, and packet logging. Treat all patient-facing payloads as coded/minimized operational messages. | Active first source |
| MESH-PROG-002 | Meshtastic Firmware, `meshtastic/firmware` | GitHub repository; official device firmware | Official firmware for Meshtastic devices. Supports long-range, low-power LoRa mesh communication without internet or cellular infrastructure, and supports ESP32, nRF52, RP2040/RP2350, and Linux-based devices. | Hardware compatibility and deployment baseline for healthcare-worker nodes, clinic nodes, relays, and gateways. | Use for firmware build/flash planning, device compatibility checks, and later review of routing, roles, telemetry, channel, and security behavior. Do not fork or modify firmware until operational requirements are clear. | Active source |
| MESH-PROG-003 | Meshtastic Python container image notes | GitHub README section | The Python repo publishes container images to GHCR and supports running the `meshtastic` CLI through a container. Local hardware access requires explicit serial-device passthrough and host permissions. | Reproducible admin tooling for field laptops or gateway machines without relying on fragile local installs. | For Mac and Linux workflows, document both native Python and containerized execution. For field hardware, serial device permissions must be tested before deployment. | Candidate implementation path |
| MESH-PROG-004 | Meshtastic Python roadmap | GitHub README roadmap | The roadmap notes gaps and future needs: stronger typing, async-friendliness, CLI completeness, consistent shell-scriptable output, better pubsub documentation, third-party helper support, standardized packet recording, persistence beyond nodedb, SQLite, maps, charts, and visualizations. | This aligns directly with the Nippes R&D layer: packet logging, node database persistence, coverage visualization, field dashboards, and operational reporting. | Build local objects conservatively so they do not depend on unstable internal behavior. Prioritize small wrappers and CSV/SQLite exports. | Design guidance |
| MESH-PROG-005 | Recent Meshtastic smart-campus implementation paper | Academic preprint | Describes a Meshtastic-based LoRa mesh system integrating heterogeneous nodes, a Raspberry Pi edge gateway, Docker Compose, Node-RED, InfluxDB, and Grafana for sensing, data ingestion, time-series storage, and dashboards. | Useful architecture reference for clinic/gateway nodes, environmental monitoring, telemetry ingestion, and visual dashboards in Nippes. | Review for gateway stack design only; healthcare message privacy requirements are stricter than campus sensor monitoring. | Add to formal source registry |
| MESH-PROG-006 | Recent Meshtastic profile/resilience evaluation paper | Academic preprint | Evaluates Meshtastic modem profiles under controlled attenuation and maps profile behavior to operational regimes including emergency maximum-range operation. | Useful for choosing modem presets and relay density in rural Nippes terrain. | Extract profile-selection rules into a field test plan; validate locally because Nippes terrain, antenna height, vegetation, and building materials will dominate performance. | Add to formal source registry |

## Source links

- Meshtastic Python repository: https://github.com/meshtastic/python
- Meshtastic Python API documentation: https://python.meshtastic.org
- Meshtastic Python getting started guide: https://meshtastic.org/docs/software/python/cli/installation
- Meshtastic Firmware repository: https://github.com/meshtastic/firmware
- Meshtastic firmware build documentation: https://meshtastic.org/docs/development/firmware/build
- Meshtastic firmware flashing documentation: https://meshtastic.org/docs/getting-started/flashing-firmware/
- Smart-campus implementation preprint: https://arxiv.org/abs/2605.20379
- Resilience/profile evaluation preprint: https://arxiv.org/abs/2605.17063

## Proposed object breakdown

```text
src/haiti_nippes/mesh/
├── __init__.py
├── interface.py          # connection wrapper for serial, TCP, BLE when available
├── message.py            # structured operational message objects
├── node.py               # node identity, role, assignment, and status objects
├── inventory.py          # device custody and firmware/config status
├── packet_log.py         # non-sensitive packet logging and export
├── training.py           # training-channel drills and message templates
└── security.py           # key-rotation records, channel policy, and incident flags
```

## First development target

Create a minimal proof-of-concept script that connects to a local Meshtastic device, sends a training-channel test message, subscribes to incoming text events, and writes non-sensitive packet metadata to a local CSV or SQLite file. The first test message should use a dummy healthcare operations format only, for example:

```text
TRAINING / CHW-00 / test check-in / no patient data / priority routine
```

## Security note

The GitHub repository is currently public. Keep this matrix limited to public documentation, code references, generalized architecture, and non-sensitive operational design. Do not commit encryption keys, private channel names, real patient information, exact deployment coordinates, live healthcare-worker identities, or sensitive security procedures unless the repository is made private and access-controlled.
