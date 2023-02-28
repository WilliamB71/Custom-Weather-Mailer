def html_table(weather_dict):
    table = """<table style="border-collapse: collapse; width: 100%; border-bottom: 0.2pt solid #2980B9;">
  <thead><tr style="text-align: center;">"""
    table += f"""<th style="padding: 5px; color: white; text-align: center; background-color: #2980B9; border-bottom: 1pt solid black">day</th>"""
    
    
    for parameter in weather_dict.get(list(weather_dict.keys())[0]):
        table += f"""<th style="padding: 5px; color: white; text-align: center; background-color: #2980B9; border-bottom: 1pt solid black">{parameter}</th>"""
    table += """</tr>
  </thead>"""
    
    table += """<tbody>"""
    for day_date in weather_dict:
        table += """<tr style="text-align: center; border-bottom: 0.2pt solid #2980B9;">"""
        table += f"""<td style="padding: 5px; color: #2980B9; background-color: #EAF2F8; font-family: Verdana, Geneva, Tahoma, sans-serif; text-align: left;">{day_date}</td>
        </tr>"""
        for value in weather_dict.get(day_date).values():
            table += f"""<td style="padding: 5px; color: #2980B9; background-color: #EAF2F8; font-family: Verdana, Geneva, Tahoma, sans-serif;">{value}</td>"""
        table += "</tr>"
    table += """ </tbody></table>"""
    return table

print(html_table({'today': {'Temperature': '7.4°C - 7.4°C', 'Weather Description': ['15:00: light rain'], 'Wind Speed': '15.1 mph - 15.1 mph'}, 'tomorrow': {'Temperature': '5.3°C - 6.9°C', 'Weather Description': ['09:00: broken clouds', '12:00: overcast clouds', '15:00: overcast clouds'], 'Wind Speed': '12.9 mph - 13.6 mph'}, 'Day after Tomorrow': {'Temperature': '3.8°C - 8.8°C', 'Weather Description': ['09:00: few clouds', '12:00: clear sky', '15:00: clear sky'], 'Wind Speed': '10.1 mph - 12.2 mph'}}))