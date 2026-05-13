from __future__ import annotations

import importlib.util
import json
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


def test_bridge_artifacts_persist_metadata_only(tmp_path: Path) -> None:
    bridge = load_bridge()
    request = {
        "runtimeRoot": str(tmp_path),
        "requestId": "req:secret",
        "traceId": "trace:input",
        "userMessage": "private launch question with raw context",
        "activeDomainChips": ["domain-chip-startup-yc"],
    }
    response = {
        "requestId": "req:secret",
        "replyText": "private advisory reply",
        "evidenceSummary": ["private evidence detail"],
        "packetRefs": ["packet:one"],
        "memoryRefs": ["artifacts/memory/documents/private.md"],
        "followupActions": ["private followup"],
        "traceRef": "trace:researcher",
        "escalationHint": "none",
    }

    bridge._write_bridge_artifacts(request, response)

    root = tmp_path / "artifacts" / "advisory" / "bridge-requests"
    request_payload = json.loads(next(root.glob("*.request.json")).read_text(encoding="utf-8"))
    response_payload = json.loads(next(root.glob("*.response.json")).read_text(encoding="utf-8"))
    combined = json.dumps({"request": request_payload, "response": response_payload}, sort_keys=True)

    assert "metadata only" in request_payload["redaction"]
    assert request_payload["hasUserMessage"] is True
    assert request_payload["userMessageLength"] == len(request["userMessage"])
    assert response_payload["replyTextLength"] == len(response["replyText"])
    assert response_payload["evidenceSummaryCount"] == 1
    assert "private launch question" not in combined
    assert "private advisory reply" not in combined
    assert "private evidence detail" not in combined
    assert "private followup" not in combined
