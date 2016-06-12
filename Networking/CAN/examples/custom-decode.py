from canard import can, bus
from canard.file import jsondb
from canard.hw import socketcan
import sys

if len(sys.argv) != 3:
    print('Usage:\n\tpython3 decode.py <dev-name> <db-file>')
    sys.exit(1)

parser = jsondb.JsonDbParser()
b = parser.parse(sys.argv[2])
print(b)

dev = socketcan.SocketCanDev(sys.argv[1])
dev.start()

while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        for s in signals:
            print(s)
        print('---------------------------------------------------')