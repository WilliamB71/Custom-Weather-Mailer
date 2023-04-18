import arrow
from weather_forecast import Weather
from wave_forecast import StormGlass

class Email_Content:

    def write():
        weather_forecast = Weather.report()
        wave_forecast = StormGlass.data()
        dt_now = arrow.now(tz='Europe/London')

        html_str1 = """<!DOCTYPE html>
        <html>

        <head>
          <style>
            body {
              font-family: Verdana, sans-serif;
              font-size: 12px;
              line-height: 1.5;
              color: #1f5070;
              text-align: center;
              margin: 10;
              padding: 0;
            }

            h1 {
              font-size: 20px;
              font-weight: bold;
              text-align: center;
              margin-top: 20px;
              margin-bottom: 10px;
            }

            h2 {
              font-size: 20px;
              font-weight: bold;
              margin-top: 20px;
              margin-bottom: 10px;
            }

            table {
              border-collapse: collapse;
              width: 100%;
              max-width: 600px;
              margin: auto auto;
            }

            td {
                color: #030303;
                border: 1px solid #297fb9;
                padding: 6px;
                text-align: center;
                vertical-align: left;
                font-weight: bold;
                color: #1f5070;
                margin: 3px 0;
                }

            th {
              background-color: #2980B9;
              color: rgb(255, 255, 255);
              font-weight: bold;
              text-align: center;
              padding: 8px 8px;
              border-top: 1px solid #2980B9;
              border-bottom: 1px solid #ffffff;
              border-left: 1px solid #2980B9;
            }

            th:first-child {
              border-left: none;
            }

            th:last-child {
              border-right: none;
            }

            img {
              display: block;
              max-width: 100%;
              height: auto;
              margin: 0 auto;
            }

            p {
              font-weight: bold;
              color: #1f5070;
              margin: 3px 0;
            }
          </style>
        </head>"""

        html_str2 = """

        <body>
          <h1>Canford Cliffs</h1>
          <h1>Weather</h1>
          <table>
            <tr>
              <th>Today</th>
              <th>{day2}</th>
              <th>{day3}</th>
              <th>{day4}</th>
              <th>{day5}</th>
            </tr>
            <tr>
              <td><img src="https://openweathermap.org/img/wn/{icon1}.png" alt="image" width=auto height=auto></td>
              <td><img src="https://openweathermap.org/img/wn/{icon2}.png" alt="image" width=auto height=auto></td>
              <td><img src="https://openweathermap.org/img/wn/{icon3}.png" alt="image" width=auto height=auto></td>
              <td><img src="https://openweathermap.org/img/wn/{icon4}.png" alt="image" width=auto height=auto></td>
              <td><img src="https://openweathermap.org/img/wn/{icon5}.png" alt="image" width=auto height=auto></td>
            </tr>
          </table>
          <br>
          <table>
            <tr>
              <th></th>
              <th>Today</th>
              <th>{day2}</th>
              <th>{day3}</th>
            </tr>
            <tr>
              <th>Temperature</th>
              <td>{tempday1}</td>
              <td>{tempday2}</td>
              <td>{tempday3}</td>
            </tr>
            <tr>
              <th>Description</th>
              <td>{descday1}</td>
              <td>{descday2}</td>
              <td>{descday3}</td>
            </tr>
            <tr>
              <th>Wind</th>
              <td>{windday1}</td>
              <td>{windday2}</td>
              <td>{windday3}</td>
            </tr>
          </table>
          <br>
          <table>
            <tr>
              <td>
                <p>Bournemouth Pier</p>
                <img src="cid:Beach_Image.png" alt="Bournemouth Pier" width="100%" height="50%">
              </td>
            </tr>
          </table>
          <br>
          <h1>Sea Conditions</h1>
          <table>
            <tr>
              <th>Today</th>
            </tr>
            <tr>
              <td>Wave (m)</td>
              <td>{wave1}</td>
            </tr>
            <tr>
              <td>Wave Period (s)</td>
              <td>{wave_period1}</td>
            </tr>
            <tr>
              <td>Wind Wave (m)</td>
              <td>{wind_wave1}</td>
            </tr>
            <tr>
              <td>Wind Speed (mph)</td>
              <td>{oceanwind1}</td>
            </tr>
            <tr>
          </table>
          <br>
          <table>
            <tr>
              <th>{day2}</th>
            </tr>
            <tr>
              <td>Wave (m)</td>
              <td>{wave2}</td>
            </tr>
            <tr>
              <td>Wave Period (s)</td>
              <td>{wave_period2}</td>
            </tr>
            <tr>
              <td>Wind Wave (m)</td>
              <td>{wind_wave2}</td>
            </tr>
            <tr>
              <td>Wind Speed (mph)</td>
              <td>{oceanwind2}</td>
            </tr>
            <tr>

          </table>
          <br>
          <table>
            <tr>
              <th>{day3}</th>
            </tr>
                <tr>
              <td>Wave (m)</td>
              <td>{wave3}</td>
            </tr>
            <tr>
              <td>Wave Period (s)</td>
              <td>{wave_period3}</td>
            </tr>
            <tr>
              <td>Wind Wave (m)</td>
              <td>{wind_wave3}</td>
            </tr>
            <tr>
              <td>Wind Speed (mph)</td>
              <td>{oceanwind3}</td>
            </tr>
            <tr>

          </table>
          <br>
          <table>
            <tr>
              <th>Water Temperature (°C)</th>
            </tr>
            <td>{water_temp}</td>
            </tr>
          </table>
        </body>

        </html>""".format(day2=dt_now.shift(days=1).format('dddd'),
                          day3=dt_now.shift(days=2).format('dddd'),
                          day4=dt_now.shift(days=3).format('dddd'),
                          day5=dt_now.shift(days=4).format('dddd'),
                          icon1=weather_forecast[0].get('icon_id'),
                          icon2=weather_forecast[1].get('icon_id'),
                          icon3=weather_forecast[2].get('icon_id'),
                          icon4=weather_forecast[3].get('icon_id'),
                          icon5=weather_forecast[4].get('icon_id'),
                          tempday1=weather_forecast[0].get('Temperature'),
                          tempday2=weather_forecast[1].get('Temperature'),
                          tempday3=weather_forecast[2].get('Temperature'),
                          descday1=weather_forecast[0].get('Weather Description'),
                          descday2=weather_forecast[1].get('Weather Description'),
                          descday3=weather_forecast[2].get('Weather Description'),
                          windday1=weather_forecast[0].get('Wind Speed'),
                          windday2=weather_forecast[1].get('Wind Speed'),
                          windday3=weather_forecast[2].get('Wind Speed'),
                          wave1=wave_forecast[0].get('waveHeight'),
                          wave2=wave_forecast[1].get('waveHeight'),
                          wave3=wave_forecast[2].get('waveHeight'),
                          wave_period1=wave_forecast[0].get('swellPeriod'),
                          wave_period2=wave_forecast[1].get('swellPeriod'),
                          wave_period3=wave_forecast[2].get('swellPeriod'),
                          wind_wave1=wave_forecast[0].get('windWaveHeight'),
                          wind_wave2=wave_forecast[1].get('windWaveHeight'),
                          wind_wave3=wave_forecast[2].get('windWaveHeight'),
                          oceanwind1= wave_forecast[0].get('windSpeed'),
                          oceanwind2=wave_forecast[1].get('windSpeed'),
                          oceanwind3=wave_forecast[2].get('windSpeed'),
                          water_temp=wave_forecast[0].get('waterTemperature')
                          )
        return html_str1 + html_str2

