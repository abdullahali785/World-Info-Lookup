# 🌍 World Info Lookup

A Python tool that retrieves detailed information about any country using data from multiple CSV datasets. It combines geography, demographics, government, and regional classification to return a human-readable summary of the selected country.

---

## 🚀 Features

- 🔎 Query by country name (e.g., "Pakistan")
- 📄 Parses and combines data from multiple CSV files:
  - Official state name
  - Form of government
  - Geographical region
  - Total land area
  - Population
- 🧠 Outputs a clean, formatted summary sentence

---

## 📦 File Structure

- `main.py` — Python script containing `gather_info()`  
- `world_codes.csv` — Contains countries and their official names  
- `world_gov.csv` — Contains constitutional forms of government  
- `world_regions.csv` — Contains regional groupings  
- `world_geo.csv` — Contains land area data  
- `world_demo.csv` — Contains population data  

---

## 📥 Example

```python
print(gather_info("Pakistan"))

Pakistan (Islamic Republic of Pakistan) is a(n) Federal republic form of government in Asia with an area of 881912 square kilometers and 240485658 number of people.
