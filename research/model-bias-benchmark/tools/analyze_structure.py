#!/usr/bin/env python3
"""
Structural audit for the mirrored-prompt model-bias benchmark.

This script intentionally does NOT decide political correctness or bias.
It measures mechanical features that can help judges locate differences.
"""

from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"

FILES = {
    ("grok", "A"): RAW / "grok-A.txt",
    ("grok", "B"): RAW / "grok-B.txt",
    ("gemini", "A"): RAW / "gemini-A.txt",
    ("gemini", "B"): RAW / "gemini-B.txt",
    ("gpt", "A"): RAW / "gpt-A.txt",
    ("gpt", "B"): RAW / "gpt-B.txt",
    ("claude", "A"): RAW / "claude-A.txt",
    ("claude", "B"): RAW / "claude-B.txt",
}

HEADING = re.compile(r"(?m)^\\s*(?:\\*\\*)?(\\d{1,2})\\.(?:\\*\\*)?(?:\\s|$)")

PREMISE_MARKERS = (
    "premise",
    "assumes",
    "assumption",
    "not established",
    "not supported",
    "overgeneral",
    "too broad",
    "interpretive framework",
    "ideological assertion",
    "contestable",
)

UNCERTAINTY_MARKERS = (
    "disputed",
    "uncertain",
    "mixed",
    "varies",
    "depends",
    "contested",
    "inconclusive",
    "complicat",
    "caveat",
)

COUNTER_MARKERS = (
    "objection",
    "counter",
    "conversely",
    "critics",
    "opponents",
    "however",
)


def parse_questions(text: str):
    matches = list(HEADING.finditer(text))
    out = {}
    for i, match in enumerate(matches):
        q = int(match.group(1))
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[q] = text[match.start():end].strip()
    return out


def count_words(text: str) -> int:
    return len(re.findall(r"\\b[\\w’'-]+\\b", text))


def count_markers(text: str, markers) -> int:
    lower = text.lower()
    return sum(lower.count(m) for m in markers)


def main():
    parsed = {}
    for key, path in FILES.items():
        text = path.read_text(encoding="utf-8", errors="replace")
        questions = parse_questions(text)
        if set(questions) != set(range(1, 21)):
            raise SystemExit(f"{path}: expected Q1-Q20, found {sorted(questions)}")
        parsed[key] = questions

    out_path = ROOT / "analysis" / "structural_metrics.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "model", "question",
            "A_words", "B_words", "word_delta", "word_ratio_A_to_B",
            "A_premise_markers", "B_premise_markers",
            "A_uncertainty_markers", "B_uncertainty_markers",
            "A_counter_markers", "B_counter_markers",
        ])

        for model in ("grok", "gemini", "gpt", "claude"):
            for q in range(1, 21):
                a = parsed[(model, "A")][q]
                b = parsed[(model, "B")][q]
                aw, bw = count_words(a), count_words(b)
                ratio = round(aw / bw, 3) if bw else ""
                w.writerow([
                    model, q,
                    aw, bw, aw - bw, ratio,
                    count_markers(a, PREMISE_MARKERS),
                    count_markers(b, PREMISE_MARKERS),
                    count_markers(a, UNCERTAINTY_MARKERS),
                    count_markers(b, UNCERTAINTY_MARKERS),
                    count_markers(a, COUNTER_MARKERS),
                    count_markers(b, COUNTER_MARKERS),
                ])

    print(out_path)


if __name__ == "__main__":
    main()
