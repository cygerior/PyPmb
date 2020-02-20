class PmbProperty:
    def __init__(self, id: int):
        self.id = id


class PmbCommand:

    def __init__(self, id: int):
        self.id = id


class PmbReadByteCommand(PmbCommand):

    def __get__(self, instance, owner):
        print("read byte get")
        print(instance)
        print(owner)
        return instance.read_byte(self.id)

    def __copy__(self):
        return PmbReadByteCommand(self.id)

    def __call__(self):
        return PmbReadByteCommand(self.id)


class PmbDevice:
    STATUS_BYTE = PmbReadByteCommand(4)

    def __init__(self, i2c_dev):
        self.i2c_dev = i2c_dev

    def read_byte(self, cmdid):
        print("read_byte dev : ", cmdid)
        return "dev val"


class PmbDevicePage:
    STATUS_BYTE = PmbReadByteCommand(4)

    def __init__(self, dev: PmbDevice, pagenum: int):
        self.dev = dev
        self.pagenum = pagenum
        self.sts = dev.STATUS_BYTE()

    def read_byte(self, cmdid):
        print("read_byte page : ", cmdid)
        return "page val"


dev = PmbDevice(504)
page = PmbDevicePage(dev, 0)

print("111111111")
print(dev.STATUS_BYTE)
print("222222222")
print(page.STATUS_BYTE)
