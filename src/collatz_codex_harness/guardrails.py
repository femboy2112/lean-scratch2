"""Claim-status discipline and hard guards for the research harness."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    VERIFIED_FACT = "Verified Fact"
    COMPUTATIONAL_OBSERVATION = "Computational Observation"
    NOT_ESTABLISHED = "Not Established"
    WITHDRAWN = "Withdrawn"
    PATCHED = "Patched"
    CONTRADICTION_DETECTED = "Contradiction Detected"
    OVER_UPGRADED = "Over-Upgraded"
    ADVISORY_ONLY = "Advisory Only"


FORBIDDEN_CLAIMS = [
    "finite-level spectral closure proves the Collatz conjecture",
    "finite-level spectral closure implies the Collatz conjecture",
    "r=3 compact factorization is closed",
    "r=3 structural mechanism is closed",
    "all-real-s determinant nonvanishing is closed",
    "cross-level spectral invariance is closed",
    "B-level descent-to-Q holds generally at s=0.55 or s=0.60",
]


@dataclass(frozen=True)
class Claim:
    text: str
    status: Status
    evidence: str


def assert_not_forbidden(text: str) -> None:
    """Raise if text contains a known over-upgrade pattern."""
    lower = text.lower()
    for forbidden in FORBIDDEN_CLAIMS:
        if forbidden.lower() in lower:
            raise ValueError(f"Forbidden/over-upgraded claim detected: {forbidden}")


def require_status(status: str | Status) -> Status:
    """Normalize and validate canonical status labels."""
    if isinstance(status, Status):
        return status
    try:
        return Status(status)
    except ValueError as exc:
        allowed = ", ".join(s.value for s in Status)
        raise ValueError(f"Unknown status {status!r}. Allowed: {allowed}") from exc


def label_observation(text: str, evidence: str) -> Claim:
    assert_not_forbidden(text)
    return Claim(text=text, status=Status.COMPUTATIONAL_OBSERVATION, evidence=evidence)
