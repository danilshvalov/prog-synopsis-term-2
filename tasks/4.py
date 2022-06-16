class ObjectWithCounter:
    counter = 1

    def __init__(self):
        self.id = ObjectWithCounter.counter
        ObjectWithCounter.counter += 1

    def print_id(self):
        print("Мой порядковый номер:", self.id)


def main():
    o1 = ObjectWithCounter()
    o2 = ObjectWithCounter()
    o3 = ObjectWithCounter()

    o1.print_id()
    o2.print_id()
    o3.print_id()

if __name__ == "__main__":
    main()
