# Experimental Design

The evaluation will comprise two stages.

Stage I - Retrieval robustness. All six configurations will be evaluated on clean and corrupted HotpotQA corpora across five corruption types and three severity levels. Comparisons will examine retrieval effectiveness, authoritativeevidence coverage, performance changes relative to the clean baseline, and the influence of reranking. This stage will not require language-model generation for every condition.

Stage II - End-to-end RAG evaluation. A predefined, representative subset of questions and conditions will be selected for answer generation, including clean, noisy, outdated, and contradictory evidence settings. A single pretrained instruction-tuned language model will be used with fixed prompts, decoding parameters, and context budgets. The specific model will be selected through an initial hardware-feasibility pilot and fixed before final evaluation.

Generated answers will include references to retrieved passage identifiers, enabling separate assessment of answer correctness and citation support. This stage will examine how differences in evidence selection influence grounded responses without requiring generation across the entire experimental matrix.
