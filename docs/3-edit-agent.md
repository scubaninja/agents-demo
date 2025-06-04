# Edit and agent mode to work with multiple files

Most coding tasks require updates across multiple files. Copilot provides two modes, Edit and Agent, to support these types of tasks. Edit mode is more guided by the developer, while Agent mode is more autonomous, and has the ability to run additional tasks like running tests and self-healing.

> [!IMPORTANT]
> Highlight the importance of **always** reviewing AI generated code and the DevOps process.

## Scenario

Now it's time to both finish out the endpoint for publishers as well as create the front end. We'll perform the former by using Copilot Edits, and the latter by using Agent Mode.

## Demo background

> [!IMPORTANT]
> Both Copilot Edit and Agent Mode can take a little bit of time (minutes) to perform their tasks. If you are demoing live, this is a good opportunity to open the floor for a question or two, or to switch to a "baked cake" where the task has already been completed and you can talk through what's been done.

This demo is built to demonstrate Copilot Chat's ability to work across multiple files, and introduce the agent capabilities recently introduced.

## Demo overview

1. Return to the prior demo, ensuring the prompt file and prompt are set correctly.
2. Enable **Edit** mode and send the prompt. Demonstrate how you can keep/undo changes, and the history provided in Edit mode to allow for experimentation.
3. Keep all the files once it's complete.
4. Utilize **Agent Mode** to create the front end and run the unit tests. Demonstrate how Agent Mode is able to perform non-coding tasks, and even self-heal if issues are discovered.

## Demo steps

### Copilot Edits

Let's demonstrate how Copilot Edits can modify multiple files.

1. Return to your codespace and to your chat window.
2. Select **Edit** mode and **Claude 3.7 Sonnet**.
3. Ensure the prompt file for **add-endpoint** is added. You can do this by selecting **Add Context**, then **Prompt** from the dropdown above (typing the word prompt in the dialog may be faster), then selecting **create-endpoint**.
4. Ensure just the **publisher.py** file is added to context. You can do this by using `#publisher.py` and selecting **publisher.py**.
5. Send the following prompt (the same which was used previously):

    ```plaintext
    Create a new blueprint for publishers. Create one for get all and one for get by id.
    ```

6. Highlight how Copilot Edits begins working across multiple files. It generates the blueprint, the necessary tests, and updates **app.py**.
7. Highlight the **Keep** and **Undo** buttons, both on individual files and for the entire operation. Highlight the importance of **always** reviewing AI generated code.
8. Highlight the **Undo** and **Redo** buttons at the top, and how this enables experimentation for developers. You can actually send multiple prompts, working iteratively and doing undo/redo to ensure you generate the correct code.
9. Once you've reviewed the code, select **Keep** in the chat window to accept all code, then **Done** to complete the session.

### Agent Mode

There's more to writing code than just writing code, and Agent Mode is able to both write code and perform external tasks. In particular, it's able to self-discover what needs to be accomplished (in a similar fashion to a developer), and run external tasks like running tests. It's also able to self-heal as issues are detected. We're going to use Agent mode to generate the front end and to run our tests.

1. Inside Copilot Chat, select **+** to start a **New Chat** to clear any context from before.
2. Select **Agent** to enable Agent Mode.
3. Send the following prompt:

    ```plaintext
    Add functionality to the website to allow users to filter games by publisher and category. The page should have dropdowns which list the publishers and categories. When the index changes the page should update. Also ensure there is an all option for each. And run the server-side tests, and ensure they pass.
    ```

> [!IMPORTANT]
> This demo may take several **minutes** to complete. You can talk through the initial portion (the exploration of the project), highlighting how Copilot is behaving in a similar fashion to a developer. Then take some questions, then return for the next steps.
> 
> Alternatively, if you [created a second codespace](./0-setup.md#optional-tasks), you can pickup from there where, explaining the tasks performed, and run the unit tests.

4. Agent Mode will begin by exploring the projecting, finding files, and figuring out what's already been done.
5. Once it's completed its information gathering, it will generate the necessary changes. This will include updating files and (potentially) creating a couple of new ones.
6. It will also prompt you to run the tests, which can be done by selecting **Continue** when prompted.
7. Once completed, you can open the website to see the changes. You may need to refresh it.
8. Highlight again the importance of code review. Once you're satisfied, select **Keep** and **Done** to complete the task.

## Summary

This demo walks through both Copilot Edits and Agent Mode. It shows the difference between the two, how Edits is more developer-guided while Agent is able to be more autonomous.

## Next demo

Finally, it's time to show how [Model Context Protocol (MCP)](./4-mcp.md) enables access to external services.
