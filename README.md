# Awesome MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers, clients, SDKs and tools.

The Model Context Protocol (MCP) is an open protocol published by [Anthropic](https://www.anthropic.com/) in November 2024. It lets LLM apps connect to external data and tools. This list covers the whole ecosystem around the protocol, organized **by use case** so you can find what you need fast.

_Servers are grouped by what they do. Each row shows the real language, repository activity (last push) and stars. **✅ = official / first-party.** Activity legend: 🟢 ≤3 mo · 🟡 ≤1 yr · 🔴 >1 yr · 🗄️ archived · ❔ unknown. Signals auto-refreshed; last update 2026-08-03._

## Contents

- [Servers](#servers)
  - [Dev, Code & Git](#dev-code--git) (15)
  - [Databases & Data](#databases--data) (2)
  - [Cloud, DevOps & Monitoring](#cloud-devops--monitoring) (6)
  - [Web, Search & Browser](#web-search--browser) (12)
  - [Productivity, Docs & Knowledge](#productivity-docs--knowledge) (5)
  - [Communication & Social](#communication--social) (5)
  - [Commerce, Ads & Business](#commerce-ads--business) (10)
  - [AI, Agents & Memory](#ai-agents--memory) (8)
  - [Media & 3D](#media--3d) (5)
  - [Finance & Crypto](#finance--crypto) (1)
  - [Other](#other) (7)
- [Clients](#clients)
- [SDKs](#sdks)
- [Tools](#tools)

## ⭐ Featured

Standout community servers by traction and activity.

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [SocialRouter](https://github.com/socialrouter/mcp) | Unified API to fetch social media data across LinkedIn, Instagram, X, Reddit, TikTok, YouTube, and more, with automatic provider failover. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 0 |
| [MarkItDown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) ✅ | Lightweight STDIO and SSE MCP server for calling MarkItDown. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 5d | 171.1k |
| [Playwright](https://github.com/microsoft/playwright-mcp) ✅ | Provides browser automation capabilities using Playwright. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 9d | 35.8k |
| [Official Github](https://github.com/github/github-mcp-server) ✅ | Seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 0d | 31.9k |
| [Blender](https://github.com/ahujasid/blender-mcp) | Interact with and control Blender using prompt assisted 3D modeling, scene creation, and manipulation. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 25.4k |
| [AWS](https://github.com/awslabs/mcp) ✅ | A suite of specialized MCP servers that bring AWS best practices directly to your development workflow. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 9.5k |
| [XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) | Provides Xcode-related tools for integration with AI assistants and other MCP clients. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 1d | 6.2k |
| [WhatsApp](https://github.com/lharries/whatsapp-mcp) | Search your personal Whatsapp messages, search your contacts and send messages to either individuals or groups. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🔴 1y | 6.1k |
| [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | Interact with Obsidian. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2mo | 4.2k |

> The canonical reference servers live in [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — listed by category below.

## Servers

### Dev, Code & Git

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) ✅ | Secure file operations with configurable access controls. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) ✅ | Repository management, file operations, and GitHub API integration. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) ✅ | GitLab API, enabling project management. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) ✅ | Tools to read, search, and manipulate Git repositories. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Official Github](https://github.com/github/github-mcp-server) ✅ | Seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 0d | 31.9k |
| [XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) | Provides Xcode-related tools for integration with AI assistants and other MCP clients. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 1d | 6.2k |
| [Filesystem](https://github.com/mark3labs/mcp-filesystem-server) | File operations with configurable access controls. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟡 8mo | 672 |
| [Muvon/octocode](https://github.com/Muvon/octocode) | Semantic code indexer with GraphRAG knowledge graph and MCP server. Tree-sitter AST parsing, ast-grep structural search, code signatures view. 13+ languages. Local-first, Apache 2.0. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 0d | 441 |
| [Node.js](https://github.com/hyperdrive-eng/mcp-nodejs-debugger) | Gives Cursor or Claude Code access to Node.js at runtime to help you debug. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🗄️ archived | 303 |
| [VSCode Devtools (Bifrost)](https://github.com/biegehydra/BifrostMCP) | Connect to VSCode IDE and use semantic tools like `find_usages`. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 4mo | 223 |
| [Hoofy](https://github.com/HendryAvila/Hoofy) | Spec-driven development companion with persistent memory (SQLite + FTS5 + knowledge graph), adaptive change pipeline, and greenfield project pipeline with Clarity Gate. 32 MCP tools, single binary, zero dependencies. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟡 4mo | 15 |
| [preflight](https://github.com/preflight-dev/preflight) | 24-tool MCP server for Claude Code that scores prompts before execution, catches ambiguity, tracks correction patterns, and estimates token cost — reduces wasted tokens from vague prompts. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 4mo | 11 |
| [Filesystem](https://github.com/philgei/mcp_server_filesystem) | File operations with configurable access controls. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 5 |
| [wopee-mcp](https://github.com/Wopee-io/wopee-mcp) | Autonomous AI testing for web apps — generate test cases and user stories, dispatch test, analysis and AI-agent runs, and fetch artifacts and project status via Wopee.io. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 13d | 5 |
| [Phabricator](https://github.com/baba786/phabricator-mcp-server) | Interact with Phabricator API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | ❌ gone | — |

### Databases & Data

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) ✅ | Read-only database access with schema inspection. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) ✅ | Database interaction and business intelligence capabilities. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |

### Cloud, DevOps & Monitoring

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [AWS Knowledge Base Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server) ✅ | Retrieve information from the AWS Knowledge Base using the Bedrock Agent Runtime. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) ✅ | Retrieving and analyzing issues from Sentry.io. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [AWS](https://github.com/awslabs/mcp) ✅ | A suite of specialized MCP servers that bring AWS best practices directly to your development workflow. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 9.5k |
| [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) ✅ | Deploy, configure & interrogate your resources on the Cloudflare developer platform (e.g. Workers/KV/R2/D1). | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 4d | 4k |
| [ZenML](https://github.com/zenml-io/mcp-zenml) | Chat with your MLOps and LLMOps pipelines using the official ZenML MCP server. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 6d | 49 |
| [Raygun](https://github.com/MindscapeHQ/mcp-server-raygun) | Interact with your crash reporting and real using monitoring data on your Raygun account. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 5mo | 21 |
| [stackql](https://github.com/stackql/stackql) | SQL for cloud APIs. Query AWS, GCP, Azure and dozens of other providers with SQL. Includes an MCP server for agent access. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 2d | 874 |

### Web, Search & Browser

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) ✅ | Browser automation and web scraping. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) ✅ | Web and local search using Brave's Search API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) ✅ | Web content fetching and conversion for efficient LLM usage. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Playwright](https://github.com/microsoft/playwright-mcp) ✅ | Provides browser automation capabilities using Playwright. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 9d | 35.8k |
| [Youtube](https://github.com/anaisbetts/mcp-youtube) | Uses `yt-dlp` to download subtitles from YouTube. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 6w | 536 |
| [newsmcp](https://github.com/pranciskus/newsmcp) | Real-time world news for AI agents — events clustered from hundreds of sources, classified by 12 topics and 30+ geographic regions, ranked by importance. Free, no API key required. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 5mo | 65 |
| [Kagi](https://github.com/ac3xx/mcp-servers-kagi) | A Model Context Protocol server implementation for Kagi's API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 45 |
| [Exa.ai](https://github.com/theishangoswami/exa-mcp-server) | Use the Exa AI Search API for web searches. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 6 |
| [Find MCP](https://github.com/agentage/find-mcp) | Discover MCP servers by searching 17,000+ entries synced from the official MCP registry, via remote streamable HTTP or stdio. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 2d | 4 |
| [BGPT MCP](https://github.com/connerlambden/bgpt-mcp) | Search scientific papers and get structured experimental data from full-text studies. Remote MCP server with free tier. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | ❌ gone | — |
| [Naver Search MCP](https://github.com/uju777/mcp-server-naver-search) | Naver Shopping, Cafe, News search for Korean users. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 6mo | 0 |
| [Helium MCP](https://github.com/connerlambden/helium-mcp) | News search with per-outlet bias scores (37 dimensions, 216 sources), balanced multi-source synthesis, live equity/ETF/crypto quotes, and ML options pricing. Remote streamable HTTP, 9 tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | ❌ gone | — |
| [StackScan](https://github.com/stackscan/stackscan-mcp) | Looks up the technologies on any domain and the company behind it, and reports how many sites run a given technology and where. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 0d | 0 |

### Productivity, Docs & Knowledge

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [MarkItDown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) ✅ | Lightweight STDIO and SSE MCP server for calling MarkItDown. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 5d | 171.1k |
| [Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) ✅ | File access and search capabilities for Google Drive. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | Interact with Obsidian. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 2mo | 4.2k |
| [Taskade MCP](https://github.com/taskade/mcp) ✅ | Official Taskade MCP server with 50+ tools for managing workspaces, projects, tasks, custom AI agents, knowledge bases, and workflow automations. Includes OpenAPI-to-MCP codegen. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 5d | 161 |
| [open-mcp-apps](https://github.com/2nd1st/open-mcp-apps) | MCP Apps engine where the AI builds interactive UI apps — todo boards, habit trackers, dashboards — that persist across conversations, backed by data collections. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 0d | 0 |

### Communication & Social

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) ✅ | Channel management and messaging capabilities. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [WhatsApp](https://github.com/lharries/whatsapp-mcp) | Search your personal Whatsapp messages, search your contacts and send messages to either individuals or groups. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🔴 1y | 6.1k |
| [posteverywhere/mcp](https://github.com/posteverywhere/mcp) | Schedule and publish to Instagram, TikTok, YouTube, LinkedIn, Facebook, X, Threads, Pinterest, Bluesky, Discord, and Telegram from natural language. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 10d | 2 |
| [SocialRouter](https://github.com/socialrouter/mcp) | Unified API to fetch social media data across LinkedIn, Instagram, X, Reddit, TikTok, YouTube, and more, with automatic provider failover. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 0 |
| [sms-florin-mcp](https://github.com/flovoice53-tech/sms-florin-mcp) | Rents a real UK phone number (physical SIM, not VoIP) and receives SMS/OTP codes, so an AI agent can complete signup/verification flows during testing without a personal number. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 0 |
| [agent-identity-mcp](https://github.com/flovoice53-tech/agent-identity-mcp) | Gives an AI agent a disposable email address and a real UK phone number, so it can complete a signup/verification flow end to end during testing. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 0 |

### Commerce, Ads & Business

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Coupang MCP](https://github.com/uju777/coupang-mcp) | Korean e-commerce (Coupang) product search with Rocket Delivery filtering. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 3mo | 17 |
| [Frihet](https://github.com/Frihet-io/frihet-mcp) | AI-native business management with 31 tools for invoicing, expenses, clients, products, quotes, and tax compliance (VeriFactu). Multi-currency, OCR, and Stripe Connect. Supports stdio and remote Streamable HTTP with OAuth 2.0. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 9 |
| [BuyWhere](https://github.com/BuyWhere/buywhere-mcp) | Real-time product search and price comparison for Singapore and Southeast Asia. 260K+ products from Lazada, Shopee, FairPrice, Courts. Remote via `mcp.buywhere.ai/mcp`. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 4d | 6 |
| [Toolradar MCP](https://github.com/Nadeus/toolradar-mcp) | Search, compare, and get pricing for 8,600+ software tools with verified data, editorial scores, G2/Capterra ratings, and real alternatives. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 4mo | 2 |
| [ProposalCraft](https://github.com/jabbawocky/proposalcraft) | Draft client proposals in your voice using your past winning proposals as style examples. Paste a brief, get a ready-to-send proposal. Includes analyze_brief, draft_proposal tools and 12 industry templates. Zero API key, fully local. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 6w | 2 |
| [recipe-commerce-mcp](https://github.com/teamsincetoday/recipe-commerce-mcp) | Extract ingredients, kitchen tools, and product recommendations from recipe content for affiliate marketing integration. Free tier (200 calls/day), remote on Cloudflare Workers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 3mo | 1 |
| [Agentic Ads](https://github.com/nicofains1/agentic-ads) | Affiliate marketing MCP server for contextual product recommendations with USDC commission payouts. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 3mo | 1 |
| [Cleo Skills MCP](https://github.com/Cleo-Labs-IA/skills_library) | Product-compliance MCP server exposing 45 production-grade compliance skills (cosmetics, food, electronics, toys, textiles, supplements, medical devices, customs, recalls, claims, sustainability) as MCP resources, prompts, and tools. `npx -y @cleo-labs/skills-mcp@latest`. MIT. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 7w | 1 |
| [podcast-commerce-mcp](https://github.com/teamsincetoday/podcast-commerce-mcp) | Extract affiliate-ready product mentions from podcast transcripts with brand recognition, confidence scoring, and commerce intelligence. Free tier (200 calls/day), remote on Cloudflare Workers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 3mo | 0 |
| [newsletter-commerce-mcp](https://github.com/teamsincetoday/newsletter-commerce-mcp) | Extract product recommendations and affiliate marketing opportunities from newsletter and email content. Free tier (200 calls/day), remote on Cloudflare Workers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 3mo | 0 |

### AI, Agents & Memory

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) ✅ | Knowledge graph-based persistent memory system. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [OpenAI](https://github.com/pierrebrunelle/mcp-server-openai) | Query OpenAI models directly from Claude. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 84 |
| [EGC](https://github.com/Fmarzochi/EGC) | Persistent cross-session memory MCP server for 13+ AI coding tools. SQLite-backed state survives context resets and keeps Claude Code, Cursor, Gemini CLI, Codex, and more in sync. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 0d | 42 |
| [WritBase](https://github.com/Writbase/writbase) | MCP-native task management for AI agent fleets with multi-agent permissions, delegation safety, and full provenance. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 4mo | 8 |
| [Nucleus MCP](https://github.com/eidetic-works/nucleus-mcp) | 114 MCP tools for persistent memory, execution verification, governance, and compliance. Local-first. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 1d | 4 |
| [PraisonAI](https://github.com/MervinPraison/praisonai-mcp) | AI Agents framework with 64+ built-in MCP tools for search, memory, workflows, code execution, and file operations. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 6mo | 1 |
| [Skillselion](https://github.com/skillselion/skillselion-mcp) | Loads community agent skills on demand, materializing a matching SKILL.md and its bundled files into the session, and can merge the top matches into one provenance-tagged digest. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟢 0d | 0 |
| [SandBase CLI](https://github.com/sandbaseai/cli) | Local MCP bridge that connects 25 AI clients to 2,000+ models and APIs through six MCP tools. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 0 |

### Media & 3D

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Blender](https://github.com/ahujasid/blender-mcp) | Interact with and control Blender using prompt assisted 3D modeling, scene creation, and manipulation. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 25.4k |
| [Funplay MCP for Unity](https://github.com/FunplayAI/funplay-unity-mcp) | Unity Editor MCP server with execute_code, play mode automation, screenshots, input simulation, prompts, and resources. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="18" alt="C#" title="C#"> | 🟢 6d | 204 |
| [VideoOverlayKit](https://github.com/alichherawalla/video-overlay-kit) | Render 4-6s animated b-roll overlay videos for short-form social (LinkedIn, IG Reels, YouTube Shorts, TikTok) and landscape video. Paste a script, the AI writes the scene spec and renders the mp4. Free, MIT, runs locally. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 7w | 1 |
| [VAP-MCP](https://github.com/elestirelbilinc-sketch/vap-showcase) | MCP server for AI media generation (images, videos, music) with deterministic cost control using reserve-burn-refund billing. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 4w | 1 |
| [Magic Hour](https://github.com/magichourhq/magic-hour-mcp) | Hosted first-party server that lets agents generate and edit video, images, and audio through Magic Hour's API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 0 |

### Finance & Crypto

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [RustChain MCP](https://github.com/Scottcjn/rustchain-mcp) | MCP server for the RustChain blockchain and BoTTube video platform. AI agent tools for mining, wallet management, bounty hunting, and video publishing. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 1d | 102 |

### Other

| Server | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) ✅ | Location services, directions, and place details. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 89.2k |
| [Stdio](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/stdio.py) ✅ | Communicate with an MCP client through standard input/output streams. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 23.9k |
| [Websocket](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/websocket.py) ✅ | WebSocket server transport. This is an ASGI application, suitable to be used with a framework like Starlette and a server like Hypercorn. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 23.9k |
| [AppleScript](https://github.com/joshrutkowski/applescript-mcp) | Implements interaction with macOS via AppleScript. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 393 |
| [Make](https://github.com/integromat/make-mcp-server) | Turn Make scenarios into callable tools for AI assistants. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 7w | 165 |
| [domain-mcp](https://github.com/joachimBrindeau/domain-mcp) | MCP server to search, register, and manage domains (availability, DNS, WHOIS) via Dynadot API. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 10d | 11 |
| [SheetsData](https://github.com/octoco-ltd/sheetsdata-mcp) | Instant access to electronic component datasheets for AI agents — specs, pinouts, package info, absolute max ratings extracted from manufacturer PDFs on demand. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🟡 3mo | 9 |
| [Live Tennis API](https://github.com/livetennisapi/livetennisapi-mcp) | Live tennis scores, fixtures, players, rankings, H2H and model win probability for AI agents across ATP, WTA, Challenger, ITF and junior tours. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 0 |

## Clients

| Client | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [n8n](https://github.com/nerding-io/n8n-nodes-mcp) | interact with Model Context Protocol (MCP) servers in your n8n workflows. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟡 7mo | 3k |
| [eechat](https://github.com/Lucassssss/eechat) | An open-source, cross-platform desktop application that seamlessly connects with full support for MCP, across Linux, macOS, and Windows. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🔴 1y | 345 |
| [Off Grid AI Desktop](https://github.com/off-grid-ai/off-grid-ai-desktop) | Local-first macOS app that runs a full AI suite on-device (LLM chat, image generation, transcription, memory/RAG) and connects to MCP servers as a client, with no account or telemetry. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 3d | 52 |

## SDKs

### Official

Core SDKs maintained by the MCP organization.

| SDK | Notes | Activity | ⭐ |
|---|---|:--:|--:|
| [Python](https://github.com/modelcontextprotocol/python-sdk) | Reference implementation, most widely used. | 🟢 0d | 23.9k |
| [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk) | Reference implementation for Node.js/browser. | 🟢 0d | 13.1k |
| [Rust (rmcp)](https://github.com/modelcontextprotocol/rust-sdk) | Official Rust SDK with proc macros. | 🟢 3d | 3.7k |
| [Go](https://github.com/modelcontextprotocol/go-sdk) | Official Go SDK, maintained with Google. | 🟢 0d | 4.9k |
| [Kotlin](https://github.com/modelcontextprotocol/kotlin-sdk) | Multiplatform (JVM, Wasm, iOS). | 🟢 0d | 1.4k |
| [C#](https://github.com/modelcontextprotocol/csharp-sdk) | ASP.NET Core, Azure Functions integration. | 🟢 0d | 4.4k |
| [Java](https://github.com/modelcontextprotocol/java-sdk) | Spring Boot integration. | 🟢 3w | 3.6k |

### Community

| SDK | Notes | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Fast MCP](https://github.com/jlowin/fastmcp) | High-level Python framework used by ~70% of Python MCP servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 27k |
| [tower-mcp](https://github.com/joshrotenberg/tower-mcp) | Tower-native implementation with middleware composition via `.layer()`. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 1d | 8 |
| [rust-mcp-sdk](https://github.com/rust-mcp-stack/rust-mcp-sdk) | Async SDK with proc macros, hyper-based HTTP transport. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 7d | 188 |
| [pmcp](https://github.com/paiml/rust-mcp-sdk) | SIMD-optimized JSON-RPC parsing, performance-focused. | <picture><source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/rust/white"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="18" alt="Rust" title="Rust"></picture> | 🟢 0d | 53 |
| [mcp-go](https://github.com/mark3labs/mcp-go) | Community SDK that inspired the official implementation. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 5d | 9k |
| [go-mcp](https://github.com/ThinkInAIXYZ/go-mcp) | Idiomatic Go API with strong typing. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 5w | 672 |

## Tools

Tooling that helps you **build, test, secure, deploy or manage** MCP servers.

| Tool | Description | Lang | Activity | ⭐ |
|---|---|---|:--:|--:|
| [Server inspector](https://github.com/modelcontextprotocol/inspector) ✅ | Visual testing tool for MCP servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 1d | 10.6k |
| [MCP Agent](https://github.com/lastmile-ai/mcp-agent) | Build effective agents with Model Context Protocol using simple, composable patterns. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 6mo | 8.5k |
| [ToolHive](https://github.com/StacklokLabs/toolhive) | A lightweight utility designed to simplify the deployment and management of MCP servers, ensuring ease of use, consistency, and security through containerization. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="18" alt="Go" title="Go"> | 🟢 0d | 2k |
| [MCP Installer](https://github.com/anaisbetts/mcp-installer) | A server that installs other MCP servers for you. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="18" alt="JavaScript" title="JavaScript"> | 🔴 1y | 1.5k |
| [Fleur MCP](https://github.com/fleuristes/fleur) | A desktop app marketplace for Claude Desktop. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🔴 1y | 534 |
| [MCP get](https://github.com/michaellatman/mcp-get) | A command-line tool for installing and managing Model Context Protocol (MCP) servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🗄️ archived | 507 |
| [Langchain](https://github.com/rectalogic/langchain-mcp) | Support for LangChain. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 205 |
| [Roundtable](https://github.com/askbudi/roundtable) | Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 10mo | 121 |
| [Dify plugin](https://github.com/hjlarry/dify-plugin-mcp_server) | Change a Dify app to a mcp server. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🔴 1y | 66 |
| [ToolRegistry](https://github.com/Oaklight/ToolRegistry) | A PyPI package that simplifies tool integration by streamlining OpenAI client tool calls and managing native Python functions and MCP servers, offering both async and sync interfaces. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 10d | 59 |
| [MCP Trust Kit](https://github.com/aak204/MCP-Trust-Kit) | Deterministic CI scanner and surface-risk scoring for MCP servers. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 3mo | 24 |
| [mcpbr](https://github.com/greynewell/mcpbr) | Benchmark runner for evaluating MCP server performance and agentic capabilities. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 3mo | 10 |
| [mcp-harness](https://github.com/gabry-ts/mcp-harness) | In-memory test harness for MCP servers in TypeScript — supertest for MCP. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 5w | 2 |
| [Agent Guard](https://github.com/Aveerayy/agent-guard) | MCP security scanner and runtime governance gateway for AI agents. Detects tool poisoning, prompt injection, typosquatting, hidden unicode, and schema abuse in MCP tool definitions. Also provides policy enforcement, rate limiting, and kill switch. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟡 3mo | 1 |
| [MCP Orchestrator](https://github.com/curtismager20/magertron-mcpm) | Kubernetes-native MCP control plane. Deploy MCP servers as pods in your own cluster, govern access with policy, audit every action. | — | 🟢 0d | 1 |
| [MCP Server Tester](https://github.com/ytkoka/mcp-tester) | Web-based inspector for remote MCP servers with token-usage estimation, latency measurement, tool-definition quality scoring, and side-by-side server comparison. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 5d | 0 |
| [MCP Debug Proxy](https://github.com/ytkoka/mcp-debug-proxy) | Logging reverse proxy that makes MCP and OAuth traffic between a client and a remote server observable, with a live web UI. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 0 |
| [MyMCPTools](https://github.com/shibley/mymcptools) | Tracks the health of remote MCP servers across a catalog of 2,467 entries: hourly handshake probes, uptime history, incident timelines, and tool-schema drift detection against the previous probe. Queryable over HTTP or as an MCP server itself. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="18" alt="TypeScript" title="TypeScript"> | 🟢 0d | 0 |
| [mcp-daemon-diet](https://github.com/tonydzi/mcp-daemon-diet) | Run one shared MCP server per machine instead of a stdio copy per client session, with autostart templates for Windows, macOS and Linux and a watchdog that restarts only on a proven-dead process. | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18" alt="Python" title="Python"> | 🟢 0d | 0 |
