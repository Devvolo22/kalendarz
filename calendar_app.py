from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Dict, List


SUPPORTED_COUNTRIES = {
    "ES": "Hiszpania",
    "PT": "Portugalia",
    "ID": "Indonezja",
    "PL": "Polska",
}


DEFAULT_HOLIDAYS_2026: Dict[str, Dict[str, str]] = {
    "PL": {
        "2026-01-01": "Nowy Rok",
        "2026-01-06": "Trzech Króli",
        "2026-04-05": "Wielkanoc",
        "2026-04-06": "Poniedziałek Wielkanocny",
        "2026-05-01": "Święto Pracy",
        "2026-05-03": "Święto Konstytucji 3 Maja",
        "2026-05-24": "Zielone Świątki",
        "2026-06-04": "Boże Ciało",
        "2026-08-15": "Wniebowzięcie NMP",
        "2026-11-01": "Wszystkich Świętych",
        "2026-11-11": "Narodowe Święto Niepodległości",
        "2026-12-25": "Boże Narodzenie (1. dzień)",
        "2026-12-26": "Boże Narodzenie (2. dzień)",
    },
    "ES": {
        "2026-01-01": "Año Nuevo",
        "2026-01-06": "Epifanía del Señor",
        "2026-04-03": "Viernes Santo",
        "2026-05-01": "Fiesta del Trabajo",
        "2026-08-15": "Asunción de la Virgen",
        "2026-10-12": "Fiesta Nacional de España",
        "2026-11-01": "Todos los Santos",
        "2026-12-06": "Día de la Constitución",
        "2026-12-08": "Inmaculada Concepción",
        "2026-12-25": "Navidad",
    },
    "PT": {
        "2026-01-01": "Ano Novo",
        "2026-04-03": "Sexta-feira Santa",
        "2026-04-05": "Páscoa",
        "2026-04-25": "Dia da Liberdade",
        "2026-05-01": "Dia do Trabalhador",
        "2026-06-10": "Dia de Portugal",
        "2026-06-11": "Corpo de Deus",
        "2026-08-15": "Assunção de Nossa Senhora",
        "2026-10-05": "Implantação da República",
        "2026-11-01": "Dia de Todos os Santos",
        "2026-12-01": "Restauração da Independência",
        "2026-12-08": "Imaculada Conceição",
        "2026-12-25": "Natal",
    },
    "ID": {
        "2026-01-01": "Tahun Baru Masehi",
        "2026-01-16": "Isra Mikraj",
        "2026-02-17": "Tahun Baru Imlek",
        "2026-03-19": "Hari Suci Nyepi",
        "2026-03-20": "Nyepi Cuti Bersama",
        "2026-04-03": "Wafat Yesus Kristus",
        "2026-05-14": "Kenaikan Yesus Kristus",
        "2026-05-27": "Hari Raya Waisak",
        "2026-05-28": "Waisak Cuti Bersama",
        "2026-06-01": "Hari Lahir Pancasila",
        "2026-07-17": "Tahun Baru Islam",
        "2026-08-17": "Hari Kemerdekaan",
        "2026-09-24": "Maulid Nabi Muhammad",
        "2026-12-25": "Hari Raya Natal",
    },
}


@dataclass
class User:
    user_id: int
    name: str


@dataclass
class Vacation:
    user_id: int
    start_date: str
    end_date: str
    reason: str = "urlop"


@dataclass
class CalendarStore:
    users: List[User] = field(default_factory=list)
    vacations: List[Vacation] = field(default_factory=list)
    custom_days_off: Dict[str, str] = field(default_factory=dict)


class HolidayCalendar:
    def __init__(self, db_path: str = "calendar_db.json") -> None:
        self.db_path = Path(db_path)
        self.store = self._load()

    def _load(self) -> CalendarStore:
        if not self.db_path.exists():
            return CalendarStore()
        raw = json.loads(self.db_path.read_text(encoding="utf-8"))
        return CalendarStore(
            users=[User(**u) for u in raw.get("users", [])],
            vacations=[Vacation(**v) for v in raw.get("vacations", [])],
            custom_days_off=raw.get("custom_days_off", {}),
        )

    def save(self) -> None:
        payload = {
            "users": [asdict(u) for u in self.store.users],
            "vacations": [asdict(v) for v in self.store.vacations],
            "custom_days_off": self.store.custom_days_off,
        }
        self.db_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def list_holidays(self, year: int = 2026, countries: List[str] | None = None) -> Dict[str, Dict[str, str]]:
        if year != 2026:
            return {}
        countries = countries or list(SUPPORTED_COUNTRIES.keys())
        return {code: DEFAULT_HOLIDAYS_2026[code] for code in countries if code in DEFAULT_HOLIDAYS_2026}

    def add_user(self, name: str) -> User:
        new_id = max((u.user_id for u in self.store.users), default=0) + 1
        user = User(user_id=new_id, name=name)
        self.store.users.append(user)
        self.save()
        return user

    def add_vacation(self, user_id: int, start_date: str, end_date: str, reason: str = "urlop") -> Vacation:
        self._validate_user(user_id)
        self._validate_date(start_date)
        self._validate_date(end_date)
        vacation = Vacation(user_id=user_id, start_date=start_date, end_date=end_date, reason=reason)
        self.store.vacations.append(vacation)
        self.save()
        return vacation

    def add_custom_day_off(self, day: str, name: str) -> None:
        self._validate_date(day)
        self.store.custom_days_off[day] = name
        self.save()

    def _validate_user(self, user_id: int) -> None:
        if not any(u.user_id == user_id for u in self.store.users):
            raise ValueError(f"Użytkownik {user_id} nie istnieje")

    @staticmethod
    def _validate_date(day: str) -> None:
        date.fromisoformat(day)


if __name__ == "__main__":
    app = HolidayCalendar()
    print("Święta 2026:")
    for country, days in app.list_holidays(2026, ["ES", "PT", "ID", "PL"]).items():
        print(f"\n{SUPPORTED_COUNTRIES[country]} ({country})")
        for day, name in sorted(days.items()):
            print(f"- {day}: {name}")
