import random
import docx
mydoc = docx.Document()
c = 0

locale = "C:\\Users\\yourway\\MathChild.txt"


def lostfd():
    x = str(random.randint(1, 9))
    return x


def example_create():
    ex = lostfd() + "  *  " + lostfd() + " =            "
    return ex

def exam_stroke():
    prime = example_create() + example_create() + example_create() + example_create() + example_create() + example_create()
    return prime


with open(locale, "w") as file:
    while c != 26:
        p = mydoc.add_paragraph(exam_stroke())
        print(example_create() + example_create() + example_create())
        c =+ 1

mydoc.save("C:\\Users\\your_way\\MathChild.txt")

file.close()