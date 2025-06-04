# Demo setup

To prep the demo, perform the following steps:

## Create and configure the repository.

1. Create a new repository from the template (**Use this template** > **Create a new repository**).
2. Add the **docs** folder to the exclusion list to ensure Copilot doesn't "cheat" by seeing information it shouldn't have.
    1. Open **Settings** in the repository.
    2. Open **Copilot** in the settings screen.
    3. Open **Content exclusions**.
    4. Add the following to **Paths to exclude in this repository**
        ```plaintext
        - /docs/**
        ```
    5. Select **Save changes**.
3. Ensure Issues are enabled for your repository by selecting **Settings** and ensuring there is a check next to **Issues** under **Features**.

## Create and configure the codespace

1. Start a codespace by returning to the **Code** tab, then selecting **Code** > **Codespaces** > **Create codespace on main**. (NOTE: This will take a few minutes to open.)
2. After the Codespace launches, open the **Extensions** workbench, and **Update** all extensions as needed, and **Reload window** when done.

## Start the MCP server for a later demo

1. Inside the codespace, open a new terminal window by selecting <kbd>Ctl</kbd>+<kbd>\`</kbd>.

> [!IMPORTANT]
> Perform the next steps off camera as it involves working with the token for your GitHub repository.

2. Obtain your GitHub token by running the following command in the terminal window:

    ```bash
    echo $GITHUB_TOKEN
    ```

3. Copy the token to your clipboard.
4. Open **.vscode/mcp.json** for the list of the MCP servers.
5. Hover over `"github": {` and select **Start** to start the GitHub MCP server.
6. Paste the token you copied earlier and select <kbd>Enter</kbd> or <kbd>Return</kbd>.

## Start the server and open the website

1. Inside the terminal window, run the following commands to install all libraries and start the servers:

    ```bash
    chmod ++x ./scripts/*
    ./scripts/start-app.sh
    ```

2. After the server starts, select <kbd>Ctl<kbd> + **Click** (or <kbd>Cmd<kbd> + **Click** on a Mac) on the link **http://localhost:4321** to open the site.

## Optional tasks

**OPTIONAL**: If you want to clean up the **docs** directory just to hide it, you can delete it if you like. Of course if you're exploring the demos for the first time, leaving it here might be the right decision. :D

**OPTIONAL**: You can create a second codespace to help when demoing Agent Mode. Because Agent Mode can take several minutes, having a second codespace which is already done can help streamline your presentation. To create the backup codespace:

1. Perform the same setup steps as above.
2. Run through the demo steps until [Agent Mode](./3-edit-agent.md#agent-mode).
3. Send the query for Agent Mode, but **do not** run the tests. This will be your pickup point for doing it live.

## Next demo

Next demo: [Code completion](./1-code-completion.md)