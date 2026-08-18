# Synthetic Mesh Programming Research Notes

Maintainer: Paul Skeffington, MS, MPH  
Project: Haiti Nippes public-health research methods  
Last updated: 2026-08-17

## Purpose

This note documents a synthetic software-engineering research lane for studying message schemas, adapter boundaries, validation, and metadata-only logging in resilient-communications prototypes.

The repository is public. This lane is limited to synthetic fixtures, memory-only or dry-run behavior, generalized examples, and reproducible programming methods. It is not an operational communications system and does not establish healthcare, emergency, or field-deployment readiness.

## Current object layer

The mesh package under `src/haiti_nippes/mesh/` may be used to study bounded software objects such as messages, nodes, packet metadata, channel-policy representations, training fixtures, interfaces, and memory transports.

These objects are research abstractions. Names such as `clinic`, `field-worker`, `urgent`, or `emergency` are categorical test labels only and do not confer authority, routing priority, clinical meaning, or operational status.

## Safe programming scope

Appropriate work includes:

- synthetic message construction and validation;
- memory-only transport tests;
- dry-run command generation;
- metadata-only packet-log examples;
- interface and adapter design;
- reproducible unit tests; and
- literature or methods review on resilient communications.

## Public-data boundary

Do not commit or transmit:

- patient information;
- real healthcare-worker identities;
- private messages;
- live encryption keys or channel files;
- private channel names;
- exact field coordinates;
- deployment schedules;
- credentials; or
- site-specific operational identifiers.

## Interpretation boundary

A passing unit test, dry run, synthetic message, or metadata-log demonstration establishes only the software behavior tested. It does not establish radio coverage, reliability, emergency suitability, clinical usefulness, institutional approval, field readiness, or deployment authorization.

## Hardware boundary

Live-device interaction, range testing, site-specific node planning, operational channel procedures, and Nippes-specific deployment design are outside the active public research scope. Any future real-world study would require a separately defined protocol, appropriate authorization, privacy and data-protection controls, and independent review.

## Reproducibility

Keep tests runnable without radio hardware whenever possible. Synthetic examples should remain clearly labeled and should not be promoted into claims about real-world communications performance.
