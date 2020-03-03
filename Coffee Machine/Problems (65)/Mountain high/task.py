class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        return self.height / 0.3048


# create mountains here
everest = Mountain("Everest", 8848)
aconcagua = Mountain("Aconcagua", 6960.8)
print(everest.convert_height(), aconcagua.convert_height())
