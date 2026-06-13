# Mesh packet log schema

Maintainer: Paul Skeffington, MS, MPH  
Project: Haiti Nippes rural and remote healthcare communications  
Last updated: 2026-06-13

## Purpose

This schema defines a public-safe, metadata-only packet log for Meshtastic programming tests, bench validation, and early planning. It is designed to support repeatable observations without storing patient data, live encryption keys, private channel names, exact field coordinates, or sensitive deployment details.

The packet log is not a clinical record. It is a communications engineering and operations-readiness artifact.

## CSV location

Synthetic demo output:

```text
outputs/mesh_packet_log_demo.csv
```

The `outputs/` directory may contain generated artifacts. Before committing any output file, confirm that it contains synthetic or approved public-safe data only.

## Generator

The current CSV writer lives at:

```text
src/haiti_nippes/mesh/logging.py
```

Demo command:

```bash
python examples/mesh_packet_log_demo.py
```

## Fields

| field | type | required | description | public-safety rule |
|---|---:|---:|---|---|
| `observed_at` | string | yes | ISO-like timestamp for the observation. | Use test timestamps or approved field timestamps only. |
| `source_node` | string | yes | Public-safe source node label. | Do not use real names, phone numbers, or private identifiers. |
| `destination_node` | string | yes | Public-safe destination node label. | Use planning labels or synthetic labels. |
| `channel_label` | string | yes | General channel category. | Use generic labels such as `training`; do not store private channel names. |
| `message_kind` | string | yes | Message category such as `training`, `check_in`, `logistics`, or `wash`. | Keep categories broad and operational. |
| `priority` | string | yes | Priority label such as `routine`, `priority`, `urgent`, or `emergency`. | Do not encode sensitive event details in the priority field. |
| `payload_summary` | string | yes | Sanitized summary of the message content. | No patient names, dates of birth, addresses, keys, passwords, or clinical details. |
| `hop_limit` | integer or blank | no | Hop limit associated with the packet, if available. | Engineering metadata only. |
| `rssi` | float or blank | no | Received signal strength indicator, if available. | Engineering metadata only. |
| `snr` | float or blank | no | Signal-to-noise ratio, if available. | Engineering metadata only. |

## Example row

```csv
observed_at,source_node,destination_node,channel_label,message_kind,priority,payload_summary,hop_limit,rssi,snr
2026-06-13T14:00:00Z,NIP-TRAIN-001,NIP-TRAIN-002,training,training,routine,synthetic training check-in,3,-78.0,8.25
```

## Validation rules

The current `PacketLogRecord` object blocks obvious sensitive terms before writing. This is a guardrail, not a full privacy filter. Operators must still review all generated logs before committing them.

Blocked terms currently include examples such as:

```text
dob
date of birth
patient name
private key
channel key
password
```

## Bench-test use

During a two-node bench test, record only:

- synthetic node labels;
- generic channel category;
- synthetic payload summary;
- timestamp;
- hop limit, RSSI, and SNR when available;
- confirmation that no patient data was transmitted.

## Nippes translation use

For Nippes planning, this schema should support engineering questions only:

- Which node role heard the message?
- How many hops were needed?
- Did message quality change after antenna placement changed?
- Which generic terrain or obstruction condition reduced reliability?
- Did training-channel users follow message formatting rules?

Exact clinic coordinates, healthcare-worker routes, real household locations, and private relay candidates belong in a private operational annex, not this public repository.
