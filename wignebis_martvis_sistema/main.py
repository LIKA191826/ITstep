# ============================================================
# წიგნების მართვის სისტემა
# მარტივი პროგრამა, სადაც შეგვიძლია წიგნების დამატება,
# ნახვა, ძებნა და წაშლა.
# ============================================================


# კლასი აღწერს ერთ წიგნს — რა მონაცემები აქვს მას
class Book:
    def __init__(self, title, author, year):
        # __init__ იძახება მაშინ, როცა ახალ წიგნს ვქმნით
        self.title = title      # წიგნის სათაური
        self.author = author    # ავტორის სახელი
        self.year = year        # გამოცემის წელი

    def show_info(self):
        # ეს მეთოდი აბრუნებს წიგნის ინფორმაციას ტექსტად
        return f"{self.title} | {self.author} | {self.year}"


# აქ ვინახავთ ყველა წიგნს სიაში (list)
# პროგრამის გაშვებისას სია ცარიელია
books = []


def add_book():
    # წიგნის დამატების ფუნქცია
    print("\n--- წიგნის დამატება ---")
    title = input("შეიყვანე სათაური: ")
    author = input("შეიყვანე ავტორი: ")
    year = input("შეიყვანე წელი: ")

    # ვამოწმებთ, რომ ველები ცარიელი არ იყოს
    if title == "" or author == "" or year == "":
        print("შეცდომა: ყველა ველი უნდა შეავსო!")
        return

    # ვქმნით ახალ წიგნის ობიექტს და ვამატებთ სიაში
    new_book = Book(title, author, year)
    books.append(new_book)
    print("წიგნი წარმატებით დაემატა!")


def show_all_books():
    # ყველა წიგნის ჩვენება
    print("\n--- ყველა წიგნი ---")

    # თუ სია ცარიელია, შეტყობინებას ვწერთ
    if len(books) == 0:
        print("სიაში ჯერ არც ერთი წიგნი არ არის.")
        return

    # for ციკლით გადავუვლით ყველა წიგნს
    # enumerate გვაძლევს ნომერსაც (1-დან)
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.show_info()}")


def search_book():
    # წიგნის ძებნა სათაურით
    print("\n--- წიგნის ძებნა ---")
    search_title = input("რომელი სათაური მოძებნო: ")

    found = False  # ჯერ ვთვლით, რომ ვერ ვიპოვეთ

    for book in books:
        # lower() რომ დიდი/პატარა ასოები არ უშლიდეს ხელს
        if search_title.lower() in book.title.lower():
            print("ნაპოვნია:", book.show_info())
            found = True

    if not found:
        print("ასეთი წიგნი ვერ მოიძებნა.")


def delete_book():
    # წიგნის წაშლა ნომრით
    print("\n--- წიგნის წაშლა ---")

    # ჯერ ვაჩვენებთ სიას, რომ მომხმარებელმა ნომერი იცოდეს
    show_all_books()

    if len(books) == 0:
        return

    number = input("რომელი ნომრის წიგნი წავშალო: ")

    # ვამოწმებთ, რომ შეყვანილია რიცხვი
    if not number.isdigit():
        print("შეცდომა: უნდა შეიყვანო რიცხვი!")
        return

    number = int(number)

    # ნომერი უნდა იყოს სწორ დიაპაზონში
    if number < 1 or number > len(books):
        print("შეცდომა: ასეთი ნომერი არ არსებობს!")
        return

    # სიაში ინდექსი იწყება 0-დან, ამიტომ ვაკლებთ 1-ს
    removed = books.pop(number - 1)
    print(f"წაიშალა: {removed.title}")


def show_menu():
    # მენიუს ბეჭდვა
    print("\n========== წიგნების მართვის სისტემა ==========")
    print("1. წიგნის დამატება")
    print("2. ყველა წიგნის ნახვა")
    print("3. წიგნის ძებნა")
    print("4. წიგნის წაშლა")
    print("5. გასვლა")
    print("==============================================")


def main():
    # მთავარი ფუნქცია — აქ იწყება პროგრამა
    # while True ნიშნავს, რომ მენიუ იძახება სანამ არ გავალთ
    while True:
        show_menu()
        choice = input("აირჩიე მოქმედება (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("ნახვამდის!")
            break  # break წყვეტს while ციკლს
        else:
            print("არასწორი არჩევანი! სცადე თავიდან.")


# ეს სტანდარტული ხაზია პითონში:
# პროგრამა გაეშვება მხოლოდ მაშინ, როცა ამ ფაილს პირდაპირ ვუშვებთ
if __name__ == "__main__":
    main()
