> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e04-python-testing` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Python: Testowanie

W tym zadaniu stworzysz funkcję, która wywołuje zewnętrzną usługę płatniczą, a następnie przetestujesz ją przy pomocy obiektu `Mock`. Dzięki temu sprawdzisz logikę działania kodu bez potrzeby faktycznego łączenia się z systemem płatności.


## Opis funkcji

Funkcja `send_payment(payment_data, gateway)`:

- otrzymuje dane płatności jako słownik (np. `{"amount": 100, "currency": "PLN"}`),
- otrzymuje obiekt `gateway`, który posiada metodę `.pay(data)`,
- wywołuje metodę `.pay()` na obiekcie `gateway`,
- zwraca `True`, jeśli płatność się powiodła (`pay()` zwraca `True`),
- zwraca `False`, jeśli płatność się nie powiodła (`pay()` zwraca `False`),
- jeśli podczas płatności zostanie rzucony wyjątek – funkcja również zwraca `False`.

## Co masz zrobić?

1. Zaimplementuj funkcję `send_payment()` w pliku `payment.py`.
2. W pliku `test_payment.py` użyj obiektu `Mock` z `unittest.mock`, aby zasymulować bramkę płatniczą (`gateway`).
3. Napisz testy, które sprawdzają:
   - poprawną płatność (mock zwraca `True`),
   - odrzuconą płatność (`False`),
   - wyjątek zgłoszony przez `pay()`.

## Wymagania

- Nie używaj dekoratorów `@patch` ani `with mock.patch()`.
- Twórz mocka ręcznie (`gateway = Mock()`), ustaw jego zachowanie i przekaż jako argument do funkcji.
- W testach użyj `assert` lub `unittest` – możesz wybrać jedną z tych opcji.


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-testing)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
