import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="CSV Data Visualizer", layout="wide")

st.title("CSV Data Visualizer")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully!")

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        numeric_cols = df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        categorical_cols = df.select_dtypes(
            include=["object"]
        ).columns.tolist()

        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        # Histogram
        if len(numeric_cols) > 0:
            st.subheader("Histogram")

            fig, ax = plt.subplots()
            ax.hist(df[numeric_cols[0]])
            ax.set_title(f"Histogram - {numeric_cols[0]}")
            st.pyplot(fig)

        # Box Plot
        if len(numeric_cols) > 0:
            st.subheader("Box Plot")

            fig, ax = plt.subplots()
            sns.boxplot(y=df[numeric_cols[0]], ax=ax)
            ax.set_title(f"Box Plot - {numeric_cols[0]}")
            st.pyplot(fig)

        # Scatter Plot
        if len(numeric_cols) > 1:
            st.subheader("Scatter Plot")

            fig, ax = plt.subplots()
            sns.scatterplot(
                x=df[numeric_cols[0]],
                y=df[numeric_cols[1]],
                ax=ax
            )
            ax.set_title(
                f"{numeric_cols[0]} vs {numeric_cols[1]}"
            )
            st.pyplot(fig)

        # Line Plot
        if len(numeric_cols) > 0:
            st.subheader("Line Plot")

            fig, ax = plt.subplots()
            ax.plot(df.index, df[numeric_cols[0]])
            ax.set_title(f"Line Plot - {numeric_cols[0]}")
            st.pyplot(fig)

        # Bar Chart
        if len(categorical_cols) > 0:
            st.subheader("Bar Chart")

            fig, ax = plt.subplots(figsize=(8, 4))
            df[categorical_cols[0]].value_counts().head(10).plot(
                kind="bar",
                ax=ax
            )
            st.pyplot(fig)

        # Pie Chart
        if len(categorical_cols) > 0:
            st.subheader("Pie Chart")

            fig, ax = plt.subplots(figsize=(6, 6))
            df[categorical_cols[0]].value_counts().head(5).plot(
                kind="pie",
                autopct="%1.1f%%",
                ax=ax
            )
            ax.set_ylabel("")
            st.pyplot(fig)

        # Heatmap
        if len(numeric_cols) > 1:
            st.subheader("Correlation Heatmap")

            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(
                df[numeric_cols].corr(),
                annot=True,
                cmap="coolwarm",
                ax=ax
            )
            st.pyplot(fig)

        # Pair Plot
        if len(numeric_cols) > 1:
            st.subheader("Pair Plot")

            pair_fig = sns.pairplot(df[numeric_cols])
            st.pyplot(pair_fig.figure)

        # Violin Plot
        if len(numeric_cols) > 0:
            st.subheader("Violin Plot")

            fig, ax = plt.subplots()
            sns.violinplot(
                y=df[numeric_cols[0]],
                ax=ax
            )
            st.pyplot(fig)

        # Count Plot
        if len(categorical_cols) > 0:
            st.subheader("Count Plot")

            fig, ax = plt.subplots(figsize=(10, 5))
            sns.countplot(
                x=df[categorical_cols[0]],
                order=df[categorical_cols[0]]
                .value_counts()
                .index[:10],
                ax=ax
            )
            plt.xticks(rotation=45)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Please upload a CSV file to begin.")