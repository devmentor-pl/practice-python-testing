> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e04-python-testing` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` Python: Testowanie

Twoim zadaniem jest przetestowanie funkcji `validate_user(data)`, która sprawdza poprawność danych użytkownika. Do testów użyjesz mechanizmu `pytest.fixture`, który pozwala w prosty sposób przygotować i wielokrotnie używać przykładowych danych.


## Opis funkcji

Funkcja `validate_user(data)` otrzymuje słownik z danymi użytkownika i sprawdza, czy:

- pole `"email"`:
  - zawiera znak `@`,
  - kończy się na `.pl` lub `.com`,
- pole `"age"`:
  - jest liczbą całkowitą,
  - jest większe lub równe 18,
- pole `"name"`:
  - składa się wyłącznie z liter (bez cyfr i znaków specjalnych).

Jeśli wszystkie warunki są spełnione, funkcja zwraca `True`. W przeciwnym razie – `False`.

## Co masz zrobić?

1. Zaimplementuj funkcję `validate_user(data)` w pliku `user.py`.
2. W pliku `test_user.py`:
   - przygotuj fixture z poprawnymi danymi użytkownika,
   - napisz test pozytywny dla danych z fixture,
   - stwórz osobne testy negatywne, modyfikując fixture (np. zły e-mail, wiek poniżej 18, imię z cyframi itp.).

## Wymagania

- Fixture powinna zwracać słownik zawierający dane: `name`, `email`, `age`.
- Nie używaj parametryzacji – wystarczy kilka oddzielnych funkcji testowych.
- Skup się na czytelności i pokryciu typowych błędów użytkownika.


&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-testing)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:
