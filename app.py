import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc

# Load dataset
df = pd.read_csv("sales_cleaned.csv")
# Start Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#FFFFFF', 'padding': '20px'}, children=[

    html.H1("📊 Amazon Sales Dashboard", style={'textAlign': 'center'}),

    # Sales by Category
    dcc.Graph(
        id='sales-by-category',
        figure=px.bar(
            df, x='Category', y='Amount', 
            title='Sales by Category',
            color='Category',
            color_discrete_sequence=px.colors.qualitative.Plotly
        ).update_layout(paper_bgcolor='#111111', plot_bgcolor='#111111', font_color='white')
    ),
    html.P("📦 This bar chart shows total sales grouped by product category. It helps you identify the most profitable product types."),

    # Top Shipping Cities
    dcc.Graph(
        id='top-cities',
        figure=px.bar(
            df.groupby('ship-city')['Amount'].sum().nlargest(10).reset_index(),
            x='ship-city', y='Amount',
            title='Top 10 Shipping Cities by Sales', color='ship-city',
            color_discrete_sequence=px.colors.sequential.Viridis
        ).update_layout(paper_bgcolor='#111111', plot_bgcolor='#111111', font_color='white')
    ),
    html.P("🏙️ These are the top 10 cities based on shipping-related sales, revealing where most purchases are being shipped."),

    # Fulfilment Type Distribution
    dcc.Graph(
        id='fulfilment-type',
        figure=px.pie(
            df, names='Fulfilment', values='Amount',
            title='Sales Distribution by Fulfilment Type',
            color_discrete_sequence=px.colors.sequential.Magenta
        ).update_layout(paper_bgcolor='#111111', font_color='white')
    ),
    html.P("🚚 This pie chart shows the distribution of sales by fulfilment type, such as Amazon vs Merchant fulfilled."),

    # Sales Channel Breakdown
    dcc.Graph(
        id='sales-channel',
        figure=px.bar(
            df.groupby('Sales Channel ')['Amount'].sum().reset_index(),
            x='Sales Channel ', y='Amount',
            title='Sales by Channel',
            color='Sales Channel ',
            color_discrete_sequence=px.colors.sequential.Tealgrn
        ).update_layout(paper_bgcolor='#111111', plot_bgcolor='#111111', font_color='white')
    ),
    html.P("🌐 This chart shows which sales channels (like Amazon.in, Amazon.com, etc.) contribute the most to revenue."),

    # Footer
    html.H3("💡 More Insights Coming Soon!", style={'marginTop': '40px'}),
    html.P("Additional dashboards like Product Performance, Customer Return Rate, and Region-wise Profitability will be added.")
])

if __name__ == '__main__':
    app.run(debug=True)
