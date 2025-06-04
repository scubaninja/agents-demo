# Presentation demo

This set of demos walks through a full collection of workloads supported by GitHub Copilot, and highlights the importance of context. In particular it shows off:

- [code completion](./1-code-completion.md) and how context works.
- [custom instructions and context](./2-custom-instructions.md) through the use of directives, hashtags, custom instructions and prompt files.
- [Copilot Edits and Agent Mode](./3-edit-agent.md) for modifying multiple files.
- [Model Context Protocol (MCP)](./4-mcp.md) to access external services.

## Scenario

The project uses a fictional website called Tailspin Toys, built for crowdfunding DevOps themed boardgames - a huge market! It's built with [Flask](https://flask.palletsprojects.com/en/stable/) & [SQLAlchemy](https://www.sqlalchemy.org/) as the backend and a [SQLite](https://sqlite.org/) database, with a frontend using [Astro](https://astro.build/) and [Svelte](https://svelte.dev/) for the frontend with [Tailwind](https://tailwindcss.com/) for style.

## Running the demo

The demo is built to run in a codespace. There are [setup steps](./0-setup.md) required.

0. [Setup](./0-setup.md)
1. [Code completion](./1-code-completion.md)
2. [Context and custom instructions](./2-custom-instructions.md)
3. [Copilot Edits and Agent Mode](./3-edit-agent.md)
4. [Model Context Protocol (MCP)](./4-mcp.md)
