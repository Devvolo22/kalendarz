# Kalendarz urlopów 2026 — widok miesięczny + roczny

Aplikacja działa w przeglądarce i ma dwa tryby widoku:
- **Widok miesięczny** (szczegóły dnia + etykiety urlopów/świąt),
- **Widok roczny** (12 miesięcy naraz, z zaznaczonymi urlopami i świętami).

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
- Przełącznik: **widok miesięczny / roczny**.
- Urlopy są widoczne w obu widokach.
- Święta kraju (PL/ES/PT/ID) są widoczne w obu widokach.
- Niestandardowe dni wolne są widoczne w obu widokach.
- Dodawanie użytkowników, urlopów i dni wolnych.

## Styl UI
Interfejs jest utrzymany w nowoczesnym stylu enterprise (fioletowe akcenty, jasne panele, ikony, czytelna legenda).

## Gdzie zapisują się dane?
Dane trzymane są w `localStorage` przeglądarki (lokalnie na Twoim komputerze).
