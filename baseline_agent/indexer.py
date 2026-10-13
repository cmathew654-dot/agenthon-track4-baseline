"""Corpus indexer for the minimal Track 4 baseline.

Reads every ``*.json`` file in the corpus directory, concatenates each document's
spans into a single text string (matching the offset convention the scorer uses
via ``qfbench2_common.scoring.faithfulness._doc_text``), and records the
``doc_date`` so the retriever can enforce the embargo at retrieval time.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

_MANIFEST_NAME = "manifest.json"


@dataclass
class IndexedDoc:
    doc_id: str
    text: str
    doc_date: str | None
    entity_ids: tuple[str, ...] = ()
    shared: bool = False


def _doc_text(doc: dict) -> str:
    """Concatenate spans (or use a flat ``text`` field) — mirrors the scorer."""
    if isinstance(doc.get("text"), str):
        return doc["text"]
    spans = doc.get("spans")
    if isinstance(spans, list):
        return " ".join(sp.get("text", "") for sp in spans if isinstance(sp, dict))
    return ""


def build_index(corpus_dir: str | Path) -> list[IndexedDoc]:
    """Index all corpus documents under ``corpus_dir`` (skips the manifest)."""
    corpus_dir = Path(corpus_dir)
    manifest_path = corpus_dir.parent / _MANIFEST_NAME
    if not manifest_path.is_file():
        manifest_path = corpus_dir / _MANIFEST_NAME
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    labels = {entry["path"]: entry for entry in manifest["files"]
              if entry.get("role") == "corpus"}
    docs: list[IndexedDoc] = []
    for path in sorted(corpus_dir.glob("*.json")):
        if path.name == _MANIFEST_NAME:
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        doc_id = doc.get("doc_id", path.stem)
        metadata = labels.get(f"corpus/{path.name}", {})
        docs.append(IndexedDoc(doc_id=doc_id, text=_doc_text(doc), doc_date=doc.get("doc_date"),
                               entity_ids=tuple(metadata.get("entity_ids", [])),
                               shared=metadata.get("shared") is True))
    return docs
