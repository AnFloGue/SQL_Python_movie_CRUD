# Movies Watch List

This project is a simple command-line application for managing a list of movies. Users can add movies, view upcoming movies, mark movies as watched, and search for movies. The application uses SQLite for data storage.

## Features

- Add new movies with a title and release date.
- View all movies.
- View upcoming movies (movies that have not been released yet).
- Mark movies as watched.
- View watched movies.
- Add users to the app.
- Search for movies by title.

## Requirements

- Python 3.x
- SQLite
## Setup

1. Clone the repository:
    ```sh
    git clone REPOSITORY_URL
    cd <repository-directory>
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python app.py
    ```

## Usage

When you run the application, you will be presented with a menu of options:

## Menu Options

### Adding a New Movie

1. Select option 1.
2. Enter the movie title.
3. Enter the release date in the format `dd-mm-YYYY`.

### Viewing Upcoming Movies

1. Select option 2.

### Viewing All Movies

1. Select option 3.

### Marking a Movie as Watched

1. Select option 4.
2. Enter the username.
3. Enter the movie ID to mark it as watched.

### Viewing Watched Movies

1. Select option 5.
2. Enter the username to view the watched movies.

### Adding a User

1. Select option 6.
2. Enter the username.

### Searching for a Movie

1. Select option 7.
2. Enter a partial movie title to search for.

### Exiting the Application

1. Select option 8 to exit the application.

## Database Schema

The application uses an SQLite database with the following tables:

- `movies`: Stores movie information (id, title, release_timestamp).
- `users`: Stores user information (username).
- `watched`: Stores information about watched movies (user_username, movie_id).

## License

This project is licensed under the MIT License.
