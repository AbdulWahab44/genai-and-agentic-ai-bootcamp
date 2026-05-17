import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="1. Pandas: Core objects, indexing, and alignment", layout="wide")

@st.cache_data
def load_sample_data(rows: int = 200) -> pd.DataFrame:
    """Create a reproducible mixed-type dataset with time, categories, numerics, and missing values."""
    rng = np.random.default_rng(42)
    dates = pd.date_range("2023-01-01", periods=rows, freq="D")
    cat = rng.choice(["North", "South", "East", "West"], size=rows)
    product = rng.choice(["A", "B", "C"], size=rows)
    value = rng.normal(loc=100, scale=15, size=rows).round(2)
    noise = rng.normal(scale=5, size=rows)
    # Inject some missing values
    value[rng.choice(rows, size=round(rows * 0.1), replace=False)] = np.nan
    df = pd.DataFrame(
        {"date": dates, "region": cat, "product": product, "value": value, "noise": noise}
    )
    return df

def demo_indexing(df: pd.DataFrame) -> None:
    st.write("Concept: Labeled indexing, alignment, and safe selection.")
    df_idx = df.set_index(["date", "region"]).sort_index()
    st.write("MultiIndex set on ['date','region']:")
    st.dataframe(df_idx.head(8))
    st.write("Select a slice with .loc on MultiIndex:")
    sample_date = df_idx.index.get_level_values("date")[0]
    st.code(f"df_idx.loc[('{sample_date.date()}', 'North')]")
    st.dataframe(df_idx.loc[(sample_date, "North") : (sample_date, "West")].head(5))
    st.write("Avoid chained assignment; use .loc for assignment:")
    st.code("df.loc[df['value'].isna(), 'value'] = df['value'].mean()")

df = load_sample_data()
demo_indexing(df)
