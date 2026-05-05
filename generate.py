"""
Gerador de Calendário ICS - Feriados de Florianópolis e Brasil
Generates an ICS calendar file with Brazilian national holidays and Florianópolis-specific dates.
"""

from datetime import date, timedelta
from dateutil.easter import easter

# Configuration
START_YEAR = date.today().year
YEARS_AHEAD = 3
OUTPUT_FILE = "feriados_FLN.ics"

# Emoji indicators
EMOJI = {
    'holiday': '🔴',  # Official holidays
    'partial': '🟡',  # Partial working days
    'cultural': '🔵',  # Cultural/commemorative dates
}


def event(uid: str, dtstart: date, dtend: date, summary: str, description: str = "") -> str:
    """
    Generate a single VEVENT component for ICS calendar.
    
    Args:
        uid: Unique identifier for the event
        dtstart: Event start date
        dtend: Event end date (exclusive - next day)
        summary: Event title/summary
        description: Optional event description
    
    Returns:
        Formatted VEVENT string
    """
    return f"""BEGIN:VEVENT
UID:{uid}-{dtstart.strftime('%Y%m%d')}@feriados-floripa
DTSTAMP:{date.today().strftime('%Y%m%d')}T000000Z
DTSTART;VALUE=DATE:{dtstart.strftime('%Y%m%d')}
DTEND;VALUE=DATE:{dtend.strftime('%Y%m%d')}
SUMMARY:{summary}
DESCRIPTION:{description}
STATUS:CONFIRMED
TRANSP:TRANSPARENT
END:VEVENT
"""


def next_day(d: date) -> date:
    """Helper to get next day."""
    return d + timedelta(days=1)


def get_mothers_day(year: int) -> date:
    """Calculate Mother's Day (2nd Sunday of May)."""
    may_first = date(year, 5, 1)
    # Find first Sunday
    days_until_sunday = (6 - may_first.weekday()) % 7
    first_sunday = may_first + timedelta(days=days_until_sunday)
    # Second Sunday
    return first_sunday + timedelta(days=7)


def get_fathers_day(year: int) -> date:
    """Calculate Father's Day (2nd Sunday of August)."""
    aug_first = date(year, 8, 1)
    # Find first Sunday
    days_until_sunday = (6 - aug_first.weekday()) % 7
    first_sunday = aug_first + timedelta(days=days_until_sunday)
    # Second Sunday
    return first_sunday + timedelta(days=7)


def is_election_year(year: int) -> bool:
    """
    Check if year has elections in Brazil.
    Presidential/Congressional: every 4 years (2022, 2026, 2030...)
    State/Municipal: every 4 years, offset by 2 (2024, 2028, 2032...)
    """
    return year % 2 == 0


def is_world_cup_year(year: int) -> bool:
    """
    Check if year has FIFA World Cup.
    Occurs every 4 years: 2022, 2026, 2030, etc.
    """
    # FIFA World Cup years (simplified - actual dates vary)
    return (year - 2022) % 4 == 0


def generate_events():
    """Generate all calendar events."""
    events = []
    
    for year in range(START_YEAR, START_YEAR + YEARS_AHEAD):
        # =========================
        # FIXED NATIONAL HOLIDAYS
        # =========================
        events += [
            event(f"newyear-{year}", date(year, 1, 1), date(year, 1, 2),
                  f"[BR] {EMOJI['holiday']} Confraternização Universal", "New Year's Day."),
            
            event(f"tiradentes-{year}", date(year, 4, 21), date(year, 4, 22),
                  f"[BR] {EMOJI['holiday']} Tiradentes", "Honors Brazil's independence movement."),
            
            event(f"trabalho-{year}", date(year, 5, 1), date(year, 5, 2),
                  f"[BR] {EMOJI['holiday']} Dia do Trabalho", "Labor Day."),
            
            event(f"independencia-{year}", date(year, 9, 7), date(year, 9, 8),
                  f"[BR] {EMOJI['holiday']} Independência do Brasil", "National independence day."),
            
            event(f"aparecida-{year}", date(year, 10, 12), date(year, 10, 13),
                  f"[BR] {EMOJI['holiday']} Nossa Senhora Aparecida", "Religious holiday."),
            
            event(f"finados-{year}", date(year, 11, 2), date(year, 11, 3),
                  f"[BR] {EMOJI['holiday']} Finados", "Day to honor the deceased."),
            
            event(f"republica-{year}", date(year, 11, 15), date(year, 11, 16),
                  f"[BR] {EMOJI['holiday']} Proclamação da República", "Republic proclamation."),
            
            event(f"consciencia-{year}", date(year, 11, 20), date(year, 11, 21),
                  f"[BR] {EMOJI['holiday']} Dia da Consciência Negra", "Afro-Brazilian culture."),
            
            event(f"natal-{year}", date(year, 12, 25), date(year, 12, 26),
                  f"[BR] {EMOJI['holiday']} Natal", "Christmas Day."),
            
            event(f"vnat-{year}", date(year, 12, 24), date(year, 12, 25),
                  f"[BR] {EMOJI['partial']} Véspera de Natal", "Partial working day."),
            
            event(f"vano-{year}", date(year, 12, 31), next_day(date(year, 12, 31)),
                  f"[BR] {EMOJI['partial']} Véspera de Ano Novo", "New Year's Eve.")
        ]
        
        # =========================
        # FLORIANÓPOLIS
        # =========================
        events.append(
            event(f"fln-{year}", date(year, 3, 23), date(year, 3, 24),
                  f"[FLN] {EMOJI['holiday']} Aniversário de Florianópolis", "City anniversary.")
        )
        
        # =========================
        # CULTURAL DAYS
        # =========================
        mothers_day = get_mothers_day(year)
        fathers_day = get_fathers_day(year)
        
        events += [
            event(f"diamulher-{year}", date(year, 3, 8), date(year, 3, 9),
                  f"[BR] {EMOJI['cultural']} Dia da Mulher", "International Women's Day."),
            
            event(f"maes-{year}", mothers_day, next_day(mothers_day),
                  f"[BR] {EMOJI['cultural']} Dia das Mães", "Mother's Day."),
            
            event(f"namorados-{year}", date(year, 6, 12), date(year, 6, 13),
                  f"[BR] {EMOJI['cultural']} Dia dos Namorados", "Brazilian Valentine's Day."),
            
            event(f"lgbt-{year}", date(year, 6, 28), date(year, 6, 29),
                  f"[BR] {EMOJI['cultural']} Dia do Orgulho LGBTQIA+", "Pride events."),
            
            event(f"pais-{year}", fathers_day, next_day(fathers_day),
                  f"[BR] {EMOJI['cultural']} Dia dos Pais", "Father's Day."),
            
            event(f"criancas-{year}", date(year, 10, 12), date(year, 10, 13),
                  f"[BR] {EMOJI['cultural']} Dia das Crianças", "Children's Day."),
            
            event(f"blackfriday-{year}", date(year, 11, 27), date(year, 11, 28),
                  f"[BR] {EMOJI['cultural']} Black Friday", "Retail event."),
            
            event(f"festa-junina-{year}", date(year, 6, 1), date(year, 7, 1),
                  f"[BR] {EMOJI['cultural']} Festa Junina Season", "Cultural month.")
        ]
        
        # =========================
        # EASTER-BASED HOLIDAYS
        # =========================
        easter_sunday = easter(year)
        good_friday = easter_sunday - timedelta(days=2)
        carnival_monday = easter_sunday - timedelta(days=47)
        carnival_tuesday = easter_sunday - timedelta(days=46)
        ash_wednesday = easter_sunday - timedelta(days=45)
        corpus_christi = easter_sunday + timedelta(days=60)
        
        events += [
            event(f"carnaval-mon-{year}", carnival_monday, next_day(carnival_monday),
                  f"[BR] {EMOJI['holiday']} Carnaval (Segunda)", "Carnival Monday."),
            
            event(f"carnaval-tue-{year}", carnival_tuesday, next_day(carnival_tuesday),
                  f"[BR] {EMOJI['holiday']} Carnaval (Terça)", "Carnival Tuesday."),
            
            event(f"ash-wed-{year}", ash_wednesday, next_day(ash_wednesday),
                  f"[BR] {EMOJI['partial']} Quarta-feira de Cinzas", "Ash Wednesday (partial)."),
            
            event(f"goodfriday-{year}", good_friday, next_day(good_friday),
                  f"[BR] {EMOJI['holiday']} Paixão de Cristo", "Good Friday."),
            
            event(f"easter-{year}", easter_sunday, next_day(easter_sunday),
                  f"[BR] {EMOJI['cultural']} Domingo de Páscoa", "Easter Sunday."),
            
            event(f"corpus-{year}", corpus_christi, next_day(corpus_christi),
                  f"[BR] {EMOJI['holiday']} Corpus Christi", "Religious observance.")
        ]
        
        # =========================
        # CONDITIONAL EVENTS
        # =========================
        
        # Elections (only in election years)
        if is_election_year(year):
            events += [
                event(f"eleicoes1-{year}", date(year, 10, 6), date(year, 10, 7),
                      f"[BR] {EMOJI['holiday']} Eleições — 1º Turno", "Voting day."),
                
                event(f"eleicoes2-{year}", date(year, 10, 27), date(year, 10, 28),
                      f"[BR] {EMOJI['holiday']} Eleições — 2º Turno", "Runoff if needed.")
            ]
        
        # World Cup (only in World Cup years - note: dates are approximate)
        if is_world_cup_year(year):
            events.append(
                event(f"copa-{year}", date(year, 6, 11), date(year, 7, 20),
                      f"[BR] {EMOJI['cultural']} Copa do Mundo", "World Cup period (dates approximate).")
            )
    
    return events


def build_ics(events: list) -> str:
    """
    Build complete ICS calendar file content.
    
    Args:
        events: List of VEVENT strings
    
    Returns:
        Complete ICS file content
    """
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "CALSCALE:GREGORIAN",
        "PRODID:-//feriados.floripa//FLN//EN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Feriados FLN",
        "X-WR-TIMEZONE:America/Sao_Paulo",
        "X-WR-CALDESC:Feriados nacionais, estaduais e municipais de Florianópolis/SC"
    ]
    
    # Add VTIMEZONE component for better compatibility
    ics_lines.append("""BEGIN:VTIMEZONE
TZID:America/Sao_Paulo
BEGIN:STANDARD
DTSTART:19700101T000000
TZOFFSETFROM:-0300
TZOFFSETTO:-0300
TZNAME:BRT
END:STANDARD
END:VTIMEZONE""")
    
    for event_str in events:
        ics_lines.append(event_str.strip())
    
    ics_lines.append("END:VCALENDAR")
    
    return "\n".join(ics_lines)


def main():
    """Main execution function."""
    try:
        print(f"Generating calendar events from {START_YEAR} to {START_YEAR + YEARS_AHEAD - 1}...")
        events = generate_events()
        
        print(f"Generated {len(events)} events.")
        
        ics_content = build_ics(events)
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(ics_content)
        
        print(f"✅ ICS file successfully created: {OUTPUT_FILE}")
        print(f"📅 Total events: {len(events)}")
        
    except Exception as e:
        print(f"❌ Error generating calendar: {e}")
        raise


if __name__ == "__main__":
    main()
