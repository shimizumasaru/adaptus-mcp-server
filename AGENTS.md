<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# Repository Guidelines

## Project Structure & Module Organization
Specs drive all work in this repo. Authoritative capabilities belong in `openspec/specs/`, while active proposals stay under `openspec/changes/<change-id>/` with `proposal.md`, `tasks.md`, and any delta specs organized by capability folders. Ship-ready artifacts move to `openspec/changes/archive/` after validation. CLI helpers that explain how to run OpenSpec live in `.claude/commands/openspec/`. Store supplementary research or design drafts beside the change that created them to simplify audits.

## Build, Test, and Development Commands
`openspec list` shows active change IDs, and `openspec list --specs` enumerates existing capabilities before edits. Run `openspec validate <change-id> --strict` any time you touch proposal or spec files. Downstream product code still relies on the shared quality gates: `npm run check` (lint + formatting), `npm run fix` (auto-fixable lint), `npm test` (Jest unit suite), and `CI=true npx playwright test --config=playwright.chromium.config.ts` (Chromium-only E2E parity with CI).

## Coding Style & Naming Conventions
Follow `CODING_STANDARDS.md`: Python uses macOS shebangs, 4-space indents, and docstrings for each function; JavaScript/TypeScript adheres to Google Style with camelCase variables, SNAKE_CASE constants, and JSDoc blocks. Keep lines within 80 characters when practical (hard limit 120) and favor bilingual comments when sharing snippets. Reference `API_FUNCTION_NAMING.md` for verb-led API names and keep change IDs in kebab-case verbs (for example `add-auth-telemetry`).

## Testing Guidelines
Tie every new or modified requirement in a spec delta to at least one automated test scenario. Run `npm test` locally with `NODE_OPTIONS="--experimental-vm-modules"` when mocking ES modules, and re-run until the suite is green. When specs impact the browser extension stack, capture Chromium Playwright videos to `test/e2e/videos/` and serve fixtures through `python3 -m http.server 8000` instead of `file://` URLs. Document manual verification steps inside the relevant `tasks.md` checklist.

## Commit & Pull Request Guidelines
Use Conventional Commits (`feat`, `fix`, `docs`, etc.) and always set `GIT_TERMINAL_PROMPT=0` before committing: `GIT_TERMINAL_PROMPT=0 git commit -m "docs: refresh contributor guide"`. Describe intent, scope, and validation results in each body plus `Closes #123` references where applicable. Create and maintain pull requests through the MCP GitHub integration (`mcp__github__create_pull_request`, `mcp__github__update_pull_request`), never via the `gh` CLI. PRs should link the relevant change ID, paste `openspec validate --strict` results, and include screenshots when UI/UX artifacts change even if this repo primarily stores specs.

## Security & Agent Workflow Tips
Never bypass the OpenSpec gate: confirm whether a request needs a proposal before touching files, and avoid implementing new behavior until the proposal gains approval. Do not install or run unauthorized networked tooling; this repo is operated in a sandbox with restricted network access. Long tasks that exceed a minute should trigger `~/bin/notify_completion.py` per `AUTO_NOTIFICATION_RULES.md`, and any manual TODO must include the `date '+%Y-%m-%d'` output and an owner tag.
