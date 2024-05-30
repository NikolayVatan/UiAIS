import time


def guess_the_number():
    # Генерируем случайное число от 1 до 100
    number_to_guess = (time.time() * 1000) % 100 + 1
    attempts = 0
    guessed = False

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать его.")

    while not guessed:
        # Просим пользователя ввести число
        user_guess = input("Введите ваше предположение: ")

        # Проверяем, что введено число
        if user_guess.isdigit():
            user_guess = int(user_guess)
            attempts += 1

            if user_guess < number_to_guess:
                print("Слишком мало! Попробуйте еще раз.")
            elif user_guess > number_to_guess:
                print("Слишком много! Попробуйте еще раз.")
            else:
                guessed = True
                print("Поздравляю! Вы угадали число!")
        else:
            print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    guess_the_number()
