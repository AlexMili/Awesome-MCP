# Awesome MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers, clients, SDKs and tools.

The Model Context Protocol (MCP) is an open protocol published by [Anthropic](https://www.anthropic.com/) in November 2024. It lets LLM apps connect to external data and tools. This list covers the whole ecosystem around the protocol, organized **by use case** so you can find what you need fast.

_Servers are grouped by what they do. Each row shows the real language, repository activity (last push) and stars. **✅ = official / first-party.** Activity legend: 🟢 ≤3 mo · 🟡 ≤1 yr · 🔴 >1 yr · 🗄️ archived · ❔ unknown. Signals auto-refreshed; last update 2026-11-22._

## Contents

- [Servers](#servers)
  - [Dev, Code & Git](#dev-code--git) (17)
  - [Databases & Data](#databases--data) (2)
  - [Cloud, DevOps & Monitoring](#cloud-devops--monitoring) (7)
  - [Web, Search & Browser](#web-search--browser) (8)
  - [Productivity, Docs & Knowledge](#productivity-docs--knowledge) (6)
  - [Communication & Social](#communication--social) (7)
  - [Commerce, Ads & Business](#commerce-ads--business) (3)
  - [AI, Agents & Memory](#ai-agents--memory) (10)
  - [Media & 3D](#media--3d) (6)
  - [Finance & Crypto](#finance--crypto) (2)
  - [Other](#other) (7)
- [Clients](#clients)
- [SDKs](#sdks)
- [Tools](#tools)

## ⭐ Featured

Standout community servers by traction and activity.

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [SocialRouter](https://github.com/socialrouter/mcp) | Unified API to fetch social media data across LinkedIn, Instagram, X, Reddit, TikTok, YouTube, and more, with automatic provider failover. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 6d | 1 |
| [MarkItDown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) ✅ | Lightweight STDIO and SSE MCP server for calling MarkItDown. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2w | 197.8k |
| [Playwright](https://github.com/microsoft/playwright-mcp) ✅ | Provides browser automation capabilities using Playwright. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 4d | 40k |
| [Official Github](https://github.com/github/github-mcp-server) ✅ | Seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 1d | 34.7k |
| [Blender](https://github.com/ahujasid/blender-mcp) | Interact with and control Blender using prompt assisted 3D modeling, scene creation, and manipulation. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 4d | 35.4k |
| [AWS](https://github.com/awslabs/mcp) ✅ | A suite of specialized MCP servers that bring AWS best practices directly to your development workflow. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 1d | 9.9k |
| [XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) | Provides Xcode-related tools for integration with AI assistants and other MCP clients. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 6.6k |
| [WhatsApp](https://github.com/lharries/whatsapp-mcp) | Search your personal Whatsapp messages, search your contacts and send messages to either individuals or groups. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🔴 1y | 6.9k |
| [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | Interact with Obsidian. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2mo | 4.5k |

> The canonical reference servers live in [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — listed by category below.

## Servers

### Dev, Code & Git

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) ✅ | Secure file operations with configurable access controls. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) ✅ | Repository management, file operations, and GitHub API integration. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) ✅ | GitLab API, enabling project management. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) ✅ | Tools to read, search, and manipulate Git repositories. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Official Github](https://github.com/github/github-mcp-server) ✅ | Seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 1d | 34.7k |
| [XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) | Provides Xcode-related tools for integration with AI assistants and other MCP clients. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 6.6k |
| [Filesystem](https://github.com/mark3labs/mcp-filesystem-server) | File operations with configurable access controls. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟡 12mo | 699 |
| [Muvon/octocode](https://github.com/Muvon/octocode) | Semantic code indexer with GraphRAG knowledge graph and MCP server. Tree-sitter AST parsing, ast-grep structural search, code signatures view. 13+ languages. Local-first, Apache 2.0. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 2w | 529 |
| [Node.js](https://github.com/hyperdrive-eng/mcp-nodejs-debugger) | Gives Cursor or Claude Code access to Node.js at runtime to help you debug. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🗄️ archived | 301 |
| [VSCode Devtools (Bifrost)](https://github.com/biegehydra/BifrostMCP) | Connect to VSCode IDE and use semantic tools like `find_usages`. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 8mo | 225 |
| [unslop](https://github.com/avivgerz-hue/unslop) | Audits UI code for AI-generated design slop with 72 rules and generates refactor plans, exposed through 4 tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 6d | 68 |
| [mcp-probe-kit](https://github.com/mybolide/mcp-probe-kit) | Spec-driven dev workflow server for coding agents: orchestrated start_feature/start_bugfix, resumable plans, and a converge gate requiring spec/test/review evidence. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 7d | 41 |
| [Apple Docs 2.0 MCP](https://github.com/mishafyi/Apple-Docs-2.0-MCP) | Searches and reads Apple's developer documentation, Human Interface Guidelines and 1,700 WWDC sessions with code, with an offline index of 336,629 pages. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 5w | 26 |
| [Hoofy](https://github.com/HendryAvila/Hoofy) | Spec-driven development companion with persistent memory (SQLite + FTS5 + knowledge graph), adaptive change pipeline, and greenfield project pipeline with Clarity Gate. 32 MCP tools, single binary, zero dependencies. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟡 8mo | 16 |
| [Bestax](https://github.com/allxsmith/bestax/tree/main/bestax-mcp) | Gives coding agents the props, examples, CSS variables and Agent Skills for the Bestax React component library (Bulma v1), served offline from a bundled index. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 15 |
| [preflight](https://github.com/preflight-dev/preflight) | 24-tool MCP server for Claude Code that scores prompts before execution, catches ambiguity, tracks correction patterns, and estimates token cost — reduces wasted tokens from vague prompts. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 8mo | 14 |
| [repomap](https://github.com/SylphxAI/repomap) | Local code graph for agents: hybrid search, symbol context with callers and callees, call paths, and change impact including git diff, plus a graph UI. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 11d | 14 |

### Databases & Data

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) ✅ | Read-only database access with schema inspection. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) ✅ | Database interaction and business intelligence capabilities. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |

### Cloud, DevOps & Monitoring

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [AWS Knowledge Base Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server) ✅ | Retrieve information from the AWS Knowledge Base using the Bedrock Agent Runtime. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) ✅ | Retrieving and analyzing issues from Sentry.io. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [AWS](https://github.com/awslabs/mcp) ✅ | A suite of specialized MCP servers that bring AWS best practices directly to your development workflow. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 1d | 9.9k |
| [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) ✅ | Deploy, configure & interrogate your resources on the Cloudflare developer platform (e.g. Workers/KV/R2/D1). | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 4w | 4.5k |
| [stackql](https://github.com/stackql/stackql) | SQL for cloud APIs. Query AWS, GCP, Azure and dozens of other providers with SQL. Includes an MCP server for agent access. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 0d | 1.1k |
| [ZenML](https://github.com/zenml-io/mcp-zenml) | Chat with your MLOps and LLMOps pipelines using the official ZenML MCP server. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2d | 49 |
| [Raygun](https://github.com/MindscapeHQ/mcp-server-raygun) | Interact with your crash reporting and real using monitoring data on your Raygun account. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2mo | 31 |

### Web, Search & Browser

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) ✅ | Browser automation and web scraping. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) ✅ | Web and local search using Brave's Search API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) ✅ | Web content fetching and conversion for efficient LLM usage. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Playwright](https://github.com/microsoft/playwright-mcp) ✅ | Provides browser automation capabilities using Playwright. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 4d | 40k |
| [Youtube](https://github.com/anaisbetts/mcp-youtube) | Uses `yt-dlp` to download subtitles from YouTube. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 3mo | 553 |
| [Kagi](https://github.com/ac3xx/mcp-servers-kagi) | A Model Context Protocol server implementation for Kagi's API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 44 |
| [newsmcp](https://github.com/pranciskus/newsmcp) | Real-time world news for AI agents — events clustered from hundreds of sources, classified by 12 topics and 30+ geographic regions, ranked by importance. Free, no API key required. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 8mo | 34 |
| [Arcmira: YouTube Transcript Search](https://github.com/arcmira/mcp) | Searches indexed YouTube transcripts for timestamped quotes, speaker appearances, sponsors, and recommendations. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2d | 33 |

### Productivity, Docs & Knowledge

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [MarkItDown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) ✅ | Lightweight STDIO and SSE MCP server for calling MarkItDown. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2w | 197.8k |
| [Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) ✅ | File access and search capabilities for Google Drive. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | Interact with Obsidian. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2mo | 4.5k |
| [anymd](https://github.com/SylphxAI/anymd) | Converts PDF, DOCX, PPTX, XLSX/CSV, EPUB, HTML/URLs, images and audio/video to clean Markdown for agents, with read, search and inspect tools; local, no API key. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 0d | 1.1k |
| [Taskade MCP](https://github.com/taskade/mcp) ✅ | Official Taskade MCP server with 50+ tools for managing workspaces, projects, tasks, custom AI agents, knowledge bases, and workflow automations. Includes OpenAPI-to-MCP codegen. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 170 |
| [open-mcp-apps](https://github.com/2nd1st/open-mcp-apps) | MCP Apps engine where the AI builds interactive UI apps — todo boards, habit trackers, dashboards — that persist across conversations, backed by data collections. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 5w | 40 |

### Communication & Social

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) ✅ | Channel management and messaging capabilities. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [WhatsApp](https://github.com/lharries/whatsapp-mcp) | Search your personal Whatsapp messages, search your contacts and send messages to either individuals or groups. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🔴 1y | 6.9k |
| [Atomic Mail](https://github.com/Atomic-Mail/atomic-mail-agentic) | Gives an agent its own mailbox: it registers an address by proof of work, then reads, sends and searches over JMAP. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2d | 256 |
| [/call-me](https://github.com/radres/call-me) | Rings the user's phone (iPhone or Android) so an agent can ask a question out loud and get the spoken answer back as text, keep the line open for follow-ups, or send a text; a hosted remote server with no auth that needs the /call-me phone app. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 0d | 47 |
| [call4me](https://github.com/skeptrunedev/call4me) | Places real phone calls to businesses for the user (bookings, appointments, cancellations), navigates phone menus and returns the transcript and outcome; hosted at call4.me/mcp with OAuth. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 1d | 18 |
| [Telegram Archive](https://github.com/GeiserX/telegram-archive-mcp) | Searches messages, browses chats and reads archived Telegram history from a Telegram-Archive instance, over stdio or HTTP. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 4d | 16 |
| [SocialRouter](https://github.com/socialrouter/mcp) | Unified API to fetch social media data across LinkedIn, Instagram, X, Reddit, TikTok, YouTube, and more, with automatic provider failover. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 6d | 1 |

### Commerce, Ads & Business

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Coupang MCP](https://github.com/uju777/coupang-mcp) | Korean e-commerce (Coupang) product search with Rocket Delivery filtering. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 7mo | 18 |
| [BuyWhere](https://github.com/BuyWhere/buywhere-mcp) | Real-time product search and price comparison for Singapore and Southeast Asia. 260K+ products from Lazada, Shopee, FairPrice, Courts. Remote via `mcp.buywhere.ai/mcp`. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 13d | 14 |
| [Frihet](https://github.com/Frihet-io/frihet-mcp) | AI-native business management with 31 tools for invoicing, expenses, clients, products, quotes, and tax compliance (VeriFactu). Multi-currency, OCR, and Stripe Connect. Supports stdio and remote Streamable HTTP with OAuth 2.0. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 1d | 13 |

### AI, Agents & Memory

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) ✅ | Knowledge graph-based persistent memory system. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [deja-vu](https://github.com/vshulcz/deja-vu) | Local cross-agent session memory MCP server and CLI across 48 coding agents (Claude Code, Codex, Cursor, OpenCode, Gemini CLI) backed by a local inverted index with secret redaction. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 0d | 1.6k |
| [Concord MCP](https://github.com/Get-Concord-AI/concord-mcp) | Local-first shared work-state for coding agents: presence, file claims, messaging, handoffs and review packets so multiple agents (Claude Code, Cursor, Codex, etc.) can coordinate on one repo. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2d | 1.5k |
| [SandBase CLI](https://github.com/sandbaseai/cli) | Local MCP bridge that connects 25 AI clients to 2,000+ models and APIs through six MCP tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 186 |
| [OpenAI](https://github.com/pierrebrunelle/mcp-server-openai) | Query OpenAI models directly from Claude. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 84 |
| [EGC](https://github.com/Fmarzochi/EGC) | Persistent cross-session memory MCP server for 13+ AI coding tools. SQLite-backed state survives context resets and keeps Claude Code, Cursor, Gemini CLI, Codex, and more in sync. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 0d | 70 |
| [Mnemoverse](https://github.com/mnemoverse/mcp-memory-server) | Hosted memory server for AI agents over MCP. Tell it a recalled memory helped or misled, and it re-ranks what comes back next. Shared rooms for multi-agent work. One key or OAuth across Claude Code, Cursor, VS Code and ChatGPT. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 30 |
| [Mnemosyne OS](https://github.com/Mnemosyne-OS/Mnemosyne-Neural-OS/tree/main/packages/mcp) | Stdio MCP server for Mnemosyne OS, a desktop memory app. Watched folders feed separate vaults on the user's machine, searched by vector and local BM25. Open core: the MCP server is MIT, the memory engine ships closed in the desktop app. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2d | 25 |
| [WritBase](https://github.com/Writbase/writbase) | MCP-native task management for AI agent fleets with multi-agent permissions, delegation safety, and full provenance. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 7mo | 12 |
| [Model Salt](https://github.com/modelsalt/model-salt) | Adds outside randomness to creative requests, so one prompt gives a different answer each time it runs. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 3d | 10 |

### Media & 3D

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Blender](https://github.com/ahujasid/blender-mcp) | Interact with and control Blender using prompt assisted 3D modeling, scene creation, and manipulation. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 4d | 35.4k |
| [Funplay MCP for Unity](https://github.com/FunplayAI/funplay-unity-mcp) | Unity Editor MCP server with execute_code, play mode automation, screenshots, input simulation, prompts, and resources. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="18" alt="C#" title="C#"> | 🟢 3d | 330 |
| [DESIGN:OS 3D Blender](https://github.com/jangtrinh/design-os-3d-blender) | Free stdio server for Blender 5.2 LTS that lets an agent check the Blender runtime, query a bpy knowledge base, validate a part spec and run a headless Blender pass that must report success, for parametric parts with glTF/STL export; source-available (PolyForm Shield). | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 6d | 121 |
| [RunAPI](https://github.com/runapi-ai/mcp) | MCP server for model discovery and AI image, video, music/audio, text-to-speech, and LLM jobs via RunAPI. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 5d | 56 |
| [YouTube Transcript](https://github.com/tubeagentkit/youtube-mcp) | Fetches YouTube transcripts, searches videos and channels, and lists channel uploads and playlists via the getyoutubetranscript.com API, as a local stdio server or a hosted endpoint. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 2d | 10 |
| [Magic Hour](https://github.com/magichourhq/magic-hour-mcp) | Hosted first-party server that lets agents generate and edit video, images, and audio through Magic Hour's API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 1d | 10 |

### Finance & Crypto

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Equibles](https://github.com/daniel3303/Equibles) | Self-hosted financial data MCP server for US companies: SEC filings with full-text search, XBRL financial statements, 13F holdings, insider and congressional trades, short interest and FRED macro series. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="18" alt="C#" title="C#"> | 🟢 0d | 247 |
| [Tapetide](https://github.com/Tapetide-hq/nse-bse-indian-stock-market-data-mcp) | Indian stock market (NSE and BSE) data for about 8,200 stocks through 55 tools: live quotes, financials, technicals, a 326-ratio fundamental screener and a technical screener, analyst ratings, shareholding, FII/DII flows, option chains and IV, parsed filings, IPOs, and portfolio and watchlist tracking. Runs locally over stdio or as a hosted Streamable HTTP endpoint with OAuth 2.1. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 5d | 151 |

### Other

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) ✅ | Location services, directions, and place details. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 92.2k |
| [Stdio](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/stdio.py) ✅ | Communicate with an MCP client through standard input/output streams. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 5d | 24.9k |
| [Websocket](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/websocket.py) ✅ | WebSocket server transport. This is an ASGI application, suitable to be used with a framework like Starlette and a server like Hypercorn. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 5d | 24.9k |
| [AppleScript](https://github.com/joshrutkowski/applescript-mcp) | Implements interaction with macOS via AppleScript. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 397 |
| [Make](https://github.com/integromat/make-mcp-server) | Turn Make scenarios into callable tools for AI assistants. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 4w | 174 |
| [domain-mcp](https://github.com/joachimBrindeau/domain-mcp) | MCP server to search, register, and manage domains (availability, DNS, WHOIS) via Dynadot API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2mo | 13 |
| [SheetsData](https://github.com/octoco-ltd/sheetsdata-mcp) | Instant access to electronic component datasheets for AI agents — specs, pinouts, package info, absolute max ratings extracted from manufacturer PDFs on demand. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 13d | 13 |

## Clients

| Client | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [n8n](https://github.com/nerding-io/n8n-nodes-mcp) | interact with Model Context Protocol (MCP) servers in your n8n workflows. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 10mo | 3k |
| [eechat](https://github.com/Lucassssss/eechat) | An open-source, cross-platform desktop application that seamlessly connects with full support for MCP, across Linux, macOS, and Windows. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟡 3mo | 354 |
| [Off Grid AI Desktop](https://github.com/off-grid-ai/off-grid-ai-desktop) | Local-first macOS app that runs a full AI suite on-device (LLM chat, image generation, transcription, memory/RAG) and connects to MCP servers as a client, with no account or telemetry. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 157 |
| [SandBase Harness](https://github.com/sandbaseai/sandbase-harness) | Local-first TypeScript agent runtime that connects agents to stdio and URL-based MCP servers, with persistent sessions, sandboxed tools, memory, credentials, audit logs, and replay. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 643 |
| [FLUJO](https://github.com/mario-andreschak/FLUJO) | Local-first visual AI agent builder and MCP client with server management, tool inspection, multi-model chat, and workflow debugging. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 1d | 674 |

## SDKs

### Official

Core SDKs maintained by the MCP organization.

| SDK | Notes | Activity | ⭐ |
|---|---|:--:|--:|
| [Python](https://github.com/modelcontextprotocol/python-sdk) | Reference implementation, most widely used. | 🟢 5d | 24.9k |
| [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk) | Reference implementation for Node.js/browser. | 🟢 3d | 13.8k |
| [Rust (rmcp)](https://github.com/modelcontextprotocol/rust-sdk) | Official Rust SDK with proc macros. | 🟢 1d | 4.1k |
| [Go](https://github.com/modelcontextprotocol/go-sdk) | Official Go SDK, maintained with Google. | 🟢 2d | 5.4k |
| [Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk) | Multiplatform (JVM, Wasm, iOS). | 🟢 2d | 1.5k |
| [C#](https://github.com/modelcontextprotocol/csharp-sdk) | ASP.NET Core, Azure Functions integration. | 🟢 6d | 4.6k |
| [Java](https://github.com/modelcontextprotocol/java-sdk) | Spring Boot integration. | 🟢 6d | 3.8k |

### Community

| SDK | Notes | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Fast MCP](https://github.com/jlowin/fastmcp) | High-level Python framework used by ~70% of Python MCP servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 28.7k |
| [tower-mcp](https://github.com/joshrotenberg/tower-mcp) | Tower-native implementation with middleware composition via `.layer()`. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 2d | 14 |
| [rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk) | Async SDK with proc macros, hyper-based HTTP transport. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 6d | 202 |
| [pmcp](https://github.com/paiml/rust-mcp-sdk) | SIMD-optimized JSON-RPC parsing, performance-focused. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 6d | 51 |
| [mcp-go](https://github.com/mark3labs/mcp-go) | Community SDK that inspired the official implementation. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 3d | 9.2k |
| [go-mcp](https://github.com/ThinkInAIXYZ/go-mcp) | Idiomatic Go API with strong typing. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 7d | 681 |
| [xmcp](https://github.com/basementstudio/xmcp) | TypeScript framework for building MCP servers with file-based tools, resources, prompts, hot reload, and deployment adapters. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 1.4k |

## Tools

Tooling that helps you **build, test, secure, deploy or manage** MCP servers.

| Tool | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Server inspector](https://github.com/modelcontextprotocol/inspector) ✅ | Visual testing tool for MCP servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 4d | 11.3k |
| [MCP Agent](https://github.com/lastmile-ai/mcp-agent) | Build effective agents with Model Context Protocol using simple, composable patterns. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 10mo | 8.6k |
| [ToolHive](https://github.com/StacklokLabs/toolhive) | A lightweight utility designed to simplify the deployment and management of MCP servers, ensuring ease of use, consistency, and security through containerization. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 0d | 2.3k |
| [MCP Installer](https://github.com/anaisbetts/mcp-installer) | A server that installs other MCP servers for you. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🔴 1y | 1.5k |
| [OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) | Records the MCP JSON-RPC a coding agent exchanges during a real session, on the same timeline as the model traffic and shell commands, then replays it offline. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 7w | 1.1k |
| [Fleur MCP](https://github.com/fleuristes/fleur) | A desktop app marketplace for Claude Desktop. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 535 |
| [MCP get](https://github.com/michaellatman/mcp-get) | A command-line tool for installing and managing Model Context Protocol (MCP) servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🗄️ archived | 501 |
| [Langchain](https://github.com/rectalogic/langchain-mcp) | Support for LangChain. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 204 |
| [Roundtable](https://github.com/askbudi/roundtable) | Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 129 |
| [ToolRegistry](https://github.com/Oaklight/ToolRegistry) | A PyPI package that simplifies tool integration by streamlining OpenAI client tool calls and managing native Python functions and MCP servers, offering both async and sync interfaces. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 67 |
| [Dify plugin](https://github.com/hjlarry/dify-plugin-mcp_server) | Change a Dify app to a mcp server. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 67 |
| [mcpscore](https://github.com/mcp-box/mcpscore) | Audits a running MCP server for protocol conformance, tool quality and security posture, and scores it 0-100 with a suggested fix for every failed check. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2d | 43 |
| [MCP Trust Kit](https://github.com/aak204/MCP-Trust-Kit) | Deterministic CI scanner and surface-risk scoring for MCP servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 7mo | 21 |
| [Sunglasses](https://github.com/sunglasses-dev/sunglasses) | Local scanner for AI agents that pins a SHA-256 of every MCP tool descriptor to flag changed tool descriptions, and checks text and files for prompt injection and credential leaks with 1,554 patterns. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 12 |
| [mcpbr](https://github.com/greynewell/mcpbr) | Benchmark runner for evaluating MCP server performance and agentic capabilities. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 6mo | 11 |

