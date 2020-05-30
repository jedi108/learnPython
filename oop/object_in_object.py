class A:
    def __init__(self, send):
        self._send = send

    def sending(self, msg):
        self._send.send(msg)


class Sender:
    def send(self, msg):
        print('msg', msg)

send = Sender()
a = A(send)
a.sending("text")
