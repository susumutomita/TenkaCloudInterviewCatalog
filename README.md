# Independent learning catalog data

These six plain JSON catalogs contain 87 lessons and are independent of the app. This repository distributes data independently of the app. Release manifests are templates: `commitSHA: null` intentionally prevents importing them until the actual public content commit is known.

Publish payloads in an authorized content repository first, then replace each template commitSHA with its actual immutable 40-character lowercase Git commit. Bytes and SHA256 refer to the exact files here; regenerate both if their bytes change. Publish the completed manifest separately. Register its public raw.githubusercontent.com HTTPS URL in the app. This first version accepts only that host, without credentials, query strings or redirects.

App schema version 1 validates size (2 MB maximum per payload), SHA256, catalog identity/version and saved original bytes. Metadata URLs may point to a moving branch; every payload is pinned to a full commit. Existing versions cannot silently change. Downloaded JSON is data only; reference code is displayed, never executed. SHA256 verifies integrity, not publisher identity. Content upgrades require explicit download; prior versions and history remain local.

The original source archive is preserved under InterviewLab/Incoming. Personal interview notes and profiles are excluded. The owner approved public distribution. App-store submission and release automation are separate actions.
