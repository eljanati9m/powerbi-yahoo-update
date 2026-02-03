# Yahoo Finance Analytics Dashboard

## Overview
**Yahoo Finance Analytics Dashboard** is an end-to-end data analytics project that automates financial data collection from **Yahoo Finance**, processes it using **Python**, and visualizes key insights through an interactive **Power BI dashboard** published online.

The project demonstrates skills in **data extraction, automation, data visualization, and business analytics**, and is designed for portfolio and professional use.

🔗 **Live Dashboard (Power BI – Publish to Web)**  
👉 https://app.powerbi.com/view?r=eyJrIjoiOTBjY2I1ODMtMzdhMy00N2MzLWJhMmQtM2QxYTRiYzlkMzU2IiwidCI6IjNmNGI5YjkyLTYwMjktNDlkNi05MzcxLTVhZDZlMDU0ODE0ZSJ9

---

##  Project Features
- Automated financial data extraction from **Yahoo Finance**
- Scheduled updates using **GitHub Actions**
- Clean and structured datasets for BI usage
- Interactive Power BI dashboard (web-published)
- Optimized visuals (dark & light mode assets)
- Portfolio-ready analytics project

---

## 🗂️ Repository Structure
```bash
.
├── .github/workflows/
│   └── update.yml                     # GitHub Actions workflow for automated updates
├── Dashboards/
│   └── Yahoo Finance Analytics.pbix   # Power BI dashboard file
├── 40_entreprises_5ans.csv            # Financial data (5-year period)
├── extract_yfinance.py                # Python script for Yahoo Finance data extraction
├── logos_dark_mode.xlsx               # Assets for dark theme visuals
├── logos_light_mode.xlsx              # Assets for light theme visuals
└── README.md                          # Project documentation
```
---

## Data Pipeline
1. **Data Extraction**  
   Financial data is retrieved programmatically from **Yahoo Finance** using Python.

2. **Automation**  
   A **GitHub Actions workflow** (`update.yml`) runs the extraction script automatically to keep datasets up to date.

3. **Data Storage**  
   Updated data is saved as structured CSV files, ready for analysis.

4. **Visualization**  
   Power BI connects to the dataset and refreshes visuals to reflect the latest data.

---

## Dashboard Insights
The Power BI dashboard provides insights such as:
- Stock price evolution over time
- Company performance comparison
- Market trends and variability
- Financial indicators for decision support

The dashboard is designed for **clarity, interactivity, and business storytelling**.

---


## Technologies Used
- **Python** (data extraction & automation)
- **yfinance** (Yahoo Finance data extraction library)
- **GitHub Actions**
- **Power BI**
- **CSV / Excel**
- **Git & GitHub**

---

## Use Cases
- Financial market analysis
- Business intelligence reporting
- Portfolio demonstration (Data Analyst / BI Analyst / Data Scientist)
- Educational & learning purposes

---

## Notes
- The Power BI dashboard is published using **Publish to Web**
- Interactive access is public and does not require authentication
- For full project details or collaboration opportunities, feel free to reach out
