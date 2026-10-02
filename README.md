# Awesome MCP

![Awesome](https://raw.githubusercontent.com/abordage/schemas/main/badges/awesome.svg)
[![Last update](https://img.shields.io/github/last-commit/abordage/awesome-mcp?label=last%20update)](README.md)
![Repositories](https://img.shields.io/badge/repositories-1,314-06b6d4)
![Total Stars](https://img.shields.io/badge/total%20stars-1,178,612-gold)
[![License](https://img.shields.io/github/license/abordage/awesome-mcp)](LICENSE)

**Automated. Curated. Ranked.**

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers, clients, and frameworks — the open standard for connecting AI assistants to external data sources and tools. This awesome list is automatically maintained with daily GitHub API updates. Projects are re-ranked daily based on current activity metrics.

**Daily process:** Merge community PRs → Scan repos → Filter stale projects → Recalculate scores → Rebuild list

- [AI Agents](#ai-agents)
  - [Code Assistants](#code-assistants)
  - [Human-in-the-Loop](#human-in-the-loop)
  - [Multi-Agent](#multi-agent)
  - [Reasoning & Prompts](#reasoning--prompts)
- [AI Memory & RAG](#ai-memory--rag)
  - [Memory](#memory)
  - [RAG](#rag)
- [AI Platforms](#ai-platforms)
- [Aggregators & Gateways](#aggregators--gateways)
  - [Aggregators](#aggregators)
  - [Gateways & Proxies](#gateways--proxies)
  - [Platforms & Registries](#platforms--registries)
- [Browser Automation](#browser-automation)
  - [AI Automation](#ai-automation)
  - [Browser Tools](#browser-tools)
  - [Cloud Services](#cloud-services)
  - [DevTools](#devtools)
  - [Playwright](#playwright)
- [CLI Tools](#cli-tools)
- [CRM & ERP](#crm--erp)
- [Cloud & Infrastructure](#cloud--infrastructure)
  - [AWS](#aws)
  - [Cloud Platforms](#cloud-platforms)
  - [Kubernetes](#kubernetes)
  - [Virtualization & IaC](#virtualization--iac)
- [Communication & Messaging](#communication--messaging)
  - [Apple Messages](#apple-messages)
  - [Email](#email)
  - [Messengers](#messengers)
  - [Notifications](#notifications)
  - [Team Chat](#team-chat)
  - [Voice & Telephony](#voice--telephony)
- [Data & Analytics](#data--analytics)
  - [AI/ML Platforms](#aiml-platforms)
  - [Data APIs](#data-apis)
  - [Data Exploration](#data-exploration)
  - [Data Platforms](#data-platforms)
  - [Jupyter & Notebooks](#jupyter--notebooks)
  - [Visualization](#visualization)
- [Databases](#databases)
  - [Analytics & Warehouses](#analytics--warehouses)
  - [Cache & Key-Value](#cache--key-value)
  - [Cloud Platforms](#cloud-platforms)
  - [Graph Databases](#graph-databases)
  - [Multi-Database Tools](#multi-database-tools)
  - [NoSQL & Document](#nosql--document)
  - [SQL Databases](#sql-databases)
  - [Search Engines](#search-engines)
  - [Spreadsheets & No-Code](#spreadsheets--no-code)
  - [Streaming & Messaging](#streaming--messaging)
  - [Time-Series & Metrics](#time-series--metrics)
  - [Vector Databases](#vector-databases)
- [Developer Tools](#developer-tools)
  - [API Tools](#api-tools)
  - [CI/CD & DevOps](#cicd--devops)
  - [Code Analysis](#code-analysis)
  - [Debuggers](#debuggers)
  - [Design & UI](#design--ui)
  - [Diagrams](#diagrams)
  - [Documentation](#documentation)
  - [IDE & Editors](#ide--editors)
  - [MCP SDKs](#mcp-sdks)
  - [Mobile Development](#mobile-development)
  - [OpenAPI](#openapi)
  - [Package Managers](#package-managers)
  - [Robotics & Automation](#robotics--automation)
  - [Task Management](#task-management)
  - [Testing & QA](#testing--qa)
  - [Utilities](#utilities)
  - [Version Control](#version-control)
- [Embedded & IoT](#embedded--iot)
- [File Systems & Storage](#file-systems--storage)
- [Finance](#finance)
  - [Accounting & Budgeting](#accounting--budgeting)
  - [Crypto & Blockchain](#crypto--blockchain)
  - [Payments & Banking](#payments--banking)
  - [Stock Data & Analytics](#stock-data--analytics)
  - [Trading & Exchanges](#trading--exchanges)
- [Frameworks & SDKs](#frameworks--sdks)
- [Gaming](#gaming)
- [Healthcare & Bioinformatics](#healthcare--bioinformatics)
- [LLM Bridges](#llm-bridges)
- [Location & Maps](#location--maps)
  - [GIS](#gis)
  - [IP Geolocation](#ip-geolocation)
  - [Maps & Navigation](#maps--navigation)
  - [Weather](#weather)
- [MCP Clients](#mcp-clients)
- [Marketing & Analytics](#marketing--analytics)
- [Media Processing](#media-processing)
  - [3D & Animation](#3d--animation)
  - [Audio & Music](#audio--music)
  - [Image Generation](#image-generation)
  - [Image Processing](#image-processing)
  - [Media Services](#media-services)
  - [Video](#video)
- [Monitoring & Observability](#monitoring--observability)
- [Productivity](#productivity)
  - [Atlassian](#atlassian)
  - [Collaboration](#collaboration)
  - [Documents](#documents)
  - [Google Workspace](#google-workspace)
  - [Helpdesk & Support](#helpdesk--support)
  - [Learning & Flashcards](#learning--flashcards)
  - [Microsoft 365](#microsoft-365)
  - [Note-taking & Docs](#note-taking--docs)
  - [Notion](#notion)
  - [Obsidian](#obsidian)
  - [Project Management](#project-management)
  - [Tasks & Calendar](#tasks--calendar)
  - [Wiki & Collaboration](#wiki--collaboration)
- [Research & Science](#research--science)
- [Sandboxing & Execution](#sandboxing--execution)
- [Search & Extraction](#search--extraction)
  - [Academic Research](#academic-research)
  - [Data APIs](#data-apis)
  - [News & Content](#news--content)
  - [Web Search Engines](#web-search-engines)
- [Security](#security)
  - [Identity & Access](#identity--access)
  - [MCP Security](#mcp-security)
  - [Network & Firewall](#network--firewall)
  - [Pentesting & OSINT](#pentesting--osint)
  - [Reverse Engineering](#reverse-engineering)
  - [SIEM & SecOps](#siem--secops)
- [Social Media](#social-media)
- [Sports](#sports)
- [Text-to-Speech](#text-to-speech)
- [Translation](#translation)
- [Travel & Transport](#travel--transport)
- [Web Scraping](#web-scraping)


## AI Agents

### Code Assistants

- [oraios/serena](https://github.com/oraios/serena) — Semantic code retrieval and editing toolkit ☆`29,941`
- [zilliztech/claude-context](https://github.com/zilliztech/claude-context) — Code search for Claude Code agents ☆`12,584`
- [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) — Code graph indexing for AI context ☆`4,242`
- [ezyang/codemcp](https://github.com/ezyang/codemcp) — Coding assistant MCP for Claude Desktop ☆`1,606`
- [ref-tools/ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp) — Reference tools for coding agents ☆`1,175`
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) — MCP implementation of Claude Code capabilities and more ☆`305`
- [stippi/code-assistant](https://github.com/stippi/code-assistant) — LLM-powered autonomous coding assistant ☆`182`
- [lamemind/mcp-server-multiverse](https://github.com/lamemind/mcp-server-multiverse) — MCP server for multiverse context management ☆`81`
- [contextstream/mcp-server](https://github.com/contextstream/mcp-server) — Shared project context for AI coding agents across MCP clients ☆`43`
- [wende/cicada](https://github.com/wende/cicada) — AI Coders search blindly. Be their guide. ☆`41`
- [gabrielmaialva33/winx-code-agent](https://github.com/gabrielmaialva33/winx-code-agent) — MCP-powered code agent for development ☆`36`
- [josephsenior/Grinta-Coding-Agent](https://github.com/josephsenior/Grinta-Coding-Agent) — Local-first resilient terminal coding agent with MCP ☆`31`
- [x51xxx/codex-mcp-tool](https://github.com/x51xxx/codex-mcp-tool) — Claude/Cursor to Codex CLI bridge with multi-turn sessions ☆`24`
- [VertexStudio/developer](https://github.com/VertexStudio/developer) — File editing, shell execution, screen capture ☆`21`
### Human-in-the-Loop

- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) — Interactive MCP server for human-in-the-loop AI ☆`352`
- [RapidataAI/human-use](https://github.com/RapidataAI/human-use) — Enable AI to ask anyone anything ☆`73`
- [gotohuman/gotohuman-mcp-server](https://github.com/gotohuman/gotohuman-mcp-server) — Human approvals for AI agentic workflows ☆`52`
- [nazar256/user-prompt-mcp](https://github.com/nazar256/user-prompt-mcp) — User input requests for Cursor ☆`21`
### Multi-Agent

- [rinadelph/Agent-MCP](https://github.com/rinadelph/Agent-MCP) — Multi-agent AI collaboration framework ☆`1,301`
- [roboticforce/sugar](https://github.com/roboticforce/sugar) — Local persistent memory, cross-session context, and optional tasks ☆`96`
### Reasoning & Prompts

- [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp) — Token optimization with caching and compression ☆`538`
- [PV-Bhat/vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server) — Mentor-like feedback tool preventing AI over-engineering ☆`502`
- [Rai220/think-mcp](https://github.com/Rai220/think-mcp) — MCP Server for reasoning ☆`107`
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) — MCP server for enhanced AI clarity and reasoning ☆`90`
- [YuChenSSR/multi-ai-advisor-mcp](https://github.com/YuChenSSR/multi-ai-advisor-mcp) — council of models for decision ☆`88`
- [nikkoxgonzales/crash-mcp](https://github.com/nikkoxgonzales/crash-mcp) — Structured reasoning with step validation ☆`72`
- [gwbischof/free-will-mcp](https://github.com/gwbischof/free-will-mcp) — Experimental AI self-prompting MCP server ☆`37`
- [aquarius-wing/actor-critic-thinking-mcp](https://github.com/aquarius-wing/actor-critic-thinking-mcp) — Dual-perspective thinking analysis server ☆`32`
- [ejentum/ejentum-mcp](https://github.com/ejentum/ejentum-mcp) — Agent loop with reasoning, code, memory, and anti-deception ☆`16`
- [vasayxtx/mcp-prompt-engine](https://github.com/vasayxtx/mcp-prompt-engine) — MCP Prompt Engine ☆`18`
- [abhinav-mangla/inner-monologue-mcp](https://github.com/abhinav-mangla/inner-monologue-mcp) — Inner Monologue MCP Server ☆`17`
- [abhinav-mangla/think-tool-mcp](https://github.com/abhinav-mangla/think-tool-mcp) — MCP Think Tool Server ☆`16`
## AI Memory & RAG

### Memory

- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) — Hindsight: Agent Memory That Learns ☆`44,420`
- [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) — AI conversations that remember context ☆`4,075`
- [agentic-box/memora](https://github.com/agentic-box/memora) — Persistent shared memories in SQLite ☆`729`
- [MaxFreedomPollard/Compartment](https://github.com/MaxFreedomPollard/Compartment) — Offline AEAD-encrypted vector memory without network ☆`578`
- [Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas) — LLM Wiki memory for team chat (Slack, Discord, Teams) ☆`450`
- [gannonh/memento-mcp](https://github.com/gannonh/memento-mcp) — Memento MCP: A Knowledge Graph Memory System for LLMs ☆`425`
- [CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) — MCP server for knowledge graph memory ☆`353`
- [pi22by7/In-Memoria](https://github.com/pi22by7/In-Memoria) — Persistent Intelligence Infrastructure for AI Agents ☆`174`
- [jean-technologies/jean-memory](https://github.com/jean-technologies/jean-memory) — AI memory with mem0 and graphiti ☆`172`
- [redleaves/context-keeper](https://github.com/redleaves/context-keeper) — Intelligent memory and context for AI agents ☆`155`
- [DrDroidLab/open-index](https://github.com/DrDroidLab/open-index) — Structured context graphs with hybrid search and writes ☆`111`
- [ukkit/memcord](https://github.com/ukkit/memcord) — MCP server for memory and context management ☆`74`
- [knowall-ai/mcp-reverie](https://github.com/knowall-ai/mcp-reverie) — Memory management using Neo4j graphs ☆`70`
- [peless/claude-thread-continuity](https://github.com/peless/claude-thread-continuity) — Save and restore project context ☆`65`
- [hungryrobot1/MCP-PIF](https://github.com/hungryrobot1/MCP-PIF) — Personal intelligence framework in Haskell ☆`57`
- [Yuchen20/Memory-Plus](https://github.com/Yuchen20/Memory-Plus) — Enhanced persistent memory management ☆`56`
- [mnemoverse/mcp-memory-server](https://github.com/mnemoverse/mcp-memory-server) — Hosted memory that re-ranks recall by reported outcomes ☆`25`
- [skydeckai/mcp-server-rememberizer](https://github.com/skydeckai/mcp-server-rememberizer) — An MCP Server to enable global access to Rememberizer ☆`36`
- [JamesANZ/memory-mcp](https://github.com/JamesANZ/memory-mcp) — Shared memory store and retrieval for multiple LLMs ☆`21`
- [unibaseio/membase-mcp](https://github.com/unibaseio/membase-mcp) — Decentralized memory layer for AI agents ☆`24`
- [hubertciebiada/context-crystallizer](https://github.com/hubertciebiada/context-crystallizer) — Large repos into AI-consumable knowledge for agents ☆`17`
- [ssmirnovpro/extended-memory-mcp](https://github.com/ssmirnovpro/extended-memory-mcp) — Cross-session persistent memory for Claude Desktop ☆`18`
### RAG

- [apecloud/ApeRAG](https://github.com/apecloud/ApeRAG) — Production GraphRAG with multi-modal ☆`1,318`
- [Minima-AI-Inc/minima](https://github.com/Minima-AI-Inc/minima) — On-premises conversational RAG with configurable containers ☆`1,049`
- [GreatScottyMac/context-portal](https://github.com/GreatScottyMac/context-portal) — Memory bank MCP with knowledge graph ☆`767`
- [shinpr/mcp-local-rag](https://github.com/shinpr/mcp-local-rag) — MCP server for local RAG operations ☆`405`
- [graphlit/graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) — Model Context Protocol (MCP) Server for Graphlit Platform ☆`379`
- [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) — MCP server for RAG document retrieval ☆`265`
- [needle-ai/needle-mcp](https://github.com/needle-ai/needle-mcp) — Needle MCP Server for easy RAG.Long-term memory for LLMs. ☆`103`
- [ragieai/ragie-mcp-server](https://github.com/ragieai/ragie-mcp-server) — Ragie Model Context Protocol Server ☆`91`
- [pinecone-io/assistant-mcp](https://github.com/pinecone-io/assistant-mcp) — Pinecone Assistant MCP server ☆`45`
- [vectara/vectara-mcp](https://github.com/vectara/vectara-mcp) — Open source MCP server for Vectara ☆`29`
- [nonatofabio/local_faiss_mcp](https://github.com/nonatofabio/local_faiss_mcp) — Local FAISS MCP - semantic search for Claude/Copilot ☆`34`
- [agentset-ai/mcp-server](https://github.com/agentset-ai/mcp-server) — Agentset MCP Server - Build RAG with Agentic superpowers ☆`30`
- [renl/mcp-rag-local](https://github.com/renl/mcp-rag-local) — Local RAG with Ollama embeddings and ChromaDB ☆`18`
## AI Platforms

- [Kiln-AI/Kiln](https://github.com/Kiln-AI/Kiln) — Build AI systems with Evals, RAG, Agents, fine-tuning ☆`5,150`
- [paiml/paiml-mcp-agent-toolkit](https://github.com/paiml/paiml-mcp-agent-toolkit) — Pragmatic AI Labs toolkit for deterministic agents ☆`164`
- [TheRaLabs/legion-mcp](https://github.com/TheRaLabs/legion-mcp) — MCP server for Legion AI platform ☆`94`
- [PromptExecution/just-mcp](https://github.com/PromptExecution/just-mcp) — mcp server for just ☆`60`
- [atlanhq/agent-toolkit](https://github.com/atlanhq/agent-toolkit) — Atlan AI Agent Toolkit ☆`40`
- [Mitek99/deepview-mcp](https://github.com/Mitek99/deepview-mcp) — MCP server for DeepView AI analysis ☆`66`
- [StitchAI/stitch-ai-mcp](https://github.com/StitchAI/stitch-ai-mcp) — Decentralized Knowledge Hub for AI ☆`39`
- [DumplingAI/mcp-server-dumplingai](https://github.com/DumplingAI/mcp-server-dumplingai) — MCP (Model Context Protocol) server for Dumpling AI ☆`31`
- [PV-Bhat/gemsuite-mcp](https://github.com/PV-Bhat/gemsuite-mcp) — MCP server for GemSuite tools ☆`30`
- [sequa-ai/sequa-mcp](https://github.com/sequa-ai/sequa-mcp) — MCP server for Sequa AI platform ☆`21`
## Aggregators & Gateways

### Aggregators

- [mindsdb/mindshub](https://github.com/mindsdb/mindshub) — Query Engine for AI Analytics - self-reasoning agents on live data ☆`39,778`
- [metatool-ai/metamcp](https://github.com/metatool-ai/metamcp) — MCP Aggregator, Orchestrator, Middleware, Gateway in one docker ☆`2,694`
- [mcpjungle/MCPJungle](https://github.com/mcpjungle/MCPJungle) — One place to manage & connect to all your MCP servers ☆`1,288`
- [1mcp-app/agent](https://github.com/1mcp-app/agent) — Unified MCP server aggregator ☆`510`
- [K-Dense-AI/claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp) — Claude Agent Skills vector search ☆`407`
- [OldJii/mcp-dock](https://github.com/OldJii/mcp-dock) — Desktop manager for 14 AI clients and 9200+ MCP servers ☆`233`
- [sitbon/magg](https://github.com/sitbon/magg) — Magg: The MCP Aggregator ☆`144`
- [wanaku-ai/wanaku](https://github.com/wanaku-ai/wanaku) — Wanaku Governed Action Proxy for AI Agents ☆`134`
- [badkk/awesome-crypto-mcp-servers](https://github.com/badkk/awesome-crypto-mcp-servers) — A collection of crypto MCP servers. ☆`145`
- [yylo-dev/roundtable](https://github.com/yylo-dev/roundtable) — Zero-config MCP unifying multiple AI coding assistants ☆`125`
- [portel-dev/ncp](https://github.com/portel-dev/ncp) — Natural Context Provider with smart MCP tool loading ☆`100`
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) — GitLab, Jira, Confluence, YouTube ☆`107`
- [VeriTeknik/pluggedin-mcp](https://github.com/VeriTeknik/pluggedin-mcp) — Plugged.in MCP Server manages all your other MCPs in one MCP. ☆`52`
- [bh-rat/context-awesome](https://github.com/bh-rat/context-awesome) — awesome-lists now available as CLI & MCP server for your agent. ☆`59`
- [hamidra/yamcp](https://github.com/hamidra/yamcp) — Local MCP workspace organization ☆`66`
- [waystation-ai/mcp](https://github.com/waystation-ai/mcp) — No-code secure MCP integration hub ☆`63`
- [gotoolkits/mcp-difyworkflow-server](https://github.com/gotoolkits/mcp-difyworkflow-server) — MCP server for Dify workflow invocation ☆`62`
- [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) — MCP server aggregator and router ☆`40`
- [membranehq/mcp-server](https://github.com/membranehq/mcp-server) — MCP Server for Membrane ☆`37`
- [nazar256/combine-mcp](https://github.com/nazar256/combine-mcp) — MCP aggregator combining multiple servers into one interface ☆`35`
- [wojtyniak/mcp-mcp](https://github.com/wojtyniak/mcp-mcp) — Meta-MCP for tool discovery and provisioning ☆`23`
- [agree-able/room-mcp](https://github.com/agree-able/room-mcp) — Coordinate agents using rooms ☆`23`
### Gateways & Proxies

- [apache/apisix](https://github.com/apache/apisix) — The Cloud-Native API Gateway and AI Gateway ☆`17,187`
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) — A bridge between Streamable HTTP and stdio MCP transports ☆`2,767`
- [stacklok/toolhive](https://github.com/stacklok/toolhive) — Runtime and gateway for deploying MCP servers in containers ☆`2,230`
- [tbxark/mcp-proxy](https://github.com/tbxark/mcp-proxy) — Aggregate multiple MCP servers via HTTP ☆`735`
- [HelpCode-ai/anythingmcp](https://github.com/HelpCode-ai/anythingmcp) — Self-hosted gateway from REST, SOAP, GraphQL, and SQL ☆`698`
- [smart-mcp-proxy/mcpproxy-go](https://github.com/smart-mcp-proxy/mcpproxy-go) — Supercharge AI Agents, Safely ☆`381`
- [ssut/Remote-MCP](https://github.com/ssut/Remote-MCP) — Type-safe solution for remote MCP communication ☆`209`
- [sxhxliang/mcp-access-point](https://github.com/sxhxliang/mcp-access-point) — Convert any web server to MCP instantly ☆`185`
- [toolprint/hypertool-mcp](https://github.com/toolprint/hypertool-mcp) — Expose tools based on Agent Persona ☆`158`
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy) — Unified MCP proxy managing multiple MCPs ☆`135`
- [universal-mcp/universal-mcp](https://github.com/universal-mcp/universal-mcp) — Middleware for API applications ☆`26`
- [pyroprompts/mcp-stdio-to-streamable-http-adapter](https://github.com/pyroprompts/mcp-stdio-to-streamable-http-adapter) — STDIO to Streamable HTTP proxy ☆`27`
- [webrix-ai/secure-mcp-gateway](https://github.com/webrix-ai/secure-mcp-gateway) — Secure OAuth gateway for MCP authentication ☆`23`
- [nick1udwig/ws-mcp](https://github.com/nick1udwig/ws-mcp) — MCP server with WebSocket transport ☆`21`
### Platforms & Registries

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) — Enterprise AI guardrails, registry, gateway, and orchestrator ☆`4,340`
- [metorial/metorial](https://github.com/metorial/metorial) — Connect any AI model to 1200+ integrations (MCP, CLI, API) ☆`3,362`
- [chatmcp/mcpso](https://github.com/chatmcp/mcpso) — directory for Awesome MCP Servers ☆`2,109`
- [julien040/anyquery](https://github.com/julien040/anyquery) — SQL queries for GitHub, Notion, +40 more ☆`1,779`
- [jaw9c/awesome-remote-mcp-servers](https://github.com/jaw9c/awesome-remote-mcp-servers) — Remote MCP Servers ☆`1,126`
- [boltmcp/boltmcp](https://github.com/boltmcp/boltmcp) — Open standard and registry for converting web APIs into MCP servers ☆`371`
- [milisp/mcp-linker](https://github.com/milisp/mcp-linker) — Sync MCP configs across clients ☆`328`
- [liuyoshio/mcp-compass](https://github.com/liuyoshio/mcp-compass) — MCP discovery and recommendation ☆`244`
- [juspay/neurolink](https://github.com/juspay/neurolink) — Universal AI platform with MCP and multi-provider support ☆`143`
- [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) — Make MCP Server ☆`173`
- [Jeamee/MCPHub-Desktop](https://github.com/Jeamee/MCPHub-Desktop) — Desktop APP for Discover and Install MCP Servers ☆`150`
- [rust-mcp-stack/mcp-discovery](https://github.com/rust-mcp-stack/mcp-discovery) — CLI for discovering MCP server capabilities ☆`86`
- [matthewdcage/cursor-mcp-installer](https://github.com/matthewdcage/cursor-mcp-installer) — Install MCPs in Cursor from git URL ☆`77`
- [useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp) — Access 130+ SaaS integrations via ActionKit ☆`48`
- [VeyraX/veyrax-mcp](https://github.com/VeyraX/veyrax-mcp) — VeyraX unified tool access via single MCP ☆`49`
- [Data-Everything/mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates) — Docker, Kubernetes, CLI, and HTTP MCP templates ☆`22`
## Browser Automation

### AI Automation

- [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp) — AI browser agent, ships as an MCP server and a web UI ☆`31,744`
- [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) — Automate browser based workflows with AI ☆`23,118`
- [nottelabs/notte](https://github.com/nottelabs/notte) — Framework to build web agents ☆`2,009`
- [imprvhub/mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent) — MCP server for autonomous browser automation with Claude ☆`41`
- [desplega-ai/qa-use](https://github.com/desplega-ai/qa-use) — Agent-first E2E testing CLI ☆`27`
### Browser Tools

- [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) — Browser control for AI applications ☆`7,151`
- [kontext-security/browser-use-mcp-server](https://github.com/kontext-security/browser-use-mcp-server) — Browse the web, directly from Cursor etc. ☆`847`
- [onllm-dev/onUI](https://github.com/onllm-dev/onUI) — Annotation-first UI pair programming in the browser ☆`102`
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) — AI assistants interact with local browser ☆`55`
- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) — Rust-based browser automation MCP server ☆`41`
### Cloud Services

- [hyperbrowserai/mcp](https://github.com/hyperbrowserai/mcp) — A MCP server implementation for hyperbrowser ☆`790`
- [browserstack/mcp-server](https://github.com/browserstack/mcp-server) — BrowserStack's Official MCP Server ☆`151`
- [kernel/kernel-mcp-server](https://github.com/kernel/kernel-mcp-server) — Secure cloud-browser automation on Kernel ☆`37`
### DevTools

- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Chrome DevTools for coding agents ☆`52,862`
- [mozilla/firefox-devtools-mcp](https://github.com/mozilla/firefox-devtools-mcp) — MCP server for Firefox DevTools integration ☆`454`
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) — Browser control via extension for AI agents ☆`326`
### Playwright

- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — Playwright MCP server ☆`37,749`
- [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) — MCP server for Playwright browser testing ☆`5,661`
- [VikashLoomba/MCP-Server-Playwright](https://github.com/VikashLoomba/MCP-Server-Playwright) — MCP server for browser automation using Playwright ☆`299`
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) — Enhanced Playwright browser automation ☆`189`
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) — Azure OpenAI with Playwright browser control ☆`35`
## CLI Tools

- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) — Terminal control, file search, diff editing ☆`9,873`
- [IBM/mcp-cli](https://github.com/IBM/mcp-cli) — Feature-rich CLI for interacting with MCP servers ☆`2,025`
- [classfang/ssh-mcp-server](https://github.com/classfang/ssh-mcp-server) — SSH MCP server included in official repo ☆`916`
- [tufantunc/ssh-mcp](https://github.com/tufantunc/ssh-mcp) — SSH control for Linux servers ☆`773`
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw) — Shell and coding agent on mcp clients ☆`678`
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) — iTerm command execution for REPL/CLI ☆`567`
- [baryhuang/mcp-remote-macos-use](https://github.com/baryhuang/mcp-remote-macos-use) — AI agent for full Mac control ☆`490`
- [peakmojo/applescript-mcp](https://github.com/peakmojo/applescript-mcp) — Execute AppleScript for Mac control ☆`465`
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) — A CLI inspector for the Model Context Protocol ☆`446`
- [domdomegg/computer-use-mcp](https://github.com/domdomegg/computer-use-mcp) — Full computer control for AI models ☆`382`
- [claude-did-this/MCPControl](https://github.com/claude-did-this/MCPControl) — MCP server for Windows OS automation ☆`332`
- [nickgnd/tmux-mcp](https://github.com/nickgnd/tmux-mcp) — A MCP server for our beloved terminal multiplexer tmux. ☆`303`
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) — MCP server to run commands (runProcess tool) ☆`233`
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) — Shell execution with whitelisted commands ☆`198`
- [dvcrn/mcp-server-siri-shortcuts](https://github.com/dvcrn/mcp-server-siri-shortcuts) — MCP for calling Siri Shorcuts from LLMs ☆`194`
- [AB498/computer-control-mcp](https://github.com/AB498/computer-control-mcp) — Mouse, keyboard, OCR via PyAutoGUI ☆`168`
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) — CLI with secure execution and custom policies ☆`177`
- [sonirico/mcp-shell](https://github.com/sonirico/mcp-shell) — Secure, auditable shell commands for AI ☆`107`
- [automateyournetwork/pyATS_MCP](https://github.com/automateyournetwork/pyATS_MCP) — An MCP Server for pyATS (experimental) ☆`86`
- [inercia/MCPShell](https://github.com/inercia/MCPShell) — Use shell scripts as MCP tools ☆`71`
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui) — Keyboard and mouse control on macOS ☆`61`
- [ooples/mcp-console-automation](https://github.com/ooples/mcp-console-automation) — MCP for AI-driven console automation and monitoring ☆`49`
- [nihalxkumar/arch-mcp](https://github.com/nihalxkumar/arch-mcp) — Arch Linux MCP (Model Context Protocol) Server ☆`58`
- [InsForge/insforge-mcp](https://github.com/InsForge/insforge-mcp) — MCP server for InsForge - full-stack builders for coding agents ☆`35`
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) — Safe Python executor from smolagents ☆`48`
- [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) — Approve terminal commands after risk and access checks ☆`18`
- [blakerouse/ssh-mcp](https://github.com/blakerouse/ssh-mcp) — Local SSH host groups and remote command execution ☆`20`
- [PhialsBasement/CMD-MCP-Server](https://github.com/PhialsBasement/CMD-MCP-Server) — CMD command execution for Claude agents ☆`25`
- [Beer-Bears/scaffold](https://github.com/Beer-Bears/scaffold) — Structural RAG system for large codebases ☆`20`
- [aybelatchane/mcp-server-terminal](https://github.com/aybelatchane/mcp-server-terminal) — TUI and CLI automation via Terminal State Tree ☆`19`
- [erniebrodeur/mcp-grep](https://github.com/erniebrodeur/mcp-grep) — simple mcp server to wrap the local instance of grep. ☆`24`
- [JoshuaRileyDev/mac-apps-launcher](https://github.com/JoshuaRileyDev/mac-apps-launcher) — Launch and manage macOS applications ☆`19`
## CRM & ERP

- [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) — MCP server for Odoo ERP integration ☆`396`
- [GeLi2001/shopify-mcp](https://github.com/GeLi2001/shopify-mcp) — Shopify API for Claude and Cursor ☆`237`
- [smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) — MCP Salesforce connector ☆`177`
- [tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) — Salesforce MCP Server ☆`167`
- [baryhuang/mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) — HubSpot CRM integration for AI assistants ☆`129`
- [augmnt/augments-mcp-server](https://github.com/augmnt/augments-mcp-server) — MCP server for Augments AI platform ☆`128`
- [tomaspavlin/rohlik-mcp](https://github.com/tomaspavlin/rohlik-mcp) — Shop groceries on Rohlik Group platforms ☆`121`
- [mafzaal/d365fo-client](https://github.com/mafzaal/d365fo-client) — Client for Microsoft Dynamics 365 F&O ☆`39`
- [AiondaDotCom/mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce) — Salesforce OAuth and CRUD for any object ☆`17`
- [dsvantien/netsuite-mcp-server](https://github.com/dsvantien/netsuite-mcp-server) — NetSuite ERP records, queries, and operations ☆`22`
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) — Attio CRM records and notes management ☆`16`
## Cloud & Infrastructure

### AWS

- [awslabs/mcp](https://github.com/awslabs/mcp) — AWS MCP servers for AI assistants ☆`9,747`
- [aarora79/aws-cost-explorer-mcp-server](https://github.com/aarora79/aws-cost-explorer-mcp-server) — MCP server for understanding AWS spend ☆`126`
- [rishikavikondala/mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws) — MCP server for AWS resource operations ☆`127`
- [aws-samples/sample-mcp-server-s3](https://github.com/aws-samples/sample-mcp-server-s3) — Retrieve PDFs and data from AWS S3 ☆`78`
- [localstack/localstack-mcp-server](https://github.com/localstack/localstack-mcp-server) — LocalStack AWS emulation ☆`27`
- [baryhuang/mcp-server-aws-resources-python](https://github.com/baryhuang/mcp-server-aws-resources-python) — Run boto3 code to manage AWS resources ☆`24`
- [trilogy-group/aws-pricing-mcp](https://github.com/trilogy-group/aws-pricing-mcp) — AWS EC2 pricing search by CPU, RAM, network ☆`21`
### Cloud Platforms

- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) — Cloudflare services management ☆`4,345`
- [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) — Azure DevOps integration for AI agents ☆`2,040`
- [TencentCloudBase/CloudBase-AI-Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) — Connect CloudBase to AI agents ☆`1,130`
- [GoogleCloudPlatform/cloud-run-mcp](https://github.com/GoogleCloudPlatform/cloud-run-mcp) — MCP server to deploy apps to Cloud Run ☆`631`
- [babelcloud/gbox](https://github.com/babelcloud/gbox) — AI control for Android, browser, desktop ☆`181`
- [aliyun/alibabacloud-devops-mcp-server](https://github.com/aliyun/alibabacloud-devops-mcp-server) — MCP server for Alibaba Yunxiao DevOps platform ☆`172`
- [dkruyt/mcp-hetzner](https://github.com/dkruyt/mcp-hetzner) — Hetzner Cloud management ☆`146`
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) — AlibabaCloud CloudOps MCP Server ☆`131`
- [heroku/heroku-mcp-server](https://github.com/heroku/heroku-mcp-server) — Heroku Platform MCP Server using the Heroku CLI ☆`81`
- [vantage-sh/vantage-mcp-server](https://github.com/vantage-sh/vantage-mcp-server) — Fetch costs and usage from Vantage ☆`85`
- [call518/MCP-OpenStack-Ops](https://github.com/call518/MCP-OpenStack-Ops) — MCP server providing OpenStack project management ☆`45`
- [aliyun/alibabacloud-hologres-mcp-server](https://github.com/aliyun/alibabacloud-hologres-mcp-server) — MCP server for Alibaba Hologres data warehouse ☆`37`
- [aliyun/alibabacloud-dataworks-mcp-server](https://github.com/aliyun/alibabacloud-dataworks-mcp-server) — Alibaba Cloud DataWorks API integration ☆`51`
- [aantti/mcp-netbird](https://github.com/aantti/mcp-netbird) — Netbird network management ☆`60`
- [kestra-io/mcp-server-python](https://github.com/kestra-io/mcp-server-python) — Python MCP for Kestra AI Agents ☆`33`
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) — Qiniu Cloud storage, CDN, and media processing ☆`39`
- [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) — MCP server for Redis Cloud database operations ☆`42`
- [pythonanywhere/pythonanywhere-mcp-server](https://github.com/pythonanywhere/pythonanywhere-mcp-server) — Manage PythonAnywhere files, apps, and tasks ☆`17`
- [Azure-Samples/mcp](https://github.com/Azure-Samples/mcp) — Samples and resources for Azure MCP ☆`42`
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) — APISIX gateway for LLM integration ☆`38`
- [liveblocks/liveblocks-mcp-server](https://github.com/liveblocks/liveblocks-mcp-server) — MCP server for Liveblocks. ☆`19`
- [pibblokto/cert-manager-mcp-server](https://github.com/pibblokto/cert-manager-mcp-server) — MCP Server for cert-manager ☆`24`
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) — Higress API gateway configuration management ☆`23`
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) — MCP IPFS Server ☆`21`
- [espressif/esp-rainmaker-mcp](https://github.com/espressif/esp-rainmaker-mcp) — ESP RainMaker MCP server ☆`18`
- [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) — Azure Resource Graph query interface ☆`18`
- [kocierik/consul-mcp-server](https://github.com/kocierik/consul-mcp-server) — A consul MCP Server (modelcontextprotocol) ☆`18`
### Kubernetes

- [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) — Kubernetes and OpenShift management ☆`2,140`
- [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) — MCP Server for kubernetes management commands ☆`1,594`
- [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) — Kubernetes cluster chat with Claude/Cursor ☆`961`
- [weibaohui/k8m](https://github.com/weibaohui/k8m) — Mini Kubernetes AI Dashboard ☆`886`
- [strowk/mcp-k8s-go](https://github.com/strowk/mcp-k8s-go) — Go-based Kubernetes connection ☆`383`
- [vfarcic/dot-ai](https://github.com/vfarcic/dot-ai) — Deploy apps to any Kubernetes cluster ☆`336`
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) — Portainer container management ☆`234`
- [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) — Kubernetes cluster management ☆`185`
- [kubestellar/console](https://github.com/kubestellar/console) — Multi-cluster Kubernetes dashboard with natural-language MCP ☆`140`
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) — Kubernetes cluster interaction ☆`151`
- [weibaohui/kom](https://github.com/weibaohui/kom) — Kubernetes SDK wrapping kubectl ☆`149`
- [StacklokLabs/mkp](https://github.com/StacklokLabs/mkp) — MKP Kubernetes MCP server ☆`59`
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) — Kubernetes diagnosis and management ☆`29`
- [cyclops-ui/mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops) — Cyclops Kubernetes management ☆`30`
- [kubesphere/ks-mcp-server](https://github.com/kubesphere/ks-mcp-server) — KubeSphere APIs for workspaces, clusters, users, and roles ☆`17`
### Virtualization & IaC

- [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) — Terraform ecosystem integration for AI ☆`1,540`
- [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) — Terraform AI-assisted infrastructure ☆`372`
- [1Panel-dev/mcp-1panel](https://github.com/1Panel-dev/mcp-1panel) — MCP server for 1Panel management ☆`168`
- [kocierik/mcp-nomad](https://github.com/kocierik/mcp-nomad) — A nomad MCP Server (modelcontextprotocol) ☆`59`
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) — MCP server for VMware ESXi management ☆`64`
- [jokemanfire/mcp-containerd](https://github.com/jokemanfire/mcp-containerd) — Use mcp to manage containerd(developing) ☆`53`
- [severity1/terraform-cloud-mcp](https://github.com/severity1/terraform-cloud-mcp) — Terraform Cloud API integration ☆`23`
- [openstack-kr/python-openstackmcp-server](https://github.com/openstack-kr/python-openstackmcp-server) — openstack mcp server ☆`19`
## Communication & Messaging

### Apple Messages

- [mattt/iMCP](https://github.com/mattt/iMCP) — Access Messages, Contacts, Reminders on Mac ☆`1,668`
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) — MCP server for secure iMessage database access on macOS ☆`331`
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) — Safe iMessage database queries ☆`81`
- [wyattjoh/imessage-mcp](https://github.com/wyattjoh/imessage-mcp) — iMessage data reading from macOS ☆`29`
### Email

- [elie222/inbox-zero](https://github.com/elie222/inbox-zero) — AI email assistant for inbox zero ☆`12,390`
- [MadLlama25/fastmail-mcp](https://github.com/MadLlama25/fastmail-mcp) — Access to Fastmail API for AI assistants ☆`132`
- [ZilongXue/claude-post](https://github.com/ZilongXue/claude-post) — Email management via natural language ☆`114`
- [mailtrap/mailtrap-mcp](https://github.com/mailtrap/mailtrap-mcp) — Official mailtrap.io MCP server ☆`65`
- [mailgun/mailgun-mcp-server](https://github.com/mailgun/mailgun-mcp-server) — Mailgun API integration ☆`62`
- [Shy2593666979/mcp-server-email](https://github.com/Shy2593666979/mcp-server-email) — Email with attachments for Gmail, Outlook, QQ ☆`80`
- [egyptianego17/email-mcp-server](https://github.com/egyptianego17/email-mcp-server) — Send emails with attachments via SMTP ☆`28`
### Messengers

- [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) — WhatsApp MCP server ☆`6,361`
- [chigwell/telegram-mcp](https://github.com/chigwell/telegram-mcp) — MCP server for Telegram messaging ☆`1,737`
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) — LINE Messaging API for AI agents ☆`784`
- [chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp) — Telegram dialogs, messages, drafts, statuses ☆`349`
- [ztxtxwd/open-feishu-mcp-server](https://github.com/ztxtxwd/open-feishu-mcp-server) — Feishu/Lark OAuth and document management ☆`87`
- [areweai/tsgram-mcp](https://github.com/areweai/tsgram-mcp) — Telegram for local Claude Code debug ☆`89`
- [pubnub/pubnub-mcp-server](https://github.com/pubnub/pubnub-mcp-server) — PubNub Model Context Protocol Server ☆`33`
- [mjknowles/matrix-mcp-server](https://github.com/mjknowles/matrix-mcp-server) — Matrix server integration and chat ☆`52`
- [DLHellMe/telegram-mcp-server](https://github.com/DLHellMe/telegram-mcp-server) — Scrape and analyze Telegram content ☆`32`
### Notifications

- [gitmotion/ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp) — MCP server for ntfy push notifications ☆`74`
- [infobip/mcp](https://github.com/infobip/mcp) — Infobip Remote MCP Servers Documentation ☆`36`
- [Cactusinhand/mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify) — Send system notification when Agent task is done. ☆`54`
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) — MCP server for ntfy push notifications ☆`45`
- [AshikNesin/pushover-mcp](https://github.com/AshikNesin/pushover-mcp) — A MCP implementation for sending notifications via Pushover ☆`43`
- [aahl/mcp-notify](https://github.com/aahl/mcp-notify) — Notify to Weixin, Telegram, Bark, Lark, DingTalk ☆`28`
### Team Chat

- [korotovsky/slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) — MCP server for Slack workspace integration ☆`1,852`
- [chatmcp/mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum) — Query and Summarize your chat messages. ☆`1,026`
- [joinly-ai/joinly](https://github.com/joinly-ai/joinly) — Make your meetings accessible to AI Agents ☆`566`
- [SaseQ/discord-mcp](https://github.com/SaseQ/discord-mcp) — MCP server for Discord integration ☆`525`
- [v-3/discordmcp](https://github.com/v-3/discordmcp) — Discord MCP Server for Claude Integration ☆`233`
- [discourse/discourse-mcp](https://github.com/discourse/discourse-mcp) — MCP client for Discourse sites ☆`76`
- [zencoderai/slack-mcp-server](https://github.com/zencoderai/slack-mcp-server) — Slack workspace interaction and messaging ☆`75`
- [jagan-shanmugam/mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host) — Mattermost integration with LangGraph agent ☆`34`
### Voice & Telephony

- [gerkensm/callcenter.js-mcp](https://github.com/gerkensm/callcenter.js-mcp) — Callcenter.JS AI Voice Agent VOIP Connector, MCP + CLI ☆`25`
## Data & Analytics

### AI/ML Platforms

- [MigoXLab/dingo](https://github.com/MigoXLab/dingo) — AI data, model, app quality evaluation ☆`757`
- [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) — HuggingFace Spaces integration ☆`389`
- [YanxingLiu/dify-mcp-server](https://github.com/YanxingLiu/dify-mcp-server) — Model Context Protocol (MCP) Server for dify workflows ☆`281`
- [0xshellming/mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) — MCP Server for AI Summarization ☆`167`
- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) — Chronulus AI forecasting and prediction agents ☆`113`
- [optuna/optuna-mcp](https://github.com/optuna/optuna-mcp) — Optuna hyperparameter optimization ☆`86`
- [zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml) — ZenML MLOps platform connection ☆`49`
- [arrismo/kaggle-mcp](https://github.com/arrismo/kaggle-mcp) — MCP server for Kaggle ☆`39`
- [HumanSignal/label-studio-mcp-server](https://github.com/HumanSignal/label-studio-mcp-server) — MCP server for Label Studio data labeling ☆`37`
- [privetin/dataset-viewer](https://github.com/privetin/dataset-viewer) — MCP server for Hugging Face dataset viewer ☆`31`
### Data APIs

- [anshumax/world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server) — World Bank open data API ☆`50`
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) — Personal data hub for AI from Steam, YouTube, Bilibili ☆`63`
- [Jellyfish-AI/jellyfish-mcp](https://github.com/Jellyfish-AI/jellyfish-mcp) — Jellyfish MCP server ☆`17`
- [explorium-ai/mcp-explorium](https://github.com/explorium-ai/mcp-explorium) — Explorium B2B Data - MCP Server ☆`21`
### Data Exploration

- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) — Interactive CSV data exploration ☆`544`
- [kdqed/zaturn](https://github.com/kdqed/zaturn) — Data Analysis With Vibes ☆`75`
- [santoshray02/csv-editor](https://github.com/santoshray02/csv-editor) — AI-powered CSV data manipulation and analysis ☆`25`
- [brightlikethelight/networkx-mcp-server](https://github.com/brightlikethelight/networkx-mcp-server) — NetworkX graph algorithms for AI conversations ☆`20`
### Data Platforms

- [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) — A MCP (Model Context Protocol) server for interacting with dbt. ☆`607`
- [kubeflow/mcp-apache-spark-history-server](https://github.com/kubeflow/mcp-apache-spark-history-server) — Apache Spark History Server bridge ☆`203`
- [microsoft/fabric-rti-mcp](https://github.com/microsoft/fabric-rti-mcp) — Fabric Real-Time Intelligence server ☆`132`
- [acryldata/mcp-server-datahub](https://github.com/acryldata/mcp-server-datahub) — Official MCP server for DataHub ☆`80`
- [keboola/mcp-server](https://github.com/keboola/mcp-server) — Model Context Protocol (MCP) Server for the Keboola Platform ☆`86`
- [thoughtspot/mcp-server](https://github.com/thoughtspot/mcp-server) — The ThoughtSpot MCP Server ☆`33`
- [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) — Kafka Schema Registry management ☆`32`
- [JordiNeil/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) — MCP Server for Databricks ☆`50`
- [RafaelCartenet/mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) — AI agents interact with Databricks ☆`43`
- [growthbook/growthbook-mcp](https://github.com/growthbook/growthbook-mcp) — GrowthBook flags and experiments ☆`23`
- [IBM/data-intelligence-mcp-server](https://github.com/IBM/data-intelligence-mcp-server) — Watsonx Data Intelligence gateway across microservices ☆`20`
- [syucream/lightdash-mcp-server](https://github.com/syucream/lightdash-mcp-server) — Access to Lightdash analytics ☆`27`
- [yangkyeongmo/mcp-server-openmetadata](https://github.com/yangkyeongmo/mcp-server-openmetadata) — OpenMetadata integration for data catalog ☆`24`
- [mattijsdp/dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp) — dbt documentation interaction ☆`23`
- [datumnova/ms-fabric-mcp](https://github.com/datumnova/ms-fabric-mcp) — Microsoft Fabric workspaces, lakehouses, and PySpark notebooks ☆`17`
- [yashshingvi/databricks-genie-MCP](https://github.com/yashshingvi/databricks-genie-MCP) — Ask Databricks Genie questions and run SQL queries ☆`17`
### Jupyter & Notebooks

- [datalayer/jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server) — Model Context Protocol (MCP) Server for Jupyter. ☆`1,292`
- [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) — A Model Context Protocol (MCP) for Jupyter Notebook ☆`129`
- [phisanti/MCPR](https://github.com/phisanti/MCPR) — AI agents in interactive R sessions ☆`26`
### Visualization

- [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) — 25+ visual charts using @antvis for data analysis ☆`4,389`
- [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) — ECharts visual charts with AI ☆`269`
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) — MCP server for Vega-Lite data visualization ☆`100`
- [palewire/datawrapper-mcp](https://github.com/palewire/datawrapper-mcp) — Create Datawrapper charts with AI ☆`57`
## Databases

### Analytics & Warehouses

- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) — Connect ClickHouse to your AI assistants. ☆`879`
- [motherduckdb/mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck) — Local MCP server for DuckDB and MotherDuck ☆`524`
- [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) — Snowflake Cortex AI and SQL orchestration ☆`299`
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) — MCP server for Snowflake database queries ☆`186`
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) — DuckDB database interaction ☆`178`
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) — MCP server for Google BigQuery integration ☆`148`
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) — Google BigQuery database access ☆`131`
- [lishenxydlgzs/aws-athena-mcp](https://github.com/lishenxydlgzs/aws-athena-mcp) — MCP server to run AWS Athena queries ☆`41`
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) — MCP server for Azure Data Explorer ☆`59`
- [aliyun/alibabacloud-adb-mysql-mcp-server](https://github.com/aliyun/alibabacloud-adb-mysql-mcp-server) — AnalyticDB for MySQL MCP Server ☆`32`
- [iunera/druid-mcp-server](https://github.com/iunera/druid-mcp-server) — Apache Druid cluster tools, resources, and analysis ☆`18`
- [startreedata/mcp-pinot](https://github.com/startreedata/mcp-pinot) — MCP Server for Apache Pinot ☆`17`
### Cache & Key-Value

- [redis/mcp-redis](https://github.com/redis/mcp-redis) — MCP server for Redis database operations ☆`629`
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) — MCP server for Alibaba Tablestore NoSQL ☆`157`
- [upstash/mcp-server](https://github.com/upstash/mcp-server) — Upstash Model Context Server ☆`59`
### Cloud Platforms

- [instantdb/instant](https://github.com/instantdb/instant) — Modern Firebase with real-time database ☆`10,536`
- [supabase/mcp](https://github.com/supabase/mcp) — Connect Supabase to your AI assistants ☆`2,927`
- [alexander-zuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) — MCP server for Supabase database and auth ☆`831`
- [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) — Neon Management API and databases ☆`648`
- [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) — Model Context Protocol (MCP) server for Firebase. ☆`246`
- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) — Model Context Protocol server for Aiven ☆`28`
- [JoshuaRileyDev/supabase-mcp-server](https://github.com/JoshuaRileyDev/supabase-mcp-server) — MCP server for Supabase database operations ☆`52`
- [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) — Nile Database tenants, users, auth for LLMs ☆`17`
### Graph Databases

- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) — Neo4j Labs Model Context Protocol servers ☆`986`
- [neo4j-contrib/gds-agent](https://github.com/neo4j-contrib/gds-agent) — Neo4j Graph Data Science tools ☆`97`
- [FalkorDB/FalkorDB-MCPServer](https://github.com/FalkorDB/FalkorDB-MCPServer) — Connect LLMs to FalkorDB ☆`41`
- [da-okazaki/mcp-neo4j-server](https://github.com/da-okazaki/mcp-neo4j-server) — mcp-neo4j-server ☆`59`
- [ravenwits/mcp-server-arangodb](https://github.com/ravenwits/mcp-server-arangodb) — ArangoDB database interaction ☆`47`
### Multi-Database Tools

- [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) — Open source database MCP toolbox ☆`16,548`
- [bytebase/dbhub](https://github.com/bytebase/dbhub) — Token-efficient multi-database MCP ☆`3,593`
- [damms005/devdb-vscode](https://github.com/damms005/devdb-vscode) — Zero-config VS Code database extension ☆`1,439`
- [centralmind/gateway](https://github.com/centralmind/gateway) — Universal database MCP for LLMs ☆`550`
- [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server) — MCP server for database operations ☆`431`
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) — MCP server for SQLAlchemy database operations ☆`419`
- [executeautomation/mcp-database-server](https://github.com/executeautomation/mcp-database-server) — Connect to SQLite, SQL Server, PostgreSQL ☆`386`
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) — Natural language database queries ☆`239`
- [s2-streamstore/s2-sdk-typescript](https://github.com/s2-streamstore/s2-sdk-typescript) — TypeScript SDK for S2, the durable streams API ☆`35`
- [schemacrawler/SchemaCrawler-AI-MCP-Server-Usage](https://github.com/schemacrawler/SchemaCrawler-AI-MCP-Server-Usage) — How to use SchemaCrawler AI MCP Server ☆`29`
- [fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) — Store and load JSON documents from LLM tool use ☆`31`
- [datastrato/mcp-server-gravitino](https://github.com/datastrato/mcp-server-gravitino) — MCP server for Apache Gravitino ☆`23`
- [OpenLinkSoftware/mcp-jdbc-server](https://github.com/OpenLinkSoftware/mcp-jdbc-server) — Java JDBC access for SQL databases ☆`16`
### NoSQL & Document

- [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) — Connect to MongoDB and Atlas clusters ☆`1,138`
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) — A Model Context Protocol Server for MongoDB ☆`282`
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) — MongoDB Lens: Full Featured MCP Server for MongoDB Databases ☆`208`
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) — A mongo db server for the model context protocol (MCP) ☆`175`
- [datastax/astra-db-mcp](https://github.com/datastax/astra-db-mcp) — An MCP server for Astra DB workloads ☆`41`
- [couchbase/mcp-server-couchbase](https://github.com/couchbase/mcp-server-couchbase) — Couchbase database cluster integration ☆`35`
### SQL Databases

- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) — Postgres with read/write access and performance ☆`3,361`
- [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) — MCP server for MySQL database operations ☆`2,140`
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) — Secure MySQL database interaction ☆`1,396`
- [subnetmarco/pgmcp](https://github.com/subnetmarco/pgmcp) — An MCP server to query any Postgres database in natural language. ☆`541`
- [apache/doris-mcp-server](https://github.com/apache/doris-mcp-server) — Apache Doris MCP Server ☆`348`
- [wenb1n-dev/mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro) — Enhanced MySQL with anomaly analysis ☆`248`
- [MariaDB/mcp](https://github.com/MariaDB/mcp) — MariaDB MCP (Model Context Protocol) server implementation ☆`204`
- [StarRocks/mcp-server-starrocks](https://github.com/StarRocks/mcp-server-starrocks) — StarRocks MCP (Model Context Protocol) Server ☆`192`
- [call518/MCP-PostgreSQL-Ops](https://github.com/call518/MCP-PostgreSQL-Ops) — PostgreSQL operations and monitoring ☆`160`
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) — A Model Context Protocol server for MySQL database operations ☆`168`
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) — High-performance Trino MCP in Go ☆`121`
- [jparkerweb/mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite) — Comprehensive SQLite interaction ☆`127`
- [oceanbase/awesome-oceanbase-mcp](https://github.com/oceanbase/awesome-oceanbase-mcp) — MCP Server for OceanBase database and its tools ☆`108`
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) — Read-only SQLite database access ☆`108`
- [Teradata/teradata-mcp-server](https://github.com/Teradata/teradata-mcp-server) — Teradata database integration ☆`57`
- [donghao1393/mcp-dbutils](https://github.com/donghao1393/mcp-dbutils) — Multi-database connector for SQLite, MySQL, PostgreSQL ☆`89`
- [aliyun/alibabacloud-rds-openapi-mcp-server](https://github.com/aliyun/alibabacloud-rds-openapi-mcp-server) — MCP server for RDS Services via OPENAPI. ☆`54`
- [wenb1n-dev/SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP) — Universal database MCP for MySQL, PostgreSQL, Oracle and more ☆`77`
- [Zhwt/go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql) — Go-based MCP server for MySQL ☆`65`
- [ydb-platform/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) — MCP server for YDB distributed database ☆`29`
- [Xexr/mcp-libsql](https://github.com/Xexr/mcp-libsql) — MCP server for libSQL database ☆`21`
- [singlestore-labs/mcp-server-singlestore](https://github.com/singlestore-labs/mcp-server-singlestore) — SingleStore database management API ☆`33`
- [dolthub/dolt-mcp](https://github.com/dolthub/dolt-mcp) — The MCP server for Dolt ☆`19`
- [aliyun/alibabacloud-adbpg-mcp-server](https://github.com/aliyun/alibabacloud-adbpg-mcp-server) — AnalyticDB PostgreSQL metadata and SQL operations ☆`16`
- [pingcap/pytidb](https://github.com/pingcap/pytidb) — TiDB AI SDK for apps and agents ☆`33`
- [isdaniel/pgtuner_mcp](https://github.com/isdaniel/pgtuner_mcp) — provides AI-powered PostgreSQL performance tuning capabilities. ☆`29`
- [ahmedmustahid/postgres-mcp-server](https://github.com/ahmedmustahid/postgres-mcp-server) — MCP server for PostgreSQL ☆`31`
- [panasenco/mcp-sqlite](https://github.com/panasenco/mcp-sqlite) — SQLite with Datasette metadata support ☆`27`
- [OpenLinkSoftware/mcp-sqlalchemy-server](https://github.com/OpenLinkSoftware/mcp-sqlalchemy-server) — ODBC server with FastAPI and SQLAlchemy ☆`24`
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) — mcp server for tidb ☆`24`
- [abel9851/mcp-server-mariadb](https://github.com/abel9851/mcp-server-mariadb) — An mcp server that provides read-only access to MariaDB. ☆`20`
- [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) — MCP Server for Trino ☆`18`
### Search Engines

- [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) — Elasticsearch queries and index management ☆`718`
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) — Elasticsearch and OpenSearch interaction ☆`308`
- [meilisearch/meilisearch-mcp](https://github.com/meilisearch/meilisearch-mcp) — Meilisearch interaction via LLM interfaces ☆`195`
- [opensearch-project/opensearch-mcp-server-py](https://github.com/opensearch-project/opensearch-mcp-server-py) — OpenSearch cluster interaction for AI ☆`153`
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server) — Official Vectorize MCP Server ☆`115`
- [suhail-ak-2/mcp-typesense-server](https://github.com/suhail-ak-2/mcp-typesense-server) — Typesense search for AI assistants ☆`19`
### Spreadsheets & No-Code

- [baserow/baserow](https://github.com/baserow/baserow) — No-code database, apps, agents with AI ☆`6,067`
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) — Google Drive and Sheets integration ☆`1,010`
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) — Airtable bases integration for AI systems ☆`457`
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) — Google Sheets read, write, manipulate ☆`100`
- [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) — Airtable integration for AI applications ☆`88`
- [edwinbernadus/nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server) — nocodb mcp server ☆`76`
- [felores/airtable-mcp](https://github.com/felores/airtable-mcp) — Manage Airtable bases and records ☆`75`
- [proompteng/bilig](https://github.com/proompteng/bilig) — Headless spreadsheet formulas, edits, and JSON persistence ☆`35`
### Streaming & Messaging

- [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) — MCP server for Confluent Kafka platform ☆`168`
- [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) — Apache Kafka server in Go ☆`56`
- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) — MCP server for interacting with RabbitMQ ☆`38`
### Time-Series & Metrics

- [GreptimeTeam/greptimedb](https://github.com/GreptimeTeam/greptimedb) — Unified observability DB for metrics, logs, traces ☆`6,727`
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) — MCP server for Prometheus metrics ☆`517`
- [VictoriaMetrics/mcp-victorialogs](https://github.com/VictoriaMetrics/mcp-victorialogs) — VictoriaLogs log management integration ☆`98`
- [apache/iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server) — Apache IoTDB MCP Server ☆`39`
- [influxdata/influxdb3_mcp_server](https://github.com/influxdata/influxdb3_mcp_server) — MCP Server for InfluxDB 3 ☆`38`
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) — A Model Context Protocol (MCP) server for GreptimeDB ☆`29`
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) — An MCP Server for querying InfluxDB ☆`46`
### Vector Databases

- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) — Official Qdrant vector database MCP ☆`1,542`
- [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) — Chroma vector database capabilities ☆`598`
- [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus) — Model Context Protocol Servers for Milvus ☆`244`
- [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) — MCP (Model Context Protocol) server for Weaviate ☆`162`
- [pinecone-io/pinecone-mcp](https://github.com/pinecone-io/pinecone-mcp) — Connect Pinecone to AI assistants ☆`71`
- [privetin/chroma](https://github.com/privetin/chroma) — MCP server for Chroma ☆`41`
## Developer Tools

### API Tools

- [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) — Expose FastAPI endpoints as MCP tools ☆`12,013`
- [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) — Bridge Abilities API to MCP ☆`1,782`
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) — A flexible HTTP fetching Model Context Protocol server. ☆`827`
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) — Convert Any OpenAPI V3 API to MCP Server ☆`625`
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) — Model Context Protocol server for GraphQL ☆`407`
- [postmanlabs/postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server) — Postman collections, OpenAPI specs, and environments ☆`316`
- [apollographql/apollo-mcp-server](https://github.com/apollographql/apollo-mcp-server) — Apollo MCP Server ☆`310`
- [MFYDev/ghost-mcp](https://github.com/MFYDev/ghost-mcp) — Interact with Ghost CMS via LLM ☆`236`
- [hostinger/api-mcp-server](https://github.com/hostinger/api-mcp-server) — MCP server for Hostinger API integration ☆`157`
- [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) — An MCP server that provides access to Postman. ☆`160`
- [webflow/mcp-server](https://github.com/webflow/mcp-server) — Model Context Protocol (MCP) server for the Webflow Data API. ☆`140`
- [shannonlal/mcp-postman](https://github.com/shannonlal/mcp-postman) — MCP Server for running Postman Collections with Newman ☆`84`
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) — Contentful CMS Management API ☆`62`
- [Arize-ai/text-to-graphql-mcp](https://github.com/Arize-ai/text-to-graphql-mcp) — MCP server for text-to-GraphQL conversion ☆`25`
- [Omedia/mcp-server-drupal](https://github.com/Omedia/mcp-server-drupal) — Drupal MCP module companion ☆`51`
- [shanejonas/openrpc-mcp-server](https://github.com/shanejonas/openrpc-mcp-server) — JSON-RPC via OpenRPC ☆`43`
- [xxxbrian/mcp-rquest](https://github.com/xxxbrian/mcp-rquest) — Browser-like HTTP with TLS fingerprinting ☆`48`
- [hannesj/mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema) — GraphQL Schema Model Context Protocol Server ☆`46`
- [Jktfe/serveMyAPI](https://github.com/Jktfe/serveMyAPI) — MCP server for custom API serving ☆`25`
- [hijaz/postmancer](https://github.com/hijaz/postmancer) — REST client replacing Postman/Insomnia ☆`28`
- [drestrepom/mcp_graphql](https://github.com/drestrepom/mcp_graphql) — Interact with GraphQL APIs via MCP tools ☆`19`
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) — Turn any GraphQL endpoint into a set of MCP tools ☆`23`
### CI/CD & DevOps

- [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) — Build n8n workflows with AI assistants ☆`23,032`
- [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) — Tools for interacting with n8n API ☆`1,633`
- [utensils/mcp-nixos](https://github.com/utensils/mcp-nixos) — MCP-NixOS - Model Context Protocol Server for NixOS resources ☆`848`
- [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) — MCP server for Docker ☆`746`
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) — A docker MCP Server (modelcontextprotocol) ☆`504`
- [TencentEdgeOne/edgeone-makers-mcp](https://github.com/TencentEdgeOne/edgeone-makers-mcp) — Deploy HTML to EdgeOne Pages with public URL ☆`435`
- [jamsocket/forevervm](https://github.com/jamsocket/forevervm) — Stateful AI code sandboxes ☆`229`
- [docker/hub-mcp](https://github.com/docker/hub-mcp) — Docker Hub MCP Server ☆`168`
- [DefangLabs/defang](https://github.com/DefangLabs/defang) — MCP server for Defang cloud deployment ☆`167`
- [yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) — MCP server for Apache Airflow workflows ☆`178`
- [nacos-group/nacos-mcp-router](https://github.com/nacos-group/nacos-mcp-router) — MCP server discovery, install, and proxy ☆`180`
- [harness/mcp-server](https://github.com/harness/mcp-server) — Harness’ official MCP Server ☆`104`
- [OctopusDeploy/mcp-server](https://github.com/OctopusDeploy/mcp-server) — Octopus Deploy Official MCP Server ☆`101`
- [Vortiago/mcp-azure-devops](https://github.com/Vortiago/mcp-azure-devops) — AI assistants with Azure DevOps ☆`79`
- [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) — Official MCP Server for Buildkite. ☆`54`
- [call518/MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API) — Apache Airflow API integration ☆`52`
- [bitrise-io/bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp) — Bitrise CI/CD app and build management ☆`42`
- [launchdarkly/mcp-server](https://github.com/launchdarkly/mcp-server) — LaunchDarkly's Model Context Protocol (MCP) Server ☆`27`
- [IvanAmador/vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp) — Vercel AI SDK documentation search ☆`50`
- [leonardosepulvedat/mcp-n8n](https://github.com/leonardosepulvedat/mcp-n8n) — n8n API plus 100 workflow templates with matching ☆`21`
- [configcat/mcp-server](https://github.com/configcat/mcp-server) — Official ConfigCat Model Context Protocol (MCP) Server ☆`17`
- [endorhq/cli](https://github.com/endorhq/cli) — Sandboxed environments for favorite services via MCP ☆`28`
- [gofireflyio/firefly-mcp](https://github.com/gofireflyio/firefly-mcp) — Firefly MCP ☆`16`
- [prassanna-ravishankar/clearml-mcp](https://github.com/prassanna-ravishankar/clearml-mcp) — lightweight MCP server for ClearML ☆`16`
- [conductor-oss/conductor-mcp](https://github.com/conductor-oss/conductor-mcp) — Model Context Protocol server for Orkes Conductor ☆`16`
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) — MCP server for executing code in Docker containers ☆`18`
### Code Analysis

- [bgauryy/octocode](https://github.com/bgauryy/octocode) — MCP server for semantic code search and context generation ☆`945`
- [SonarSource/sonarqube-mcp-server](https://github.com/SonarSource/sonarqube-mcp-server) — Official SonarQube quality and security for agents ☆`654`
- [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP) — Codebase dependency diagrams ☆`302`
- [janreges/ai-distiller](https://github.com/janreges/ai-distiller) — Fast tool for extracting essential public information from code ☆`168`
- [st3v3nmw/sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp) — Semantic code search reducing token waste ☆`119`
- [micl2e2/code-to-tree](https://github.com/micl2e2/code-to-tree) — Source code to AST tree conversion ☆`88`
- [codacy/codacy-mcp-server](https://github.com/codacy/codacy-mcp-server) — Codacy's MCP Server implementation ☆`61`
- [lineai-intelligence/lineai-mcp-server](https://github.com/lineai-intelligence/lineai-mcp-server) — Codelogic software dependency analysis ☆`38`
- [Disentinel/grafema](https://github.com/Disentinel/grafema) — Semantic code graphs for call chains, data flow, and search ☆`36`
- [azer/react-analyzer-mcp](https://github.com/azer/react-analyzer-mcp) — React code analysis and docs generation ☆`58`
- [vezlo/src-to-kb](https://github.com/vezlo/src-to-kb) — Convert source code to LLM ready knowledge base ☆`40`
- [cqfn/aibolit-mcp-server](https://github.com/cqfn/aibolit-mcp-server) — Aibolit Java static analyzer for AI agents ☆`27`
- [kandrwmrtn/cplusplus_mcp](https://github.com/kandrwmrtn/cplusplus_mcp) — MCP server for C++ codebase analysis using libclang ☆`33`
- [j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) — MCP server for SQL static analysis. ☆`32`
- [isiahw1/mcp-server-bing-webmaster](https://github.com/isiahw1/mcp-server-bing-webmaster) — Bing Webmaster Tools for SEO and analytics ☆`25`
### Debuggers

- [jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) — Interactive debugging via MCP and VS Code ☆`516`
- [Continuum-AI-Corp/OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) — Record, replay and fork coding-agent runs ☆`272`
- [cameroncooke/reloaderoo](https://github.com/cameroncooke/reloaderoo) — Powerful MCP debugging proxy and CLI inspection tool. ☆`125`
- [stass/lldb-mcp](https://github.com/stass/lldb-mcp) — LLDB MCP server ☆`113`
- [pansila/mcp_server_gdb](https://github.com/pansila/mcp_server_gdb) — MCP Server to expose the GDB debugging capabilities ☆`68`
### Design & UI

- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) — Figma layout info for AI coding agents ☆`15,944`
- [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) — Cursor and Figma communication ☆`7,048`
- [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) — Frontend development with AI like Magic ☆`5,959`
- [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) — MCP server for shadcn/ui component library ☆`3,011`
- [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) — Generate mermaid diagram and chart with AI MCP dynamically. ☆`639`
- [mastergo-design/mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp) — Connect MasterGo to AI assistants ☆`286`
- [public-ui/kolibri](https://github.com/public-ui/kolibri) — The accessible HTML-Standard ☆`283`
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) — mindmap, mcp server, artifact ☆`239`
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) — MCP server for extracting design system components ☆`69`
- [starwind-ui/starwind-ui-mcp](https://github.com/starwind-ui/starwind-ui-mcp) — Starwind UI for Cursor and Windsurf ☆`35`
- [themesberg/flowbite-mcp](https://github.com/themesberg/flowbite-mcp) — Figma to code with Flowbite ☆`42`
- [themeselection/flyonui-mcp](https://github.com/themeselection/flyonui-mcp) — MCP server for flyonUI ☆`32`
- [smartzan63/lucid-mcp-server](https://github.com/smartzan63/lucid-mcp-server) — Search, export, and create Lucid charts and diagrams ☆`19`
- [heilgar/shadcn-ui-mcp-server](https://github.com/heilgar/shadcn-ui-mcp-server) — MCP server for shadcn/ui component library ☆`26`
- [NonicaTeam/AI-Connector-for-Revit](https://github.com/NonicaTeam/AI-Connector-for-Revit) — Issue tracker for the NonicaTab Revit AI Connector ☆`17`
- [kapilduraphe/webflow-mcp-server](https://github.com/kapilduraphe/webflow-mcp-server) — Webflow MCP server ☆`21`
### Diagrams

- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) — Markdown to interactive mind maps ☆`289`
- [veelenga/claude-mermaid](https://github.com/veelenga/claude-mermaid) — MCP Server to previewing mermaid diagrams with live reload ☆`214`
- [apeyroux/mcp-xmind](https://github.com/apeyroux/mcp-xmind) — Analyze and query XMind mind maps ☆`95`
- [Narasimhaponnada/mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp) — MCP server for Mermaid diagram generation ☆`53`
### Documentation

- [upstash/context7](https://github.com/upstash/context7) — Up-to-date code docs for LLMs ☆`62,594`
- [lingodotdev/lingo.dev](https://github.com/lingodotdev/lingo.dev) — MCP server for Lingo localization platform ☆`5,407`
- [MicrosoftDocs/mcp](https://github.com/MicrosoftDocs/mcp) — Microsoft Learn MCP for LLMs ☆`1,923`
- [kimsungwhee/apple-docs-mcp](https://github.com/kimsungwhee/apple-docs-mcp) — Apple Developer Documentation search ☆`1,380`
- [andrea9293/mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server) — Document management with Gemini ☆`342`
- [szeider/consult7](https://github.com/szeider/consult7) — MCP server to consult a language model with large context size ☆`296`
- [Govcraft/rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server) — Rust documentation lookup ☆`297`
- [khromov/svelte-llm-mcp](https://github.com/khromov/svelte-llm-mcp) — Svelte developer documentation as an MCP and in llms.txt format ☆`158`
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) — Structured Go docs to avoid dumping source into context ☆`124`
- [tosin2013/mcp-adr-analysis-server](https://github.com/tosin2013/mcp-adr-analysis-server) — AI-powered ADR and architecture analysis ☆`35`
- [yWorks/mcp-typescribe](https://github.com/yWorks/mcp-typescribe) — TypeScript library support for LLMs ☆`46`
- [yikakia/godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server) — Go package docs from pkg.go.dev ☆`38`
- [V0v1kkk/DotNetMetadataMcpServer](https://github.com/V0v1kkk/DotNetMetadataMcpServer) — .NET type metadata for AI coding agents ☆`30`
- [inkeep/mcp-server-python](https://github.com/inkeep/mcp-server-python) — Inkeep MCP Server ☆`25`
- [Excoriate/mcp-terragrunt-docs](https://github.com/Excoriate/mcp-terragrunt-docs) — Terragrunt documentation context ☆`20`
- [idachev/mcp-javadc](https://github.com/idachev/mcp-javadc) — MCP server for decompiling Java .class files to source ☆`20`
- [oborchers/mcp-server-docy](https://github.com/oborchers/mcp-server-docy) — Documentation access capabilities ☆`18`
- [augmentedivan/fabric-mcp-server](https://github.com/augmentedivan/fabric-mcp-server) — Fabric patterns with AI agents ☆`18`
### IDE & Editors

- [getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) — MCP server for Xcode build operations ☆`6,449`
- [isaacphi/mcp-language-server](https://github.com/isaacphi/mcp-language-server) — MCP server implementing Language Server Protocol ☆`1,599`
- [JetBrains/mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains) — MCP server for JetBrains IDE integration ☆`963`
- [juehang/vscode-mcp-server](https://github.com/juehang/vscode-mcp-server) — VS Code editing features for LLM coding ☆`395`
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) — Xcode project management ☆`384`
- [hechtcarmel/jetbrains-index-mcp-plugin](https://github.com/hechtcarmel/jetbrains-index-mcp-plugin) — JetBrains plugin for MCP index integration ☆`351`
- [bigcodegen/mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server) — Control Neovim via MCP ☆`322`
- [biegehydra/BifrostMCP](https://github.com/biegehydra/BifrostMCP) — VS Code semantic tools via MCP ☆`224`
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) — Line-oriented text editing for LLM tools ☆`200`
- [hechtcarmel/jetbrains-debugger-mcp-plugin](https://github.com/hechtcarmel/jetbrains-debugger-mcp-plugin) — JetBrains debugger control via MCP ☆`108`
- [Tritlo/lsp-mcp](https://github.com/Tritlo/lsp-mcp) — An MCP server that lets you interact with LSP servers ☆`125`
- [hloiseau/mcp-gopls](https://github.com/hloiseau/mcp-gopls) — Go LSP server via gopls ☆`102`
- [marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) — CodeMirror MCP extension ☆`79`
- [linw1995/nvim-mcp](https://github.com/linw1995/nvim-mcp) — MCP server for Neovim integration ☆`72`
- [ShenghaiWang/xcodebuild](https://github.com/ShenghaiWang/xcodebuild) — Xcode iOS build with error feedback ☆`85`
- [laurynas-biveinis/elisp-dev-mcp](https://github.com/laurynas-biveinis/elisp-dev-mcp) — Emacs Elisp development tools for LLMs ☆`47`
- [AB498/code-context-provider-mcp](https://github.com/AB498/code-context-provider-mcp) — Code context and analysis for AI ☆`20`
### MCP SDKs

- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) — Python framework for building MCP servers and clients ☆`27,953`
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) — Go implementation of MCP ☆`9,150`
- [QuantGeekDev/mcp-framework](https://github.com/QuantGeekDev/mcp-framework) — TypeScript framework with auto-discovery ☆`929`
- [bhauman/clojure-mcp](https://github.com/bhauman/clojure-mcp) — Clojure MCP ☆`779`
- [php-mcp/laravel](https://github.com/php-mcp/laravel) — Laravel SDK for building MCP servers ☆`476`
- [opgginc/laravel-mcp-server](https://github.com/opgginc/laravel-mcp-server) — Laravel package for MCP servers ☆`331`
- [Epistates/turbomcp](https://github.com/Epistates/turbomcp) — High-performance MCP framework ☆`98`
- [tachyonmcp/tachyon](https://github.com/tachyonmcp/tachyon) — Java/Kotlin MCP runtime with HTTP, Netty, and sessions ☆`32`
- [reflagcom/javascript](https://github.com/reflagcom/javascript) — JS/TS SDKs for Reflag ☆`25`
- [oatpp/oatpp-mcp](https://github.com/oatpp/oatpp-mcp) — C++ MCP implementation for Oat++ framework ☆`50`
- [Super-I-Tech/mcp_plexus](https://github.com/Super-I-Tech/mcp_plexus) — Multi-tenant MCP framework built on FastMCP ☆`30`
- [stephencme/create-mcp-ts](https://github.com/stephencme/create-mcp-ts) — TypeScript MCP server template ☆`21`
### Mobile Development

- [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) — Mobile automation for iOS, Android, emulators ☆`8,536`
- [joshuayoes/ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) — MCP server for interacting with the iOS simulator ☆`2,185`
- [minhalvp/android-mcp-server](https://github.com/minhalvp/android-mcp-server) — Android device control via adb ☆`811`
- [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind) — Control your Android devices with AI using Model Context Protocol ☆`435`
- [InditexTech/mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb) — MCP server for iOS simulator via IDB ☆`315`
- [mhmzdev/figma-flutter-mcp](https://github.com/mhmzdev/figma-flutter-mcp) — Figma design tokens for Flutter code agents ☆`244`
- [zillow/auto-mobile](https://github.com/zillow/auto-mobile) — Mobile automation tools with MCP ☆`80`
- [JoshuaRileyDev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) — MCP server for iOS Simulator control ☆`53`
- [Tommertom/awesome-ionic-mcp](https://github.com/Tommertom/awesome-ionic-mcp) — Ionic and Capacitor mobile app development ☆`46`
- [XixianLiang/HarmonyOS-mcp-server](https://github.com/XixianLiang/HarmonyOS-mcp-server) — MCP server for manipulating HarmonyOS next devices. ☆`35`
- [ambar/simctl-mcp](https://github.com/ambar/simctl-mcp) — MCP server for iOS Simulator control ☆`20`
### OpenAPI

- [janwilmake/openapi-mcp-server](https://github.com/janwilmake/openapi-mcp-server) — Complex OpenAPI exploration with plain language ☆`903`
- [ckanthony/openapi-mcp](https://github.com/ckanthony/openapi-mcp) — Dockerized OpenAPI to MCP conversion ☆`197`
- [twilio-labs/mcp](https://github.com/twilio-labs/mcp) — OpenAPI to MCP tools and Twilio APIs ☆`112`
- [zaizaizhao/mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server) — OpenAPI/Swagger to MCP conversion ☆`76`
- [kadykov/mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer) — Token-efficient OpenAPI/Swagger exploration ☆`76`
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) — OpenAPI specification MCP server. ☆`90`
- [baryhuang/mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi) — Call APIs via semantic search ☆`82`
- [hannesj/mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema) — OpenAPI Schema Model Context Protocol Server ☆`49`
- [criteo/openapi-to-mcp](https://github.com/criteo/openapi-to-mcp) — An MCP server for your API ☆`35`
### Package Managers

- [arvindand/maven-tools-mcp](https://github.com/arvindand/maven-tools-mcp) — Maven Central dependency intelligence for JVM build tools ☆`33`
- [Artmann/package-registry-mcp](https://github.com/Artmann/package-registry-mcp) — NPM, Cargo, PyPi, NuGet package search ☆`39`
- [Bigsy/maven-mcp-server](https://github.com/Bigsy/maven-mcp-server) — Maven build and dependency tools ☆`34`
- [jeannier/homebrew-mcp](https://github.com/jeannier/homebrew-mcp) — Homebrew package management ☆`29`
- [btwiuse/npm-search-mcp-server](https://github.com/btwiuse/npm-search-mcp-server) — MCP server for searching npm packages ☆`16`
- [subelsky/bundler_mcp](https://github.com/subelsky/bundler_mcp) — MCP server for Ruby Bundler integration ☆`20`
### Robotics & Automation

- [trycua/cua](https://github.com/trycua/cua) — MCP server for CUA platform ☆`27,717`
- [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) — ROS robot control with Claude and GPT ☆`1,480`
- [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) — Isaac Simulation MCP Extension and Server ☆`193`
- [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) — ROS 2 robotics AI bridge ☆`89`
- [abrinsmead/mindpilot-mcp](https://github.com/abrinsmead/mindpilot-mcp) — Visualize code and architect new systems ☆`90`
- [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) — MCP server for Unitree Go2 robot control ☆`87`
- [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) — MCP server for ROS to control robots via topics, services, and actions. ☆`36`
### Task Management

- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) — Task manager with chain-of-thought and reflection ☆`2,145`
- [amxv/mcp-manager](https://github.com/amxv/mcp-manager) — Web UI to manage MCP servers in Claude ☆`295`
### Testing & QA

- [QAInsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) — JMeter AI workflow integration ☆`74`
- [debugg-ai/debugg-ai-mcp](https://github.com/debugg-ai/debugg-ai-mcp) — AI-managed end-to-end testing ☆`68`
- [SmartBear/smartbear-mcp](https://github.com/SmartBear/smartbear-mcp) — SmartBear's official MCP Server ☆`44`
- [mrexodia/user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp) — Human-in-the-loop workflow for Cursor ☆`54`
- [reportportal/reportportal-mcp-server](https://github.com/reportportal/reportportal-mcp-server) — MCP server for ReportPortal ☆`23`
- [currents-dev/currents-mcp](https://github.com/currents-dev/currents-mcp) — Currents MCP Server ☆`20`
- [hungthai1401/bruno-mcp](https://github.com/hungthai1401/bruno-mcp) — MCP Server for running Bruno Collections ☆`44`
- [QAInsights/k6-mcp-server](https://github.com/QAInsights/k6-mcp-server) — k6 MCP server ☆`27`
### Utilities

- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) — An MCP server that installs other MCP servers for you ☆`1,533`
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) — A Model Context Protocol server for calculating. ☆`159`
- [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server) — Remote network commands for LLMs ☆`64`
- [Mtehabsim/ScreenPilot](https://github.com/Mtehabsim/ScreenPilot) — AI device control like a human ☆`54`
- [zazencodes/random-number-mcp](https://github.com/zazencodes/random-number-mcp) — MCP server for random number generation ☆`51`
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) — Automatic operation of on-screen GUI. ☆`71`
- [bharathvaj-ganesan/whois-mcp](https://github.com/bharathvaj-ganesan/whois-mcp) — MCP Server for whois lookups. ☆`59`
- [newtype-01/prompthouse-mcp](https://github.com/newtype-01/prompthouse-mcp) — Personal prompt library manager ☆`53`
- [FelixFoster/mcp-enhance-prompt](https://github.com/FelixFoster/mcp-enhance-prompt) — AI-powered prompt enhancement and generation ☆`25`
- [ofek/pycli-mcp](https://github.com/ofek/pycli-mcp) — MCP server for any Python command line application ☆`23`
- [abhiphile/fermat-mcp](https://github.com/abhiphile/fermat-mcp) — SymPy, NumPy, and Matplotlib in one math engine ☆`20`
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) — Datetime info for agentic systems ☆`42`
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) — Current time check for Claude via MCP ☆`34`
- [fastn-ai/fastn-mcp](https://github.com/fastn-ai/fastn-mcp) — Governed, audited access to customer systems of record ☆`23`
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) — A MCP server for datetime formatting and file name generation. ☆`31`
- [TheoBrigitte/mcp-time](https://github.com/TheoBrigitte/mcp-time) — Dates and times with natural language and timezones ☆`25`
### Version Control

- [github/github-mcp-server](https://github.com/github/github-mcp-server) — GitHub's official MCP Server ☆`33,320`
- [idosal/git-mcp](https://github.com/idosal/git-mcp) — Free remote MCP for any GitHub project ☆`8,447`
- [gitkraken/gk-cli](https://github.com/gitkraken/gk-cli) — GitKraken CLI Releases and Documentation ☆`461`
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) — An MCP server for Azure DevOps ☆`394`
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) — GitHub repository content reading ☆`314`
- [puravparab/Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP) — mcp server for gitingest ☆`136`
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) — MCP server for GitLab merge requests and issues ☆`94`
- [oschina/mcp-gitee](https://github.com/oschina/mcp-gitee) — MCP server for Gitee repositories ☆`66`
- [Ryan0204/github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp) — GitHub repository reading ☆`32`
- [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) — github-enterprise-mcp ☆`29`
- [kurdin/github-repos-manager-mcp](https://github.com/kurdin/github-repos-manager-mcp) — GitHub Repos Manager MCP Server for MCP clients ☆`22`
## Embedded & IoT

- [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) — A JavaScript-driven M5Stack-embedded super-kawaii robot. ☆`1,743`
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) — A MCP server for Home Assistant ☆`576`
- [lamaalrajih/kicad-mcp](https://github.com/lamaalrajih/kicad-mcp) — KiCad integration for Mac, Windows, Linux ☆`524`
- [Extelligence-ai/bagel](https://github.com/Extelligence-ai/bagel) — Chat with robotics, drone, IoT data ☆`397`
- [voska/hass-mcp](https://github.com/voska/hass-mcp) — Home Assistant control and queries from LLMs ☆`344`
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) — Apple Shortcuts automation on macOS ☆`351`
- [jeff-nasseri/mikrotik-mcp](https://github.com/jeff-nasseri/mikrotik-mcp) — MCP server for Mikrotik ☆`288`
- [hao-cyber/phone-mcp](https://github.com/hao-cyber/phone-mcp) — Control Android phone via ADB ☆`246`
- [FradSer/mcp-server-apple-events](https://github.com/FradSer/mcp-server-apple-events) — Native integration with Apple Reminders and Calendar ☆`213`
- [horw/esp-mcp](https://github.com/horw/esp-mcp) — ESP32 commands and getting started ☆`158`
- [johannesPettersson80/codesys-mcp-toolkit](https://github.com/johannesPettersson80/codesys-mcp-toolkit) — CODESYS industrial automation platform ☆`124`
- [LGDiMaggio/predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp) — Predictive maintenance and fault diagnosis ☆`96`
- [thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) — MCP server for ThingsBoard IoT platform interaction ☆`98`
- [vishalmysore/choturobo](https://github.com/vishalmysore/choturobo) — Arduino robotics with AI integration ☆`79`
- [yoelbassin/gr-mcp](https://github.com/yoelbassin/gr-mcp) — MCP server for GNU Radio ☆`50`
- [aqara/aqara-mcp-server](https://github.com/aqara/aqara-mcp-server) — Aqara's official MCP Server ☆`45`
- [chrisgleissner/c64bridge](https://github.com/chrisgleissner/c64bridge) — Commodore 64 Ultimate, Ultimate II, and VICE control ☆`37`
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) — AI pilot for PTY operations - control terminals via MCP ☆`45`
- [nokia-steward/mcp-redfish](https://github.com/nokia-steward/mcp-redfish) — Query DMTF Redfish servers, systems, and network interfaces ☆`20`
- [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) — 3D printing live status and control ☆`38`
- [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) — An MCP server that connects to OPC UA-enabled industrial systems. ☆`30`
- [thinq-connect/thinqconnect-mcp](https://github.com/thinq-connect/thinqconnect-mcp) — ThinQ Connect MCP Server ☆`31`
- [MiddlePoint-Solutions/mcp-on-android-tv](https://github.com/MiddlePoint-Solutions/mcp-on-android-tv) — MCP server on Android TV with ADB ☆`22`
- [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) — Industrial Modbus data for AI ☆`25`
- [Hypijump31/bluetooth-mcp-server](https://github.com/Hypijump31/bluetooth-mcp-server) — bluetooth-mcp-server for Claude AI ☆`23`
- [gNucleus/text-to-cad-mcp](https://github.com/gNucleus/text-to-cad-mcp) — gNucleus Text To CAD MCP server ☆`18`
## File Systems & Storage

- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) — Go filesystem operations via MCP ☆`694`
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) — Python library for LLM context management ☆`308`
- [isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive) — Google Drive file reading ☆`283`
- [8b-is/smart-tree](https://github.com/8b-is/smart-tree) — Context-aware AI-crafted replacement for tree command ☆`270`
- [rust-mcp-stack/rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem) — Fast async filesystem operations ☆`180`
- [efforthye/fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp) — High-performance MCP server for file operations ☆`63`
- [vespo92/TrueNasCoreMCP](https://github.com/vespo92/TrueNasCoreMCP) — A working TrueNAS Core MCP Server ☆`31`
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) — MCP server for merging multiple files into one ☆`27`
- [Tencent/cos-mcp](https://github.com/Tencent/cos-mcp) — Tencent Cloud COS storage integration ☆`38`
- [willianpinho/large-file-mcp](https://github.com/willianpinho/large-file-mcp) — Chunk, search, navigate, and stream large files ☆`19`
- [NetApp/mcp](https://github.com/NetApp/mcp) — Model Context Protocol servers for NetApp services ☆`17`
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) — Model Context Protocol Server for Apache OpenDAL ☆`35`
## Finance

### Accounting & Budgeting

- [XeroAPI/xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server) — Xero accounting API integration ☆`371`
- [akutishevsky/lunchmoney-mcp](https://github.com/akutishevsky/lunchmoney-mcp) — MCP server for Lunch Money budgeting app ☆`109`
- [iiAtlas/hledger-mcp](https://github.com/iiAtlas/hledger-mcp) — A local MCP server for interacting with the HLedger cli ☆`65`
- [openMF/mcp-mifosx](https://github.com/openMF/mcp-mifosx) — Model Context Protocol - MCP for Mifos X ☆`25`
- [minhyeoky/mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger) — MCP server for Ledger CLI double-entry accounting ☆`51`
- [john-zhang-dev/xero-mcp](https://github.com/john-zhang-dev/xero-mcp) — Interact with Xero accounting ☆`23`
### Crypto & Blockchain

- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) — EVM network interaction for LLMs ☆`379`
- [aaronjmars/web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp) — Deep Research for crypto - free & fully local ☆`163`
- [armorwallet/armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) — Blockchain swaps and strategic planning ☆`179`
- [kukapay/crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp) — Cryptocurrency technical analysis indicators ☆`131`
- [alchemyplatform/alchemy-mcp-server](https://github.com/alchemyplatform/alchemy-mcp-server) — Alchemy blockchain API for AI agents ☆`88`
- [twelvedata/mcp](https://github.com/twelvedata/mcp) — MCP server for real-time financial market data access ☆`82`
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) — A coincap mcp server to access crypto data from coincap API ☆`92`
- [Bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp) — Bringing the bankless onchain API to MCP ☆`80`
- [getAlby/mcp](https://github.com/getAlby/mcp) — Bitcoin Lightning wallet via Nostr ☆`66`
- [norman-finance/norman-mcp-server](https://github.com/norman-finance/norman-mcp-server) — AI-powered bookkeeping and tax automation via MCP ☆`60`
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) — Provide latest cryptocurrency news to AI agents. ☆`74`
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) — Bitcoin & Lightning Network MCP Server. ☆`77`
- [bnb-chain/bnbchain-mcp](https://github.com/bnb-chain/bnbchain-mcp) — BNB Chain, BSC, opBNB, Greenfield ☆`60`
- [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) — Blockchain and web3 via Heurist Mesh ☆`67`
- [GoPlausible/algorand-mcp](https://github.com/GoPlausible/algorand-mcp) — Algorand Local Model Context Protocol (Server & Client) ☆`44`
- [coinpaprika/dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp) — MCP server for DEX trading data and crypto token analytics ☆`42`
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) — A mcp server for tracking cryptocurrency whale transactions. ☆`56`
- [shinzo-labs/coinmarketcap-mcp](https://github.com/shinzo-labs/coinmarketcap-mcp) — MCP Implementation for CoinMarketCap ☆`51`
- [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) — Crypto Fear & Greed Index data ☆`52`
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) — MCP server for CoinMarketCap cryptocurrency data ☆`50`
- [kukapay/crypto-sentiment-mcp](https://github.com/kukapay/crypto-sentiment-mcp) — Cryptocurrency sentiment analysis ☆`47`
- [wowinter13/solscan-mcp](https://github.com/wowinter13/solscan-mcp) — Solana transaction queries ☆`47`
- [hive-intel/hive-sdk](https://github.com/hive-intel/hive-sdk) — Crypto intel for markets, DeFi, wallets, NFTs, and Solana ☆`20`
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) — A mcp server that bridges Dune Analytics data to AI agents. ☆`41`
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) — Uniswap token swaps for AI agents ☆`40`
- [CoinStatsHQ/coinstats-mcp](https://github.com/CoinStatsHQ/coinstats-mcp) — Crypto prices, portfolios, and wallets via CoinStats ☆`16`
- [kukapay/kukapay-mcp-servers](https://github.com/kukapay/kukapay-mcp-servers) — Suite of MCP servers from Kukapay ☆`32`
- [longmans/coin_api_mcp](https://github.com/longmans/coin_api_mcp) — CoinMarketCap cryptocurrency data ☆`36`
- [noditlabs/nodit-mcp-server](https://github.com/noditlabs/nodit-mcp-server) — Blockchain data via Nodit Web3 API ☆`23`
- [kukapay/hyperliquid-info-mcp](https://github.com/kukapay/hyperliquid-info-mcp) — MCP server for Hyperliquid DEX data ☆`30`
- [kukapay/jupiter-mcp](https://github.com/kukapay/jupiter-mcp) — Jupiter DEX token swaps on Solana ☆`29`
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) — Cryptocurrency info via Bitget API ☆`26`
- [devonmojito/ton-blockchain-mcp](https://github.com/devonmojito/ton-blockchain-mcp) — TON blockchain interaction ☆`26`
- [Codex-Data/codex-mcp](https://github.com/Codex-Data/codex-mcp) — A Model Context Protocol server for the Codex API ☆`25`
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) — BICScan MCP Server ☆`17`
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) — ERC-20 token minting for AI agents ☆`22`
- [kukapay/rug-check-mcp](https://github.com/kukapay/rug-check-mcp) — An MCP server that detects potential risks in Solana meme tokens. ☆`21`
- [magnetai/mcp-free-usdc-transfer](https://github.com/magnetai/mcp-free-usdc-transfer) — Free USDC transfer via Coinbase CDP ☆`21`
- [janswist/mcp-dexscreener](https://github.com/janswist/mcp-dexscreener) — Dexscreener on-chain price checking ☆`19`
- [kukapay/crypto-rss-mcp](https://github.com/kukapay/crypto-rss-mcp) — Real-time cryptocurrency news from multiple RSS feeds ☆`17`
- [syronlabs/stellar-mcp](https://github.com/syronlabs/stellar-mcp) — A Stellar MCP to interact with Horizon API and Soroban ☆`18`
- [kukapay/defi-yields-mcp](https://github.com/kukapay/defi-yields-mcp) — DeFi yield opportunities powered by DefiLlama ☆`16`
- [kukapay/crypto-orderbook-mcp](https://github.com/kukapay/crypto-orderbook-mcp) — Order-book depth and imbalance on major crypto exchanges ☆`16`
### Payments & Banking

- [stripe/ai](https://github.com/stripe/ai) — One-stop shop for building AI-powered products and businesses with Stripe. ☆`1,852`
- [razorpay/razorpay-mcp-server](https://github.com/razorpay/razorpay-mcp-server) — Razorpay's Official MCP Server ☆`230`
- [paypal/agent-toolkit](https://github.com/paypal/agent-toolkit) — PayPal Agent ☆`195`
- [square/square-mcp-server](https://github.com/square/square-mcp-server) — A Model Context Protocol (MCP) server for square ☆`108`
- [PaddleHQ/paddle-mcp-server](https://github.com/PaddleHQ/paddle-mcp-server) — Interact with Paddle API ☆`49`
- [qonto/qonto-mcp-server](https://github.com/qonto/qonto-mcp-server) — Qonto MCP Server ☆`42`
- [atharvagupta2003/mcp-stripe](https://github.com/atharvagupta2003/mcp-stripe) — Stripe payments, customers, and refunds ☆`44`
- [Fewsats/fewsats-mcp](https://github.com/Fewsats/fewsats-mcp) — Fewsats MCP server ☆`21`
### Stock Data & Analytics

- [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) — Financial Datasets stock market API ☆`2,300`
- [massive-com/mcp_massive](https://github.com/massive-com/mcp_massive) — An MCP server for Massive.com Financial Market Data ☆`395`
- [stefanoamorelli/sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp) — A SEC EDGAR MCP (Model Context Protocol) Server ☆`362`
- [narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp) — MCP server for Yahoo Finance stock data and news ☆`196`
- [jjlabsio/korea-stock-mcp](https://github.com/jjlabsio/korea-stock-mcp) — MCP Server for Korean stock analysis ☆`177`
- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) — Public filings, earnings, financial analysis ☆`148`
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) — MCP server for BaoStock Chinese stock market data ☆`119`
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) — MCP Server for Alpha Advantage API ☆`104`
- [Adity-star/mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server) — Real-time stock data with yfinance ☆`54`
- [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) — Polymarket, PredictIt, Kalshi data ☆`37`
- [AgentX-ai/yahoo-finance-server](https://github.com/AgentX-ai/yahoo-finance-server) — Yahoo Finance stock data and news ☆`53`
- [zlinzzzz/finData-mcp-server](https://github.com/zlinzzzz/finData-mcp-server) — Financial data from Tushare, Wind, DataYes ☆`58`
- [Mrbaeksang/korea-stock-analyzer-mcp](https://github.com/Mrbaeksang/korea-stock-analyzer-mcp) — Korean stocks from DART filings and KRX quotes ☆`23`
- [OctagonAI/octagon-vc-agents](https://github.com/OctagonAI/octagon-vc-agents) — AI-driven venture capitalist agents ☆`33`
### Trading & Exchanges

- [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server) — Trade stocks, ETFs, crypto, options ☆`1,005`
- [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) — MetaTrader trading platform for AI LLMs ☆`815`
- [ferdousbhai/investor-agent](https://github.com/ferdousbhai/investor-agent) — Investor agent building via MCP ☆`347`
- [kukapay/freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp) — Freqtrade crypto trading bot ☆`146`
- [doggybee/mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt) — Cryptocurrency exchange integration via CCXT ☆`145`
- [taylorwilsdon/quantconnect-mcp](https://github.com/taylorwilsdon/quantconnect-mcp) — QuantConnect trading orchestration ☆`122`
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) — Let Claude manage your tastytrade portfolio. ☆`86`
- [QuantConnect/mcp-server](https://github.com/QuantConnect/mcp-server) — QuantConnect algo trading interaction ☆`77`
- [trade-it-inc/trade-it-mcp](https://github.com/trade-it-inc/trade-it-mcp) — Trade It stocks and crypto trading ☆`60`
- [ozgureyilmaz/polymarket-mcp](https://github.com/ozgureyilmaz/polymarket-mcp) — Polymarket prediction markets data ☆`48`
- [mektigboy/server-hyperliquid](https://github.com/mektigboy/server-hyperliquid) — Hyperliquid DEX trading integration ☆`44`
- [ethancod1ng/binance-mcp-server](https://github.com/ethancod1ng/binance-mcp-server) — Binance exchange API integration ☆`32`
- [laukikk/alpaca-mcp](https://github.com/laukikk/alpaca-mcp) — Alpaca stock and crypto trading ☆`35`
- [ferdousbhai/wsb-analyst-mcp](https://github.com/ferdousbhai/wsb-analyst-mcp) — MCP server for analyzing WallStreetBets ☆`30`
- [paperinvest/mcp-server](https://github.com/paperinvest/mcp-server) — Paper trading platform integration ☆`24`
- [solangii/upbit-mcp-server](https://github.com/solangii/upbit-mcp-server) — MCP(Model Context Protocol) server for Upbit ☆`17`
## Frameworks & SDKs

- [mastra-ai/mastra](https://github.com/mastra-ai/mastra) — TypeScript AI agent framework with RAG ☆`28,492`
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) — Build agents with MCP and workflow patterns ☆`8,567`
- [posit-dev/mcptools](https://github.com/posit-dev/mcptools) — Model Context Protocol For R ☆`198`
- [quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers) — Model Context Protocol Servers in Quarkus ☆`196`
- [agentrpc/agentrpc](https://github.com/agentrpc/agentrpc) — Universal RPC layer for AI agents ☆`135`
- [vishalmysore/a2ajava](https://github.com/vishalmysore/a2ajava) — Google A2A protocol for Spring Boot ☆`108`
- [strowk/foxy-contexts](https://github.com/strowk/foxy-contexts) — Library for MCP context servers ☆`114`
- [abap-ai/mcp](https://github.com/abap-ai/mcp) — ABAP MCP - Model Context Protocol - Server SDK ☆`85`
- [tesla0225/mcp-create](https://github.com/tesla0225/mcp-create) — Dynamic MCP server creation and management ☆`98`
- [mcpdotdirect/template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server) — Template to quickly set up your own MCP server ☆`76`
- [particlefuture/1mcpserver](https://github.com/particlefuture/1mcpserver) — Auto-discover and configure MCP servers ☆`53`
- [domdomegg/programmatic-mcp-prototype](https://github.com/domdomegg/programmatic-mcp-prototype) — Programmatic MCP tool composition ☆`43`
- [mojolicious/mojo-mcp](https://github.com/mojolicious/mojo-mcp) — Perl SDK for Model Context Protocol servers and clients ☆`21`
- [mcpx-dev/mcp-badges](https://github.com/mcpx-dev/mcp-badges) — Get your projects MCP (Model Context Protocol) badges ☆`30`
## Gaming

- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) — MCP server for Godot game engine ☆`5,907`
- [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) — AI-powered bridge connecting LLMs to Unity Editor ☆`4,373`
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) — MCP server for Unity game engine integration ☆`1,919`
- [IvanMurzak/Godot-MCP](https://github.com/IvanMurzak/Godot-MCP) — Godot 4.x editor and runtime for AI agents ☆`262`
- [playcanvas/editor-mcp-server](https://github.com/playcanvas/editor-mcp-server) — MCP Server for AI automation of the PlayCanvas Editor ☆`137`
- [quazaai/UnityMCPIntegration](https://github.com/quazaai/UnityMCPIntegration) — Enable AI Agents to Control Unity ☆`159`
- [pab1it0/chess-mcp](https://github.com/pab1it0/chess-mcp) — MCP server for Chess.com player data, games and statistics ☆`90`
- [codemaestroai/advanced-unity-mcp](https://github.com/codemaestroai/advanced-unity-mcp) — Advanced Unity game engine integration ☆`94`
- [kkjdaniel/bgg-mcp](https://github.com/kkjdaniel/bgg-mcp) — MCP server for BoardGameGeek data ☆`53`
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) — VRChat API interaction ☆`66`
- [IvanMurzak/Unreal-MCP](https://github.com/IvanMurzak/Unreal-MCP) — Unreal Engine 5.7 editor and runtime for AI agents ☆`40`
- [jalpp/chessagine-mcp](https://github.com/jalpp/chessagine-mcp) — Advanced chess analysis capabilities ☆`31`
- [jifrozen0110/mcp-riot](https://github.com/jifrozen0110/mcp-riot) — League of Legends MCP Server ☆`27`
- [jiayao/mcp-chess](https://github.com/jiayao/mcp-chess) — MCP server for playing chess against AI ☆`24`
## Healthcare & Bioinformatics

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) — BioMCP: Biomedical Model Context Protocol ☆`646`
- [the-momentum/apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server) — Apple Health data queries with DuckDB ☆`270`
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) — FHIR healthcare API integration ☆`137`
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) — MCP server for medical data processing ☆`114`
- [ChristianHinge/dicom-mcp](https://github.com/ChristianHinge/dicom-mcp) — DICOM server (PACS) interaction ☆`101`
- [the-momentum/fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server) — FHIR MCP Server for handling medical data standard. ☆`101`
- [cafferychen777/ChatSpatial](https://github.com/cafferychen777/ChatSpatial) — Spatial transcriptomics via natural language (Python/R) ☆`45`
- [akutishevsky/withings-mcp](https://github.com/akutishevsky/withings-mcp) — MCP server for Withings health data integration ☆`43`
- [srijanshukla18/xray](https://github.com/srijanshukla18/xray) — MCP server for X-ray analysis ☆`54`
- [OHNLP/omop_mcp](https://github.com/OHNLP/omop_mcp) — MCP server for OMOP medical data standard ☆`41`
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) — MCP (Model Context Protocol) server for biothings ☆`35`
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) — MCP server for Oura API integration ☆`39`
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) — Bioinformatic gget functions ☆`32`
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) — MCP for the open-genes ☆`21`
## LLM Bridges

- [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol) — Official Perplexity API MCP server ☆`2,550`
- [jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool) — MCP server for Gemini CLI with large file analysis ☆`2,287`
- [DMontgomery40/deepseek-mcp-server](https://github.com/DMontgomery40/deepseek-mcp-server) — MCP server for DeepSeek language models ☆`352`
- [nesquikm/mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck) — MCP bridge to query multiple OpenAI-compatible LLMs ☆`177`
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) — MCP Server for using any LLM as a Tool ☆`165`
- [eLyiN/gemini-bridge](https://github.com/eLyiN/gemini-bridge) — Bridge AI agents to Google Gemini via CLI ☆`96`
- [choplin/mcp-gemini-cli](https://github.com/choplin/mcp-gemini-cli) — MCP server for Gemini CLI integration ☆`101`
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) — Query OpenAI models from Claude via MCP ☆`84`
- [merterbak/Grok-MCP](https://github.com/merterbak/Grok-MCP) — MCP server for xAI Grok API with tool calling and vision ☆`52`
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) — Chat with OpenAI models from Claude Desktop ☆`76`
- [ruixingshi/deepseek-thinker-mcp](https://github.com/ruixingshi/deepseek-thinker-mcp) — DeepSeek reasoning for MCP-enabled clients ☆`70`
- [kamelirzouni/MCP-server-Deepseek_R1](https://github.com/kamelirzouni/MCP-server-Deepseek_R1) — Connect Claude Desktop with DeepSeek ☆`69`
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) — Unified chat across multiple LLM providers ☆`40`
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) — Use OpenAI GPTs assistants from Claude ☆`39`
- [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) — ChatGPT, Claude, Gemini, Mistral, Kimi, and DeepSeek APIs ☆`16`
- [billster45/mcp-chatgpt-responses](https://github.com/billster45/mcp-chatgpt-responses) — MCP server for OpenAI ChatGPT API with Responses API ☆`24`
- [kamelirzouni/MCP-server-Qwen_Max](https://github.com/kamelirzouni/MCP-server-Qwen_Max) — MCP server for Qwen Max model ☆`24`
- [HyperbolicLabs/hyperbolic-mcp](https://github.com/HyperbolicLabs/hyperbolic-mcp) — MCP Server for Claude ☆`18`
## Location & Maps

### GIS

- [jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp) — QGIS Desktop control for language models ☆`1,114`
- [mahdin75/gis-mcp](https://github.com/mahdin75/gis-mcp) — MCP server connecting LLMs to GIS capabilities ☆`194`
- [mahdin75/geoserver-mcp](https://github.com/mahdin75/geoserver-mcp) — GeoServer geospatial integration ☆`92`
- [JordanGunn/gdal-mcp](https://github.com/JordanGunn/gdal-mcp) — Geospatial analysis with epistemic reasoning ☆`81`
- [BnJam/stac-mcp](https://github.com/BnJam/stac-mcp) — An MCP Server for STAC requests ☆`18`
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) — Geocoding MCP server with GeoPY! ☆`34`
### IP Geolocation

- [briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) — IP Geolocation Server for MCP using ipinfo.io ☆`44`
- [ip2location/mcp-ip2location-io](https://github.com/ip2location/mcp-ip2location-io) — IP Geolocation MCP server using IP2Location.io API ☆`17`
- [iplocate/mcp-server-iplocate](https://github.com/iplocate/mcp-server-iplocate) — IP geolocation, proxy detection via IPLocate.io API ☆`20`
### Maps & Navigation

- [baidu-maps/mcp](https://github.com/baidu-maps/mcp) — Baidu Map MCP Server ☆`445`
- [mapbox/mcp-server](https://github.com/mapbox/mcp-server) — Mapbox Model Context Protocol (MCP) server ☆`358`
- [jagan-shanmugam/open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) — MCP server for OpenStreetMap data ☆`226`
- [tomtom-international/tomtom-maps-mcp](https://github.com/tomtom-international/tomtom-maps-mcp) — TomTom location, search, routing ☆`55`
- [stadiamaps/stadiamaps-mcp-server-ts](https://github.com/stadiamaps/stadiamaps-mcp-server-ts) — Stadia Maps API integration in TypeScript ☆`25`
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) — Nearby place search with IP-based location ☆`22`
### Weather

- [isdaniel/mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) — Weather info via Open-Meteo API ☆`61`
- [TimLukaHorstmann/mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather) — AccuWeather hourly and daily forecasts ☆`34`
- [sjanaX01/weather-mcp-server](https://github.com/sjanaX01/weather-mcp-server) — A simple minimal weather mcp server :) ☆`24`
- [mschneider82/mcp-openweather](https://github.com/mschneider82/mcp-openweather) — mcp server for openweather free api ☆`21`
## MCP Clients

- [Upsonic/Upsonic](https://github.com/Upsonic/Upsonic) — Build autonomous AI agents in Python. ☆`7,956`
- [genkit-ai/genkit](https://github.com/genkit-ai/genkit) — AI app framework for JavaScript and Go ☆`6,465`
- [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) — MCP client for Neovim with intuitive server management ☆`1,784`
- [ASCIT31/Dark-Moon](https://github.com/ASCIT31/Dark-Moon) — Autonomous pentest host for 80+ security tools ☆`986`
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) — OpenAI-compatible endpoint calling MCP tools ☆`928`
- [aeonfun/aeon](https://github.com/aeonfun/aeon) — GitHub Actions agents with OAuth to remote MCP servers ☆`760`
- [mario-andreschak/FLUJO](https://github.com/mario-andreschak/FLUJO) — Local visual agent builder with MCP and multi-model chat ☆`629`
- [Lucassssss/eechat](https://github.com/Lucassssss/eechat) — Local AI chat application ☆`350`
- [3choff/mcp-chatbot](https://github.com/3choff/mcp-chatbot) — CLI chatbot with MCP integration demo ☆`251`
- [EvalsOne/MCP-connect](https://github.com/EvalsOne/MCP-connect) — Cloud AI access to local Stdio MCP servers ☆`240`
- [AI-QL/chat-mcp](https://github.com/AI-QL/chat-mcp) — Desktop chat app with MCP support ☆`240`
- [johannesbrandenburger/typst-mcp](https://github.com/johannesbrandenburger/typst-mcp) — MCP server for Typst markup-based typesetting system ☆`182`
- [off-grid-ai/OGAD](https://github.com/off-grid-ai/OGAD) — On-device MCP client for Mac with a local LLM ☆`116`
- [tanaikech/ToolsForMCPServer](https://github.com/tanaikech/ToolsForMCPServer) — MCP server built with Google Apps Script for Gemini CLI ☆`106`
- [ckanthony/gin-mcp](https://github.com/ckanthony/gin-mcp) — Enable MCP features for any Gin API with a line of code ☆`85`
- [xzq-xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server) — JVM-based MCP server implementation ☆`90`
- [php-mcp/client](https://github.com/php-mcp/client) — Core PHP implementation for the Model Context Protocol (MCP) Client ☆`58`
- [zacharypodbela/django-rest-framework-mcp](https://github.com/zacharypodbela/django-rest-framework-mcp) — MCP server for Django REST Framework ☆`54`
- [rakesh-eltropy/mcp-client](https://github.com/rakesh-eltropy/mcp-client) — REST API and CLI client for MCP with LangChain ☆`49`
## Marketing & Analytics

- [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) — SEO, GEO, ads, Search Console, and Analytics skills ☆`3,886`
- [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) — Google Ads diagnosis, recommendations, and edits ☆`3,886`
- [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) — Hosted Facebook and Instagram Ads for AI agents ☆`1,286`
- [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) — Facebook and Instagram Ads management ☆`366`
- [proxy-intell/facebook-ads-library-mcp](https://github.com/proxy-intell/facebook-ads-library-mcp) — Facebook Ads Library search and access ☆`307`
- [open-strategy-partners/osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools) — MCP server for marketing automation tools ☆`272`
- [surendranb/google-analytics-mcp](https://github.com/surendranb/google-analytics-mcp) — Google Analytics 4 data access ☆`242`
- [cnych/seo-mcp](https://github.com/cnych/seo-mcp) — SEO tool based on Ahrefs data ☆`261`
- [stape-io/google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server) — MCP server for Google Tag Manager ☆`222`
- [gomarble-ai/google-ads-mcp-server](https://github.com/gomarble-ai/google-ads-mcp-server) — Google Ads performance data analysis ☆`145`
- [microsoft/clarity-mcp-server](https://github.com/microsoft/clarity-mcp-server) — Microsoft Clarity integration ☆`120`
- [amekala/ads-mcp](https://github.com/amekala/ads-mcp) — Google, Meta, LinkedIn, and TikTok campaign management ☆`97`
- [AdsMCP/tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) — TikTok Ads Marketing API integration via MCP ☆`49`
- [builtwith/builtwith-mcp](https://github.com/builtwith/builtwith-mcp) — BuiltWith MCP Server ☆`41`
- [gvaibhav/TAM-MCP-Server](https://github.com/gvaibhav/TAM-MCP-Server) — Market sizing and TAM/SAM analysis ☆`36`
- [stape-io/stape-mcp-server](https://github.com/stape-io/stape-mcp-server) — Stape API for Claude, Cursor, and other AI clients ☆`17`
- [Kiran1689/storyblok-mcp-server](https://github.com/Kiran1689/storyblok-mcp-server) — MCP server for Storyblok CMS management ☆`41`
- [rafaelstz/adobe-commerce-dev-mcp](https://github.com/rafaelstz/adobe-commerce-dev-mcp) — Adobe Commerce Dev MCP Server ☆`27`
- [MarketplaceAdPros/amazon-ads-mcp-server](https://github.com/MarketplaceAdPros/amazon-ads-mcp-server) — MCP Server to interact with Amazon Ads ☆`29`
- [jonathan-politzki/smartlead-mcp-server](https://github.com/jonathan-politzki/smartlead-mcp-server) — Smartlead MCP deployment ☆`18`
## Media Processing

### 3D & Animation

- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) — MCP server integration for DaVinci Resolve Studio ☆`3,282`
- [ATH-MaaS/Pixelle-MCP](https://github.com/ATH-MaaS/Pixelle-MCP) — Multimodal AIGC with ComfyUI + MCP ☆`1,120`
- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) — Manim animation code execution ☆`646`
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) — MCP server for interacting with the Aseprite API ☆`619`
- [8beeeaaat/touchdesigner-mcp](https://github.com/8beeeaaat/touchdesigner-mcp) — MCP server for TouchDesigner ☆`560`
- [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) — Autodesk Maya 3D integration ☆`105`
- [pranav-deshmukh/blender-mcp](https://github.com/pranav-deshmukh/blender-mcp) — Blender 3D modeling integration ☆`98`
- [wilsonchenghy/ShaderToy-MCP](https://github.com/wilsonchenghy/ShaderToy-MCP) — Create and explore GLSL shaders on ShaderToy ☆`50`
- [junmer/mcp-server-lottiefiles](https://github.com/junmer/mcp-server-lottiefiles) — Search and retrieve Lottie animations from LottieFiles ☆`19`
### Audio & Music

- [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) — MCP to connect your LLM with Spotify. ☆`615`
- [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) — Lightweight MCP server for Spotify ☆`470`
- [Simon-Kansara/ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server) — Ableton Live OSC control ☆`395`
- [adamjmurray/producer-pal](https://github.com/adamjmurray/producer-pal) — AI music production assistant for Ableton Live ☆`313`
- [tiianhk/MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server) — MCP (Model Context Protocol) Server for Max (Max/MSP/Jitter) ☆`277`
- [dschuler36/reaper-mcp-server](https://github.com/dschuler36/reaper-mcp-server) — An MCP Server for interacting with Reaper projects. ☆`124`
- [SkyworkAI/Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp) — AI lyrics, song, and music generation ☆`117`
- [TwelveTake-Studios/reaper-mcp](https://github.com/TwelveTake-Studios/reaper-mcp) — REAPER DAW mixing, mastering, MIDI, and production ☆`73`
- [imprvhub/mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify) — Spotify interaction for Claude Desktop ☆`50`
- [vsaez/mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player) — MCP server to manage Spotify from MCP clients ☆`22`
### Image Generation

- [shinpr/mcp-image](https://github.com/shinpr/mcp-image) — AI image generation with Gemini 3 ☆`168`
- [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) — MCP server for Replicate Flux image and SVG generation ☆`106`
- [GenWaveLLC/svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp) — MCP server for SVG generation ☆`87`
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) — PiAPI media: Midjourney, Flux, Kling ☆`75`
- [Flyworks-AI/flyworks-mcp](https://github.com/Flyworks-AI/flyworks-mcp) — Fast and free zeroshot lipsync MCP server ☆`94`
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) — MCP server for Google Imagen 3 image generation ☆`71`
- [WaveSpeedAI/mcp-server](https://github.com/WaveSpeedAI/mcp-server) — Image and video generation with WaveSpeed AI ☆`33`
- [MohamedAbdallah-14/prompt-to-asset](https://github.com/MohamedAbdallah-14/prompt-to-asset) — Images from 30+ models through one API ☆`20`
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) — High-performance image compression service ☆`34`
- [zxkane/mcp-server-amazon-bedrock](https://github.com/zxkane/mcp-server-amazon-bedrock) — Amazon Bedrock Nova Canvas image generation ☆`25`
### Image Processing

- [openclaw/Peekaboo](https://github.com/openclaw/Peekaboo) — macOS screenshot and window capture MCP server ☆`5,237`
- [sunriseapps/imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp) — Image processing operations ☆`333`
- [IDEA-Research/DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP) — MCP server for DINO-X vision model ☆`113`
- [upnorthmedia/ScreenshotMCP](https://github.com/upnorthmedia/ScreenshotMCP) — Website screenshot capture and optimization ☆`61`
- [screenshotone/mcp](https://github.com/screenshotone/mcp) — A CLI version of an MCP server for the ScreenshotOne API ☆`38`
- [groundlight/mcp-vision](https://github.com/groundlight/mcp-vision) — Computer vision models as MCP servers ☆`62`
- [nota/gyazo-mcp-server](https://github.com/nota/gyazo-mcp-server) — Official Model Context Protocol server for Gyazo ☆`29`
- [MoussaabBadla/code-screenshot-mcp](https://github.com/MoussaabBadla/code-screenshot-mcp) — Generate code screenshots ☆`45`
- [stass/exif-mcp](https://github.com/stass/exif-mcp) — MCP server to extract image metadata (EXIF, XMP, etc) ☆`39`
- [magarcia/mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy) — Giphy GIF integration ☆`35`
- [flowy11/imagician](https://github.com/flowy11/imagician) — A MCP server for image edition ☆`19`
### Media Services

- [garylab/pexels-mcp-server](https://github.com/garylab/pexels-mcp-server) — A Pexels MCP Server for Images and Videos searching ☆`25`
### Video

- [eat-pray-ai/yutu](https://github.com/eat-pray-ai/yutu) — The AI-powered toolkit that grows your YouTube channel on autopilot. ☆`696`
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) — YouTube video transcript downloader ☆`598`
- [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) — YouTube API and video management ☆`577`
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) — A Model-Context Protocol Server for YouTube ☆`546`
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) — MCP Interface for Video Jungle ☆`290`
- [muxinc/mux-ts](https://github.com/muxinc/mux-ts) — Mux Video and Data API wrapper ☆`181`
- [tan-yong-sheng/ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp) — Image and video analysis capabilities ☆`79`
- [Laksh-star/mcp-server-tmdb](https://github.com/Laksh-star/mcp-server-tmdb) — MCP Server with TMDB ☆`76`
- [luminarylane/fal-mcp-server](https://github.com/luminarylane/fal-mcp-server) — Fal.ai image, video, music generation ☆`57`
- [nabid-pf/youtube-video-summarizer-mcp](https://github.com/nabid-pf/youtube-video-summarizer-mcp) — YouTube video captions and summarization ☆`62`
- [video-db/agent-toolkit](https://github.com/video-db/agent-toolkit) — MCP toolkit for video database operations ☆`47`
- [marcindulak/stt-mcp-server-linux](https://github.com/marcindulak/stt-mcp-server-linux) — Local speech-to-text for Tmux on Linux ☆`24`
- [omergocmen/json2video-mcp-server](https://github.com/omergocmen/json2video-mcp-server) — json2video API integration ☆`26`
- [sinjab/mcp_youtube_extract](https://github.com/sinjab/mcp_youtube_extract) — YouTube clip information extraction ☆`19`
- [TSavo/creatify-mcp](https://github.com/TSavo/creatify-mcp) — MCP server for AI video generation ☆`23`
- [13rac1/videocapture-mcp](https://github.com/13rac1/videocapture-mcp) — MCP server to capture images from webcam or video source ☆`19`
## Monitoring & Observability

- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) — MCP server for Grafana ☆`3,521`
- [getsentry/toolkit](https://github.com/getsentry/toolkit) — Agentic tooling for Sentry ☆`885`
- [mpeirone/zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server) — MCP server for Zabbix monitoring with 40+ tools ☆`256`
- [VictoriaMetrics/mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics) — VictoriaMetrics monitoring integration ☆`237`
- [comet-ml/opik-mcp](https://github.com/comet-ml/opik-mcp) — MCP server for Opik LLM evaluation platform ☆`220`
- [grafana/loki-mcp](https://github.com/grafana/loki-mcp) — An MCP ( Model Context Protocol ) Server for Grafana Loki ☆`174`
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) — The Logfire MCP Server is here! ☆`161`
- [langfuse/mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse) — MCP server for Langfuse LLM observability ☆`173`
- [prometheus/prometheus-mcp](https://github.com/prometheus/prometheus-mcp) — MCP server for LLMs to interact with Prometheus ☆`115`
- [Necmttn/ax](https://github.com/Necmttn/ax) — Local observability for agent sessions, tools, and costs ☆`114`
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) — MCP server monitoring tool ☆`91`
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) — Last9 MCP Server ☆`62`
- [mcpcap/mcpcap](https://github.com/mcpcap/mcpcap) — Network analysis for the AI age ☆`51`
- [GeLi2001/datadog-mcp-server](https://github.com/GeLi2001/datadog-mcp-server) — MCP server interacts with the official Datadog API ☆`69`
- [rootlyhq/rootly-mcp-server](https://github.com/rootlyhq/rootly-mcp-server) — Rootly MCP server ☆`45`
- [mhajder/librenms-mcp](https://github.com/mhajder/librenms-mcp) — MCP server for LibreNMS management ☆`39`
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) — Metoro MCP Server ☆`51`
- [RedHatInsights/insights-mcp](https://github.com/RedHatInsights/insights-mcp) — Red Hat Insights AI connection ☆`25`
- [inspektor-gadget/ig-mcp-server](https://github.com/inspektor-gadget/ig-mcp-server) — Container and Kubernetes debugging with AI ☆`27`
- [ntk148v/alertmanager-mcp-server](https://github.com/ntk148v/alertmanager-mcp-server) — MCP server for Prometheus Alertmanager integration ☆`25`
- [MindscapeHQ/mcp-server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) — Raygun error investigation for AI ☆`22`
- [gologinapp/gologin-mcp](https://github.com/gologinapp/gologin-mcp) — Manage GoLogin browser profiles, proxies, and fingerprints ☆`22`
- [emicklei/mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy) — a web logging proxy for MCP client-server communication ☆`32`
- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) — Grafana Loki MCP Repository ☆`29`
- [tgeselle/bugsnag-mcp](https://github.com/tgeselle/bugsnag-mcp) — MCP server for Bugsnag error monitoring ☆`24`
- [Pratyay/mac-monitor-mcp](https://github.com/Pratyay/mac-monitor-mcp) — MCP server for macOS system monitoring ☆`23`
- [iLert/mcp-ilert](https://github.com/iLert/mcp-ilert) — MCP server for ilert ☆`17`
## Productivity

### Atlassian

- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) — MCP server for Atlassian tools (Confluence, Jira) ☆`5,962`
- [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) — Atlassian Bitbucket repositories and PRs ☆`162`
- [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) — Jira issues and sprints via Go MCP ☆`97`
- [aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira) — Atlassian Jira projects, issues and sprints ☆`77`
- [aashari/mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence) — Atlassian Confluence spaces and pages ☆`62`
- [phuc-nt/mcp-atlassian-server](https://github.com/phuc-nt/mcp-atlassian-server) — Jira and Confluence integration ☆`52`
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) — A test of jira mcp server ☆`26`
- [rahulthedevil/Jira-Context-MCP](https://github.com/rahulthedevil/Jira-Context-MCP) — Jira tickets info for AI coding agents ☆`26`
### Collaboration

- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) — MCP server for Miro whiteboard manipulation and sticky creation ☆`112`
- [k-jarzyna/mcp-miro](https://github.com/k-jarzyna/mcp-miro) — Miro integration for Model Context Protocol ☆`66`
- [kintone/mcp-server](https://github.com/kintone/mcp-server) — kintone official MCP server ☆`57`
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) — Raindrop.io bookmark management ☆`74`
- [orellazri/coda-mcp](https://github.com/orellazri/coda-mcp) — MCP Server for Coda ☆`63`
- [Fibery-inc/fibery-mcp-server](https://github.com/Fibery-inc/fibery-mcp-server) — MCP server for Fibery workspace integration ☆`29`
### Documents

- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) — Convert almost anything to Markdown ☆`2,997`
- [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) — MCP server for document format conversion using pandoc. ☆`582`
- [onebirdrocks/ebook-mcp](https://github.com/onebirdrocks/ebook-mcp) — MCP server for ebook processing ☆`396`
- [baruchiro/paperless-mcp](https://github.com/baruchiro/paperless-mcp) — MCP server for Paperless-NGX document management ☆`146`
- [PSPDFKit/nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server) — Nutrient Document Web Services ☆`71`
- [vgnshiyer/apple-books-mcp](https://github.com/vgnshiyer/apple-books-mcp) — Apple Books MCP Server ☆`60`
- [Unstructured-IO/UNS-MCP](https://github.com/Unstructured-IO/UNS-MCP) — MCP server for Unstructured document processing ☆`43`
- [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) — eSignatures.com document signing ☆`40`
- [thechandanbhagat/cv-forge](https://github.com/thechandanbhagat/cv-forge) — ATS-friendly CVs, cover letters, and job-tailored emails ☆`30`
- [danielkennedy1/pdf-tools-mcp](https://github.com/danielkennedy1/pdf-tools-mcp) — MCP server for PDF manipulation (merge, extract, snippets) ☆`32`
- [gpetraroli/mcp_pdf_reader](https://github.com/gpetraroli/mcp_pdf_reader) — An MCP server to extraxt/search text from pdf ☆`32`
- [intsig-textin/textin-mcp](https://github.com/intsig-textin/textin-mcp) — OCR and document-to-Markdown conversion ☆`29`
- [Sohaib-2/pdf-mcp-server](https://github.com/Sohaib-2/pdf-mcp-server) — Comprehensive PDF manipulation toolkit. Merge, split, encrypt, optimize PDFs through natural language commands via MCP protocol. ☆`16`
### Google Workspace

- [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) — MCP server for Google Workspace integration ☆`3,274`
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) — MCP Server to interact with Google Gsuite prodcuts ☆`490`
- [v-3/google-calendar](https://github.com/v-3/google-calendar) — Google Calendar events and scheduling ☆`72`
- [baryhuang/mcp-headless-gmail](https://github.com/baryhuang/mcp-headless-gmail) — Gmail without local credentials ☆`55`
- [giuseppe-coco/Google-Workspace-MCP-Server](https://github.com/giuseppe-coco/Google-Workspace-MCP-Server) — Gmail, Calendar, and Drive integration ☆`30`
- [vakharwalad23/google-mcp](https://github.com/vakharwalad23/google-mcp) — Gmail, Calendar, and other Google workspace tools ☆`21`
### Helpdesk & Support

- [echelon-ai-labs/servicenow-mcp](https://github.com/echelon-ai-labs/servicenow-mcp) — MCP Server for ServiceNow ☆`298`
- [effytech/freshdesk_mcp](https://github.com/effytech/freshdesk_mcp) — Freshdesk support ticket integration ☆`69`
- [modesty/fluent-mcp](https://github.com/modesty/fluent-mcp) — MCP server for Fluent (ServiceNow SDK) ☆`31`
- [quickchatai/quickchat-ai-mcp](https://github.com/quickchatai/quickchat-ai-mcp) — The Quickchat AI MCP server ☆`24`
### Learning & Flashcards

- [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) — MCP server for Anki spaced repetition flashcards ☆`502`
- [scorzeth/anki-mcp-server](https://github.com/scorzeth/anki-mcp-server) — An MCP server for Anki ☆`184`
- [jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) — MCP server for LeetCode problems and solutions ☆`152`
- [nietus/anki-mcp](https://github.com/nietus/anki-mcp) — MCP server for anki ☆`39`
- [rember/rember-mcp](https://github.com/rember/rember-mcp) — A Model Context Protocol (MCP) server for Rember. ☆`63`
- [doggybee/mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode) — MCP server for LeetCode coding challenges ☆`43`
- [spacholski1225/anki-connect-mcp](https://github.com/spacholski1225/anki-connect-mcp) — MCP implementation for Anki Web ☆`24`
### Microsoft 365

- [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) — Excel file manipulation ☆`4,208`
- [Softeria/ms-365-mcp-server](https://github.com/Softeria/ms-365-mcp-server) — Microsoft 365 and Office via Graph API ☆`1,006`
- [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) — Excel MCP Server - 23 tools for AI-powered automation ☆`799`
- [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) — MCP server for Microsoft Teams integration ☆`409`
- [merill/lokka](https://github.com/merill/lokka) — MCP for Microsoft 365 and Graph ☆`301`
- [pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server) — Manage Microsoft 365 using MCP server ☆`131`
- [Norcim133/OutlookMCPServer](https://github.com/Norcim133/OutlookMCPServer) — MCP Server for msgraph - mail, calendar, files ☆`16`
### Note-taking & Docs

- [RafalWilinski/mcp-apple-notes](https://github.com/RafalWilinski/mcp-apple-notes) — RAG over Apple Notes for Claude ☆`415`
- [lostintangent/gistpad-mcp](https://github.com/lostintangent/gistpad-mcp) — Personal knowledge and daily notes management ☆`208`
- [Vortiago/mcp-outline](https://github.com/Vortiago/mcp-outline) — AI assistants with Outline docs ☆`156`
- [entanglr/zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp) — MCP server implementing Zettelkasten knowledge management ☆`164`
- [gornskew/cyborg-whisperer](https://github.com/gornskew/cyborg-whisperer) — Manage Lisply lisp-speaking backends ☆`54`
- [2slides/mcp-2slides](https://github.com/2slides/mcp-2slides) — MCP Server for 2slides - AI agent for PPT generation ☆`32`
- [ONLYOFFICE/docspace-mcp](https://github.com/ONLYOFFICE/docspace-mcp) — DocSpace MCP Server ☆`31`
- [Piotr1215/mcp-obsidian](https://github.com/Piotr1215/mcp-obsidian) — simple mcp server for interacting with local obsidian notes ☆`23`
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) — MCP Server integration for Bear note app ☆`45`
- [joshylchen/zettelkasten](https://github.com/joshylchen/zettelkasten) — Zettelkasten notes with search, links, CLI, API, and web ☆`39`
- [danield137/mcp-workflowy](https://github.com/danield137/mcp-workflowy) — An MCP server for workflowy ☆`28`
- [Harry-027/JotDown](https://github.com/Harry-027/JotDown) — An MCP Server in Rust for creating Notion pages & mdBooks with LLMs ☆`23`
- [louis030195/easy-obsidian-mcp](https://github.com/louis030195/easy-obsidian-mcp) — wire your brain to AGI through the best obsidian MCP ☆`18`
### Notion

- [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) — Official Notion MCP Server ☆`4,655`
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) — MCP server for Notion API with Markdown conversion ☆`919`
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) — Notion integration with advanced formatting ☆`208`
- [Badhansen/notion-mcp](https://github.com/Badhansen/notion-mcp) — Notion workspace management ☆`31`
### Obsidian

- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) — Obsidian integration via REST API plugin ☆`4,458`
- [bitbonsai/mcpvault](https://github.com/bitbonsai/mcpvault) — Lightweight Obsidian vault access ☆`1,676`
- [StevenStavrakis/obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) — A simple MCP server for Obsidian ☆`737`
### Project Management

- [mondaycom/mcp](https://github.com/mondaycom/mcp) — AI agents with secure data access ☆`427`
- [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) — Plane's Official Model Context Protocol Server ☆`334`
- [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) — MCP server for Linear issue tracking ☆`347`
- [taskade/mcp](https://github.com/taskade/mcp) — MCP server for Taskade project management ☆`165`
- [tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) — MCP server for Linear project management ☆`146`
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) — MCP server for Asana task and project management ☆`148`
- [its-dart/dart-mcp-server](https://github.com/its-dart/dart-mcp-server) — Dart AI Model Context Protocol (MCP) server ☆`128`
- [aikts/yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp) — Yandex Tracker MCP Server with OAuth2 support ☆`121`
- [feuerdev/keep-mcp](https://github.com/feuerdev/keep-mcp) — MCP server for Google Keep ☆`104`
- [georgeantonopoulos/Basecamp-MCP-Server](https://github.com/georgeantonopoulos/Basecamp-MCP-Server) — Basecamp 3+ project management ☆`101`
- [tonyzorin/youtrack-mcp](https://github.com/tonyzorin/youtrack-mcp) — YouTrack server, ARM64 and AMD64 ☆`98`
- [taazkareem/clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server) — ClickUp MCP Server - project management with AI ☆`52`
- [m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server) — A simple yet powerful MCP server for Trello. ☆`54`
- [EduBase/MCP](https://github.com/EduBase/MCP) — MCP server for EduBase e-learning platform ☆`29`
- [Teamwork/mcp](https://github.com/Teamwork/mcp) — Teamwork.com MCP server ☆`26`
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) — MCP server for Plane.so project management ☆`40`
- [kocakli/Trello-Desktop-MCP](https://github.com/kocakli/Trello-Desktop-MCP) — Trello integration for Claude Desktop via MCP ☆`38`
- [bivex/kanboard-mcp](https://github.com/bivex/kanboard-mcp) — MCP server for Kanboard project management integration ☆`28`
- [Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday) — MCP Server to interact with Monday.com boards and items ☆`34`
- [khaoss85/mcp-orchestro](https://github.com/khaoss85/mcp-orchestro) — Task breakdown, dependencies, and progress for AI teams ☆`16`
### Tasks & Calendar

- [screenpipe/screenpipe](https://github.com/screenpipe/screenpipe) — Searchable screen text and audio history via MCP; source-available under the Screenpipe Commercial License ☆`21,796`
- [nspady/google-calendar-mcp](https://github.com/nspady/google-calendar-mcp) — MCP integration for Google Calendar to manage events. ☆`1,193`
- [Doist/todoist-mcp](https://github.com/Doist/todoist-mcp) — Todoist tools for AI agents ☆`553`
- [abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server) — Todoist natural language task management ☆`393`
- [Omar-V2/mcp-ical](https://github.com/Omar-V2/mcp-ical) — Interact with MacOS Calendar ☆`331`
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) — A Google Tasks Model Context Protocol Server for Claude ☆`167`
- [dominik1001/caldav-mcp](https://github.com/dominik1001/caldav-mcp) — CalDAV calendar sync ☆`102`
- [alexarevalo9/ticktick-mcp-server](https://github.com/alexarevalo9/ticktick-mcp-server) — TickTick task management ☆`73`
- [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) — Google Calendar for Claude Desktop ☆`59`
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) — MCP server for Google Tasks management ☆`50`
- [stanislavlysenko0912/todoist-mcp-server](https://github.com/stanislavlysenko0912/todoist-mcp-server) — Todoist Rest API and Sync API ☆`63`
- [flesler/mcp-tasks](https://github.com/flesler/mcp-tasks) — Efficient task management with views ☆`47`
- [jen6/ticktick-mcp](https://github.com/jen6/ticktick-mcp) — TickTick task management with filtering ☆`66`
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) — MCP Server for TaskWarrior! ☆`51`
- [urbanogardun/things3-mcp](https://github.com/urbanogardun/things3-mcp) — MCP server for Things3 integration on macOS ☆`24`
- [jbrinkman/valkey-ai-tasks](https://github.com/jbrinkman/valkey-ai-tasks) — MCP server for task management with Valkey persistence ☆`25`
- [hichana/goalstory-mcp](https://github.com/hichana/goalstory-mcp) — Goal tracking with AI-powered storytelling ☆`18`
- [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) — Cal.com event types, bookings, and schedule data ☆`19`
### Wiki & Collaboration

- [anyproto/anytype-mcp](https://github.com/anyproto/anytype-mcp) — AI with Anytype encrypted local data ☆`528`
- [ProfessionalWiki/MediaWiki-MCP-Server](https://github.com/ProfessionalWiki/MediaWiki-MCP-Server) — Connect AI with any MediaWiki ☆`136`
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) — HackMD note-taking integration ☆`67`
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) — Yuque mcp server ☆`69`
- [growilabs/growi-mcp-server](https://github.com/growilabs/growi-mcp-server) — GROWI wiki search and retrieval for AI answers ☆`20`
## Research & Science

- [oOo0oOo/lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) — Lean Theorem Prover MCP ☆`522`
- [szeider/mcp-solver](https://github.com/szeider/mcp-solver) — Constraint optimization and solving ☆`182`
- [NellyW8/MCP4EDA](https://github.com/NellyW8/MCP4EDA) — RTL-to-GDSII automation with LLM ☆`112`
- [Pantheon-Security/notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure) — Secure NotebookLM MCP with 14 security layers ☆`85`
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) — Wolfram Alpha computational intelligence ☆`75`
- [neuromechanist/matlab-mcp-tools](https://github.com/neuromechanist/matlab-mcp-tools) — MATLAB pipelines by section and figure inspection ☆`19`
## Sandboxing & Execution

- [superradcompany/microsandbox](https://github.com/superradcompany/microsandbox) — easy, fast, programmable and local-first microVM runtime ☆`8,506`
- [dagger/container-use](https://github.com/dagger/container-use) — MCP server for container orchestration ☆`4,053`
- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) — Sandboxed local agent runtime with approvals and audit ☆`679`
- [Automata-Labs-team/code-sandbox-mcp](https://github.com/Automata-Labs-team/code-sandbox-mcp) — Secure code sandbox in Docker ☆`327`
- [bazinga012/mcp_code_executor](https://github.com/bazinga012/mcp_code_executor) — Execute Python in Conda environment ☆`212`
- [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp) — MCP server for Node.js code sandbox execution ☆`157`
- [hopx-ai/mcp](https://github.com/hopx-ai/mcp) — Execute code in isolated cloud containers ☆`156`
- [gradion-ai/ipybox](https://github.com/gradion-ai/ipybox) — Python code execution sandbox with MCP tool calling ☆`75`
- [r33drichards/mcp-js](https://github.com/r33drichards/mcp-js) — MCP server exposing V8 JavaScript runtime for AI agents ☆`57`
- [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) — JavaScript MCP server framework by YepCode ☆`46`
- [hileamlakB/Python-Runtime-Interpreter-MCP-Server](https://github.com/hileamlakB/Python-Runtime-Interpreter-MCP-Server) — Safe Python runtime interpreter ☆`28`
- [gwbischof/outsource-mcp](https://github.com/gwbischof/outsource-mcp) — Give your AI assistant its own AI assistants. ☆`30`
## Search & Extraction

### Academic Research

- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) — arXiv paper search and analysis ☆`3,185`
- [JackKuo666/Google-Scholar-MCP-Server](https://github.com/JackKuo666/Google-Scholar-MCP-Server) — Search Google Scholar papers ☆`410`
- [reading-plus-ai/mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research) — Comprehensive research with reports ☆`215`
- [adityak74/mcp-scholarly](https://github.com/adityak74/mcp-scholarly) — A MCP server to search for accurate academic articles. ☆`186`
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) — arXiv paper search and reading ☆`201`
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) — PubMed medical research search ☆`172`
- [takashiishida/arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp) — MCP server for arXiv LaTeX paper retrieval ☆`146`
- [kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) — Zotero collections for Claude Desktop ☆`164`
- [JackKuo666/PubMed-MCP-Server](https://github.com/JackKuo666/PubMed-MCP-Server) — Search and analyze PubMed articles ☆`129`
- [OctagonAI/octagon-deep-research-mcp](https://github.com/OctagonAI/octagon-deep-research-mcp) — AI-powered comprehensive research and analysis ☆`93`
- [akalaric/mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha) — Wolfram Alpha integration for Python ☆`86`
- [HzaCode/OneCite](https://github.com/HzaCode/OneCite) — Parse and format academic references ☆`67`
- [szeider/mcp-dblp](https://github.com/szeider/mcp-dblp) — Access DBLP computer science bibliography ☆`45`
- [drAbreu/alex-mcp](https://github.com/drAbreu/alex-mcp) — MCP server for OpenAlex ☆`56`
- [prashalruchiranga/arxiv-mcp-server](https://github.com/prashalruchiranga/arxiv-mcp-server) — arXiv API via natural language ☆`39`
- [hbg/mcp-paperswithcode](https://github.com/hbg/mcp-paperswithcode) — MCP interface for PapersWithCode API ☆`26`
- [JackKuo666/bioRxiv-MCP-Server](https://github.com/JackKuo666/bioRxiv-MCP-Server) — Access bioRxiv papers ☆`25`
- [mochow13/google-scholar-mcp](https://github.com/mochow13/google-scholar-mcp) — MCP server for Google Scholar written in TypeScript ☆`24`
- [gemy411/multi-agents-research](https://github.com/gemy411/multi-agents-research) — Kotlin multi-agent research server on Ktor ☆`16`
### Data APIs

- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) — Bazi Chinese astrology information ☆`435`
- [Rudra-ravi/wikipedia-mcp](https://github.com/Rudra-ravi/wikipedia-mcp) — Retrieve Wikipedia information ☆`297`
- [ahonn/mcp-server-gsc](https://github.com/ahonn/mcp-server-gsc) — Google Search Console data access ☆`275`
- [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server) — A MCP server for Unsplash image search. ☆`237`
- [deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition) — MCP server for nutrition data and analysis ☆`208`
- [cameronrye/openzim-mcp](https://github.com/cameronrye/openzim-mcp) — MCP server for OpenZIM archive access ☆`143`
- [damionrashford/RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP) — MCP server for competitive search analysis ☆`131`
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) — Connect any Open Data to any LLM with Model Context Protocol. ☆`154`
- [cswkim/discogs-mcp-server](https://github.com/cswkim/discogs-mcp-server) — MCP Server for Discogs ☆`127`
- [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) — MCP server for Open Library book and author search ☆`95`
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) — AniList MCP server for accessing anime and manga data ☆`89`
- [riemannzeta/patent_mcp_server](https://github.com/riemannzeta/patent_mcp_server) — MCP Server for USPTO data ☆`81`
- [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) — MCP server for ZoomEye network asset information ☆`82`
- [Linked-API/linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp) — LinkedIn account control and data retrieval ☆`68`
- [anysiteio/anysite-mcp-server](https://github.com/anysiteio/anysite-mcp-server) — LinkedIn data access ☆`65`
- [imprvhub/mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability) — MCP server to check domain availability ☆`59`
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) — Rijksmuseum artwork exploration ☆`72`
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) — Quran.com verses, translations, tafsir ☆`72`
- [0xDAEF0F/job-searchoor](https://github.com/0xDAEF0F/job-searchoor) — A simple MCP server that delivers you jobs based on your needs ☆`65`
- [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) — An MCP server that provides comprehensive US legislation. ☆`38`
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) — Web API Baseline status information ☆`37`
- [amurshak/congressMCP](https://github.com/amurshak/congressMCP) — US Congress data for AI agents ☆`32`
- [zzaebok/mcp-wikidata](https://github.com/zzaebok/mcp-wikidata) — Wikidata API implementation ☆`49`
- [joelio/stocky](https://github.com/joelio/stocky) — An MCP server for searching and downloading stock photography. ☆`27`
- [jhomen368/overseerr-mcp](https://github.com/jhomen368/overseerr-mcp) — Overseerr/Seerr media search, requests, and library ☆`23`
- [adawalli/nexus](https://github.com/adawalli/nexus) — MCP Server to make searching openrouter easy ☆`23`
- [Himalayas-App/himalayas-mcp](https://github.com/Himalayas-App/himalayas-mcp) — Remote job search, listings, candidates, and salaries ☆`21`
- [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) — MCP server for Dappier AI integration ☆`44`
- [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) — Met Museum art collection discovery ☆`34`
- [angheljf/nyt](https://github.com/angheljf/nyt) — MCP server for New York Times article search ☆`18`
- [cameronrye/activitypub-mcp](https://github.com/cameronrye/activitypub-mcp) — Fediverse browsing and interaction via ActivityPub ☆`17`
- [parallel-web/task-mcp](https://github.com/parallel-web/task-mcp) — Hosted deep research and dataset enrichment via Parallel ☆`16`
- [siva010928/multi-chat-mcp-server](https://github.com/siva010928/multi-chat-mcp-server) — MCP server for multi-chat capabilities ☆`26`
- [kehvinbehvin/json-mcp-filter](https://github.com/kehvinbehvin/json-mcp-filter) — JSON MCP server to filter only relevant data for your LLM ☆`26`
- [r-huijts/opentk-mcp](https://github.com/r-huijts/opentk-mcp) — MCP server for Dutch parliamentary data via OpenTK ☆`23`
- [delorenj/mcp-server-ticketmaster](https://github.com/delorenj/mcp-server-ticketmaster) — Ticketmaster Discovery API ☆`25`
- [AshwinSundar/congress_gov_mcp](https://github.com/AshwinSundar/congress_gov_mcp) — Query US Congress.gov API ☆`19`
### News & Content

- [lfnovo/content-core](https://github.com/lfnovo/content-core) — Extract what matters from any media source ☆`174`
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) — MCP Server for Hackernews ☆`76`
- [imprvhub/mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator) — RSS feed aggregation for Claude Desktop ☆`27`
- [pskill9/hn-server](https://github.com/pskill9/hn-server) — Hacker news MCP server ☆`40`
- [format37/youtube_mcp](https://github.com/format37/youtube_mcp) — youtube transcriber mcp server ☆`32`
- [the0807/GeekNews-MCP-Server](https://github.com/the0807/GeekNews-MCP-Server) — GeekNews MCP Server ☆`18`
### Web Search Engines

- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) — Exa MCP for web search and web crawling! ☆`5,069`
- [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) — Real-time search, extract, map and crawl ☆`2,415`
- [Aas-ee/open-webSearch](https://github.com/Aas-ee/open-webSearch) — MCP server for open web search ☆`1,835`
- [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) — MCP server for DuckDuckGo search ☆`1,510`
- [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server) — Brave Search with AI summarization ☆`1,480`
- [ihor-sokoliuk/mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng) — Private SearXNG web search for AI assistants ☆`1,271`
- [mrkrsl/web-search-mcp](https://github.com/mrkrsl/web-search-mcp) — Local web search for Claude Desktop ☆`1,159`
- [kagisearch/kagimcp](https://github.com/kagisearch/kagimcp) — Official Kagi search MCP server ☆`527`
- [pskill9/web-search](https://github.com/pskill9/web-search) — Web search using free google search (NO API KEYS REQUIRED) ☆`471`
- [jae-jae/g-search-mcp](https://github.com/jae-jae/g-search-mcp) — Parallel Google search with summaries ☆`272`
- [serpapi/serpapi-mcp](https://github.com/serpapi/serpapi-mcp) — SerpApi MCP Server for Google and other search engine results ☆`176`
- [superagents-lab/search1api-mcp](https://github.com/superagents-lab/search1api-mcp) — MCP server for web search and crawl via Search1API ☆`175`
- [nkapila6/mcp-local-rag](https://github.com/nkapila6/mcp-local-rag) — RAG-like web search via MCP ☆`135`
- [ChanMeng666/server-google-news](https://github.com/ChanMeng666/server-google-news) — MCP server for Google News integration ☆`129`
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) — SearXNG search for agentic systems ☆`129`
- [mikechao/brave-search-mcp](https://github.com/mikechao/brave-search-mcp) — MCP server for Brave Search with filtering options ☆`127`
- [isnow890/naver-search-mcp](https://github.com/isnow890/naver-search-mcp) — MCP server for Naver search integration ☆`86`
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) — Perplexity API chat with citations ☆`95`
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp) — openai websearch tool as mcp server ☆`94`
- [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mcp-server) — MCP server for DuckDuckGo web search ☆`87`
- [leehanchung/bing-search-mcp](https://github.com/leehanchung/bing-search-mcp) — MCP Server for Bing Search API ☆`80`
- [OvertliDS/mcp-searxng-enhanced](https://github.com/OvertliDS/mcp-searxng-enhanced) — SearXNG web search with category awareness ☆`55`
- [pwilkin/mcp-searxng-public](https://github.com/pwilkin/mcp-searxng-public) — Query public SearXNG instances ☆`55`
- [ubie-oss/mcp-vertexai-search](https://github.com/ubie-oss/mcp-vertexai-search) — A MCP server for Vertex AI Search ☆`38`
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) — MCP Server for Tavily API integration ☆`50`
- [garylab/serper-mcp-server](https://github.com/garylab/serper-mcp-server) — A Serper MCP Server ☆`39`
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) — A Model Context Protocol server implementation for Kagi's API ☆`44`
- [mnhlt/WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP) — MCP server for web search integration ☆`41`
## Security

### Identity & Access

- [auth0/auth0-mcp-server](https://github.com/auth0/auth0-mcp-server) — Auth0 tenant management via natural language ☆`121`
- [sshaaf/keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server) — MCP server for Keycloak identity and access management ☆`48`
- [atomicchonk/roadrecon_mcp_server](https://github.com/atomicchonk/roadrecon_mcp_server) — Azure AD ROADrecon analysis for Claude ☆`52`
- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) — Authenticator App for AI agents ☆`45`
- [ChristophEnglisch/keycloak-model-context-protocol](https://github.com/ChristophEnglisch/keycloak-model-context-protocol) — Keycloak user and realm management ☆`46`
- [hieuttmmo/entraid-mcp-server](https://github.com/hieuttmmo/entraid-mcp-server) — EntraID via Microsoft Graph API ☆`41`
- [descope-sample-apps/descope-mcp-server-stdio](https://github.com/descope-sample-apps/descope-mcp-server-stdio) — Descope user management and audits ☆`37`
- [kapilduraphe/okta-mcp-server](https://github.com/kapilduraphe/okta-mcp-server) — Okta MCP Server ☆`22`
### MCP Security

- [eqtylab/mcp-guardian](https://github.com/eqtylab/mcp-guardian) — Manage / Proxy / Secure your MCP Servers ☆`201`
- [kapilduraphe/mcp-watch](https://github.com/kapilduraphe/mcp-watch) — Security scanner for MCP servers ☆`136`
- [82ch/MCP-Dandan](https://github.com/82ch/MCP-Dandan) — MCP security with real-time proxying ☆`67`
- [postralai/masquerade](https://github.com/postralai/masquerade) — The Privacy Firewall for LLMs ☆`77`
- [kontext-security/attestable-mcp-server](https://github.com/kontext-security/attestable-mcp-server) — Hardware attestation for MCP server integrity ☆`22`
- [AIM-Intelligence/AIM-MCP](https://github.com/AIM-Intelligence/AIM-MCP) — AIM MCP Server :: Guard and Protect your MCPs & AI Chatting ☆`22`
- [cromwellian/hippycampus](https://github.com/cromwellian/hippycampus) — REST endpoint to MCP conversion ☆`20`
### Network & Firewall

- [vespo92/OPNSenseMCP](https://github.com/vespo92/OPNSenseMCP) — MCP Server for OPNSense to act as IaC proxy ☆`87`
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) — An MCP server to let AI agents control Intruder ☆`26`
### Pentesting & OSINT

- [PortSwigger/mcp-server](https://github.com/PortSwigger/mcp-server) — MCP Server for Burp ☆`1,203`
- [w0h1v/mcp-maigret](https://github.com/w0h1v/mcp-maigret) — Maigret OSINT user account collection ☆`267`
- [w0h1v/mcp-shodan](https://github.com/w0h1v/mcp-shodan) — MCP server for Shodan - device search, IP recon, CVE intel ☆`173`
- [w0h1v/mcp-virustotal](https://github.com/w0h1v/mcp-virustotal) — VirusTotal API queries ☆`149`
- [roadwy/cve-search_mcp](https://github.com/roadwy/cve-search_mcp) — CVE database security queries ☆`107`
- [mobb-dev/bugsy](https://github.com/mobb-dev/bugsy) — Automatic security vulnerability remediation for your code. ☆`69`
- [StacklokLabs/osv-mcp](https://github.com/StacklokLabs/osv-mcp) — An MCP server for OSV ☆`42`
- [GitGuardian/ggmcp](https://github.com/GitGuardian/ggmcp) — Scan and remediate hardcoded secrets ☆`37`
- [w0h1v/mcp-dnstwist](https://github.com/w0h1v/mcp-dnstwist) — DNS fuzzing for phishing detection ☆`51`
- [nickpending/mcp-recon](https://github.com/nickpending/mcp-recon) — Tellix conversational recon interface ☆`31`
- [gnlds/mcp-cve-intelligence-server-lite](https://github.com/gnlds/mcp-cve-intelligence-server-lite) — CVE intelligence from NVD, MITRE, GitHub ☆`19`
### Reverse Engineering

- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) — IDA Pro reverse engineering with AI ☆`12,433`
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) — MCP Server for Ghidra ☆`10,242`
- [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) — Plugin for JADX to integrate MCP server ☆`2,849`
- [LING71671/open-reverselab](https://github.com/LING71671/open-reverselab) — Ghidra, Frida, x64dbg, Rizin, and YARA in one lab ☆`1,201`
- [symgraph/GhidrAssistMCP](https://github.com/symgraph/GhidrAssistMCP) — An native MCP server extension for Ghidra ☆`760`
- [zinja-coder/apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) — APK Tool for Android reverse engineering ☆`662`
- [fosdickio/binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp) — Binary Ninja plugin for LLM integration ☆`445`
- [radareorg/radare2-mcp](https://github.com/radareorg/radare2-mcp) — MCP stdio server for radare2 ☆`312`
- [13bm/GhidraMCP](https://github.com/13bm/GhidraMCP) — Active Socket based MCP Server for Ghidra ☆`143`
- [pullkitsan/mobsf-mcp-server](https://github.com/pullkitsan/mobsf-mcp-server) — MobSF APK and IPA security scanning ☆`22`
### SIEM & SecOps

- [beelzebub-labs/beelzebub](https://github.com/beelzebub-labs/beelzebub) — Low-code honeypot with AI virtualization ☆`2,188`
- [MorDavid/BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI) — BloodHound integration with AI through MCP ☆`377`
- [CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) — CrowdStrike Falcon security analysis ☆`261`
- [gbrigandi/mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh) — MCP Server for Wazuh SIEM ☆`237`
- [securityfortech/secops-mcp](https://github.com/securityfortech/secops-mcp) — All-in-one security testing toolbox via MCP ☆`216`
- [cycodehq/cycode-cli](https://github.com/cycodehq/cycode-cli) — SAST, SCA, Secrets, IaC security scanning ☆`100`
- [panther-labs/mcp-panther](https://github.com/panther-labs/mcp-panther) — Detections, alerts, and log queries ☆`47`
- [zxzinn/opencti-mcp](https://github.com/zxzinn/opencti-mcp) — OpenCTI threat intelligence platform ☆`40`
- [qianniuspace/mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit) — MCP server for security auditing ☆`57`
- [fr0gger/MCP_Security](https://github.com/fr0gger/MCP_Security) — This is a repository to experiment with MCP for security ☆`52`
- [Gaffx/volatility-mcp](https://github.com/Gaffx/volatility-mcp) — This repo hosts an MCP server for volatility3.x ☆`52`
- [slouchd/cyberchef-api-mcp-server](https://github.com/slouchd/cyberchef-api-mcp-server) — CyberChef API MCP Server ☆`44`
- [Contrast-Security-OSS/mcp-contrast](https://github.com/Contrast-Security-OSS/mcp-contrast) — MCP Server for Contrast Security ☆`23`
- [jyjune/mcp_vms](https://github.com/jyjune/mcp_vms) — MCP server for controlling and accessing a video surveillance system ☆`17`
- [gbrigandi/mcp-server-cortex](https://github.com/gbrigandi/mcp-server-cortex) — MCP Server for Cortex ☆`17`
## Social Media

- [iFurySt/RedNote-MCP](https://github.com/iFurySt/RedNote-MCP) — MCP server for accessing RedNote(XiaoHongShu, xhs). ☆`1,116`
- [karanb192/reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) — Clean Reddit data: posts, search, users ☆`841`
- [dialog-tools/reddit-research-mcp](https://github.com/dialog-tools/reddit-research-mcp) — Reddit research with structured insights ☆`253`
- [HagaiHen/facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) — Facebook posts, comments, insights automation ☆`227`
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) — Twitter interaction via MCP ☆`235`
- [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper) — X/Twitter search, profiles, posting, and media download ☆`210`
- [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) — Model Context Protocol (MCP) with TikTok integration ☆`201`
- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) — Bilibili video search MCP service ☆`194`
- [trypeggy/instagram_dm_mcp](https://github.com/trypeggy/instagram_dm_mcp) — Instagram Direct messages MCP ☆`183`
- [anwerj/youtube-uploader-mcp](https://github.com/anwerj/youtube-uploader-mcp) — Upload, update, and schedule YouTube videos ☆`56`
- [LuniaKunal/mcp-twitter](https://github.com/LuniaKunal/mcp-twitter) — Manage your twitter account using mcp ☆`60`
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) — MCP server for Product Hunt data access ☆`54`
- [macrocosm-os/macrocosmos-mcp](https://github.com/macrocosm-os/macrocosmos-mcp) — The MCP for macrocosmos subnets. ☆`29`
- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) — Nostr posting and interaction ☆`38`
- [ertiqah/linkedin-mcp-runner](https://github.com/ertiqah/linkedin-mcp-runner) — LinkedIn content analysis and posting ☆`31`
- [laulauland/bluesky-context-server](https://github.com/laulauland/bluesky-context-server) — Bluesky MCP server ☆`34`
- [jonathan-politzki/mcp-writer-substack](https://github.com/jonathan-politzki/mcp-writer-substack) — Bridge Substack writings to Claude ☆`32`
- [mbelinky/x-mcp-server](https://github.com/mbelinky/x-mcp-server) — MCP server to post on x.com with OAuth v1 and v2 ☆`24`
- [gwbischof/bluesky-social-mcp](https://github.com/gwbischof/bluesky-social-mcp) — A Bluesky MCP ☆`16`
## Sports

- [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) — Strava fitness data integration ☆`492`
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp) — Fantasy Premier League MCP Server ☆`80`
- [guillochon/mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp) — MCP server for MLB baseball statistics ☆`59`
- [RobSpectre/mvf1](https://github.com/RobSpectre/mvf1) — Python package and CLI for MultiViewer For F1 ☆`19`
- [yeonupark/mcp-soccer-data](https://github.com/yeonupark/mcp-soccer-data) — Real-time football data ☆`39`
- [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) — MCP server for NBA, NFL, MLB sports data ☆`26`
- [lenwood/cfbd-mcp-server](https://github.com/lenwood/cfbd-mcp-server) — An MCP server enabling CFBD API queries within Claude Desktop. ☆`28`
- [kw510/strava-mcp](https://github.com/kw510/strava-mcp) — MCP server with Strava OAuth on Cloudflare Workers ☆`26`
- [tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server) — MCP server for Strava API integration ☆`24`
- [willvelida/mcp-afl-server](https://github.com/willvelida/mcp-afl-server) — Australian Football League data from Squiggle ☆`18`
- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) — MCP server for professional cycling data from FirstCycling ☆`18`
## Text-to-Speech

- [mbailey/voicemode](https://github.com/mbailey/voicemode) — Natural voice conversations with Claude Code ☆`1,385`
- [mberg/kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) — Kokoro Text to Speech (TTS) MCP Server ☆`82`
## Translation

- [caol64/wenyan-mcp](https://github.com/caol64/wenyan-mcp) — Markdown formatting and translation to Chinese ☆`1,329`
- [aymericzip/intlayer](https://github.com/aymericzip/intlayer) — MCP server for Intlayer internationalization ☆`844`
- [DeepL/deepl-mcp-server](https://github.com/DeepL/deepl-mcp-server) — Translation with DeepL API ☆`117`
- [translated/lara-mcp](https://github.com/translated/lara-mcp) — Lara Translate API with language detection ☆`97`
- [mmntm/weblate-mcp](https://github.com/mmntm/weblate-mcp) — Manage Weblate projects, components, and translations ☆`22`
## Travel & Transport

- [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) — Search Airbnb using your AI Agent ☆`548`
- [cobanov/teslamate-mcp](https://github.com/cobanov/teslamate-mcp) — MCP server for TeslaMate vehicle data and analytics ☆`140`
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) — MCP server for Tripadvisor location data and reviews ☆`64`
- [r-huijts/ns-mcp-server](https://github.com/r-huijts/ns-mcp-server) — MCP server for Dutch Railways (NS) travel information ☆`62`
- [variflight/variflight-mcp](https://github.com/variflight/variflight-mcp) — Variflight services implementation ☆`33`
- [Pradumnasaraf/aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) — MCP for AviationStack API - real-time flight data ☆`24`
- [mfukushim/map-traveler-mcp](https://github.com/mfukushim/map-traveler-mcp) — Virtual traveler library for MCP ☆`24`
- [sunsetcoder/flightradar24-mcp-server](https://github.com/sunsetcoder/flightradar24-mcp-server) — Model Context Protocol server for Flight Tracking ☆`47`
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) — US National Parks info via NPS API ☆`41`
- [campertunity/mcp-server](https://github.com/campertunity/mcp-server) — Search campgrounds, check availability, and book campsites ☆`17`
- [JordanDalton/DoorDash-MCP-Server](https://github.com/JordanDalton/DoorDash-MCP-Server) — MCP server for DoorDash delivery service integration ☆`25`
## Web Scraping

- [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) — Python scraper based on AI ☆`31,486`
- [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) — MCP server for Apify web scraping and data extraction ☆`9,309`
- [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) — Web scraping and search for LLM clients ☆`7,538`
- [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) — All-in-one public web access solution ☆`2,662`
- [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) — Playwright web page content fetching ☆`1,086`
- [etsd-tech/mcp-pointer](https://github.com/etsd-tech/mcp-pointer) — DOM element pointing for agents ☆`598`
- [tinyfish-io/agentql-mcp](https://github.com/tinyfish-io/agentql-mcp) — AgentQL data extraction integration ☆`181`
- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) — Scrapeless Mcp Server ☆`169`
- [just-every/mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast) — Fast webpage to markdown conversion ☆`161`
- [pskill9/website-downloader](https://github.com/pskill9/website-downloader) — MCP server to download entire websites ☆`156`
- [cyberchitta/scrapling-fetch-mcp](https://github.com/cyberchitta/scrapling-fetch-mcp) — Access bot-protected websites ☆`120`
- [just-every/mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast) — Fast webpage screenshots for LLMs ☆`110`
- [supadata-ai/mcp](https://github.com/supadata-ai/mcp) — Video and web scraping for Claude ☆`64`
- [pragmar/mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl) — Web crawler data and archives connection ☆`46`
- [webscraping-ai/webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server) — MCP server for AI-powered web scraping ☆`44`
- [crawlbase/crawlbase-mcp](https://github.com/crawlbase/crawlbase-mcp) — MCP server connecting AI agents with real-time web data ☆`58`
- [Decodo/mcp-server](https://github.com/Decodo/mcp-server) — Decodo web scraping for MCP clients ☆`37`
- [puremd/puremd-mcp](https://github.com/puremd/puremd-mcp) — Unblock, scrape, and search tools for MCP clients ☆`60`
- [ananddtyagi/webpage-screenshot-mcp](https://github.com/ananddtyagi/webpage-screenshot-mcp) — MCP server for webpage screenshot capture ☆`57`
- [djannot/puppeteer-vision-mcp](https://github.com/djannot/puppeteer-vision-mcp) — Web scraping with AI-driven interaction handling ☆`48`
- [olostep/olostep-mcp-server](https://github.com/olostep/olostep-mcp-server) — Live web scrape, crawl, batch extract, and search ☆`24`
- [wong2/mcp-jina-reader](https://github.com/wong2/mcp-jina-reader) — Jina Reader MCP Server ☆`47`
- [DevEnterpriseSoftware/scrapi-mcp](https://github.com/DevEnterpriseSoftware/scrapi-mcp) — MCP server for using ScrAPI to scrape web pages. ☆`18`
- [levz0r/html-to-markdown-mcp](https://github.com/levz0r/html-to-markdown-mcp) — HTML to Markdown converter using Turndown ☆`26`


---

## 🏆 Top 100 by Stars

> The most starred projects in this list, sorted by GitHub stars.

1. [upstash/context7](https://github.com/upstash/context7) — Up-to-date code docs for LLMs ☆`62,594`
1. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Chrome DevTools for coding agents ☆`52,862`
1. [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) — Hindsight: Agent Memory That Learns ☆`44,420`
1. [mindsdb/mindshub](https://github.com/mindsdb/mindshub) — Query Engine for AI Analytics - self-reasoning agents on live data ☆`39,778`
1. [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — Playwright MCP server ☆`37,749`
1. [github/github-mcp-server](https://github.com/github/github-mcp-server) — GitHub's official MCP Server ☆`33,320`
1. [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp) — AI browser agent, ships as an MCP server and a web UI ☆`31,744`
1. [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) — Python scraper based on AI ☆`31,486`
1. [oraios/serena](https://github.com/oraios/serena) — Semantic code retrieval and editing toolkit ☆`29,941`
1. [mastra-ai/mastra](https://github.com/mastra-ai/mastra) — TypeScript AI agent framework with RAG ☆`28,492`
1. [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) — Python framework for building MCP servers and clients ☆`27,953`
1. [trycua/cua](https://github.com/trycua/cua) — MCP server for CUA platform ☆`27,717`
1. [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) — Automate browser based workflows with AI ☆`23,118`
1. [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) — Build n8n workflows with AI assistants ☆`23,032`
1. [screenpipe/screenpipe](https://github.com/screenpipe/screenpipe) — Searchable screen text and audio history via MCP; source-available under the Screenpipe Commercial License ☆`21,796`
1. [apache/apisix](https://github.com/apache/apisix) — The Cloud-Native API Gateway and AI Gateway ☆`17,187`
1. [googleapis/mcp-toolbox](https://github.com/googleapis/mcp-toolbox) — Open source database MCP toolbox ☆`16,548`
1. [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) — Figma layout info for AI coding agents ☆`15,944`
1. [zilliztech/claude-context](https://github.com/zilliztech/claude-context) — Code search for Claude Code agents ☆`12,584`
1. [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) — IDA Pro reverse engineering with AI ☆`12,433`
1. [elie222/inbox-zero](https://github.com/elie222/inbox-zero) — AI email assistant for inbox zero ☆`12,390`
1. [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) — Expose FastAPI endpoints as MCP tools ☆`12,013`
1. [instantdb/instant](https://github.com/instantdb/instant) — Modern Firebase with real-time database ☆`10,536`
1. [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) — MCP Server for Ghidra ☆`10,242`
1. [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) — Terminal control, file search, diff editing ☆`9,873`
1. [awslabs/mcp](https://github.com/awslabs/mcp) — AWS MCP servers for AI assistants ☆`9,747`
1. [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) — MCP server for Apify web scraping and data extraction ☆`9,309`
1. [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) — Go implementation of MCP ☆`9,150`
1. [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) — Build agents with MCP and workflow patterns ☆`8,567`
1. [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) — Mobile automation for iOS, Android, emulators ☆`8,536`
1. [superradcompany/microsandbox](https://github.com/superradcompany/microsandbox) — easy, fast, programmable and local-first microVM runtime ☆`8,506`
1. [idosal/git-mcp](https://github.com/idosal/git-mcp) — Free remote MCP for any GitHub project ☆`8,447`
1. [Upsonic/Upsonic](https://github.com/Upsonic/Upsonic) — Build autonomous AI agents in Python. ☆`7,956`
1. [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) — Web scraping and search for LLM clients ☆`7,538`
1. [BrowserMCP/mcp](https://github.com/BrowserMCP/mcp) — Browser control for AI applications ☆`7,151`
1. [grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp) — Cursor and Figma communication ☆`7,048`
1. [GreptimeTeam/greptimedb](https://github.com/GreptimeTeam/greptimedb) — Unified observability DB for metrics, logs, traces ☆`6,727`
1. [genkit-ai/genkit](https://github.com/genkit-ai/genkit) — AI app framework for JavaScript and Go ☆`6,465`
1. [getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) — MCP server for Xcode build operations ☆`6,449`
1. [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) — WhatsApp MCP server ☆`6,361`
1. [baserow/baserow](https://github.com/baserow/baserow) — No-code database, apps, agents with AI ☆`6,067`
1. [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) — MCP server for Atlassian tools (Confluence, Jira) ☆`5,962`
1. [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) — Frontend development with AI like Magic ☆`5,959`
1. [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) — MCP server for Godot game engine ☆`5,907`
1. [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) — MCP server for Playwright browser testing ☆`5,661`
1. [lingodotdev/lingo.dev](https://github.com/lingodotdev/lingo.dev) — MCP server for Lingo localization platform ☆`5,407`
1. [openclaw/Peekaboo](https://github.com/openclaw/Peekaboo) — macOS screenshot and window capture MCP server ☆`5,237`
1. [Kiln-AI/Kiln](https://github.com/Kiln-AI/Kiln) — Build AI systems with Evals, RAG, Agents, fine-tuning ☆`5,150`
1. [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) — Exa MCP for web search and web crawling! ☆`5,069`
1. [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) — Official Notion MCP Server ☆`4,655`
1. [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) — Obsidian integration via REST API plugin ☆`4,458`
1. [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) — 25+ visual charts using @antvis for data analysis ☆`4,389`
1. [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) — AI-powered bridge connecting LLMs to Unity Editor ☆`4,373`
1. [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) — Cloudflare services management ☆`4,345`
1. [archestra-ai/archestra](https://github.com/archestra-ai/archestra) — Enterprise AI guardrails, registry, gateway, and orchestrator ☆`4,340`
1. [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) — Code graph indexing for AI context ☆`4,242`
1. [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) — Excel file manipulation ☆`4,208`
1. [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) — AI conversations that remember context ☆`4,075`
1. [dagger/container-use](https://github.com/dagger/container-use) — MCP server for container orchestration ☆`4,053`
1. [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) — Google Ads diagnosis, recommendations, and edits ☆`3,886`
1. [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) — SEO, GEO, ads, Search Console, and Analytics skills ☆`3,886`
1. [bytebase/dbhub](https://github.com/bytebase/dbhub) — Token-efficient multi-database MCP ☆`3,593`
1. [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) — MCP server for Grafana ☆`3,521`
1. [metorial/metorial](https://github.com/metorial/metorial) — Connect any AI model to 1200+ integrations (MCP, CLI, API) ☆`3,362`
1. [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) — Postgres with read/write access and performance ☆`3,361`
1. [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) — MCP server integration for DaVinci Resolve Studio ☆`3,282`
1. [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) — MCP server for Google Workspace integration ☆`3,274`
1. [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) — arXiv paper search and analysis ☆`3,185`
1. [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) — MCP server for shadcn/ui component library ☆`3,011`
1. [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) — Convert almost anything to Markdown ☆`2,997`
1. [supabase/mcp](https://github.com/supabase/mcp) — Connect Supabase to your AI assistants ☆`2,927`
1. [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) — Plugin for JADX to integrate MCP server ☆`2,849`
1. [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) — A bridge between Streamable HTTP and stdio MCP transports ☆`2,767`
1. [metatool-ai/metamcp](https://github.com/metatool-ai/metamcp) — MCP Aggregator, Orchestrator, Middleware, Gateway in one docker ☆`2,694`
1. [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) — All-in-one public web access solution ☆`2,662`
1. [perplexityai/modelcontextprotocol](https://github.com/perplexityai/modelcontextprotocol) — Official Perplexity API MCP server ☆`2,550`
1. [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) — Real-time search, extract, map and crawl ☆`2,415`
1. [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) — Financial Datasets stock market API ☆`2,300`
1. [jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool) — MCP server for Gemini CLI with large file analysis ☆`2,287`
1. [stacklok/toolhive](https://github.com/stacklok/toolhive) — Runtime and gateway for deploying MCP servers in containers ☆`2,230`
1. [beelzebub-labs/beelzebub](https://github.com/beelzebub-labs/beelzebub) — Low-code honeypot with AI virtualization ☆`2,188`
1. [joshuayoes/ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) — MCP server for interacting with the iOS simulator ☆`2,185`
1. [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) — Task manager with chain-of-thought and reflection ☆`2,145`
1. [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) — Kubernetes and OpenShift management ☆`2,140`
1. [benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) — MCP server for MySQL database operations ☆`2,140`
1. [chatmcp/mcpso](https://github.com/chatmcp/mcpso) — directory for Awesome MCP Servers ☆`2,109`
1. [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) — Azure DevOps integration for AI agents ☆`2,040`
1. [IBM/mcp-cli](https://github.com/IBM/mcp-cli) — Feature-rich CLI for interacting with MCP servers ☆`2,025`
1. [nottelabs/notte](https://github.com/nottelabs/notte) — Framework to build web agents ☆`2,009`
1. [MicrosoftDocs/mcp](https://github.com/MicrosoftDocs/mcp) — Microsoft Learn MCP for LLMs ☆`1,923`
1. [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) — MCP server for Unity game engine integration ☆`1,919`
1. [stripe/ai](https://github.com/stripe/ai) — One-stop shop for building AI-powered products and businesses with Stripe. ☆`1,852`
1. [korotovsky/slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) — MCP server for Slack workspace integration ☆`1,852`
1. [Aas-ee/open-webSearch](https://github.com/Aas-ee/open-webSearch) — MCP server for open web search ☆`1,835`
1. [ravitemer/mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) — MCP client for Neovim with intuitive server management ☆`1,784`
1. [WordPress/mcp-adapter](https://github.com/WordPress/mcp-adapter) — Bridge Abilities API to MCP ☆`1,782`
1. [julien040/anyquery](https://github.com/julien040/anyquery) — SQL queries for GitHub, Notion, +40 more ☆`1,779`
1. [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) — A JavaScript-driven M5Stack-embedded super-kawaii robot. ☆`1,743`
1. [chigwell/telegram-mcp](https://github.com/chigwell/telegram-mcp) — MCP server for Telegram messaging ☆`1,737`
1. [bitbonsai/mcpvault](https://github.com/bitbonsai/mcpvault) — Lightweight Obsidian vault access ☆`1,676`

## Contributing

Please see [CONTRIBUTING](.github/CONTRIBUTING.md) for details.

## Feedback

Found something wrong? Open an issue or submit a pull request — contributions are welcome!

## Credits

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)
- [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)
- [All Contributors](https://github.com/abordage/awesome-mcp/graphs/contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
