import secrets
#Генератор надежных паролей
class Password:
    length: int
    capital_letters_needed: bool
    need_numbers: bool
    special_characters_needed: bool
    LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    CAPITAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBER = "0123456789"
    SPECIAL_CHARACTERS = "!@#$%^&*"
    def __init__(self, capital_letters_needed=True, need_numbers=True, special_characters_needed=True, length=8):
        self.length = length
        self.capital_letters_needed = capital_letters_needed
        self.need_numbers = need_numbers
        self.special_characters_needed = special_characters_needed



    def asks(self):
        while True:
            length = input("Введите длину пароля: ")
            if length.isdigit():
                self.length = int(length)
                break
            else:
                print("Значение которые вы ввели это строка, а не целое число")
                
        self.capital_letters_needed = yes_no("Нужны ли залавные буквы: да/нет ")
        self.need_numbers = yes_no("Нужны ли цифры: да/нет ")
        self.special_characters_needed = yes_no("Нужны ли специальные символы: да/нет ")
        

    

    def create_password(self):
        result = ""
        i = self.length
        number = "1234"
        while i > 0:
            random_number = secrets.choice(number)
            if random_number == "1" and self.capital_letters_needed == True:
                result += secrets.choice(self.CAPITAL_LETTERS)
                i -= 1
            elif random_number == "2" and self.need_numbers == True:
                result += secrets.choice(self.NUMBER)
                i -= 1
            elif random_number == "3" and self.special_characters_needed == True:
                result += secrets.choice(self.SPECIAL_CHARACTERS)
                i -= 1
            elif random_number == "4":
                result += secrets.choice(self.LOWERCASE_LETTERS)
                i -= 1
            elif not self.special_characters_needed and not self.need_numbers and self.capital_letters_needed:
                result += secrets.choice(self.LOWERCASE_LETTERS)
                i -= 1
        return result

def yes_no(question):
    while True:
        answer = input(f"{question}").lower()
        if answer == "да":
            return True
        elif answer == "нет":
            return False
        else:
            print("Ошибка")

def main():
    password = Password()
    password.asks()
    result = password.create_password()
    print(result)
    print(len(result))
    

main()