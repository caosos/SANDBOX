# Source Inventory — Michael Truth-Method / CAOS First Pass

STATUS: first-pass inventory only. Full paper drafting is blocked until quote vault and claim ledger expansion are approved.

## Source priority used

1. Current conversation transcript: available in this task prompt.
2. Uploaded ABOUTME / ABOUTME(1).txt: not present in `/workspace/SANDBOX`; only the prompt's summary of ABOUTME anchors is available.
3. Other uploaded files: none found in the working repo.
4. Saved source exports from past ChatGPT conversations: no full exports found; `project-index/CONVERSATION-MAP.md` indexes likely conversation titles.
5. GitHub repositories owned or controlled by `caosos`: public profile inspected by browser; command-line Git/API access failed with CONNECT 403.
6. Local SANDBOX GitHub files: inspected via repo files.
7. Public web research: deferred to target list; not used as source support for claims in this first pass except GitHub profile/repository listing.

## Local repository sources inspected

| Source ID | Source type | Location | Relevance | Status |
|---|---|---|---|---|
| SRC-LOCAL-README | GitHub file | `README.md` | SANDBOX purpose, default storage, hard boundaries, workflow | inspected |
| SRC-OPS-STORAGE | GitHub file | `_Ops/storage-rules.md` | default behavior for storing sanitized Markdown/project artifacts | inspected |
| SRC-RULES-DO-NOT-ASSUME | GitHub file | `project-index/rules/do-not-assume.md` | exact key words, verification, no generic assumptions | inspected |
| SRC-PROJECT-INDEX | GitHub file | `project-index/PROJECT-INDEX.md` | active lanes and known repos | inspected |
| SRC-CONVERSATION-MAP | GitHub file | `project-index/CONVERSATION-MAP.md` | conversation-title map and search terms | inspected |
| SRC-CAOS-ARIA | GitHub file | `project-index/projects/caos-aria-os.md` | CAOS / Aria OS core thesis and concepts | inspected |
| SRC-CAOSCARE | GitHub file | `project-index/projects/caoscare.md` | CAOSCare thesis and product areas | inspected |
| SRC-DATING | GitHub file | `project-index/projects/dating-service.md` | relationship compatibility service thesis and constraints | inspected |
| SRC-BROOKDALE | GitHub file | `project-index/projects/brookdale-work-systems.md` | real-world workflow observation source | inspected |
| SRC-BUSINESS | GitHub file | `project-index/projects/business-visibility-engine.md` | business visibility engine lane | inspected |
| SRC-CUTLER | GitHub file | `project-index/projects/cutler-landscaping.md` | Cutler lane | inspected |
| SRC-HARDWARE | GitHub file | `project-index/projects/hardware-workstation.md` | CAOSCare hardware separation | inspected |

## Public GitHub repository inventory

Source: `https://github.com/caosos?tab=repositories`, accessed 2026-06-30 through browser tool.

| Repo | Default branch | README | Docs folders | AGENTS.md | Package files | Active branches | Recent commits | Recent PRs | Project relevance | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `caosos/Project-Riverfuck` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely TypeScript package, unconfirmed | needs repo inspection | profile says updated Jun 29, 2026 | needs repo inspection | AI-powered human compatibility platform | public profile listed; deeper git access blocked |
| `caosos/SANDBOX` | current local branch: `work`; remote default needs source | yes locally | none found locally | none found locally | none found locally | needs remote inspection | profile says updated Jun 28, 2026 | needs repo inspection | working storage for Michael's build ideas | local repo inspected |
| `caosos/CUTLERLAWNS.COM` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely TypeScript package, unconfirmed | needs repo inspection | profile says updated Jun 21, 2026 | needs repo inspection | landscaping / property preservation | public profile listed |
| `caosos/caos-os-A1` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely JavaScript package, unconfirmed | needs repo inspection | profile says updated Jun 18, 2026 | needs repo inspection | CAOS A.I. app | public profile listed |
| `caosos/caosai.net` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely Python project files, unconfirmed | needs repo inspection | profile says updated Jun 17, 2026 | needs repo inspection | server build / CAOS AI | public profile listed |
| `caosos/CAOSCARE.COM` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely JavaScript package, unconfirmed | needs repo inspection | profile says updated Jun 17, 2026 | needs repo inspection | governed AI orchestration platform | public profile listed |
| `caosos/emergent-caos-build` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely Python files, unconfirmed | needs repo inspection | profile says updated Jun 17, 2026 | needs repo inspection | governed AI platform with memory/tools/receipts | public profile listed |
| `caosos/carl-repair-leads` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely TypeScript package, unconfirmed | needs repo inspection | profile says updated Jun 13, 2026 | needs repo inspection | repair leads/local work board | public profile listed |
| `caosos/bringyourai.net` | needs source | needs repo inspection | needs repo inspection | needs repo inspection | likely HTML project files, unconfirmed | needs repo inspection | profile says updated Jun 11, 2026 | needs repo inspection | business visibility / personal project context | public profile listed |

## Access failures / limits

- `git ls-remote https://github.com/caosos/<repo>.git` failed for all known repos with `CONNECT tunnel failed, response 403`.
- Python `urllib.request` against `https://api.github.com/users/caosos/repos?...` failed with `Tunnel connection failed: 403 Forbidden`.
- Browser access to the public GitHub profile succeeded and listed 9 repositories.

## Missing source list

- Full uploaded `ABOUTME` / `ABOUTME(1).txt` exact text.
- Full saved ChatGPT source exports.
- Repo-level README/docs/issues/PRs/branches/recent commits for public repos other than local SANDBOX.
- Any Gmail/calendar/source exports.
