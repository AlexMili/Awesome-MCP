# Awesome MCP

A curated list of Model Context Protocol (MCP) resources.

# Content
- [Servers](#servers)
  - [Javascript](#javascript)
  - [Python](#python)
  - [Go](#go)
- [SDKs](#sdks)
- [Tools](#tools)


# Servers

All current MCP servers are not in one language. Here is a list from official repository with associated programming languages.

## Javascript
- [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - Official - Secure file operations with configurable access controls
- [Github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - Official - Repository management, file operations, and GitHub API integration
- [Gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) - Official - GitLab API, enabling project management
- [Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) - Official - File access and search capabilities for Google Drive
- [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - Official - Read-only database access with schema inspection
- [Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) - Official - Channel management and messaging capabilities
- [Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) - Official - Knowledge graph-based persistent memory system
- [Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) - Official - Browser automation and web scraping
- [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Official - Web and local search using Brave's Search API
- [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) - Official - Location services, directions, and place details
- [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) - Community - Deploy, configure & interrogate your resources on the Cloudflare developer platform (e.g. Workers/KV/R2/D1)
- [Raygun](https://github.com/MindscapeHQ/mcp-server-raygun) - Community - Interact with your crash reporting and real using monitoring data on your Raygun account
- [Kagi](https://github.com/ac3xx/mcp-servers-kagi) - Community - A Model Context Protocol server implementation for Kagi's API
- [Exa.ai](https://github.com/theishangoswami/exa-mcp-server) - Community - Use the Exa AI Search API for web searches
- [Youtube](https://github.com/anaisbetts/mcp-youtube) - Community - Uses `yt-dlp` to download subtitles from YouTube

## Python
- [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) - Official - Tools to read, search, and manipulate Git repositories
- [Sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) - Official - Database interaction and business intelligence capabilities
- [Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) - Official - Retrieving and analyzing issues from Sentry.io
- [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) - Official - Web content fetching and conversion for efficient LLM usage
- [Stdio](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/stdio.py) - Official - Communicate with an MCP client through standard input/output streams
- [Websocket](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/websocket.py) - Official - WebSocket server transport. This is an ASGI application, suitable to be used with a framework like Starlette and a server like Hypercorn
- [OpenAI](https://github.com/pierrebrunelle/mcp-server-openai) - Community - Query OpenAI models directly from Claude
- [Phabricator](https://github.com/baba786/phabricator-mcp-server) - Community - Interact with Phabricator API
- [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) - Community - Interact with Obsidian
- [Filesystem](https://github.com/philgei/mcp_server_filesystem) - Community - File operations with configurable access controls

## Go
- [Filesystem](https://github.com/mark3labs/mcp-filesystem-server) - Community - File operations with configurable access controls

# SDKs
- [Python](https://github.com/modelcontextprotocol/python-sdk) - Official
- [Typescript](https://github.com/modelcontextprotocol/typescript-sdk) - Official
- [Rust](https://github.com/jeanlucthumm/modelcontextprotocol-rust-sdk) - Community - **:warning: Under development**
- [Go](https://github.com/mark3labs/mcp-go) - Community - **:warning: Under development**

# Tools
- [Server inspector](https://github.com/modelcontextprotocol/inspector) - Official - Visual testing tool for MCP servers
- [Langchain](https://github.com/rectalogic/langchain-mcp) - Community - Support for LangChain
- [MCP Installer](https://github.com/anaisbetts/mcp-installer) - Community - A server that installs other MCP servers for you
- [MCP get](https://github.com/michaellatman/mcp-get) - Community - A command-line tool for installing and managing Model Context Protocol (MCP) servers
