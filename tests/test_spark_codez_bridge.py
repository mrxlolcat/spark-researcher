from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


def load_bridge() -> ModuleType:
    path = Path(__file__).resolve().parents[1] / "scripts" / "spark_codez_bridge.py"
    spec = importlib.util.spec_from_file_location("spark_codez_bridge", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_infers_domain_from_active_domain_chip() -> None:
    bridge = load_bridge()

    assert bridge._infer_domain({"activeDomainChips": ["domain-chip-startup-yc"]}) == "startup"
    assert bridge._infer_domain({"activeDomainChips": ["domain-chip-xcontent"]}) == "content"
    assert bridge._infer_domain({"activeDomainChips": ["domain-chip-crypto-trading"]}) == "trading"


def test_maps_advisory_to_spark_codez_researcher_response() -> None:
    bridge = load_bridge()
    response = bridge._response_from_advisory(
        {
            "requestId": "req:test",
            "traceId": "trace:harness",
            "userMessage": "Do we need deep research?",
        },
        {
            "domain": "startup",
            "trace_id": "trace:researcher",
            "selected_packet_ids": ["packet:one"],
            "guidance": ["Prefer narrow wedges."],
            "boundaries": ["Only apply to early-stage startup strategy."],
            "packets": [{"path": "artifacts/memory/documents/packet-one.md"}],
            "packet_stability": {"status": "durable_supported"},
            "epistemic_status": {
                "status": "grounded",
                "packet_count": 1,
                "missing_evidence": [],
                "recommended_actions": ["Keep claims bounded."],
                "clarifying_questions": [],
            },
        },
    )

    assert response["requestId"] == "req:test"
    assert response["traceRef"] == "trace:researcher"
    assert response["packetRefs"] == ["packet:one"]
    assert response["memoryRefs"] == ["artifacts/memory/documents/packet-one.md"]
    assert response["followupActions"] == ["Keep claims bounded."]
    assert "epistemic_status=grounded" in response["evidenceSummary"]
