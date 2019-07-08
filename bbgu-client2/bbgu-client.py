import websocket
import spider

try:
    import thread
except ImportError:
    import _thread as thread
import time

class WSRserver:
    def on_message(self,ws, message):
        print(message)

    def on_error(self,ws, error):
        print(error)

    def on_close(self,ws):
        print("### closed ###")

    def on_open(self,ws):
        print("connect websocket successful")
        ws.send("hello")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.21.118:8080/backend",
                              on_message = WSRserver.on_message,
                              on_error = WSRserver.on_error,
                              on_close = WSRserver.on_close)
    ws.on_open = WSRserver.on_open
    ws.run_forever()