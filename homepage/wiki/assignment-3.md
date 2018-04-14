# Assignment 3 - An HTTP-based Movie Search Engine

* Full Mark: **100** (**10%** of the course assessment scheme)
* Deadline: 24th March, 2018
* Submission: See instructions below
* NOTE: The assignment must be finished using Python

## Overview

In this assignment, you will implement a simple **movie search engine** with some **social functions**. The server will provide APIs (application programming interfaces) for clients to use functions such as searching for a movie or leaving a comment. Both the server and the client program should be implemented in Python.

In this assignment, we will use a dataset from the [Internet Movie Database](http://www.imdb.com/) (IMDb) to populate the content of our search engine. The dataset can be found on Kaggle ([https://www.kaggle.com/PromptCloudHQ/imdb-data/data](https://www.kaggle.com/PromptCloudHQ/imdb-data/data)). A copy of the data in CSV format can also be found here: [http://iems5703.albertauyeung.com/files/imdb_top1000.csv](http://iems5703.albertauyeung.com/files/imdb_top1000.csv).

## Detailed Descriptions

### Server

The server provides several functions:

1. **[Search for movies using a given query string]**: The client can choose to search for the query string in the **movie title** or in the **list of actors/actresses**. A list of movies matching the criteria will be returned to the client, sorted in the way specified by in the request.
2. **[Retrieve information of a movie]**: When given the ID of a movie, the server will return the all the information about the movie. Including the list of comments left by the users (see the next function).
3. **[User comment]**: A user can leave a comment on a movie by submitting a request to the server, by specifying the ID of the movie and the content of the message.

The server should be executed by providing the port number on which it should listen for incoming client connections:

    :::bash
    $ python3 server.py 5000


#### APIs

The server should be implemented using the [Flask](http://flask.pocoo.org/) Web framework. It should provide **three APIs** (i.e. three different paths for accessing the three different functions). The detailed description of each API can be found below. All response should be in **JSON** format.

* `GET: /search`
    - Receives HTTP GET requests from clients. Search for movies that matches the search criteria (see below for more instructions on how to match). Also, the result will be sorted in a way specified in the query
    - Search should be **case insensitive**
    - Return **at most 10 results**
    - Query string parameters:
        - `query`: the query string specified by the user
        - `attribute`: the attribute in which the query string should appear. This must be one of the following: **title**, **actor** or **both**. If it is **both**, it means the query should either appear in the title or in the actor field.
        - `sortby`: specify how the results should be sorted. This must be one of the following: **year**, **revenue** or **rating**
        - `order`: the order in which results should be sorted. This must be one of the following: **ascending** or **descending**
* `GET: /movie/<movie_id>`
    - Receives HTTP GET requests from clients. Retrieve the information of a movie using the movie ID provided in the URL.
    - You can assume that the movie ID is always valid
    - No query string parameter is needed.
* `POST: /comment`
    - Receives HTTP POST requests from clients. The server will stores the comment for a particular movie as part of the information of a movie.
    - A timestamp in the format of **YYYY-MM-DD HH:MM:SS** should be added to the record
    - It should return the details of the movie commented on, with the same format as the movie details API
    - Parameters:
        - `movie_id`: the ID of the movie
        - `user_name`: the name of the user
        - `comment`: the content of the comment

Examples of requests and responses of each of the above APIs are given below:

Search Example 1: (not all results are shown)

    :::javascript
    Request: /search?query=world&attribute=title&sortby=year&order=descending

    Response:
    {
    "movies": [
        {
            "Actors": "Nathalie Baye, Vincent Cassel, Marion Cotillard, L\u00e9a Seydoux", 
            "Director": "Xavier Dolan", 
            "Genre": "Drama", 
            "Rating": 7.0, 
            "Revenue (Millions)": 0.0, 
            "Title": "It's Only the End of the World", 
            "Year": 2016, 
            "id": 978
        }, 
        {
            "Actors": "Chris Pratt, Bryce Dallas Howard, Ty Simpkins,Judy Greer", 
            "Director": "Colin Trevorrow", 
            "Genre": "Action,Adventure,Sci-Fi", 
            "Rating": 7.0, 
            "Revenue (Millions)": 652.18, 
            "Title": "Jurassic World", 
            "Year": 2015, 
            "id": 85
        },
        ...
    }

Search Example 2: (not all results are shown)

    :::javascript
    Request: /search?query=leonardo&attribute=actor&sortby=rating&order=descending

    Response:
    {
    "movies": [
        {
            "Actors": "Leonardo DiCaprio, Matt Damon, Jack Nicholson, Mark Wahlberg", 
            "Director": "Martin Scorsese", 
            "Genre": "Crime,Drama,Thriller", 
            "Rating": 8.5, 
            "Revenue (Millions)": 132.37, 
            "Title": "The Departed", 
            "Year": 2006, 
            "id": 99
        }, 
        {
            "Actors": "Leonardo DiCaprio, Djimon Hounsou, Jennifer Connelly, Kagiso Kuypers", 
            "Director": "Edward Zwick", 
            "Genre": "Adventure,Drama,Thriller", 
            "Rating": 8.0, 
            "Revenue (Millions)": 57.37, 
            "Title": "Blood Diamond", 
            "Year": 2006, 
            "id": 669
        },
        ...
    }

Movie Details Example 1:

    :::javascript
    Request: /movie/99

    Response:
    {
        "Actors": "Leonardo DiCaprio, Matt Damon, Jack Nicholson, Mark Wahlberg", 
        "Description": "An undercover cop and a mole in the police attempt to identify each other ...", 
        "Director": "Martin Scorsese", 
        "Genre": "Crime,Drama,Thriller", 
        "Metascore": 85.0, 
        "Rank": 100, 
        "Rating": 8.5, 
        "Revenue (Millions)": 132.37, 
        "Runtime (Minutes)": 151, 
        "Title": "The Departed", 
        "Votes": 937414, 
        "Year": 2006, 
        "comments": [], 
        "id": 99
    }

Comment Example:

    :::javascript
    Request: /comment
    user_name = albertauyeung
    movie_id = 85
    comment = Nice movie!

    Response:
    {
        "Actors": "Chris Pratt, Bryce Dallas Howard, Ty Simpkins,Judy Greer", 
        "Description": "A new theme park, built on the original site of Jurassic Park, ...",
        "Director": "Colin Trevorrow", 
        "Genre": "Action,Adventure,Sci-Fi", 
        "Metascore": 59.0, 
        "Rank": 86, 
        "Rating": 7.0, 
        "Revenue (Millions)": 652.18, 
        "Runtime (Minutes)": 124, 
        "Title": "Jurassic World", 
        "Votes": 455169, 
        "Year": 2015, 
        "comments": [
            {
                "comment": "Nice movie!", 
                "timestamp": "2018-03-04 08:34:18", 
                "user_name": "albertauyeung"
            }
        ], 
        "id": 85
    }

### Data Preprocessing

You application starts by reading the data stored in the CSV file provided. To be an efficient search engine, your app should load the data from the file during initialization, and NOT when a request is received.

In addition, you should NOT use a simple string operation for searching movies using the given query. For example, if the user's query is **moon**, the search engine should return the movie **Transformers: Dark of the Moon**, but not **Moonlight**. This is because **moon** does not appear in the title **Moonlight** as a separate word.

Therefore, during initialization, you should perform the following operations to prepare the data:

1. Load the data from the CSV file, create a data structure for holding the movie information in memory
2. Create a [inverted index](https://en.wikipedia.org/wiki/Inverted_index) for the movie titles and movie actors

For Step 1, you can do so with the help of [pandas](https://pandas.pydata.org/), which is a library for processing and manipulating tabular data. You can use it to load a CSV file and convert the data, say, into a list of dictionaries (where each row in the CSV becomes a dictionary in Python).

For Step 2, an inverted index is an index of data using the words that appear in it. The purpose of an inverted index is to speed up the process of looking up some data when given a search query. For example, given the word **moon**, instead of going through all the movie titles and look for the word **moon**, we can first build an inverted index, and then use the index to find movies with the word **moon**.

An inverted index may look like something below:

    :::python
    title_index = {
        "moon": [556, 598],
        "world": [75, 85, 158, 214, 432, 799, 978],
        ...
    }

In the above example, the keys of the index are words that are found in some movie titles, while the values are lists of the IDs of movies whose titles contain that word. When a query is received, we can simply look up the list of movies using this `title_index` variable.

To create the inverted index for titles and actors, you can use [nltk](https://www.nltk.org)'s `word_tokenize` function to split a sentence into separate words.

### Storing Data in the Flask App

In this assignment, we do not use a database to store our data. Hence, all data will be stored in the memory. (As a result, when you terminate the application, all data submitted by the clients, such as the comments, will be lost.)

When using Flask, you can store data in the application when performing initalization. For example:

    :::python
    from flask import Flask

    app = Flaks(__name__)
    app.movies = [...]
    app.title_index = {...}
    ...

Afterwards, when a request arrives at the application, you can access these variables by using the `current_app` object. For example:

    :::python
    from flask import current_app

    ...

    @app.route('/search', method=['GET'])
    def search():
        ...
        movies = current_app.movies  # Get the movies loaded during initialization
        ...

### Client

You should also create a simple client to access the three APIs of the server. You are advised to use the [requests](http://docs.python-requests.org/en/master/) library to make HTTP requests.

Your client script should accept arguments on the command line, and print out the JSON response from the server directly on the screen.

For output, you can simply convert the JSON response into a well-formatted string using the `json` module. You can specify the indentation in the `dumps` method. For example:

    :::python
    >>> import json
    >>> d = {"x": 1, "y": 2}
    >>> formatted_json = json.dumps(d, indent=4)
    >>> print(d)
    {
        "y": 2,
        "x": 1
    }


Submit the query **world** to search movies with the word in the **title**, and sort the movies by **year** in **descending** order. The first two arguments are always the host and the port number of the server.

    :::bash
    $ python3 client.py localhost 50000 search world title year descending
    ...

Submit a request to retrieve information about a movie by providing a `movie_id`:

    :::bash
    $ python3 client.py localhost 50000 movie 85
    ...

For submitting comment, the user specifies the `user_name` and `movie_id` in the command line arguments. But you should use the `input` function of Python to get the input from the user after the script is executed:

    :::bash
    $ python3 client.py localhost 50000 comment albert 85
    What is your comment? <User inputs his/her comment here and press enter>
    ...


### Testing

To test your application, you can simply access a particular URL on your browser. However, it would be more difficult to test the comment API as it accepts POST requests. You can use [Postman](https://www.getpostman.com/), which is a standalone application for issuing HTTP requests to HTTP servers. It allows sending GET or POST requests to your application and inspecting the resposne easily.


### FAQ

1. What would be submitted as a query string?
    - You can assume that the query string is always a single word with no special characters
2. Does the client need to check the validity of the input?
    - You can assume that the arguments provided to the client is always valid
3. Should the search be case sensitive or case insensitive?
    - The search should be CASE INSENSITIVE
4. How should the server be deployed?
    - You just have to make sure that the server works by using the internal test server of Flask
5. You see different order of the fields when printing the JSON response.
    - You can set `sort_keys=True` when using `json.dumps()`, then the keys of the dictionary will always be sorted.

## Submission

Prepare the following python scripts:

1. The server script `server.py`
2. The client script `client.py`

Put the two scripts in a folder named using your student ID, and compress the folder using zip, resulting in a compressed file `<student_id>.zip` (e.g. `12345678.zip`). Submit this file to the assignment submission page in Blackboard.
