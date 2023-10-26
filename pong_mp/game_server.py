import socket
import threading
import time

from .game_state import GameState


class GameServer:
    is_running: bool
    tick_rate: int
    connected_clients_lock: threading.Lock
    connected_clients: list[socket.socket]
    sock: socket.socket
    game_state: GameState

    def __init__(self, tick_rate: int = 64) -> None:
        # intialize parameters
        self.is_running = False
        self.tick_rate = tick_rate
        self.connected_clients_lock = threading.Lock()
        self.connected_clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.game_state = GameState()

        # start the update thread
        update_thread = threading.Thread(target=self.update_clients)
        update_thread.daemon = True
        update_thread.start()

    def run(self, host: str, port: int) -> None:
        # start the server
        self.sock.bind((host, port))
        self.sock.listen(2)

        self.is_running = True
        while self.is_running:
            # create a new thread for each connected client
            client_socket, _addr = self.sock.accept()
            client_handler = threading.Thread(
                target=self.handle_client, args=(client_socket,)
            )
            client_handler.daemon = True
            client_handler.start()

    def handle_client(self, client_socket: socket.socket) -> None:
        try:
            # add to connected clients list
            with self.connected_clients_lock:
                self.connected_clients.append(client_socket)

            # receive loop
            while True:
                data = client_socket.recv(data)
                self.parse_client_data(data)
        except Exception as e:
            print(e)

        finally:
            # remove from connected clients list
            with self.connected_clients_lock:
                self.connected_clients.remove(client_socket)

            # close socket
            client_socket.close()

    def parse_client_data(self, data) -> None:
        # parse the data to determine the type of action, like moving the player
        # update game_state to account for this
        pass

    def update_game(self) -> None:
        # new thread for this?
        # should update the ball position within the game state
        pass

    def update_clients(self) -> None:
        try:
            while True:
                # send the game state to every client, at the specified tick rate
                for client in self.connected_clients:
                    client.send(bytes(repr(self.game_state), "utf-8"))
                time.sleep(1 / self.tick_rate)
        except Exception as e:
            print(e)
