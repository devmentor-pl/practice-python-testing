> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e04-python-testing` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#02` Python: Testowanie

Twoim zadaniem jest stworzenie funkcji `is_valid_promo(code)`, która sprawdza poprawność kodu promocyjnego. Następnie napiszesz testy z użyciem `pytest` i mechanizmu parametryzacji, aby sprawdzić funkcję dla wielu różnych przypadków.


## Wymagania funkcji

Funkcja `is_valid_promo(code)` powinna zwracać `True` tylko wtedy, gdy:

- `code` to string,
- długość kodu wynosi dokładnie 10 znaków,
- kod zawiera wyłącznie **duże litery (A-Z)** i **cyfry (0–9)**,
- kod zawiera **przynajmniej dwie cyfry**.

W przeciwnym wypadku funkcja powinna zwracać `False`.

## Co masz zrobić?

1. Zaimplementuj funkcję `is_valid_promo(code)` w pliku `promo.py`.
2. W pliku `test_promo.py` napisz testy z użyciem `pytest.mark.parametrize`, które sprawdzają poprawność różnych kodów.
3. Uwzględnij zarówno testy pozytywne (poprawne kody), jak i negatywne (błędne formaty).

## Przykładowe przypadki testowe

- Kod poprawny: `"ABC123XY90"`
- Za krótki kod: `"AB123"`
- Małe litery: `"abc123defg"`
- Brak cyfr: `"ABCDEFGHIJ"`
- Nie-string (np. liczba): `1234567890`
- Znaki specjalne: `"ABC!@#123$"`


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-testing)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
