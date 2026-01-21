# MCP Demo Project

A demonstration of the Model Context Protocol (MCP) showing how to build a client-server architecture for integrating LLM agents with external tools.

## Overview

This project contains:

- **Server**: Exposes tools via MCP (weather info and sum operations)
- **Client**: Connects to the server using LangChain and Google Gemini to query the tools through an LLM agent

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager
- Google API key (set in `client/.env`)

## Running Locally

### 1. Start the Server

```bash
cd server
uv run main.py
```

The server will listen on `http://localhost:8000/mcp`

### 2. Run the Client

In a separate terminal:

```bash
cd client
uv run main.py
```

The client will connect to the server, load the available tools, and execute a sample query.

## Project Structure

```
├── server/
│   ├── main.py          # MCP server with tools
│   └── pyproject.toml
└── client/
    ├── main.py          # LangChain agent client
    ├── .env             # Environment variables
    └── pyproject.toml
```
