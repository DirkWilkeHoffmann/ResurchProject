import pandas as pd


def generate_selected_sales(sales_file, article_file, output_file):
    # Load the data
    sales = pd.read_csv(sales_file)
    article = pd.read_csv(article_file)

    # Merge sales and article data
    sales = pd.merge(sales, article, on="article_code", how="left").drop(columns=["site_code"])

    # Count the occurrences of each article_code
    article_code_counts = sales["article_code"].value_counts()

    # Create a new column in the DataFrame with the count of each article_code
    sales["article_code_total_count"] = sales["article_code"].map(article_code_counts)

    # Convert ticket_end_time to datetime
    sales["ticket_end_time"] = pd.to_datetime(sales["ticket_end_time"], errors="coerce")

    # Filter the sales data for selected categories
    selected_category_no = {203601, 203401, 103204, 103210, 103207}
    selected_sales = sales[sales["category_no"].isin(selected_category_no)]

    # Save the selected sales data to a CSV file
    selected_sales.to_csv(output_file, index=False)
    print(f"Selected sales data saved to {output_file}")


if __name__ == "__main__":
    sales_file = "data/ShopriteData/STB CompSci Hons Project - sales data.csv"
    article_file = "data/ShopriteData/STB CompSci Hons Project - article data.csv"
    output_file = "selected_sales.csv"

    generate_selected_sales(sales_file, article_file, output_file)
