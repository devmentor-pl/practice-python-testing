> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e04-python-testing` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#01` Python: Testowanie

Twoim celem jest stworzenie walidatora danych zamówienia oraz testów, które sprawdzają jego poprawność i odporność na błędy.

## Wymagania

Funkcja `validate_order(order)` powinna:
- zaakceptować zamówienie, jeśli spełnia warunki (zwrócić true),
- rzucić wyjątek `ValueError` w przypadku:
  - błędnego typu `user_id`,
  - pustej listy `items`,
  - nieprawidłowego `delivery["method"]` (`"courier"`, `"pickup"`, `"drone"`),
  - pustego `delivery["address"]`.

Zamówienie to `słownik` o strukturze np.:
```json
{
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}
```

## Uruchomienie testów

```bash
python -m unittest test_orders.py
```

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-testing)*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:
