# ZeroWaste Kitchen

A Streamlit web app for institutional kitchens: track and understand food waste, plan menus from near-expiry stock,
predict batch/event waste risk, and find safe, reachable partners for surplus food (with an interactive map).
Runs on your computer and opens in the browser.

## Run
    pip install -r requirements.txt
    streamlit run app.py          # opens http://localhost:8501
    pytest -q                     # 142 tests
    ZW_E2E=1 pytest tests/e2e -q  # 17 real-browser tests (needs: playwright install chromium)

## Pages
Dashboard - KPIs, trend, categories, pattern reality check, recent activity
Waste Log - filters, analytics, financial impact, honest pattern tests, entries (log new waste)
Forecast & Risk - expected waste per meal (backtested) and batch/event waste-risk predictor (what-if levers)
Menu Planner - stock with expiry status, optimizer-built menu, shopping list, cooking guide
Redistribution - what is left -> safe time -> ranked partners -> interactive map -> confirm and record
Partners - searchable directory with colour-coded map and details
Settings & Data - kitchen location (pick on the map), preferences, data sources and model cards

## Your data (in data/raw and data/source_partners.xlsx)
- Dataset Propely.csv: canteen waste log (new entries are appended to data/waste_log.csv; the original is never changed)
- food_wastage_data.csv: event waste records (duplicates removed) -> risk model
- bengaluru_food_redistribution_partners.xlsx -> data/partners.csv (python scripts/convert_partners.py)
Menu Planner uses reference recipes/prices (data/recipes.csv etc.): typical values, not kitchen data.

## Honest limits
- Waste per entry in the canteen log is statistically similar across meals/sections/categories/weekdays (no hotspot);
  expected waste is the plain average (best in backtest).
- Event risk model is accurate on its own dataset (CV error ~2 units vs 8.7 for guessing the average) but that data is event catering.
- Partner map positions are approximate area centres; most partners have not publicly confirmed surplus intake. Nothing is contacted.
- Safe-time windows, trip-time factors, 0.4 kg/meal and 2.5 kg CO2e/kg are assumptions in config.py.
- legacy/ holds the earlier synthetic demand forecaster (not used by the app).
