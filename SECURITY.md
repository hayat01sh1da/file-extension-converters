# Security Policy

## Supported Versions

- The default `master` branch is the only supported release line.
- Older tags or local modifications are considered out of scope unless they can
  be reproduced on the latest commit.

## Ecosystem & Compatibility

| Component            | Version(s) / Tooling            | Notes |
| -------------------- | ------------------------------ | ----- |
| OS baseline          | WSL (Ubuntu 24.04.3 LTS)       | Matches the setup steps in the README. |
| Ruby CLI utilities   | Ruby 4.0.1 (`.ruby-version`)   | Uses only Ruby stdlib (e.g., `Find`, `FileUtils`). Extra gems must be declared at the script level. |
| Python CLI utilities | CPython 3.14.2 (`.python-version`) | Standard-library only (`argparse`, `pathlib`). Add `requirements.txt` if third-party packages are introduced. |

## Backward Compatibility

- CLI prompts and dry-run behavior are stable for Ruby 4.0.x / Python 3.14.x.
	Any breaking change (such as new parameter requirements) will be documented
	in the README prior to release.
- Earlier interpreter majors are considered legacy and will not receive
	backported fixes.

## Reporting a Vulnerability

Please disclose suspected vulnerabilities privately:

1. Use GitHub’s **Security → Report a vulnerability** form to open a private
	advisory (preferred).
2. If needed, email `security@project.org` with reproduction steps, affected
	parameters (`original_extension`, `target_extension`, `mode`), and
	environment details.

We aim to acknowledge within **3 business days** and provide updates at least
every **7 business days** until resolution. Fixes are released on `master` and
communicated via the changelog.
