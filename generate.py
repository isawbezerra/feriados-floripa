from datetime import date, timedelta
from dateutil.easter import easter

YEAR = date.today().year + 1

def event(uid, dtstart, dtend, summary, description=""):
    return f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{date.today().strftime('%Y%m%d')}T000000Z
DTSTART;VALUE=DATE:{dtstart}
DTEND;VALUE=DATE:{dtend}
SUMMARY:{summary}
DESCRIPTION:{description}
END:VEVENT
"""

events = []

# Base holidays
events.append(event(
    "newyear",
    date(YEAR, 1, 1),
    date(YEAR, 1, 2),
    "[BR] 🔴 Confraternização Universal",
    "New Year’s Day."
))

events.append(event(
    "tiradentes",
    date(YEAR, 4, 21),
    date(YEAR, 4, 22),
    "[BR] 🔴 Tiradentes",
    "Honors a key figure in Brasil’s independence movement."
))

events.append(event(
    "trabalho",
    date(YEAR, 5, 1),
    date(YEAR, 5, 2),
    "[BR] 🔴 Dia do Trabalho",
    "Labor Day."
))

# Easter system
easter_sunday = easter(YEAR)
good_friday = easter_sunday - timedelta(days=2)
carnival_mon = easter_sunday - timedelta(days=47)
carnival_tue = easter_sunday - timedelta(days=46)
corpus = easter_sunday + timedelta(days=60)

events.append(event("carnival-mon", carnival_mon, carnival_mon + timedelta(days=1),
    "[BR] 🔴 Carnaval (Segunda)", "Carnival Monday."))

events.append(event("carnival-tue", carnival_tue, carnival_tue + timedelta(days=1),
    "[BR] 🔴 Carnaval (Terça)", "Carnival Tuesday."))

events.append(event("goodfriday", good_friday, good_friday + timedelta(days=1),
    "[BR] 🔴 Paixão de Cristo", "Good Friday."))

events.append(event("easter", easter_sunday, easter_sunday + timedelta(days=1),
    "[BR] 🔴 Domingo de Páscoa", "Easter Sunday."))

events.append(event("corpus", corpus, corpus + timedelta(days=1),
    "[BR] 🔴 Corpus Christi", "Religious observance."))

# IMPORTANT: build FINAL string only once
ics = [
"BEGIN:VCALENDAR",
"VERSION:2.0",
"CALSCALE:GREGORIAN",
"PRODID:-//feriados.floripa//FLN//EN",
"METHOD:PUBLISH",
"X-WR-CALNAME:Feriados FLN",
"X-WR-TIMEZONE:America/Sao_Paulo",
]

for e in events:
    ics.append(e)

ics.append("END:VCALENDAR")

final_output = "\n".join(ics)

with open("feriados_FLN.ics", "w", encoding="utf-8") as f:
    f.write(final_output)

print("ICS generated with", len(events), "events")
