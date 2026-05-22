# Kalendarz dni wolnych 2026 (HTML)

To jest prosta aplikacja **HTML + JavaScript** (bez backendu), która:
- pokazuje dni wolne od pracy w 2026 r. dla: Hiszpanii (ES), Portugalii (PT), Indonezji (ID), Polski (PL),
- pozwala dodawać użytkowników,
- pozwala dodawać urlopy,
- pozwala dodawać własne dni wolne.

## Jak uruchomić

### Opcja 1 (najprościej)
1. Otwórz plik `index.html` w przeglądarce (dwuklik).

### Opcja 2 (lokalny serwer)
W folderze projektu uruchom:

```bash
python3 -m http.server 8000
```

Następnie wejdź w przeglądarce na:

- `http://localhost:8000`

## Gdzie zapisywane są dane?
Dane użytkowników/urlopów/dodatkowych dni wolnych zapisują się w `localStorage` przeglądarki.
