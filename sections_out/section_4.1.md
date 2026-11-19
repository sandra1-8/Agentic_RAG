# Datasets and Corpus Preparation

HotpotQA will serve as the primary dataset because it provides multi-hop questions, reference answers, and annotated supporting facts (Yang et al., 2018). Publicly available labeled data will be divided into nonoverlapping development and evaluation partitions.

A shared retrieval corpus will be constructed by pooling documents associated with multiple questions rather than creating a separate collection for each query. Documents will be standardized, segmented, and indexed using consistent passage boundaries. Source identifiers and gold supporting-fact mappings will be preserved to support evidence-level evaluation. This controlled corpus will not be presented as equivalent to full-Wikipedia retrieval.

Natural Questions Open (NQ-Open) may provide a supplementary evaluation of answer-level generalization if resources permit. Because its standard format lacks comparable supporting-fact annotations, HotpotQA will remain the basis for evidence-level analysis.
