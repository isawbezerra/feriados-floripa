from datetime import date, timedelta
from dateutil.easter import easter

START_YEAR = date.today().year
YEARS_AHEAD = 3

def event(uid, dtstart, dtend, summary, description=""):
    return f"""BEGIN:VEVENT
UID:{uid}-{dtstart}
DTSTAMP:{date.today().strftime('%Y%m%d')}T000000Z
DTSTART;VALUE=DATE:{dtstart}
DTEND;VALUE=DATE:{dtend}
SUMMARY:{summary}
DESCRIPTION:{description}
END:VEVENT
"""

events = []

for YEAR in range(START_YEAR, START_YEAR + YEARS_AHEAD):

    # =========================
    # FIXED NATIONAL HOLIDAYS
    # =========================

    events += [
        event(f"newyear-{YEAR}", date(YEAR,1,1), date(YEAR,1,2),
            "[BR] 🔴 Confraternização Universal","New Year’s Day."),

        event(f"tiradentes-{YEAR}", date(YEAR,4,21), date(YEAR,4,22),
            "[BR] 🔴 Tiradentes","Honors Brazil’s independence movement."),

        event(f"trabalho-{YEAR}", date(YEAR,5,1), date(YEAR,5,2),
            "[BR] 🔴 Dia do Trabalho","Labor Day."),

        event(f"independencia-{YEAR}", date(YEAR,9,7), date(YEAR,9,8),
            "[BR] 🔴 Independência do Brasil","National independence day."),

        event(f"aparecida-{YEAR}", date(YEAR,10,12), date(YEAR,10,13),
            "[BR] 🔴 Nossa Senhora Aparecida","Religious holiday."),

        event(f"finados-{YEAR}", date(YEAR,11,2), date(YEAR,11,3),
            "[BR] 🔴 Finados","Day to honor the deceased."),

        event(f"republica-{YEAR}", date(YEAR,11,15), date(YEAR,11,16),
            "[BR] 🔴 Proclamação da República","Republic proclamation."),

        event(f"consciencia-{YEAR}", date(YEAR,11,20), date(YEAR,11,21),
            "[BR] 🔴 Dia da Consciência Negra","Afro-Brazilian culture."),

        event(f"natal-{YEAR}", date(YEAR,12,25), date(YEAR,12,26),
            "[BR] 🔴 Natal","Christmas Day."),

        event(f"vnat-{YEAR}", date(YEAR,12,24), date(YEAR,12,25),
            "[BR] 🟡 Véspera de Natal","Partial working day."),

        event(f"vano-{YEAR}", date(YEAR,12,31), date(YEAR+1,1,1),
            "[BR] 🟡 Véspera de Ano Novo","New Year’s Eve.")
    ]

    # =========================
    # FLORIANÓPOLIS
    # =========================

    events.append(
        event(f"fln-{YEAR}", date(YEAR,3,23), date(YEAR,3,24),
        "[FLN] 🔴 Aniversário de Florianópolis","City anniversary.")
    )

    # =========================
    # CULTURAL DAYS
    # =========================

    events += [
        event(f"diamulher-{YEAR}", date(YEAR,3,8), date(YEAR,3,9),
            "[BR] 🔵 Dia da Mulher","International Women’s Day."),

        event(f"namorados-{YEAR}", date(YEAR,6,12), date(YEAR,6,13),
            "[BR] 🔵 Dia dos Namorados","Brazilian Valentine’s Day."),

        event(f"lgbt-{YEAR}", date(YEAR,6,28), date(YEAR,6,29),
            "[BR] 🔵 Dia do Orgulho LGBTQIA+","Pride events."),

        event(f"pais-{YEAR}", date(YEAR,8,9), date(YEAR,8,10),
            "[BR] 🔵 Dia dos Pais","Father’s Day."),

        event(f"criancas-{YEAR}", date(YEAR,10,12), date(YEAR,10,13),
            "[BR] 🔵 Dia das Crianças","Children’s Day."),

        event(f"blackfriday-{YEAR}", date(YEAR,11,27), date(YEAR,11,28),
            "[BR] 🔵 Black Friday","Retail event.")
    ]

    # =========================
    # EASTER SYSTEM
    # =========================

    easter_sunday = easter(YEAR)

    good_friday = easter_sunday - timedelta(days=2)
    carnaval_mon = easter_sunday - timedelta(days=47)
    carnaval_tue = easter_sunday - timedelta(days=46)
    corpus = easter_sunday + timedelta(days=60)

    events += [
        event(f"carnaval-mon-{YEAR}", carnaval_mon, carnaval_mon + timedelta(days=1),
            "[BR] 🔴 Carnaval (Segunda)","Carnival Monday."),

        event(f"carnaval-tue-{YEAR}", carnaval_tue, carnaval_tue + timedelta(days=1),
            "[BR] 🔴 Carnaval (Terça)","Carnival Tuesday."),

        event(f"goodfriday-{YEAR}", good_friday, good_friday + timedelta(days=1),
            "[BR] 🔴 Paixão de Cristo","Good Friday."),

        event(f"easter-{YEAR}", easter_sunday, easter_sunday + timedelta(days=1),
            "[BR] 🔴 Domingo de Páscoa","Easter Sunday."),

        event(f"corpus-{YEAR}", corpus, corpus + timedelta(days=1),
            "[BR] 🔴 Corpus Christi","Religious observance.")
    ]

    # =========================
    # SPECIAL EVENTS
    # =========================

    events += [
        event(f"copa-{YEAR}", date(YEAR,6,11), date(YEAR,7,20),
            "[BR] 🔵 Copa do Mundo","World Cup period."),

        event(f"eleicoes1-{YEAR}", date(YEAR,10,4), date(YEAR,10,5),
            "[BR] 🔴 Eleições — 1º Turno","Voting day."),

        event(f"eleicoes2-{YEAR}", date(YEAR,10,25), date(YEAR,10,26),
            "[BR] 🔴 Eleições — 2º Turno","Runoff if needed."),

        event(f"festa-junina-{YEAR}", date(YEAR,6,1), date(YEAR,7,1),
            "[BR] 🔵 Festa Junina Season","Cultural month.")
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
"X-WR-TIMEZONE:America/Sao_Paulo"
]

for e in events:
    ics.append(e)

ics.append("END:VCALENDAR")

with open("feriados_FLN.ics", "w", encoding="utf-8") as f:
    f.write("\n".join(ics))

print("ICS generated:", len(events))
