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

# =========================
# FIXED NATIONAL HOLIDAYS
# =========================

events += [
    event("newyear", date(YEAR,1,1), date(YEAR,1,2),
        "[BR] 🔴 Confraternização Universal","New Year’s Day."),

    event("tiradentes", date(YEAR,4,21), date(YEAR,4,22),
        "[BR] 🔴 Tiradentes","Honors Brazil’s independence movement."),

    event("trabalho", date(YEAR,5,1), date(YEAR,5,2),
        "[BR] 🔴 Dia do Trabalho","Labor Day."),

    event("independencia", date(YEAR,9,7), date(YEAR,9,8),
        "[BR] 🔴 Independência do Brasil","National independence day."),

    event("aparecida", date(YEAR,10,12), date(YEAR,10,13),
        "[BR] 🔴 Nossa Senhora Aparecida","Religious holiday."),

    event("finados", date(YEAR,11,2), date(YEAR,11,3),
        "[BR] 🔴 Finados","Day to honor the deceased."),

    event("republica", date(YEAR,11,15), date(YEAR,11,16),
        "[BR] 🔴 Proclamação da República","Republic proclamation."),

    event("consciencia", date(YEAR,11,20), date(YEAR,11,21),
        "[BR] 🔴 Dia da Consciência Negra","Afro-Brazilian culture."),
    
    event("natal", date(YEAR,12,25), date(YEAR,12,26),
        "[BR] 🔴 Natal","Christmas Day."),

    event("vnat", date(YEAR,12,24), date(YEAR,12,25),
        "[BR] 🟡 Véspera de Natal","Partial working day."),

    event("vano", date(YEAR,12,31), date(YEAR,2026,1,1),
        "[BR] 🟡 Véspera de Ano Novo","Year end."),
]

# =========================
# FLORIANÓPOLIS
# =========================

events.append(
    event("fln", date(YEAR,3,23), date(YEAR,3,24),
    "[FLN] 🔴 Aniversário de Florianópolis","City anniversary.")
)

# =========================
# CULTURAL DAYS
# =========================

events += [
    event("diamulher", date(YEAR,3,8), date(YEAR,3,9),
        "[BR] 🔵 Dia da Mulher","International Women’s Day."),

    event("namorados", date(YEAR,6,12), date(YEAR,6,13),
        "[BR] 🔵 Dia dos Namorados","Brazilian Valentine’s Day."),

    event("lgbt", date(YEAR,6,28), date(YEAR,6,29),
        "[BR] 🔵 Dia do Orgulho LGBTQIA+","Pride events."),

    event("pais", date(YEAR,8,9), date(YEAR,8,10),
        "[BR] 🔵 Dia dos Pais","Father’s Day."),

    event("criancas", date(YEAR,10,12), date(YEAR,10,13),
        "[BR] 🔵 Dia das Crianças","Children’s Day."),

    event("blackfriday", date(YEAR,11,27), date(YEAR,11,28),
        "[BR] 🔵 Black Friday","Retail event."),
]

# =========================
# EASTER SYSTEM (DYNAMIC)
# =========================

easter_sunday = easter(YEAR)

good_friday = easter_sunday - timedelta(days=2)
carnaval_mon = easter_sunday - timedelta(days=47)
carnaval_tue = easter_sunday - timedelta(days=46)
corpus = easter_sunday + timedelta(days=60)

events += [
    event("carnaval-mon", carnaval_mon, carnaval_mon + timedelta(days=1),
        "[BR] 🔴 Carnaval (Segunda)","Carnival Monday."),

    event("carnaval-tue", carnaval_tue, carnaval_tue + timedelta(days=1),
        "[BR] 🔴 Carnaval (Terça)","Carnival Tuesday."),

    event("goodfriday", good_friday, good_friday + timedelta(days=1),
        "[BR] 🔴 Paixão de Cristo","Good Friday."),

    event("easter", easter_sunday, easter_sunday + timedelta(days=1),
        "[BR] 🔴 Domingo de Páscoa","Easter Sunday."),

    event("corpus", corpus, corpus + timedelta(days=1),
        "[BR] 🔴 Corpus Christi","Religious observance."),
]

# =========================
# SPECIAL EVENTS
# =========================

events += [
    event("copa", date(YEAR,6,11), date(YEAR,7,20),
        "[BR] 🔵 Copa do Mundo","World Cup period."),

    event("eleicoes1", date(YEAR,10,4), date(YEAR,10,5),
        "[BR] 🔴 Eleições — 1º Turno","Voting day."),

    event("eleicoes2", date(YEAR,10,25), date(YEAR,10,26),
        "[BR] 🔴 Eleições — 2º Turno","Runoff if needed."),

    event("festa-junina", date(YEAR,6,1), date(YEAR,7,1),
        "[BR] 🔵 Festa Junina Season","Cultural month."),
]

# =========================
# BUILD ICS FILE
# =========================

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

with open("feriados_FLN.ics", "w", encoding="utf-8") as f:
    f.write("\n".join(ics))

print("ICS generated:", len(events))
