import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE SETTINGS & TITLE
# ---------------------------------------------------
st.set_page_config(page_title="Supermarket Sales Dashboard", page_icon="🛒", layout="wide")

st.title("Supermarket Sales Dashboard")
st.write("This dashboard allows us to explore supermarket sales data using interactive Streamlit widgets.")

st.divider()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/supermarket_sales.csv"
    )
    df["Date"] = pd.to_datetime(df["Date"])
    return df


df = load_data()

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("Filters")

# City
selected_city = st.sidebar.selectbox(
    "Select a city",
    options=["All"] + list(df["City"].unique())
)

# Gender
selected_gender = st.sidebar.radio(
    "Select the gender",
    options=["All", "Male", "Female"]
)

# Rating
selected_rating = st.sidebar.slider(
    "Minimum rating",
    min_value=0,
    max_value=10,
    step=1
)

# Payment method
selected_payment = st.sidebar.multiselect(
    "Select payment method",
    options=df["Payment"].unique(),
    default=df["Payment"].unique()
)

# ---------------------------------------------------
# FILTER DATAFRAME
# ---------------------------------------------------
filtered_df = df.copy()

# City
if selected_city != "All":
    filtered_df = filtered_df[filtered_df["City"] == selected_city]

# Gender
if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["Gender"] == selected_gender]

# Rating
filtered_df = filtered_df[filtered_df["Rating"] >= selected_rating]

# Payment
if len(selected_payment) > 0:
    filtered_df = filtered_df[filtered_df["Payment"].isin(selected_payment)]

# Stop here if the filters leave no rows (avoids errors below)
if filtered_df.empty:
    st.warning("No data matches these filters. Please change the filters in the sidebar.")
    st.stop()

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
st.header("Summary statistics (KPIs)")

total_sales = filtered_df["Total"].sum()
average_rating = filtered_df["Rating"].mean()
total_transactions = filtered_df["Invoice ID"].nunique()
average_transaction = filtered_df["Total"].mean()
top_product_line = filtered_df["Product line"].value_counts().index[0]

# First row
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Sales", f"{total_sales:,.2f} €")
with col2:
    st.metric("Average Rating", f"{average_rating:.2f}")

# Second row
col3, col4 = st.columns(2)
with col3:
    st.metric("Total Transactions", f"{total_transactions:,}")
with col4:
    st.metric("Average Transaction", f"{average_transaction:,.2f} €")

# Third row
st.write("### Top Product Line")
st.success(top_product_line)

st.divider()

# ---------------------------------------------------
# DATAFRAME SECTION
# ---------------------------------------------------
show_data = st.checkbox("Show dataset")
if show_data:
    st.dataframe(filtered_df)

st.divider()

# ---------------------------------------------------
# SALES OVER TIME
# ---------------------------------------------------
st.header("Sales Over Time")

sales_over_time = filtered_df.groupby(filtered_df["Date"].dt.date)["Total"].sum()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(sales_over_time.index, sales_over_time.values)
ax.set_title("Sales Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Total Sales (€)")
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()

st.pyplot(fig)

st.divider()

# ---------------------------------------------------
# TOP 5 TRANSACTIONS
# ---------------------------------------------------
st.header("Top 5 Transactions")

top5 = (
    filtered_df.sort_values("Total", ascending=False)
    .head(5)
    .reset_index(drop=True)
)

st.table(top5[["Invoice ID", "City", "Product line", "Total", "Rating"]])

# ---------------------------------------------------
# FINAL MESSAGE
# ---------------------------------------------------
st.markdown(
    """
    <h2 style='color:#4CAF50;'>
        📈 Dashboard loaded successfully!
    </h2>
    """,
    unsafe_allow_html=True
)
