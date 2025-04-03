> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e04-python-testing` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Python: Testowanie

Twoim zadaniem jest zaimplementowanie klasy `Cart`, która pozwala dodawać i usuwać produkty oraz obliczać łączną cenę koszyka. Następnie napiszesz testy sprawdzające poprawność działania tej klasy.


## Zachowanie klasy Cart

Klasa `Cart` powinna działać zgodnie z poniższymi zasadami:

- Przechowuje listę produktów w postaci słowników np. `{"name": "apple", "price": 3.5}`
- Metody:
  - `add(product)` – dodaje produkt do koszyka,
  - `remove(product_name)` – usuwa pierwszy produkt o podanej nazwie,
  - `total()` – zwraca łączną cenę wszystkich produktów jako `float`,
  - `items()` – zwraca listę aktualnych produktów w koszyku.

## Co masz zrobić?

1. Zaimplementuj klasę `Cart` w pliku `cart.py`.
2. W pliku `test_cart.py` napisz testy jednostkowe:
   - dodawanie produktu,
   - usuwanie produktu,
   - obliczanie sumy,
   - zachowanie się przy pustym koszyku,
   - próba usunięcia nieistniejącego produktu (powinna nie robić nic).

## Wymagania

- Przetestuj każdy przypadek w osobnej funkcji testowej.
- Możesz użyć `pytest` lub `unittest`.
- Nie używaj zaawansowanego mockowania – testuj tylko logikę klasy.


## Wskazówki

- Do obliczania sumy użyj np. `sum(p["price"] for p in self._products)`.
- Usuwając produkt, sprawdź jego `name` – nie musisz sprawdzać całego słownika.
- Metoda `items()` może zwracać kopię listy lub oryginał – ważne, by testy nie zmieniały jej bezpośrednio.

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-testing)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
