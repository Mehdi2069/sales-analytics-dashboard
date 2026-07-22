from pathlib import Path
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def export_to_pdf(
    user,
    total_revenue,
    total_profit,
    total_orders,
    profit_margin,
    average_order_value,
    selected_region,
    selected_products,
    start_date,
    end_date
):
    """
    Generate a PDF summary report from dashboard KPIs.
    """

    output_dir = Path("output/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / (
        f"sales_dashboard_report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )

    doc = SimpleDocTemplate(str(file_path))

    styles = getSampleStyleSheet()
    content = []

    username = user.get("username", "Unknown")

    report_data = [
        "Sales Analytics Dashboard Report",
        f"User: {username}",
        f"Period: {start_date} to {end_date}",
        f"Regions: {selected_region}",
        f"Products: {selected_products}",
        "",
        f"Total Revenue: {total_revenue:,.2f}",
        f"Total Profit: {total_profit:,.2f}",
        f"Total Orders: {total_orders}",
        f"Profit Margin: {profit_margin:.2f}%",
        f"Average Order Value: {average_order_value:,.2f}",
    ]

    for item in report_data:
        content.append(Paragraph(str(item), styles["Normal"]))
        content.append(Spacer(1, 8))

    doc.build(content)

    return str(file_path)
