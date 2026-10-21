markdown
# 🛒 Supermarket Sales Dashboard

An interactive dashboard built with **Streamlit** to explore supermarket sales data.
Users can filter the data from the sidebar, and all KPIs, charts and tables update instantly.

🔗 **Live app:** [Open the dashboard](https://appstoreseptember-fpxgxc7fgekcwn5sjxd45y.streamlit.app/)

---

## 📊 Features

**Sidebar filters**
- City
- Gender
- Minimum customer rating
- Payment method (multi-select)

**KPIs**
- Total sales (€)
- Average rating
- Total transactions
- Average transaction value (€)
- Top product line (by number of transactions)

**Visuals and tables**
- Optional view of the full filtered dataset
- Line chart of daily sales over time
- Table of the top 5 transactions by total value

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – web app and interactive widgets
- **pandas** – data loading, filtering and aggregation
- **matplotlib** – sales-over-time chart

---

## 📁 Project Structure

```
app_store_september/
├── app.py              # Streamlit dashboard code
├── requirements.txt    # Python libraries needed to run the app
└── README.md           # Project description
```

---

## ▶️ Run Locally

1. Clone the repository:
```bash
   git clone https://github.com/pari14830/app_store_september.git
   cd app_store_september
```

2. Install the requirements:
```bash
   pip install -r requirements.txt
```

3. Start the app:
```bash
   streamlit run app.py
```

---

## 📂 Data

The app uses the **Supermarket Sales** dataset (1,000 transactions from 3 cities: Yangon, Naypyitaw and Mandalay).
The data is loaded directly from the Ironhack Data Bootcamp repository, so no local CSV file is needed.

---

## 💡 What I Practiced

- Building interactive filters with Streamlit widgets (`selectbox`, `radio`, `slider`, `multiselect`)
- Filtering a DataFrame step by step with boolean conditions and `.isin()`
- Calculating KPIs with pandas (`sum`, `mean`, `nunique`, `value_counts`)
- Grouping time-series data with `groupby` and plotting it with matplotlib
- Caching data with `@st.cache_data` for faster loading
- Deploying an app from GitHub to Streamlit Community Cloud

---

## 👩‍💻 Author

**Pariya Lakani**
GitHub: [@pari14830](https://github.com/pari14830)
