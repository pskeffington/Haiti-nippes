"""Tests for public-safe Meshtastic planning objects."""

from __future__ import annotations

import pytest

from haiti_nippes.mesh import (
    ChannelPolicy,
    DeviceInventoryRecord,
    DeviceStatus,
    FieldMessage,
    KeyRotationRecord,
    MeshNode,
    MessageKind,
    MessagePriority,
    NodeRole,
    PacketLogRecord,
)
from haiti_nippes.mesh.interface import MemoryTransport, MeshInterface
from haiti_nippes.mesh.training import basic_check_in_drill


def test_field_message_renders_compact_text() -> None:
    message = FieldMessage(
        sender="CHW-00",
        location_label="training-site",
        kind=MessageKind.TRAINING,
        priority=MessagePriority.ROUTINE,
        summary="test check-in no patient data",
        request="confirm receipt",
    )

    assert message.to_text() == (
        "ROUTINE / TRAINING / CHW-00 / training-site / "
        "test check-in no patient data / REQ confirm receipt"
    )


def test_field_message_blocks_obvious_patient_identifier_terms() -> None:
    message = FieldMessage(
        sender="CHW-01",
        location_label="clinic-zone",
        kind=MessageKind.REFERRAL,
        priority=MessagePriority.URGENT,
        summary="patient name included by mistake",
    )

    with pytest.raises(ValueError, match="patient-identifying"):
        message.validate_public_safe()


def test_memory_transport_records_sent_message() -> None:
    drill = basic_check_in_drill()
    transport = MemoryTransport()
    interface = MeshInterface(transport=transport)

    sent_text = interface.send_field_message(drill.expected_message)

    assert sent_text in transport.sent_messages
    assert sent_text.startswith("ROUTINE / TRAINING")


def test_mesh_node_display_name() -> None:
    node = MeshNode(
        node_id="NIP-REL-001",
        label="ridge-relay-test",
        role=NodeRole.RELAY,
        commune="public-test-commune",
    )

    assert node.display_name() == "NIP-REL-001 relay ridge-relay-test"


def test_inventory_attention_flags() -> None:
    maintenance_record = DeviceInventoryRecord(
        asset_id="DEV-001",
        node_id="NIP-001",
        status=DeviceStatus.MAINTENANCE,
    )
    active_record = DeviceInventoryRecord(
        asset_id="DEV-002",
        node_id="NIP-002",
        status=DeviceStatus.IN_SERVICE,
    )

    assert maintenance_record.needs_attention() is True
    assert active_record.needs_attention() is False


def test_packet_log_rejects_sensitive_summary() -> None:
    record = PacketLogRecord(
        observed_at="2026-06-13T00:00:00Z",
        source_node="NIP-001",
        destination_node="NIP-002",
        channel_label="training",
        message_kind="training",
        priority="routine",
        payload_summary="contains private key by mistake",
    )

    with pytest.raises(ValueError, match="sensitive"):
        record.to_row()


def test_channel_policy_validate_requires_positive_rotation() -> None:
    policy = ChannelPolicy(
        policy_id="POL-001",
        purpose="training channel policy",
        allowed_roles=("trainer", "field_worker"),
        message_rules=("no patient data",),
        rotation_interval_days=30,
    )

    policy.validate()


def test_key_rotation_record_blocks_key_material() -> None:
    record = KeyRotationRecord(
        policy_id="POL-001",
        rotated_on="2026-06-13",
        reason="secret value accidentally pasted",
        authorized_by_role="communications_lead",
        next_rotation_due="2026-07-13",
    )

    with pytest.raises(ValueError, match="sensitive material"):
        record.validate_public_safe()
