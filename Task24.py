text = input("Введите слово - полиндром : ")
# text_len = len(text)

def poli(text):
    if text[:].lower() == text[::-1].lower():
        return True
        # print("polindrom")
    else:
        return False
        # print("not a polindrom")

print(poli(text))