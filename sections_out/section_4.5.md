# Evaluation and Error Analysis

Retrieval quality will be assessed using Recall@k, Mean Reciprocal Rank (MRR), and nDCG@k where supported by relevance annotations. Supportingfact coverage will measure whether the evidence required for a question appears in the candidate pool and final context. Duplicate-aware coverage and authoritative-evidence selection will provide additional measures for relevant corruption conditions.

Answer quality will be evaluated using Exact Match (EM), token-level F1, and evidence-grounding measures. Citation validity will be distinguished from actual citation support, with manually reviewed samples used to assess ambiguous cases and verify evidence attribution.

Failure attribution will distinguish three principal categories:

1. Retrieval failure: Required supporting evidence is absent from the initial candidate pool.
2. Evidence-selection failure: Required evidence is retrieved but does not reach the final context.
3. Generation failure: Sufficient authoritative evidence is available in the final context, but the answer is incorrect or unsupported.

Ambiguous or overlapping failures will be documented separately. Computational efficiency will be assessed using retrieval and reranking latency, end-toend response time, and token usage.

Statistical comparisons will use paired observations across identical questions and corruption conditions, supported by confidence intervals and uncertainty estimates. Both positive and negative findings will be reported to avoid assuming that hybrid retrieval or reranking consistently improves robustness.
