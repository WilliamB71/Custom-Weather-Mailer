data = {'Today': {'windSpeed': (7.91, 10.15), 'windWaveHeight': (0.4, 0.67), 'windWavePeriod': (2.68, 3.135), 'waterTemperature': (7.35, 8.65), 'swellPeriod': (5.055, 12.57), 'waveHeight': (0.565, 0.97), 'wavePeriod': (2.91, 3.77), 'swellHeight': (0.095, 0.62)}, 
        'Tomorrow': {'windSpeed': (8.64, 10.08), 'windWaveHeight': (0.56, 0.79), 'windWavePeriod': (2.8, 3.395), 'waterTemperature': (8.36, 8.6), 'swellPeriod': (5.775, 9.190000000000001), 'waveHeight': (0.75, 0.905), 'wavePeriod': (3.39, 3.88), 'swellHeight': (0.26, 0.5700000000000001)}, 
        'Day After Tomorrow': {'windSpeed': (9.73, 10.36), 'windWaveHeight': (0.625, 0.88), 'windWavePeriod': (2.92, 3.8), 'waterTemperature': (8.38, 8.64), 'swellPeriod': (5.43, 7.91), 'waveHeight': (0.715, 0.98), 'wavePeriod': (3.35, 3.91), 'swellHeight': (0.165, 0.5800000000000001)}}

# Format the data as an HTML table
table_rows = ""
for day, values in data.items():
    for variable, range_ in values.items():
        min_val = "{:.2f}".format(range_[0])
        max_val = "{:.2f}".format(range_[1])
        table_rows += f"<tr><td>{day}</td><td>{variable}</td><td>{min_val} - {max_val}</td></tr>"

# Create the HTML table
table_html = f"""
<html>
  <head>
    <style>
      table {{
        border-collapse: collapse;
        width: 100%;
      }}
      th, td {{
        padding: 8px;
        text-align: left;
        border-bottom: 1px solid #ddd;
      }}
      th {{
        background-color: #f2f2f2;
        font-weight: bold;
      }}
      tr:nth-child(even) {{
        background-color: #f2f2f2;
      }}
      tr:hover {{
        background-color: #ddd;
      }}
    </style>
  </head>
  <body>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Variable</th>
          <th>Value Range</th>
        </tr>
      </thead>
      <tbody>
        {table_rows}
      </tbody>
    </table>
  </body>
</html>
"""

# Print or send the HTML table as an email
print(table_html)

