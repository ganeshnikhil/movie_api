# movie_api


**Project Name**

This Flask application provides a web API for searching and retrieving movie data from a CSV file.

**Features**

* Search for movies by name using a user-friendly API endpoint.
* Retrieve movie details (ID, name, and summary) by movie name or ID.
* Handle cases where movies are not found and return appropriate error messages.


**Movie Search with Fuzzy Matching**

This Python script searches and retrieves movie data from a CSV file. It supports exact and fuzzy (misspelled) searches and measures execution time.

**Features:**

* Reads movie data from CSV (ID, Name, Summary)
* Sorts by name (case-insensitive)
* Finds movies by exact name (binary search)
* Performs fuzzy matching with `fuzzywuzzy`
* Returns movie details (ID, Name, Summary) or empty string (not found)
* Measures execution time of search function

**Installation:**

1. **Prerequisites:** Ensure you have Python (version 3.x recommended) and pip (the package installer) installed on your system. You can verify this by running `python --version` and `pip --version` in your terminal.
2. **Create a virtual environment (recommended):** This helps isolate project dependencies and avoid conflicts. You can use tools like `venv` or `virtualenv` for this.
3. Python (version 3.x recommended)
4. `pip install -r requirements.txt`

**Usage:**

1. Update CSV file path if needed (`"database/film.csv"`)
2. Run: `python your_script_name.py` (prints search function execution time)

**CSV Example:**

```csv
ID,Name,Summary
1,The Shawshank Redemption,A timeless story...
2,The Godfather,Epic saga of a family...
```

**Further Enhancements:**

* User Input for Searches
* Error Handling
* CSV Writing (optional)

**Usage**

1. **Run the application:** Start the Flask development server by running `python app.py` (replace `app.py` with your actual script name) in your terminal.
2. **Search by movie name:** Send a GET request to the following endpoint, replacing `<movie_name>` with the movie you want to search for (spaces can be replaced with underscores):

   ```
   http://localhost:5000/<movie_name>/
   ```

   Example:

   ```
   http://localhost:5000/The_Shawshank_Redemption/
   ```

3. **Search by ID:** Send a GET request to the following endpoint, replacing `<id>` with the numerical ID of the movie you want to find:

   ```
   http://localhost:5000/<id>/
   ```

   Example:

   ```
   http://localhost:5000/1/
   ```

**Response**

The API will respond with a JSON object containing the movie's details (ID, name, and summary) if found. If the movie is not found, the response will contain an error message.

**Example Response (Movie Found):**

```json
{
  "ID": 1,
  "Name": "The Shawshank Redemption",
  "Summary": "A timeless story of hope and friendship in prison"
}
```

**Example Response (Movie Not Found):**

```json
{
  "ID": null,
  "Name": "not found.",
  "summary": null
}
```

**CSV Data**

The application expects a CSV file named `database/film.csv` to be present in the same directory as your Python script. This file should contain movie data in the following format:

```csv
ID,Name,Summary
1,The Shawshank Redemption,A timeless story of hope and friendship in prison
2,The Godfather,Epic saga of a family in organized crime
# ... (more movies)
```

**Error Handling**

The application handles potential errors gracefully, such as:

* Missing CSV file: If the `database/film.csv` file is not found, the application will log an error message.
* Invalid movie name or ID: If a movie with the provided name or ID is not found, the API will return a JSON response indicating that the movie is not found.

**Testing**

You can use tools like Postman or curl to send requests to the API endpoints and verify the responses.

**Deployment**

For production deployment, you'll need to choose a suitable web server like Gunicorn or uWSGI to host the Flask application. Refer to the respective documentation for detailed instructions.

**Additional Notes**

* This is a basic example to demonstrate movie search functionality. You can extend it to include features like sorting, filtering, or adding new movies.
* Consider implementing authentication and authorization mechanisms for a more secure production environment.

I hope this README file provides a clear and comprehensive guide to using your Flask application!
