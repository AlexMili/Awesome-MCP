# Contributing to Awesome MCP

Thanks for helping keep this list useful! This guide explains how to add a new entry (server, client, SDK or tool).

## What belongs here

This is a curated list of **Model Context Protocol (MCP)** servers, clients, SDKs and tools. Before submitting, make sure your entry:

- Is directly related to MCP (implements, consumes, or tools the protocol).
- Points to a **public repository** (preferably GitHub) that actually exists and works.
- Has a real, non-promotional description of what it does.
- Is not a duplicate of an existing entry.

We favor projects that are functional and maintained. Brand-new projects are welcome, but abandoned or empty repos may be declined.

### The "is it really an MCP server?" test (for the Servers list)

This is the one rule that most often gets a PR closed, so it's worth getting right. A **Server** entry must have the MCP server as its **reason for being**, not as a feature bolted onto another product. The presence of the word "MCP" in a README is not enough.

Ask: **if you removed the MCP server, would the project lose its purpose?**

- **Yes** → it's a real MCP server. ✅
- **No** — the project is still a complete product (a framework, CLI, SaaS, app) and MCP is just one more connector → it's **off-topic** for the Servers list. ❌

The other sections have their own eligibility bars (see [Where to put your entry](#where-to-put-your-entry)); a Tools entry, for example, doesn't have to be an MCP server itself, but it must serve the building/testing/running of MCP servers.

## How an entry is structured

Each entry is a single row in a Markdown table. Here is the format for the **Servers**, **Clients** and **Tools** tables:

```markdown
| [Name](https://github.com/owner/repo) | Short description of what it does. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 0 |
```

| Column | What you fill in | Notes |
|---|---|---|
| **Name** | `[Name](repo-url)` | The link text and the repository URL. The only link in the row lives here, and it must point to a GitHub repository (`https://github.com/owner/repo`). Leave the ` ✅` marker off, automation adds it to official / first-party entries. |
| **Description** | One concise sentence | Start with a capital, end with a period. **No links in the description.** No marketing fluff, no "the best…". Mention notable capabilities if helpful. |
| **Lang** | Language icon (best guess) | Drop in a [devicon](https://devicon.dev/) `<img>` tag (see snippets below), or `—` if unsure. It gets auto-detected, so don't stress over it. |
| **Activity** & **⭐** | Leave a placeholder | Just put `🟢 0d` and `0`. |

> You really only need to get the **Name**, the **Description** and the **right section** right. The **Lang** icon, **Activity**, **⭐** and the **✅** marker are all filled in or recomputed automatically when the entry is merged, so approximate or empty values are fine, they get normalized.

### Language icon snippets

Most languages use a plain `<img>`:

```markdown
<!-- TypeScript -->
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript">
<!-- Python -->
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python">
<!-- JavaScript -->
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript">
<!-- Go -->
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go">
<!-- C# -->
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="18" alt="C#" title="C#">
```

Rust uses a `<picture>` so the icon stays visible in dark mode:

```markdown
<picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture>
```

Swap the language slug (`typescript`, `python`, `go`, …) for any other [devicon](https://devicon.dev/). If the repo has no clear language, use `—` for the Lang cell.

## Where to put your entry

### Servers

Servers are grouped **by use case**. Pick the single best-fitting category:

- Dev, Code & Git
- Databases & Data
- Cloud, DevOps & Monitoring
- Web, Search & Browser
- Productivity, Docs & Knowledge
- Communication & Social
- Commerce, Ads & Business
- AI, Agents & Memory
- Media & 3D
- Finance & Crypto
- Other

If nothing fits, use **Other**. Don't create a new category in your PR — open an issue first if you think one is missing.

> **Don't add yourself to ⭐ Featured.** The Featured table at the top is curated by the maintainer based on traction (stars/activity), not self-declared. Add your server to its normal category under `Servers`; a PR that promotes its own entry into Featured will be asked to remove that line.

### Clients, SDKs, Tools

- **Clients** — apps/integrations that *connect to* MCP servers.
- **SDKs** — libraries to *build* MCP servers/clients. Official ones (maintained by the MCP org) go under `SDKs › Official`; everything else under `SDKs › Community`.
- **Tools** — anything that helps you *build, test, secure, deploy or manage* MCP servers.

## Ordering

Rows are **not** alphabetical. Within each table they're sorted by **star count, highest first**, and that ordering is recomputed automatically when signals refresh. So in practice: **just add your row as the last line of its section.** It'll get re-sorted into place at merge.

## Update the Contents counts

The `## Contents` section lists each server category with a count, e.g. `[Dev, Code & Git](#dev-code--git) (15)`. If you add a server, bump the count for its category by one.

## Submitting your change

1. Fork the repo and create a branch.
2. Edit `README.md` to add your row (and update the Contents count if it's a server).
3. Keep your PR focused — **one entry per pull request** is easiest to review.
4. Open the PR with a title like `Add <Name> to <Category>` and a one-line note on what the project does.

That's it — thanks for contributing! 🎉
