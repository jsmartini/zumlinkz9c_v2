from serial import Serial
from serial import SerialException
import pickle
from alive_progress import alive_bar


def serialize(data):
    bdata = pickle.dumps(data)
    size = len(bdata)
    start = "A{0}A".format(size).encode()
    return start + bdata


def setup(dev:str, baud = 115200):
    try:
        return Serial(dev, baudrate=baud)

    except SerialException as e:
        print(e)
        print("could not create radio device")
        exit(-1)

def send(device, data):
    data = serialize(data)
    device.write(data)

def send_progress(device, data):

    """
    coolness factor
    :param data:
    :return:
    """
    data = serialize(data)
    sz = len(data)
    with alive_bar(sz, bar="filling") as bar:
        for i in range(sz):
            device.write(data[i])
            bar()

def read_next(device):
    while device.inWaiting > 0:
        buffer = device.read(1)
        size = ""
        if buffer == b'A':
            while True:
                buffer = device.read(1)
                print(buffer)
                if buffer == b'A':
                    break
                else:
                    size += buffer.decode()
                    continue
        size = int(size)
        try:
            return pickle.loads(device.read(size))
        except:
            continue

def read_next_progress(device):
    if True:
        while True:
            buffer = device.read(1)
            size = ""
            if buffer == b'A':
                while True:
                    buffer = device.read(1)
                    if buffer == b'A':
                        break
                    else:
                        size += buffer.decode()
                        continue
            size = int(size)
            try:
                with alive_bar(size, bar="filling") as bar:
                    data = ""
                    for _ in range(size):
                        data.join(device.read(1).decode())
                        bar()
                    data = data.encode()
                    return pickle.loads(data)
            except:
                continue


