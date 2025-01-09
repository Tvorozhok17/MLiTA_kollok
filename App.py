from Parser import *
from Prover import *
from time import time


class App:
    def __init__(self):
        self.axioms = []  # Список для хранения аксиом
        self.keywords = ['exit', 'help', 'axioms', 'axiom', 'prove', 'del']

    def run(self):
        expression_str = "A>(B>A)"
        parser = Parser(expression_str, self.keywords)
        expression = parser.parse()
        self.axioms.append(expression)

        expression_str = "((A>(B>C))>((A>B)>(A>C)))"
        parser = Parser(expression_str, self.keywords)
        expression = parser.parse()
        self.axioms.append(expression)

        expression_str = "((!B>!A)>((!B>A)>B))"
        parser = Parser(expression_str, self.keywords)
        expression = parser.parse()
        self.axioms.append(expression)

        print("Введите выражение для его разбора")

        while True:
            user_input = input("> ").strip()

            try:
                # Разделение команды и выражения
                parts = user_input

                if user_input == "quit":
                    break

                if len(parts) > 1:
                    expression_str = parts
                    parser = Parser(expression_str, self.keywords)
                    expression = parser.parse()
                    start_time = time()
                    prover = Prover(self.axioms, expression)
                    result = prover.prove()
                    end_time = time()
                    if result:
                        print(f"Выражение {expression} доказано")
                        print(f"Время разбора: {end_time - start_time} секунд")
                        print()
                        continue
                    else:
                        print(f"Выражение не доказуемо :(")
                        print()
                        continue

                else:
                    print("Некорректный формат ввода")

            except ValueError as e:
                print(f"Ошибка разбора выражения: {e}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

            print()
