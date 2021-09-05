import argparse
import logging

import socketio
import treefiles as tf
from pyPS4Controller.controller import Controller

sio = socketio.Client()
device_path = "/dev/input/js1"  # Default, overwritten by parsed `device` argument


@sio.event
def connect():
    log.info("Connection established with server")

    class MyController(Controller):
        def on_R2_press(self, v):
            sio.emit("updt", {"x": 0, "y": v * 1e-3})

        def on_L2_press(self, v):
            sio.emit("updt", {"x": v * 1e-3, "y": 0})

        def on_L3_down(self, v):
            sio.emit("updt", {"x": 0, "y": v * 1e-3})

        def on_L3_up(self, v):
            sio.emit("updt", {"x": 0, "y": v * 1e-3})

        def on_L3_left(self, v):
            sio.emit("updt", {"x": v * 1e-3, "y": 0})

        def on_L3_right(self, v):
            sio.emit("updt", {"x": v * 1e-3, "y": 0})

    controller = MyController(interface=device_path)
    controller.listen()


def start_client():
    url = "https://loc.kerga.ga"
    log.info(f"Click here to play: {url}")
    sio.connect(url)


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    log = tf.get_logger()
    logging.getLogger("urllib3").setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("device", type=str)
    args = parser.parse_args()
    device_path = args.device

    start_client()
