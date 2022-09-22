import psutil
import time


def get_memory() -> dict:
    memory_dict = {}
    memory = psutil.virtual_memory()
    memory_dict["total"] = round(memory.total / 1024.0 ** 3, 3)
    memory_dict["available"] = round(memory.available / 1024.0 ** 3, 3)
    memory_dict["used"] = round(memory.used / 1024.0 ** 3, 3)
    memory_dict["percent"] = round(memory.percent / 1024.0 ** 3, 3)

    return memory_dict


while True:
    memory = get_memory()
    memory["time"] = str(time.strftime("%H:%M:%S"))
    print(memory)
    time.sleep(120)