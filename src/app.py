import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.set_page_config(page_title="GRC Risk Heatmap", layout="wide")

st.title("🔥 GRC Risk Heatmap Generator")
st.markdown("Upload your CSV with `likelihood` and `impact` columns (1–5) to generate a 5×5 risk heatmap.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of your data:")
    st.dataframe(df.head())

    if 'likelihood' in df.columns and 'impact' in df.columns:
        matrix = pd.crosstab(df['likelihood'], df['impact'],
                             dropna=False).reindex(index=range(1, 6),
                                                   columns=range(1, 6),
                                                   fill_value=0)

        cmap = st.selectbox("Choose colour palette:",
                            ['Reds', 'Blues', 'Greens', 'OrRd', 'PuRd', 'YlOrRd'])

        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, fmt='d', cmap=cmap,
                    cbar_kws={'label': 'Number of Risks'},
                    xticklabels=range(1, 6), yticklabels=range(1, 6),
                    linewidths=0.5, linecolor='white', ax=ax)
        ax.set_xlabel('Impact', fontsize=12)
        ax.set_ylabel('Likelihood', fontsize=12)
        ax.set_title('5×5 Risk Heatmap', fontsize=16, fontweight='bold')

        st.pyplot(fig)

        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        buf.seek(0)
        st.download_button("Download Heatmap as PNG", data=buf,
                           file_name="risk_heatmap.png",
                           mime="image/png")
    else:
        st.error("Your CSV must contain columns named 'likelihood' and 'impact'.")
else:
    st.info("👈 Upload a CSV file to get started.")
    st.markdown("""
**Example CSV format:**
risk_name,likelihood,impact
Data breach,5,5
Phishing attack,4,4
Ransomware,3,5
""")