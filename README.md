# JSON API Server

A simple locally hosted HTTP server that serves JSON data from a JSON file.

## Getting Started

### Prerequisites

- Python 3.x

### Installing

1. Clone the repository: git clone https://github.com/micahburnside/JSON-HTTP-Server.git
2. Open the terminal or command prompt and navigate to the directory where the program is saved.
`cd "project file path"`
3. Run the program by entering the following command: `python3 csv_to_json_converter.py`


### Usage

1. Place your JSON data file in the project directory. The file should have a `.json` file extension.
2. Start the server by running the following command in the terminal:  `python3 JSON_REST_APIGenerator.py`
3. Select the JSON data file by clicking the "Select JSON File" button in the GUI window that appears.
4. Click the "Start Server" button to start serving the JSON data.
5. Use a web browser or an HTTP client to make a GET request to `http://localhost:8000` to retrieve the JSON data.
6. Click the "Stop Server" button to stop serving the JSON data.

### Queries / Web Browser

To query the API from a web browser, the paramater is `?query`, pass in any value. Queries are case sensitive.
Example: If you have a JSON document that contains fruit names and you wanted to get all the records that contain a certain word, add "=", and then the search term. "Banana". The query would look like this in a web browser `http://localhost:8000?query=Banana`


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


