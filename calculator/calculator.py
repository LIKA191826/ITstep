# tkinter - გრაფიკული ფანჯრის ბიბლიოთეკა
import tkinter as tk

# first_number - პირველი რიცხვი (ოპერატორის დაჭერისას ვინახავთ)
# operator - რომელი მოქმედება ავირჩიეთ (+, -, *, /)
# new_number - True თუ შემდეგი ციფრი ახალი რიცხვის დასაწყისია
first_number = ""
operator = ""
new_number = True


# ციფრის ან წერტილის დაჭერისას იძახება
def press_number(number):
    global new_number

    # თუ ახალი რიცხვი უნდა დაიწყოს, ეკრანი ჯერ გავასუფთავოთ
    if new_number:
        entry.delete(0, tk.END)
        new_number = False

    # ციფრი ეკრანის ბოლოში დაემატოს
    entry.insert(tk.END, number)


# ოპერატორის (+, -, *, /) დაჭერისას იძახება
def press_operator(op):
    global first_number, operator, new_number

    # ეკრანზე რაც წერია, პირველ რიცხვად შევინახოთ
    first_number = entry.get()
    # რომელი ოპერატორი ავირჩიეთ
    operator = op
    # შემდეგი ციფრი უკვე მეორე რიცხვი იქნება
    new_number = True


# ტოლობის (=) დაჭერისას იძახება და ითვლის პასუხს
def calculate():
    global first_number, operator, new_number

    # ეკრანზე ახლა მეორე რიცხვი წერია
    second_number = entry.get()

    # თუ რამე აკლია, გამოთვლა არ გავაკეთოთ
    if first_number == "" or operator == "" or second_number == "":
        return

    # ტექსტი რიცხვებად გადავიყვანოთ
    num1 = float(first_number)
    num2 = float(second_number)

    # ოპერატორის მიხედვით ვითვლით
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # ნულზე გაყოფა არ შეიძლება
        if num2 == 0:
            entry.delete(0, tk.END)
            entry.insert(0, "შეცდომა")
            new_number = True
            return
        result = num1 / num2

    # თუ პასუხი მთელია (მაგ: 5.0), წერტილი აღარ გამოჩნდეს
    if result == int(result):
        result = int(result)

    # პასუხი ეკრანზე გამოვაჩინოთ
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

    # შემდეგი გამოთვლისათვის ცვლადები გავასუფთავოთ
    first_number = ""
    operator = ""
    new_number = True


# C ღილაკი - ყველაფერს ასუფთავებს
def clear():
    global first_number, operator, new_number

    entry.delete(0, tk.END)
    first_number = ""
    operator = ""
    new_number = True


# ---------- ფანჯარა ----------

# მთავარი ფანჯრის შექმნა
window = tk.Tk()
# ფანჯრის სათაური
window.title("კალკულატორი")
# ფანჯრის ზომა (სიგანე x სიმაღლე)
window.geometry("280x380")
# ზომის შეცვლა გამორთულია
window.resizable(False, False)

# ზედა მარცხენა კუთხის ნიშანი - სამი ხაზი
icon = tk.PhotoImage(width=16, height=16)
icon.put("#333333", to=(3, 3, 13, 5))
icon.put("#333333", to=(3, 7, 13, 9))
icon.put("#333333", to=(3, 11, 13, 13))
window.iconphoto(False, icon)

# ეკრანი, სადაც რიცხვები ჩანს
# justify="right" - ტექსტი მარჯვნივ იწერება
entry = tk.Entry(window, font=("Arial", 18), justify="right", bd=4)
# columnspan=4 - ოთხივე სვეტზე გადაჭიმულია
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

# ღილაკების სია: (ტექსტი, რიგი, სვეტი)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# თითოეული ღილაკის შექმნა
for text, row, col in buttons:
    # თუ ციფრია ან წერტილი - press_number გამოიძახოს
    if text.isdigit() or text == ".":
        btn = tk.Button(window, text=text, font=("Arial", 14),
                        command=lambda t=text: press_number(t))
    # თუ ტოლობაა - calculate გამოიძახოს
    elif text == "=":
        btn = tk.Button(window, text=text, font=("Arial", 14), command=calculate)
    # თუ ოპერატორია - press_operator გამოიძახოს
    else:
        btn = tk.Button(window, text=text, font=("Arial", 14),
                        command=lambda t=text: press_operator(t))

    # ღილაკი ცხრილში ჩავსვათ
    # sticky="nsew" - ღილაკი უჯრას მთლიანად ავსებს
    btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

# C ღილაკი - ქვემოთ, ყველა სვეტზე გადაჭიმული
clear_btn = tk.Button(window, text="C", font=("Arial", 14), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=4, pady=4, sticky="nsew")

# რიგები და სვეტები თანაბრად გაიჭიმოს
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# ფანჯარა გაიხსნას და პროგრამა იმუშაოს
window.mainloop()
