from pathlib import Path
from datetime import datetime

def generate_html_report(quality_report: dict, output_dir: Path) -> None:
    raw_c  = quality_report["raw_customers"]
    raw_t  = quality_report["raw_transactions"]
    cln_c  = quality_report["cleaned_customers"]
    cln_t  = quality_report["cleaned_transactions"]

    c_pass_rate = round(cln_c["total_rows"] / raw_c["total_rows"] * 100, 1)
    t_pass_rate = round(cln_t["total_rows"] / raw_t["total_rows"] * 100, 1)

    def rows(d):
        return "\n".join(
            f"<tr><td>{k}</td><td>{v}</td></tr>"
            for k, v in d.items()
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Data Quality Report</title>
<style>
  body {{ font-family: Arial, sans-serif; margin: 40px; color: #333; }}
  h1 {{ color: #2c3e50; }}
  h2 {{ color: #2980b9; margin-top: 30px; }}
  table {{ border-collapse: collapse; width: 480px; margin-bottom: 20px; }}
  th, td {{ border: 1px solid #ccc; padding: 8px 12px; text-align: left; }}
  th {{ background: #2980b9; color: white; }}
  .summary {{ background: #ecf0f1; padding: 16px; border-radius: 6px; width: 460px; }}
  .good {{ color: #27ae60; font-weight: bold; }}
  .warn {{ color: #e67e22; font-weight: bold; }}
</style>
</head>
<body>
<h1>Data Quality Report</h1>
<p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

<div class="summary">
  <strong>Pipeline Summary</strong><br><br>
  Customers: {raw_c['total_rows']:,} raw → {cln_c['total_rows']:,} cleaned
  &nbsp;<span class="{'good' if c_pass_rate >= 90 else 'warn'}">({c_pass_rate}% pass rate)</span><br>
  Transactions: {raw_t['total_rows']:,} raw → {cln_t['total_rows']:,} cleaned
  &nbsp;<span class="{'good' if t_pass_rate >= 90 else 'warn'}">({t_pass_rate}% pass rate)</span>
</div>

<h2>Customer Issues</h2>
<table>
  <tr><th>Check</th><th>Count</th></tr>
  {rows(raw_c)}
</table>

<h2>Transaction Issues</h2>
<table>
  <tr><th>Check</th><th>Count</th></tr>
  {rows(raw_t)}
</table>

</body>
</html>"""

    path = output_dir / "data_quality_report.html"
    path.write_text(html, encoding="utf-8")
    print(f"HTML report saved → {path}")