import streamlit as st
import pandas as pd

# Function to load CSV file
def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to apply color based on the "Status" column
def color_status(val):
    if val == "Online":
        color = "green"
    elif val == "Offline":
        color = "red"
    else:
        color = ""
    return f"background-color: {color}"

# Streamlit app
def main():
    st.title("ITOS Dashboard for Avocent hardware")

    # Path to the existing CSV file
    file_path = "MockAvocent.csv"  # Replace with the name of your CSV file

    # Load the CSV file
    df = load_csv(file_path)

    # Sidebar for sorting options
    st.sidebar.title("Sorting Options")

    # Select the number of columns to sort by
    num_sort_columns = st.sidebar.slider("Number of columns to sort by", min_value=1, max_value=len(df.columns), value=1)

    # Store selected columns and their sort orders
    sort_columns = []
    sort_orders = []

    for i in range(num_sort_columns):
        column = st.sidebar.selectbox(f"Select column {i+1} to sort by", df.columns, key=f"sort_col_{i}")
        order = st.sidebar.radio(f"Sort {column} in", ["Ascending", "Descending"], key=f"sort_order_{i}")
        sort_columns.append(column)
        sort_orders.append(order == "Ascending")

    # Sort the dataframe
    sorted_df = df.sort_values(by=sort_columns, ascending=sort_orders)

    # Apply the color styling to the "Status" column
    if 'Status' in sorted_df.columns:
        styled_df = sorted_df.style.applymap(color_status, subset=['Status'])
    else:
        styled_df = sorted_df

    # Display the styled dataframe
    st.dataframe(styled_df)

if __name__ == "__main__":
    main()

