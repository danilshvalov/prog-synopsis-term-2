class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def read_title():
        return input("Введите название: ")

    def read_price():
        return float(input("Введите стоимость: "))

    def get_data():
        print("Информация о публикации")
        title = Publication.read_title()
        price = Publication.read_price()
        return Publication(title, price)

    def put_data(self):
        return f"Publication {{ title: {self.title}, price: {self.price} }}"


class PaperBook(Publication):
    def __init__(self, title, price, page_count):
        super().__init__(title, price)
        self.page_count = page_count

    def get_page_count(self):
        return self.page_count

    def read_page_count():
        return int(input("Введите количество страниц: "))

    def get_data():
        print("Информация о книге")
        title = Publication.read_title()
        price = Publication.read_price()
        page_count = PaperBook.read_page_count()
        return PaperBook(title, price, page_count)

    def put_data(self):
        return f"PaperBook {{ title: {self.title}, price: {self.price}, page_count: {self.page_count} }}"


class AudioBook(Publication):
    def __init__(self, title, price, duration):
        super().__init__(title, price)
        self.duration = duration

    def get_duration(self):
        return self.duration

    def read_duration():
        return float(input("Введите продолжительность: "))

    def get_data():
        print("Информация об аудио книге: ")
        title = Publication.read_title()
        price = Publication.read_price()
        duration = AudioBook.read_duration()
        return AudioBook(title, price, duration)

    def put_data(self):
        return f"AudioBook {{ title: {self.title}, price: {self.price}, page_count: {self.duration} }}"


def main():
    pub = Publication.get_data()
    paper = PaperBook.get_data()
    audio = AudioBook.get_data()

    print(pub.put_data())
    print(paper.put_data())
    print(audio.put_data())


if __name__ == "__main__":
    main()
