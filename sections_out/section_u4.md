# Research hypotheses.

- H1. The relative effectiveness of sparse, dense, and hybrid retrieval varies across corruption types, with hybrid retrieval providing benefits under some conditions.
- H2. Cross-encoder reranking improves evidence ranking when relevant candidates are available, but its effectiveness depends on corpus quality and candidate selection.
- H3. Outdated and contradictory evidence produces different patterns of evidenceselection and answer-grounding errors from lexical corruption.
- H4. Corruption severity influences retrieval and answer quality, with effects varying across corruption mechanisms and retrieval configurations.

Expected results. The expected outcomes include a reproducible corruption benchmark, a comparative evaluation of six retrieval and reranking configurations, and quantitative analyses of robustness across five corruption types and multiple severity levels. Selected end-to-end RAG experiments will assess answer correctness, citation grounding, and failure attribution.

The thesis will also provide statistical comparisons, computational-cost measurements, documented experimental limitations, and reproducible implementation artifacts. The findings will support evidence-based recommendations for retrieval and reranking under imperfect document conditions, without assuming that more complex methods consistently outperform simpler alternatives.
