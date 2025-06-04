# Custom instructions and context in chat

Copilot Chat is extremely powerful, and continues to gain new functionality. However, context is always key regardless of the operations being performed. We'll highlight various ways of providing the right information to context to drive quality code suggestions.

## Scenario

To continue adding functionality to our website, we want to include an ability to filter games by publisher. We're going to start by exploring the project, then creating the blueprint and the required tests for the backend functionality.

## Demo background

Couple of core notes about this demo:

- You will be performing the same steps different ways. This is to help highlight the impact certain operations have on code generation.
- The demo will end with a transition to the next section of using Copilot Edit.
- As for the model, the author personally uses **Claude 3.7 Sonnet** for basically everything, but you can explore as you see fit.

## Demo overview

1. Start by using `@workspace` to explore the project and determine what files are used for the backend.
2. Highlight how `#file` can be used to add a file to context when talking to chat.
3. Introduce [custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) and highlight the difference in code generation as updates are made.
4. Close by exploring a prompt file and transitioning to an introduction of Copilot edit mode.

## Demo steps

### Using @workspace to explore a project

Let's highlight how `@workspace` can be used to interact with the entire workspace, and is really powerful for tasks like searching.

1. Return to your codespace.
2. Open Copilot Chat and ensure **Ask** mode is enabled and **Claude 3.7 Sonnet** (or your preferred model) is selected.
3. Explain you need to create a new blueprint for publishers, but are a new developer to the project. You're not sure where code is defined in your application.
4. Add `@workspace` to the chat prompt, selecting <kbd>Tab</kbd> to activate it.
5. Send the following prompt to Copilot Chat:

    ```plaintext
    @workspace How is the backend built for this application? If I needed to add a new route for listing all publishers where would I put it?
    ```

6. Highlight the information Copilot gives you. Show how you didn't use any technical terms, but were able to explore the project in natural language. Also show how Copilot gave you instructions on what needs to be done to create your new route.
7. Scroll to the top of the answer and expand the **references** section. Note how `@workspace` created an index of your project, and was able to use it to do a search.
8. Introduce the fact that too much context can be a bad thing at times, that it can be difficult for Copilot to determine what's important. This is of course the same as with real life, that too much information can make it challenging to determine the key points.

### Adding specific files for context

Highlight the importance of pointing to the most relevant information, and how `#file` can be used to introduce context.

1. Create a new file at **server/routes/publishers.py**.
2. Explain that you want to create a new route for returning all publishers. You want to use an existing route as a blueprint.
3. Inside chat, begin typing `#games.py` and select **games.py** from the inline selection window which appears as you begin typing. Explain that this adds the `games` blueprint to context, which you want to use as, well, a blueprint.
4. Repeat the step for `#publisher.py` (**NOTE:** not plural) and select **publisher.py** inside **server/models** to bring the model into context. This will allow Copilot to understand the schema.
5. Add the following prompt to tell Copilot to generate the code:

    ```plaintext
    Create a new blueprint for publishers. Create one for get all and one for get by id.
    ```

6. Select <kbd>Enter</kbd> or <kbd>Return</kbd> to send the query.
7. Highlight the **references** section, noting it used the two files you added.
8. Note the code generated, how it follows the pattern set in **games.py**.
9. **DO NOT** add the code to the file. We'll do that later.
10. Explain that we're currently missing docstrings, which is a spec we want to follow.

### Custom instructions

Highlight how custom instructions (copilot-instructions.md) allow you to set project-level guidance for Copilot.

1. Return to your chat window.
2. Scroll to the top of the last prompt you sent, and show how **copilot-instructions.md** was sent even though you didn't add it to the context.
3. Highlight this is custom instructions, and is used for **every** request made of Copilot Chat (and Copilot Chat only).
4. Open **.github/copilot-instructions.md**.
5. Walk through the file, highlighting the key sections.
6. Add the following to the bottom of the file:

    ```markdown
    - Docstrings are required for all Python functions
    ```

7. Close **custom-instructions.md** and open the empty **publishers.py** file.
8. Inside Copilot Chat, select **+** to start a **New Chat** to clear any context from before.
9. Build the same query as before, using `#games.py` and `#publisher.py` to the context.
10. Send the same prompt as before:

    ```plaintext
    Create a new blueprint for publishers. Create one for get all and one for get by id.
    ```

11. Note the difference in code, how docstrings are new included in the code.

### Prompt files

Highlight that coding often involves performing tasks which need to follow a particular template. For example, maybe all React components need to use the same structure. Prompt files allow you to set templates to follow.

1. When creating a new set of routes there's going to be a set of rules we need to follow. Prompt files allow us to provide that set of instructions for specific tasks.
2. Open **.github/prompts/create-endpoint.prompt.md**.
3. Walk through the key sections of the file, noting:
    - Guidelines for creating the files, which include background and instructions about unit tests.
    - The prototype files, which are links to existing files in the project but are good examples of what we're doing and how we're doing it.
    - Highlight how to build a proper blueprint we need to update 3 files - the blueprint itself, a set of tests, and registration with **app.py**.
4. Return to Copilot Chat and create a new chat by again selecting **+** for **New Chat**.
5. Add the prompt file by selecting **Add Context**, then **Prompt** from the dropdown above (typing the word prompt in the dialog may be faster), then selecting **create-endpoint**.
6. Add just the publisher definition this time by using `#publisher.py`.
7. **BUT** before typing the rest of the prompt, note how multiple files need to be updated or created. **Ask** mode is built for questions and working with individual files. For multiple files we need a different mode... **Edit mode**

> [!IMPORTANT]
> This is the transition point to the next section, a bit of a cliffhanger. Don't worry, we won't leave everyone hanging for long.

## Summary

This demo walks through how to set context on Copilot Chat. It explored various commands like `@workspace` and individual files. It also introduces both custom instructions, which are used for every message sent to chat, and prompt files for individual tasks.

## Next demo

Next you'll explore both [Copilot Edits and Agent Mode](./3-edit-agent.md).
