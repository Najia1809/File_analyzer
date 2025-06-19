import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyzer():
    st.subheader(f"Welcome, {st.session_state.username}")
    uploaded_file = st.file_uploader("Upload a .txt or .csv file", type=["txt", "csv"])

    content = None
    df = None
    file_type = None

    if uploaded_file:
        file_type = uploaded_file.name.split('.')[-1].lower()

        if file_type == "txt":
            try:
                content = uploaded_file.read().decode("utf-8")
                st.subheader("File Content")
                st.text(content)
            except:
                st.error("Unable to read this TXT file.")

        elif file_type == "csv":
            try:
                df = pd.read_csv(uploaded_file)
                st.subheader("CSV Data Preview")
                st.write(df.head())
            except:
                st.error("Unable to read this CSV file.")

        st.markdown("---")

        # 📌 Universal Buttons for Both File Types
        if st.button("Show Head"):
            if df is not None:
                st.write(df.head())
            elif content:
                st.text("\n".join(content.splitlines()[:5]))

        if st.button("Show Tail"):
            if df is not None:
                st.write(df.tail())
            elif content:
                st.text("\n".join(content.splitlines()[-5:]))

        if st.button("Show Statistics"):
            if df is not None:
                st.write(df.describe())
            elif content:
                words = content.split()
                st.write(f"Total Words: {len(words)}")

        if st.button("Preprocess"):
            if df is not None:
                st.write("Before:")
                st.write(df.isnull().sum())
                df_clean = df.dropna()
                st.write("After:")
                st.write(df_clean.isnull().sum())
            elif content:
                clean = "\n".join([line for line in content.splitlines() if line.strip() != ""])
                st.text("After Removing Empty Lines:")
                st.text(clean)

        if st.button("Show Graph"):
            if df is not None:
               num_cols = df.select_dtypes(include='number').columns
               if len(num_cols) > 0:
                  plt.figure(figsize=(8, 5))
                  sns.histplot(df[num_cols[0]], bins=30, kde=True, color="skyblue")
                  plt.title(f"Distribution of {num_cols[0]}")
                  st.pyplot(plt.gcf())
               else:
                  st.warning("No numeric columns available for plotting.")


            elif content:
                lines = content.splitlines()
                line_lengths = [len(line) for line in lines if line.strip()]
                if line_lengths:
                    plt.figure(figsize=(8, 5))
                    sns.lineplot(x=range(len(line_lengths)), y=line_lengths)
                    plt.title("Line Lengths in Text File")
                    st.pyplot(plt.gcf())
                else:
                    st.warning("Text is empty or not suitable for graph.")

        if st.button("Show Full Text/CSV Stats"):
            if df is not None:
                st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
            elif content:
                lines = content.splitlines()
                words = content.split()
                characters = len(content)
                st.write(f"Lines: {len(lines)} | Words: {len(words)} | Characters: {characters}")





