# TenkaCloud Interview Catalog

Six versioned JSON catalogs contain 91 original AI-assisted interview-practice lessons. Content is independent of the Passport app; no executable code is downloaded. Reference implementation text is displayed only. Free explanations are self-assessed, and neither mastery nor hiring outcomes are guaranteed.

## Catalog manifests

- アルゴリズムの導出: https://raw.githubusercontent.com/susumutomita/TenkaCloudInterviewCatalog/main/native-algorithms-manifest.json
- システム設計: https://raw.githubusercontent.com/susumutomita/TenkaCloudInterviewCatalog/main/native-design-manifest.json
- CS・数学の基礎: https://raw.githubusercontent.com/susumutomita/TenkaCloudInterviewCatalog/main/native-foundations-manifest.json
- アルゴリズム実装・説明: https://raw.githubusercontent.com/susumutomita/TenkaCloudInterviewCatalog/main/native-implementation-manifest.json
- 面接・経験・英語の説明: https://raw.githubusercontent.com/susumutomita/TenkaCloudInterviewCatalog/main/native-interview-manifest.json
- 短い練習カード: https://raw.githubusercontent.com/susumutomita/TenkaCloudInterviewCatalog/main/native-warmups-manifest.json

Algorithm and design release: **2026.10.1302** (other four catalogs remain 2026.10.1301). New algorithm/design payloads are pinned to `a88d40cd5922d06129b435e1e43ad6f747e887de`; the previous 2026.10.1301 descriptors remain available. Manifests carry schema v1, catalog identity, version, immutable commit, payload path, byte length and SHA256. SHA256 verifies integrity, not publisher identity. Updating requires a new version and commit; existing versions cannot silently change. App downloads are explicit and preserve prior local versions/history.

Source attributions and original AI-assisted authorship are in each lesson. Personal profiles, answers and account credentials are excluded. This repository contains learning data only; app signing, releases and App Store distribution are separate.

## Understand, implement, and transfer

The algorithm path reuses the existing derivation and implementation lessons. Begin with constraints and small exhaustive search, then lookup/two pointers, prefix sums and interval events, condition-dependent windows, answer boundaries and the remaining topics. Practice the corresponding implementation lesson from a blank file, run boundary tests in your own environment, then attempt a changed problem without guidance. ABC C/D labels are a source-discovery aid, not a fixed difficulty or a mastery guarantee.

This release adds two original lessons (binary choices and interval events), strengthens the existing window/prefix comparison with signed-input counterexamples, and retains every original lesson ID. Official AtCoder problem and editorial links are references for transfer; official problem statements are not reproduced. ABC190 C's published problem constraint is K <= 16; the inconsistent English editorial bound is not used.

System design retains the six existing explanations and adds their technical references. Two original integrated exercises cover seat holds with late payments, and outbox/queue notification delivery with an ACK crash. The existing rate-limit exercise gains boundary traces and partition-budget analysis. Use requirements → estimates → minimal design → failure sequences → tradeoffs → changed conditions, not one memorized architecture diagram.

Reference details distinguish an officially published practice suggestion from technical documentation and original exercises. Neither is evidence that a company actually asked these questions. Company names are absent from lesson categories and badges; precise attribution remains in sources. No unverified interview anecdotes are presented as official questions.

A completed app flow is a record of answers or self-assessment, not verified implementation. Hints and references support practice; external code execution and tests require separate evidence. Existing versions and their progress remain on-device until the user explicitly removes them.
