
from core import GsmCore

class CallMixin(GsmCore):
    def call(self, number):
        self._write("ATD" + number + ";")
    def accept_call(self):
        self._write("ATA")
    def cut_call(self):
        self._write("ATH")
    def loop(self):
        notification = self.get_response(timeout_ms=200)
        if "RING" in notification:
            print("Incoming call......")
        if notification:
            print(notification)
