# 📅 Feriados Florianópolis - ICS Calendar Generator

Gerador automático de calendário ICS com feriados nacionais, estaduais e municipais de Florianópolis/SC.

## 🚀 Features

- ✅ Feriados nacionais brasileiros
- ✅ Datas municipais de Florianópolis
- ✅ Datas culturais e comemorativas
- ✅ Cálculo automático de feriados móveis (Carnaval, Páscoa, Corpus Christi)
- ✅ Geração automática via GitHub Actions
- ✅ Timezone correto (America/Sao_Paulo)

## 📖 How to Use

### Option 1: Subscribe to Calendar (Recommended)

Copy this URL and add to your calendar app:
```
https://raw.githubusercontent.com/isawbezerra/feriados_floripa/main/feriados_FLN.ics
```

**Instructions by app:**

- **Google Calendar**: Settings → Add Calendar → From URL → paste link
- **Apple Calendar**: File → New Calendar Subscription → paste link
- **Outlook**: Add Calendar → From Internet → paste link

### Option 2: Generate Locally

```bash
# Clone repository
git clone https://github.com/isawbezerra/feriados-floripa.git
cd feriados-floripa

# Install dependencies
pip install -r requirements.txt

# Generate calendar
python generate.py
```

## 🎨 Color Coding

The calendar uses emojis to indicate event types:

- 🔴 **Official Holidays** - Public holidays with no work
- 🟡 **Partial Days** - Partial working days (e.g., Christmas Eve)
- 🔵 **Cultural/Commemorative** - Cultural dates and celebrations

## 📝 What's Included

### National Holidays (🔴)
- New Year's Day
- Tiradentes Day
- Labor Day
- Independence Day
- Nossa Senhora Aparecida
- Finados (All Souls' Day)
- Republic Day
- Black Consciousness Day
- Christmas
- Carnival Monday & Tuesday
- Good Friday
- Corpus Christi

### Florianópolis (🔴)
- City Anniversary (March 23)

### Cultural Dates (🔵)
- International Women's Day
- Mother's Day (2nd Sunday of May)
- Father's Day (2nd Sunday of August)
- Valentine's Day (June 12)
- LGBT Pride Day
- Children's Day
- Black Friday
- Festa Junina Season

### Conditional Events
- **Elections** (🔴) - Only in election years (every 2 years)
- **World Cup** (🔵) - Only in World Cup years (every 4 years)

## 🔄 Automatic Updates

The calendar is automatically regenerated weekly via GitHub Actions, ensuring:
- Always up-to-date for the next 3 years
- Automatic calculation of movable holidays
- Fresh subscription without manual updates

## 🛠️ Development

### Improvements in Latest Version

**Fixes:**
- ✅ World Cup only appears in correct years (2022, 2026, 2030...)
- ✅ Elections only appear in election years
- ✅ Added Mother's Day (was missing)
- ✅ Proper calculation of Father's Day and Mother's Day (dynamic Sundays)
- ✅ Added Ash Wednesday (partial working day)
- ✅ Better error handling
- ✅ Added VTIMEZONE component for better calendar compatibility
- ✅ Improved code documentation

**Code Quality:**
- Type hints on functions
- Docstrings
- Error handling
- Constants for configuration
- Helper functions for date calculations
- Better code organization

### Project Structure

```
feriados-floripa/
├── generate.py              # Main script
├── requirements.txt         # Python dependencies
├── feriados_FLN.ics        # Generated ICS file
├── .github/
│   └── workflows/
│       └── generate.yml    # Auto-generation workflow
└── README.md               # This file
```

## 🤝 Contributing

Contributions are welcome! To add or fix holidays:

1. Fork the repository
2. Edit `generate.py`
3. Test locally: `python generate.py`
4. Submit a Pull Request

## 📄 License

MIT License - feel free to use and modify

## 🙋‍♀️ Author

Created by [@isawbezerra](https://github.com/isawbezerra)

---

**Note:** This calendar is maintained as a community resource. Holiday dates are based on Brazilian federal, state, and municipal legislation. Election and World Cup dates are approximate and subject to official confirmation.
