# Controlled Document Corruption

Five corruption mechanisms will be investigated, informed by previous research on RAG noise robustness (Wu et al., 2025):

1. Lexical errors: Controlled spelling and character-level perturbations that preserve factual meaning.
2. Duplicates: Repeated passages introduced to examine ranking diversity and unique evidence coverage.
3. Semantic distractors: Topically similar but non-supporting passages that may compete with relevant evidence.
4. Outdated information: Superseded document versions with a verifiable relationship to an authoritative reference.
5. Contradictory evidence: Non-authoritative variants containing claims that conflict with verified supporting evidence.

Each variant will retain its original document identifier, corruption type, severity, and validity status. Three severity levels will be defined using mechanismspecific quantities and calibrated through an initial pilot. Authoritative supporting evidence will remain available in the principal experiments, allowing retrieval and selection failures to be assessed against a stable reference answer. Where corruption changes corpus size, matched controls will help distinguish corruption effects from corpus-growth effects.

Individual corruption types will form the main benchmark. Selected combinednoise conditions may be explored if time permits, without requiring an exhaustive combination of all mechanisms.
