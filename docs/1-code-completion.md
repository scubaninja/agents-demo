# Code completion

Code completion is often overlooked these days as Copilot Chat has become more powerful. However, it remains a valuable tool for the developer, as it supports them as they're writing code and helps keep them in the flow. This demo will highlight the importance of context, and demonstrate how open tabs are used by code completion 
to determine context.

## Scenario

You want to create a new [Flask blueprint](https://flask.palletsprojects.com/en/stable/blueprints/) for the application to list all categories for the games in the database.

## Demo background

Because there aren't dialog boxes or options to set context, and the fact that code completion needs to be fast, context is determined "behind the scenes". This can be a bit confusing for developers new to Copilot. This demo highlights how open files are used for context by code completion.

## Demo overview

1. Start with a blank file at **server/routes/categories.py**. Add a couple of comments to explain what you're doing. Note that code completion may not be able to generate optimal code because, among other pieces of information, it lacks the schema for the database and the pattern you've used for other blueprints.
2. Open an existing blueprint at **server/routes/games.py** and the model description at **server/models/game.py**.
3. Return to the new file at **server/routes/categories.py**. Let Copilot begin generating code. Note how Copilot's suggestions follow existing patterns because it saw what you were doing previously.

## Demo steps

1. Explain you want to create a new route for returning all categories from the database.
2. Create a new file at **server/routes/categories.py**.
3. Explain that you have an existing Flask blueprint which you want Copilot to follow the pattern for, and want to ensure it sees the schema for `Category`.
4. Open **server/models/category.py**, the definition for the category model.
5. Open **server/routes/games.py**, an example of an existing Flask blueprint.
6. Inside **server/routes/games.py**, make note of the `get_games_base_query`, a pattern which you want every Flask blueprint to follow.
7. Add the following comments to prompt Copilot to create a new route for returning a list of all categories:

    ```python
    # Create a new Flask blueprint for categories
    # There needs to be a route to list all categories
    # Ensure the list of categories is alphabetized
    # Include docstrings for any functions created
    ```

8. Select <kbd>Enter</kbd> or <kbd>Return</kbd> a couple of times to move away from comments and into code.
9. Begin creating code, explaining that you're going to start by adding in the import statements. This also helps provide context for Copilot to ensure it knows what you're using.

    ```python
    from flask import jsonify, Response, Blueprint
    from models import db, Category
    from sqlalchemy.orm import Query
    ```

10. Select <kbd>Enter</kbd> or <kbd>Return</kbd> a couple of times to move away from the libraries, which will prompt Copilot to begin creating code.
11. Allow Copilot to begin creating code. Note how it includes a comment similar to what appears in **games.py**. Note the `get_categories_base_query` which is created.

> [!IMPORTANT]
> Press enter after the creation of the `categories_bp` variable and the creation of `get_categories_base_query` to ensure spacing and readability.

12. Let Copilot generate the function for returning all categories. The code should look like the following:

    ```python
    # Create a Blueprint for categories routes
    categories_bp = Blueprint('categories', __name__)

    def get_categories_base_query() -> Query:
        """
        Create and return a base query for categories
        
        Returns:
            Query: SQLAlchemy query object for categories
        """
        return db.session.query(Category).order_by(Category.name)

    @categories_bp.route('/api/categories', methods=['GET'])
    def get_categories() -> Response:
        """
        Get all categories
        Returns:
            Response: JSON response with list of categories
        """
        # Use the base query for all categories
        categories_query = get_categories_base_query().all()
        
        # Convert the results using the model's to_dict method
        categories_list = [category.to_dict() for category in categories_query]
        
        return jsonify(categories_list)
    ```

13. Explain the importance of context, and by how having those two files open we set Copilot up for success.
14. Also indicate how when you're writing code you'd naturally have opened those files anyway - you create routes in bunches, and of course would need to refer to an model's schema to create routes for returning the data.
15. Open **server/app.py** and indicate you need to register the new blueprint with the application.
16. Add a new line below line **4** (which should read `from routes.games import games_bp`).
17. Add the code: `from routes.categories import categories_bp`.
18. Add a new line below line **18** (which should read `app.register_blueprint(games_bp)`).
19. Copilot should automatically suggest `app.register_blueprint(categories_bp)` as it saw you import the library previously.
20. Copilot may also suggest registering a route for publishers, which of course doesn't exist yet. It's trying to predict what you're doing, and making the next suggestion.

## Summary

Context is key across all of Copilot. When using code completion, the file currently open and tabs (starting from the one currently open and working out from there) are considered for context. Comments help Copilot quite a bit in understanding what you're trying to do and how you're trying to do it.

## Next demo

Next up, it's time to explore [custom instructions](./2-custom-instructions.md).