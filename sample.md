## Robust RAG under Noisy and Conflicting Knowledge Bases

Author: Sandramol Santhosh

Cohort: DSIA.vzM.25

Date: 17 October 2026

First Supervisor: Mohammadreza Mohebbi, MSc

## 1 Initial Situation and Problem Statement

Large language models (LLMs) support applications such as question answering, summarization, and knowledge assistance, but their responses may contain factual inaccuracies, unsupported claims, or outdated information. Retrieval-Augmented Generation (RAG) addresses these limitations by incorporating external documents into the generation process (Lewis et al., 2020). However, access to retrieved information does not guarantee reliable answers, as performance depends on the relevance, quality, and interpretation of the supporting evidence.

Real-world knowledge repositories frequently contain duplicate records, outdated versions, lexical errors, irrelevant content, and contradictory statements. These imperfections can affect different stages of a RAG pipeline: relevant documents may be missed during retrieval, misleading passages may be ranked highly, and language models may generate incorrect answers despite receiving relevant evidence. Moreover, language models do not always use information in their context consistently (Liu et al., 2024), making both evidence selection and interpretation important for reliable answer generation.

Sparse, dense, and hybrid retrieval methods offer different mechanisms for identifying relevant documents, while cross-encoder reranking can refine the ordering of retrieved candidates. Their effectiveness, however, may depend on the type and severity of corpus corruption. Lexical errors can disrupt term matching, duplicates can limit evidence diversity, and outdated or contradictory information can complicate evidence selection. Previous research, including NoiserBench, has shown that different noise types affect RAG performance differently and may not always reduce answer quality (Wu et al., 2025). Nevertheless, further controlled comparisons are needed to understand how retrieval and reranking strategies respond to document-level imperfections and how these effects influence grounded answers.

Problem statement. This thesis investigates the robustness of sparse, dense, and hybrid retrieval, each with and without cross-encoder reranking, under five controlled corruption conditions: lexical errors, duplicates, semantically similar distractors, outdated information, and contradictory evidence. Using consistent evaluation questions, retrieval budgets, and generation settings, the study will examine evidence retrieval, final-context selection, answer correctness, and failure attribution. The objective is to provide a reproducible comparison of established retrieval configurations and identify their strengths and limitations when document collections contain unreliable or conflicting information.

## 2 Relevance

Scientific relevance. Reliable evidence retrieval is essential for Retrieval-Augmented Generation (RAG), particularly when document collections contain noisy or conflicting information. Previous research has examined the effects of noise on RAG performance (Wu et al., 2025) and the importance of citation-supported generation (Gao et al., 2023). Building on these findings, this thesis investigates how retrieval and reranking strategies respond to controlled corpus imperfections and how these effects influence evidence selection and answer reliability.

The scientific contribution comprises three components: (1) a reproducible benchmark covering five document-corruption types with documented severity and provenance; (2) a systematic comparison of sparse, dense, and hybrid retrieval, with and without cross-encoder reranking; and (3) an evidence-aware evaluation that distinguishes retrieval, evidence-selection, and generation failures. Rather than introducing a new retrieval algorithm, the study provides a controlled empirical analysis connecting corpus quality, retrieval robustness, and grounded answer generation.

Practical relevance. Organizations increasingly rely on RAG systems to access technical documentation, internal knowledge repositories, and frequently updated information. However, duplicate records, outdated versions, and conflicting statements can compromise the reliability of retrieved evidence. Knowledge updating, retrieval quality, and response reliability are recognized challenges in RAG applications (Gao et al., 2024).

The findings are expected to provide practical guidance on selecting retrieval and reranking configurations under different document-quality conditions. By identifying when particular methods improve evidence selection and when corpus maintenance remains necessary, the study can support more informed RAG system design without requiring the development of a production-ready platform.

## 3 Objectives and Expected Results

The primary objective of this thesis is to evaluate the robustness of RetrievalAugmented Generation (RAG) under controlled document corruption. The study examines how retrieval strategies and cross-encoder reranking influence evidence selection, answer correctness, and citation grounding across different corruption types and severity levels.

## Specific objectives.

1. Construct a reproducible evaluation corpus containing lexical errors, duplicates, semantically similar distractors, outdated information, and contradictory evidence, with documented severity, provenance, and evidence validity.
2. Compare six configurations combining BM25, dense retrieval, and hybrid retrieval, each with and without cross-encoder reranking.
3. Quantify the effects of corruption type and severity on retrieval effectiveness, authoritative-evidence coverage, and final-context selection.
4. Evaluate downstream answer correctness and citation grounding while distinguishing retrieval, evidence-selection, and generation failures.

Main research question. How do retrieval and reranking strategies influence evidence reliability and grounded answer generation under different types and levels of document corruption?

## Sub-research questions.

- RQ1. How do corruption type and severity affect the effectiveness of sparse, dense, and hybrid retrieval?
- RQ2. Under which document-quality conditions does cross-encoder reranking improve the selection of relevant and authoritative evidence?
- RQ3. How do retrieval and evidence-selection failures affect answer correctness and citation grounding, and how can they be distinguished from generation errors?

## Research hypotheses.

- H1. The relative effectiveness of sparse, dense, and hybrid retrieval varies across corruption types, with hybrid retrieval providing benefits under some conditions.
- H2. Cross-encoder reranking improves evidence ranking when relevant candidates are available, but its effectiveness depends on corpus quality and candidate selection.
- H3. Outdated and contradictory evidence produces different patterns of evidenceselection and answer-grounding errors from lexical corruption.
- H4. Corruption severity influences retrieval and answer quality, with effects varying across corruption mechanisms and retrieval configurations.

Expected results. The expected outcomes include a reproducible corruption benchmark, a comparative evaluation of six retrieval and reranking configurations, and quantitative analyses of robustness across five corruption types and multiple severity levels. Selected end-to-end RAG experiments will assess answer correctness, citation grounding, and failure attribution.

The thesis will also provide statistical comparisons, computational-cost measurements, documented experimental limitations, and reproducible implementation artifacts. The findings will support evidence-based recommendations for retrieval and reranking under imperfect document conditions, without assuming that more complex methods consistently outperform simpler alternatives.

## 4 Approach and Methods

This thesis adopts a controlled experimental design to evaluate the robustness of Retrieval-Augmented Generation (RAG) under document corruption. The methodology combines corpus preparation, systematic perturbations, retrieval and reranking comparisons, and evidence-aware answer evaluation. Experiments are divided into a comprehensive retrieval benchmark and a focused end-to-end RAG evaluation to maintain scientific rigor while limiting computational requirements.

## 4.1 Datasets and Corpus Preparation

HotpotQA will serve as the primary dataset because it provides multi-hop questions, reference answers, and annotated supporting facts (Yang et al., 2018). Publicly available labeled data will be divided into nonoverlapping development and evaluation partitions.

A shared retrieval corpus will be constructed by pooling documents associated with multiple questions rather than creating a separate collection for each query. Documents will be standardized, segmented, and indexed using consistent passage boundaries. Source identifiers and gold supporting-fact mappings will be preserved to support evidence-level evaluation. This controlled corpus will not be presented as equivalent to full-Wikipedia retrieval.

Natural Questions Open (NQ-Open) may provide a supplementary evaluation of answer-level generalization if resources permit. Because its standard format lacks comparable supporting-fact annotations, HotpotQA will remain the basis for evidence-level analysis.

## 4.2 Controlled Document Corruption

Five corruption mechanisms will be investigated, informed by previous research on RAG noise robustness (Wu et al., 2025):

1. Lexical errors: Controlled spelling and character-level perturbations that preserve factual meaning.
2. Duplicates: Repeated passages introduced to examine ranking diversity and unique evidence coverage.
3. Semantic distractors: Topically similar but non-supporting passages that may compete with relevant evidence.
4. Outdated information: Superseded document versions with a verifiable relationship to an authoritative reference.
5. Contradictory evidence: Non-authoritative variants containing claims that conflict with verified supporting evidence.

Each variant will retain its original document identifier, corruption type, severity, and validity status. Three severity levels will be defined using mechanismspecific quantities and calibrated through an initial pilot. Authoritative supporting evidence will remain available in the principal experiments, allowing retrieval and selection failures to be assessed against a stable reference answer. Where corruption changes corpus size, matched controls will help distinguish corruption effects from corpus-growth effects.

Individual corruption types will form the main benchmark. Selected combinednoise conditions may be explored if time permits, without requiring an exhaustive combination of all mechanisms.

## 4.3 Retrieval and Reranking Strategies

Three retrieval approaches will be compared:

1. Sparse retrieval: BM25 for lexical matching.
2. Dense retrieval: A pretrained embedding model, initially BGE-small-env1.5, for semantic similarity.
3. Hybrid retrieval: BM25 and dense retrieval combined through Reciprocal Rank Fusion (RRF).

Each approach will be evaluated with and without cross-encoder reranking, producing six configurations. BGE-reranker-base will be the initial reranking model, with a lighter pretrained alternative permitted if required by available hardware.

All configurations will use identical questions, corpus versions, passage boundaries, and evaluation partitions. Candidate-retrieval depth and final-context budgets will be standardized. Model choices and ranking parameters will be finalized using development data before evaluation. Candidate recall and final evidence coverage will be measured separately because reranking cannot recover evidence absent from the initial candidate pool.

## 4.4 Experimental Design

The evaluation will comprise two stages.

Stage I - Retrieval robustness. All six configurations will be evaluated on clean and corrupted HotpotQA corpora across five corruption types and three severity levels. Comparisons will examine retrieval effectiveness, authoritativeevidence coverage, performance changes relative to the clean baseline, and the influence of reranking. This stage will not require language-model generation for every condition.

Stage II - End-to-end RAG evaluation. A predefined, representative subset of questions and conditions will be selected for answer generation, including clean, noisy, outdated, and contradictory evidence settings. A single pretrained instruction-tuned language model will be used with fixed prompts, decoding parameters, and context budgets. The specific model will be selected through an initial hardware-feasibility pilot and fixed before final evaluation.

Generated answers will include references to retrieved passage identifiers, enabling separate assessment of answer correctness and citation support. This stage will examine how differences in evidence selection influence grounded responses without requiring generation across the entire experimental matrix.

## 4.5 Evaluation and Error Analysis

Retrieval quality will be assessed using Recall@k, Mean Reciprocal Rank (MRR), and nDCG@k where supported by relevance annotations. Supportingfact coverage will measure whether the evidence required for a question appears in the candidate pool and final context. Duplicate-aware coverage and authoritative-evidence selection will provide additional measures for relevant corruption conditions.

Answer quality will be evaluated using Exact Match (EM), token-level F1, and evidence-grounding measures. Citation validity will be distinguished from actual citation support, with manually reviewed samples used to assess ambiguous cases and verify evidence attribution.

Failure attribution will distinguish three principal categories:

1. Retrieval failure: Required supporting evidence is absent from the initial candidate pool.
2. Evidence-selection failure: Required evidence is retrieved but does not reach the final context.
3. Generation failure: Sufficient authoritative evidence is available in the final context, but the answer is incorrect or unsupported.

Ambiguous or overlapping failures will be documented separately. Computational efficiency will be assessed using retrieval and reranking latency, end-toend response time, and token usage.

Statistical comparisons will use paired observations across identical questions and corruption conditions, supported by confidence intervals and uncertainty estimates. Both positive and negative findings will be reported to avoid assuming that hybrid retrieval or reranking consistently improves robustness.

## 4.6 Work Packages and Feasibility

The project will be organized into six work packages:

1. WP1: Literature review, HotpotQA preparation, and verification of supportingfact mappings.
2. WP2: Implementation and validation of sparse, dense, and hybrid retrieval baselines.
3. WP3: Generation and validation of controlled corruption scenarios and severity levels.
4. WP4: Evaluation of six retrieval and reranking configurations.
5. WP5: Selected end-to-end RAG experiments, citation evaluation, and failure attribution.
6. WP6: Statistical analysis, reproducibility documentation, and thesis preparation.

The planned duration is approximately six months. An early pilot will assess corpus processing, model compatibility, and computational requirements before the final evaluation protocol is fixed. The research will use pretrained models and established retrieval methods; developing or training a new language model is outside its scope.

## 4.7 Reproducibility

Dataset partitions, document transformations, evidence mappings, random seeds, model versions, retrieval parameters, and evaluation procedures will be documented. Code, configurations, and derived evaluation artifacts will be made available where licensing permits. These materials will support independent reproduction of the controlled experiments and transparent interpretation of the resulting findings.

## Literatur

Gao, T., Yen, H., Yu, J., and Chen, D. (2023). Enabling large language models to generate text with citations. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 6465-6488, Singapore. Association for Computational Linguistics.

- Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, M., and Wang, H. (2024). Retrieval-augmented generation for large language models: A survey. Revised March 2024.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., Riedel, S., and Kiela, D. (2020). Retrievalaugmented generation for knowledge-intensive NLP tasks. In Advances in Neural Information Processing Systems, volume 33, pages 9459-9474.
- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., and Liang, P. (2024). Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12:157-173.
- Wu, J., Zhang, S., Che, F., Feng, M., Shao, P., and Tao, J. (2025). Pandora's box or aladdin's lamp: A comprehensive analysis revealing the role of RAG noise in large language models. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5019-5039, Vienna, Austria. Association for Computational Linguistics.
- Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W. W., Salakhutdinov, R., and Manning, C. D. (2018). HotpotQA: A dataset for diverse, explainable multihop question answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 2369-2380, Brussels, Belgium. Association for Computational Linguistics.