# Kalendarz urlopów 2026 — nowoczesny widok HTML

Aplikacja działa w przeglądarce i pokazuje **miesięczny widok kalendarza**, gdzie od razu widać:
- święta kraju (PL / ES / PT / ID),
- niestandardowe dni wolne,
- urlopy użytkowników (kto i kiedy).

## Uruchomienie

### 1) Najprościej
Otwórz `index.html` bezpośrednio w przeglądarce.

### 2) Lokalny serwer (polecane)
```bash
python3 -m http.server 8000
```
Następnie otwórz:
- `http://localhost:8000`

## Funkcje
- Dodawanie użytkowników.
- Dodawanie urlopów z zakresem dat.
- Dodawanie własnych dni wolnych.
- Przełączanie miesiąca (styczeń–grudzień 2026).
- Zmiana kraju świąt.

## Gdzie zapisują się dane?
Dane trzymane są w `localStorage` przeglądarki (lokalnie na Twoim komputerze).
