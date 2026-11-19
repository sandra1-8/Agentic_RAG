# Retrieval and Reranking Strategies

Three retrieval approaches will be compared:

1. Sparse retrieval: BM25 for lexical matching.
2. Dense retrieval: A pretrained embedding model, initially BGE-small-env1.5, for semantic similarity.
3. Hybrid retrieval: BM25 and dense retrieval combined through Reciprocal Rank Fusion (RRF).

Each approach will be evaluated with and without cross-encoder reranking, producing six configurations. BGE-reranker-base will be the initial reranking model, with a lighter pretrained alternative permitted if required by available hardware.

All configurations will use identical questions, corpus versions, passage boundaries, and evaluation partitions. Candidate-retrieval depth and final-context budgets will be standardized. Model choices and ranking parameters will be finalized using development data before evaluation. Candidate recall and final evidence coverage will be measured separately because reranking cannot recover evidence absent from the initial candidate pool.
