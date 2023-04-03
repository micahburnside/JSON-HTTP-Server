import json
import http.server
import socketserver
import urllib.parse
import tkinter as tk
from tkinter import filedialog
import threading

# This class extends the BaseHTTPRequestHandler class from the http.server module
class JSONHandler(http.server.BaseHTTPRequestHandler):
    # This method is called when a GET request is received
    def do_GET(self):
        # Parse the query string to get the value of the 'query' parameter
        parsed_query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        query_term = parsed_query.get('query', [''])[0]

        # Check if a JSON file has been selected
        if not selected_file_path:
            # If no JSON file is selected, send a 500 error response
            self.send_error(500, 'No JSON file selected')
            return

        try:
            # Set response headers
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Load data from selected JSON file
            with open(selected_file_path) as f:
                data = json.load(f)

            # Filter data by query term
            filtered_data = [record for record in data if query_term in record.values()]

            # Send prettified JSON data as response
            response_data = json.dumps(filtered_data, indent=4)
            self.wfile.write(response_data.encode())

        except Exception as e:
            # If an error occurs while processing the request, send a 500 error response
            self.send_error(500, str(e))
            return



# This function starts the HTTP server and listens for incoming requests
def start_server():
    global server
    PORT = 8000
    # Create a new instance of the TCPServer class and bind it to the specified port
    server = socketserver.TCPServer(("", PORT), JSONHandler)
    print(f"Serving at port {PORT}")
    # Start serving requests indefinitely
    server.serve_forever()

# This function stops the HTTP server
def stop_server():
    # Shut down the server and close the socket
    server.shutdown()
    server.server_close()
    print("Server stopped")

# This function opens a file dialog window and allows the user to select a JSON file
def choose_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    # Update the file label text to display the selected file path
    file_label.config(text="Selected file: " + selected_file_path)
    # Resize GUI width to fit selected file path text
    root.geometry(f"{file_label.winfo_reqwidth()+40}x200")
    
# This function starts the HTTP server in a separate thread
def start_server_thread():
    global server_thread
    # Create a new thread and target it to the start_server() function
    server_thread = threading.Thread(target=start_server)
    # Start the thread
    server_thread.start()

# Create a new instance of the Tk class to create the GUI window
root = tk.Tk()
root.title("JSON API Server")

# Set the initial size of the GUI window to fit the file path text
root.geometry("400x200")

# Initialize the selected_file_path variable to an empty string
selected_file_path = ""

# Create the GUI widgets
file_button = tk.Button(root, text="Select JSON File", command=choose_file)
file_button.pack(pady=10)

file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=10)

start_button = tk.Button(root, text="Start Server", command=start_server_thread)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Server", command=stop_server)
stop_button.pack(pady=10)

# Start the Tkinter main loop to run the GUI application
root.mainloop()
