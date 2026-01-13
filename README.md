# Awesome MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) resources.

The Model Context Protocol (MCP) is an open protocol published by [Anthropic](https://www.anthropic.com/) in November 2024. It enables seamless integration between LLM applications and external data sources and tools. This repo is not just about MCP Servers but the whole ecosystem arround the protocol itself.


## Contents

- [Servers](#servers)
- [Clients](#clients)
- [SDKs](#sdks)
- [Tools](#tools)


## Servers

All current MCP servers are not in one language. Here is a list from official repository with associated programming languages.

### Typescript

#### Official
- [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - Secure file operations with configurable access controls.
- [Github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - Repository management, file operations, and GitHub API integration.
- [Gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) - GitLab API, enabling project management.
- [Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) - File access and search capabilities for Google Drive.
- [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - Read-only database access with schema inspection.
- [Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) - Channel management and messaging capabilities.
- [Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) - Knowledge graph-based persistent memory system.
- [Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) - Browser automation and web scraping.
- [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Web and local search using Brave's Search API.
- [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) - Location services, directions, and place details.
- [AWS Knowledge Base Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server) - Retrieve information from the AWS Knowledge Base using the Bedrock Agent Runtime.

#### Community
- [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) - Deploy, configure & interrogate your resources on the Cloudflare developer platform (e.g. Workers/KV/R2/D1).
- [Raygun](https://github.com/MindscapeHQ/mcp-server-raygun) - Interact with your crash reporting and real using monitoring data on your Raygun account.
- [Kagi](https://github.com/ac3xx/mcp-servers-kagi) - A Model Context Protocol server implementation for Kagi's API.
- [Exa.ai](https://github.com/theishangoswami/exa-mcp-server) - Use the Exa AI Search API for web searches.
- [Youtube](https://github.com/anaisbetts/mcp-youtube) - Uses `yt-dlp` to download subtitles from YouTube.
- [AppleScript](https://github.com/joshrutkowski/applescript-mcp) - Implements interaction with macOS via AppleScript.
- [Make](https://github.com/integromat/make-mcp-server) - Turn Make scenarios into callable tools for AI assistants.
- [VSCode Devtools (Bifrost)](https://github.com/biegehydra/BifrostMCP) - Connect to VSCode IDE and use semantic tools like `find_usages`.
- [Playwright](https://github.com/microsoft/playwright-mcp) - Provides browser automation capabilities using Playwright.
- [Node.js](https://github.com/hyperdrive-eng/mcp-nodejs-debugger) - Gives Cursor or Claude Code access to Node.js at runtime to help you debug.
- [XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) - Provides Xcode-related tools for integration with AI assistants and other MCP clients.
- [domain-mcp](https://github.com/joachimBrindeau/domain-mcp) - MCP server to search, register, and manage domains (availability, DNS, WHOIS) via Dynadot API.

### Python

#### Official
- [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) - Tools to read, search, and manipulate Git repositories.
- [Sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) - Database interaction and business intelligence capabilities.
- [Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) - Retrieving and analyzing issues from Sentry.io.
- [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) - Web content fetching and conversion for efficient LLM usage.
- [Stdio](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/stdio.py) - Communicate with an MCP client through standard input/output streams.
- [Websocket](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/websocket.py) - WebSocket server transport. This is an ASGI application, suitable to be used with a framework like Starlette and a server like Hypercorn.

#### Community
- [OpenAI](https://github.com/pierrebrunelle/mcp-server-openai) - Query OpenAI models directly from Claude.
- [Phabricator](https://github.com/baba786/phabricator-mcp-server) - Interact with Phabricator API.
- [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) - Interact with Obsidian.
- [Filesystem](https://github.com/philgei/mcp_server_filesystem) - File operations with configurable access controls.
- [ZenML](https://github.com/zenml-io/mcp-zenml) - Chat with your MLOps and LLMOps pipelines using the official ZenML MCP server.
- [Blender](https://github.com/ahujasid/blender-mcp) - Interact with and control Blender using prompt assisted 3D modeling, scene creation, and manipulation.
- [WhatsApp](https://github.com/lharries/whatsapp-mcp) - Search your personal Whatsapp messages, search your contacts and send messages to either individuals or groups.
- [AWS](https://github.com/awslabs/mcp) - A suite of specialized MCP servers that bring AWS best practices directly to your development workflow.
- [MarkItDown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) - Lightweight STDIO and SSE MCP server for calling MarkItDown.
- [PraisonAI](https://github.com/MervinPraison/praisonai-mcp) - AI Agents framework with 64+ built-in MCP tools for search, memory, workflows, code execution, and file operations.

### Go
- [Filesystem](https://github.com/mark3labs/mcp-filesystem-server) - File operations with configurable access controls.
- [Official Github](https://github.com/github/github-mcp-server) - Seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools.

## Clients

### Community
- [n8n](https://github.com/nerding-io/n8n-nodes-mcp) - interact with Model Context Protocol (MCP) servers in your n8n workflows.
- [eechat](https://github.com/Lucassssss/eechat) - An open-source, cross-platform desktop application that seamlessly connects with full support for MCP, across Linux, macOS, and Windows.

## SDKs

### Offcial
- [Python](https://github.com/modelcontextprotocol/python-sdk) - Official Python SDK.
- [Typescript](https://github.com/modelcontextprotocol/typescript-sdk) - Official Typescript SDK.

### Community
- [Rust](https://github.com/jeanlucthumm/modelcontextprotocol-rust-sdk) - Community-driven Rust adaptation of offcials SDK. **:warning: Under development**.
- [Go](https://github.com/mark3labs/mcp-go) - Community-driven Go adaptation of offcials SDK. **:warning: Under development**.

## Tools

### Official
- [Server inspector](https://github.com/modelcontextprotocol/inspector) - Visual testing tool for MCP servers.

### Community
- [Langchain](https://github.com/rectalogic/langchain-mcp) - Support for LangChain.
- [MCP Installer](https://github.com/anaisbetts/mcp-installer) - A server that installs other MCP servers for you.
- [MCP get](https://github.com/michaellatman/mcp-get) - A command-line tool for installing and managing Model Context Protocol (MCP) servers.
- [Fast MCP](https://github.com/jlowin/fastmcp) - Create tools, expose resources, and define prompts with clean Pythonic code.
- [Fleur MCP](https://github.com/fleuristes/fleur) - A desktop app marketplace for Claude Desktop.
- [MCP Agent](https://github.com/lastmile-ai/mcp-agent) - Build effective agents with Model Context Protocol using simple, composable patterns.
- [ToolRegistry](https://github.com/Oaklight/ToolRegistry) - A PyPI package that simplifies tool integration by streamlining OpenAI client tool calls and managing native Python functions and MCP servers, offering both async and sync interfaces.
- [ToolHive](https://github.com/StacklokLabs/toolhive) - A lightweight utility designed to simplify the deployment and management of MCP servers, ensuring ease of use, consistency, and security through containerization.
- [Roundtable](https://github.com/askbudi/roundtable) - Zero-configuration MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized interface.
- [Dify plugin](https://github.com/hjlarry/dify-plugin-mcp_server) - Change a Dify app to a mcp server.
