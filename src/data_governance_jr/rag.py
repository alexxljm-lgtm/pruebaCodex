from __future__ import annotations

from pathlib import Path
import re


class MiniRAG:
    """RAG mínimo sin dependencias externas: retrieval por solape léxico."""

    def __init__(self, kb_path: Path):
        self.kb_path = kb_path
        self.chunks = self._load_chunks()

    def _load_chunks(self) -> list[str]:
        text = self.kb_path.read_text(encoding="utf-8")
        return [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

    def _tokenize(self, text: str) -> set[str]:
        return set(re.findall(r"[a-záéíóúñ0-9]{3,}", text.lower()))

    def ask(self, question: str) -> dict:
        q_tokens = self._tokenize(question)
        scored: list[tuple[int, str]] = []
        for chunk in self.chunks:
            overlap = len(q_tokens.intersection(self._tokenize(chunk)))
            scored.append((overlap, chunk))
        scored.sort(key=lambda x: x[0], reverse=True)

        top_score, top_context = scored[0] if scored else (0, "")
        answer = (
            f"Contexto relevante encontrado (score={top_score}):\n{top_context}\n\n"
            "Respuesta sugerida: revisa el contexto y compleméntalo con reglas del negocio."
        )
        return {"score": top_score, "context": top_context, "answer": answer}
