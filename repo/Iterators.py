list = [1,2,3,4,5]
print(dir(list)) # see __iter__

iterator = iter(list)
print(iterator)
print(next(iterator))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


class RemoteControl():
    def __init__(self,channel_list):
        self.channel_list = channel_list
        self.index = -1

    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if(self.index < len(self.channel_list)):
            return self.channel_list[self.index]
        else:
            self.index = -1
            raise StopIteration

rc = RemoteControl(["Trt","DMax","Fox","Kanal D","Bloomberg"])
itera = iter(rc)

for i in rc:
    print(i)


