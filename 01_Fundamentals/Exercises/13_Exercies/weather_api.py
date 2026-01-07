# ============================================================
# Features:
#   - Dynamic city search (Geocoding API)
#   - Multiple city options + user selection
#   - Current weather table (+ Cold/Mild/Hot label)
#   - Hourly forecast table (+ label)
#   - Daily summary (min/max temperature)
#   - Feels-like temperature (apparent_temperature)
#   - Precipitation label (rain / snow / showers / dry)
# ============================================================

from requests import get
from requests.exceptions import RequestException
from pprint import pprint


while True:
    city_name = input("\nPlease type city name (or 'q' to quit): ").strip()

    if city_name.lower() == "q":
        print("Program terminated.")
        break

    if not city_name:
        print("City name cannot be empty.")
        continue

    # --------------------------------------------------------
    # STEP 1: Fetch city list (Geocoding API)
    # --------------------------------------------------------
    # Expected Output: A list of cities matching the given name with latitude and longitude information.

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city_name,
        "count": 5,
        "language": "en",
        "format": "json"
    }

    try:
        geo_response = get(geo_url, params=geo_params, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        # pprint(geo_data)
    except RequestException as error:
        print("An error occurred while fetching city coordinates.")
        print(error)
        continue

    results = geo_data.get("results")

    if not results:
        print("City not found.")
        continue

    # --------------------------------------------------------
    # STEP 2: Locations table + selection
    # --------------------------------------------------------
    # Expected Output: A table listing multiple city options and user selects one by number.

    print("\nAvailable Locations:")
    print("-" * 90)
    print(f"{'No':<4} {'City':<22} {'Country':<12} {'Latitude':<12} {'Longitude':<12}")
    print("-" * 90)

    for index, city in enumerate(results, start=1):
        print(
            f"{index:<4} "
            f"{(city.get('name') or 'N/A'):<22} "
            f"{(city.get('country') or 'N/A'):<12} "
            f"{str(city.get('latitude') or 'N/A'):<12} "
            f"{str(city.get('longitude') or 'N/A'):<12}"
        )

    print("-" * 90)

    while True:
        choice = input("Please select a city number (or 'c' to cancel): ").strip()
        
        if choice.lower() == 'c':
            selected_city = None
            break
        
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            selected_city = results[int(choice) - 1]
            break
        else:
            print(f"Invalid selection! Please enter a number between 1 and {len(results)}.")

    if not selected_city:
        continue

    latitude = selected_city.get("latitude")
    longitude = selected_city.get("longitude")
    city_display_name = selected_city.get("name")
    country = selected_city.get("country")

    # --------------------------------------------------------
    # STEP 3: Fetch weather data (current + hourly + daily)
    # --------------------------------------------------------
    # Expected Output: JSON data containing current, hourly, and daily weather information.

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "hourly": "temperature_2m,apparent_temperature,precipitation,rain,showers,snowfall,wind_speed_10m,wind_direction_10m",
        "daily": "temperature_2m_max,temperature_2m_min,sunrise,sunset",
        "timezone": "auto"
    }

    try:
        weather_response = get(weather_url, params=weather_params, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
    except RequestException as error:
        print("An error occurred while fetching weather data.")
        print(error)
        continue

    current_weather = weather_data.get("current_weather")
    hourly = weather_data.get("hourly", {})
    daily = weather_data.get("daily", {})

    if not current_weather:
        print("Weather data could not be retrieved.")
        continue

    # --------------------------------------------------------
    # STEP 4: Current weather table + label
    # --------------------------------------------------------
    # Raw API values
    raw_temperature = current_weather.get("temperature")
    raw_wind_speed = current_weather.get("windspeed")
    raw_wind_direction = current_weather.get("winddirection")

    # Convert to float safely
    try:
        temperature_celsius = float(raw_temperature) if raw_temperature is not None else None
        wind_speed_kmh = float(raw_wind_speed) if raw_wind_speed is not None else 0.0
        wind_direction_degree = float(raw_wind_direction) if raw_wind_direction is not None else None
    except (ValueError, TypeError):
        temperature_celsius = None
        wind_speed_kmh = 0.0
        wind_direction_degree = None

    # String formatting
    temperature_text = f"{temperature_celsius:.1f}" if temperature_celsius is not None else "N/A"
    wind_speed_text = f"{wind_speed_kmh:.1f}" if wind_speed_kmh is not None else "N/A"
    wind_direction_text = f"{wind_direction_degree:.0f}" if wind_direction_degree is not None else "N/A"

    # Temperature label
    if temperature_celsius is None:
        temperature_label = "N/A"
    elif temperature_celsius < 10:
        temperature_label = "Cold"
    elif temperature_celsius <= 25:
        temperature_label = "Mild"
    else:
        temperature_label = "Hot"

    # Wind warning label
    if wind_speed_kmh > 40:
        wind_status = "STORM!"
    elif wind_speed_kmh > 20:
        wind_status = "Breezy"
    else:
        wind_status = "Calm"

    print("\nCurrent Weather")
    print("-" * 98)
    print(
        f"{'City':<20} "
        f"{'Country':<12} "
        f"{'Temp (°C)':<12} "
        f"{'Label':<10} "
        f"{'Wind (km/h)':<14} "
        f"{'Dir (°)':<10} "
        f"{'Wind Status':<10}"
    )
    print("-" * 98)

    print(
        f"{(city_display_name or 'N/A'):<20} "
        f"{(country or 'N/A'):<12} "
        f"{temperature_text:<12} "
        f"{temperature_label:<10} "
        f"{wind_speed_text:<14} "
        f"{wind_direction_text:<10} "
        f"{wind_status:<10}"
    )

    print("-" * 98)
    # --------------------------------------------------------
    # STEP 5: Hourly forecast table (Next 10 Hours) + feels-like + precipitation label
    # --------------------------------------------------------
    # Saat bilgileri
    hourly_times = hourly.get("time", [])
    current_time_string = current_weather.get("time")  # Örn: "2025-12-18T01:00"

    # Hourly veriler
    hourly_temperatures = hourly.get("temperature_2m", [])
    hourly_feels_like = hourly.get("apparent_temperature", [])
    hourly_precipitation = hourly.get("precipitation", [])
    hourly_rain = hourly.get("rain", [])
    hourly_showers = hourly.get("showers", [])
    hourly_snowfall = hourly.get("snowfall", [])
    hourly_wind_speed = hourly.get("wind_speed_10m", [])          # ✅ NEW
    hourly_wind_direction = hourly.get("wind_direction_10m", [])  # ✅ NEW (optional)

    # Zaman formatını normalize et (saniyeyi kes)
    normalized_current_time = current_time_string[:16] if isinstance(current_time_string, str) else None
    normalized_hourly_times = [
        time[:16] if isinstance(time, str) else "" 
        for time in hourly_times
    ]

    start_hour_index = None

    if normalized_hourly_times and normalized_current_time:
        if normalized_current_time in normalized_hourly_times:
            start_hour_index = normalized_hourly_times.index(normalized_current_time)
        else:
            # Mevcut zamandan sonraki ilk saat
            for index, time in enumerate(normalized_hourly_times):
                if time and time >= normalized_current_time:
                    start_hour_index = index
                    break

            if start_hour_index is None:
                start_hour_index = 0
    elif normalized_hourly_times:
        start_hour_index = 0

    if start_hour_index is not None and isinstance(hourly_temperatures, list):
        display_start_time = (normalized_hourly_times[start_hour_index] or "N/A").replace("T", " ")
        print(f"\nHourly Forecast (Starting from: {display_start_time})")
        print("-" * 146)
        print(
            f"{'Time':<22} "
            f"{'Temp (°C)':<12} "
            f"{'Label':<10} "
            f"{'Feels (°C)':<12} "
            f"{'Precip':<10} "
            f"{'Weather':<12} "
            f"{'Wind (km/h)':<14} "
            f"{'Wind Status':<12} "
            f"{'Advice':<28}"
        )
        print("-" * 146)

        safe_limit = min(
            len(hourly_times),
            len(hourly_temperatures),
            len(hourly_feels_like),
            len(hourly_precipitation),
            len(hourly_rain),
            len(hourly_showers),
            len(hourly_snowfall),
            len(hourly_wind_speed),
        )

        end_hour_index = min(start_hour_index + 10, safe_limit)

        for hour_index in range(start_hour_index, end_hour_index):
            # Zaman
            hour_time = (normalized_hourly_times[hour_index] or "N/A").replace("T", " ")

            # Sıcaklık
            temperature = (
                float(hourly_temperatures[hour_index])
                if hour_index < len(hourly_temperatures) and hourly_temperatures[hour_index] is not None
                else None
            )
            temperature_text = f"{temperature:.1f}" if temperature is not None else "N/A"

            if temperature is None:
                temperature_label = "N/A"
            elif temperature < 10:
                temperature_label = "Cold"
            elif temperature <= 25:
                temperature_label = "Mild"
            else:
                temperature_label = "Hot"

            # Hissedilen sıcaklık
            feels_like_temperature = (
                float(hourly_feels_like[hour_index])
                if hour_index < len(hourly_feels_like) and hourly_feels_like[hour_index] is not None
                else None
            )
            feels_like_text = f"{feels_like_temperature:.1f}" if feels_like_temperature is not None else "N/A"

            # Yağış miktarı
            precipitation_amount = (
                float(hourly_precipitation[hour_index])
                if hour_index < len(hourly_precipitation) and hourly_precipitation[hour_index] is not None
                else 0.0
            )
            precipitation_text = f"{precipitation_amount:.1f}mm"

            # Yağış türü önceliği: Snow > Rain > Showers > Dry
            snowfall_amount = (
                float(hourly_snowfall[hour_index])
                if hour_index < len(hourly_snowfall) and hourly_snowfall[hour_index] is not None
                else 0.0
            )
            rain_amount = (
                float(hourly_rain[hour_index])
                if hour_index < len(hourly_rain) and hourly_rain[hour_index] is not None
                else 0.0
            )
            showers_amount = (
                float(hourly_showers[hour_index])
                if hour_index < len(hourly_showers) and hourly_showers[hour_index] is not None
                else 0.0
            )

            if snowfall_amount > 0:
                weather_label = "Snow"
            elif rain_amount > 0:
                weather_label = "Rain"
            elif showers_amount > 0:
                weather_label = "Showers"
            else:
                weather_label = "Dry"

            # ✅ Wind per hour + status
            wind_speed_kmh = float(hourly_wind_speed[hour_index]) if hour_index < len(hourly_wind_speed) and hourly_wind_speed[hour_index] is not None else 0.0
            wind_speed_text = f"{wind_speed_kmh:.1f}"

            if wind_speed_kmh > 40:
                wind_status = "STORM!"
            elif wind_speed_kmh > 20:
                wind_status = "Breezy"
            else:
                wind_status = "Calm"

            hourly_advice = "✅ Good conditions"

            # Wind-based advice (priority)
            if wind_speed_kmh > 40:
                hourly_advice = "⚠️ Storm expected"
            elif wind_speed_kmh > 30:
                hourly_advice = "💨 Very windy"

            # Precipitation-based advice (can override)
            if precipitation_amount > 3:
                hourly_advice = "☔ Heavy rain possible"
            elif precipitation_amount > 0:
                hourly_advice = "🌧️ Light rain possible"

            # Temperature-based advice (can override)
            if temperature is not None and temperature < 5:
                hourly_advice = "🥶 Very cold, dress warm"
            elif temperature is not None and temperature > 30:
                hourly_advice = "🥵 Hot, stay hydrated"

            print(
                f"{hour_time:<22} "
                f"{temperature_text:<12} "
                f"{temperature_label:<10} "
                f"{feels_like_text:<12} "
                f"{precipitation_text:<10} "
                f"{weather_label:<12} "
                f"{wind_speed_text:<14} "
                f"{wind_status:<12} "
                f"{hourly_advice:<28}"
            )

        # STEP 5.9: Comfort Overview (Next 10 Hours) — Summary
        # --------------------------------------------------------
        comfort_rows = []
        storm_hours = []
        caution_hours = []

        best_score = -1
        best_time = "N/A"
        best_reason = ""

        worst_score = 999
        worst_time = "N/A"
        worst_reason = ""

        storm_hours = []
        caution_hours = []

        for hour_index in range(start_hour_index, end_hour_index):
            # Time
            overview_time = (normalized_hourly_times[hour_index] or "N/A").replace("T", " ")

            # Hourly values
            ov_temp = (
                float(hourly_temperatures[hour_index])
                if hour_index < len(hourly_temperatures) and hourly_temperatures[hour_index] is not None
                else None
            )
            ov_feels = (
                float(hourly_feels_like[hour_index])
                if hour_index < len(hourly_feels_like) and hourly_feels_like[hour_index] is not None
                else None
            )
            ov_precip = (
                float(hourly_precipitation[hour_index])
                if hour_index < len(hourly_precipitation) and hourly_precipitation[hour_index] is not None
                else 0.0
            )
            ov_wind = (
                float(hourly_wind_speed[hour_index])
                if hour_index < len(hourly_wind_speed) and hourly_wind_speed[hour_index] is not None
                else 0.0
            )

            # Comfort Score (0–100) per hour
            score = 100
            reason_parts = []

            # Temp penalty
            if ov_temp is not None:
                if ov_temp < 0:
                    score -= 50; reason_parts.append("freezing")
                elif ov_temp < 5:
                    score -= 35; reason_parts.append("very cold")
                elif ov_temp < 10:
                    score -= 20; reason_parts.append("cold")
                elif ov_temp > 35:
                    score -= 45; reason_parts.append("extremely hot")
                elif ov_temp > 30:
                    score -= 30; reason_parts.append("hot")
                elif ov_temp > 28:
                    score -= 20; reason_parts.append("warm")

            # Feels-like mismatch penalty
            if ov_temp is not None and ov_feels is not None:
                diff = abs(ov_temp - ov_feels)
                if diff >= 8:
                    score -= 25; reason_parts.append("feels much different")
                elif diff >= 5:
                    score -= 15; reason_parts.append("feels different")
                elif diff >= 3:
                    score -= 8;  reason_parts.append("slight wind/humidity effect")

            # Feels-like difference
            if ov_temp is not None and ov_feels is not None:
                feels_diff = abs(ov_temp - ov_feels)
            else:
                feels_diff = None

            # Wind penalty
            if ov_wind > 40:
                score -= 35; reason_parts.append("storm wind")
            elif ov_wind > 30:
                score -= 20; reason_parts.append("very windy")
            elif ov_wind > 20:
                score -= 10; reason_parts.append("breezy")

            # Precip penalty
            if ov_precip > 5:
                score -= 30; reason_parts.append("heavy rain")
            elif ov_precip > 2:
                score -= 18; reason_parts.append("rain")
            elif ov_precip > 0:
                score -= 8;  reason_parts.append("light rain")

            score = max(0, min(100, score))

            # --- Weather label for overview hour (Snow > Rain > Showers > Dry)
            ov_snow = float(hourly_snowfall[hour_index]) if hour_index < len(hourly_snowfall) and hourly_snowfall[hour_index] is not None else 0.0
            ov_rain = float(hourly_rain[hour_index]) if hour_index < len(hourly_rain) and hourly_rain[hour_index] is not None else 0.0
            ov_show = float(hourly_showers[hour_index]) if hour_index < len(hourly_showers) and hourly_showers[hour_index] is not None else 0.0

            if ov_snow > 0:
                ov_weather_label = "Snow"
            elif ov_rain > 0:
                ov_weather_label = "Rain"
            elif ov_show > 0:
                ov_weather_label = "Showers"
            else:
                ov_weather_label = "Dry"

            reason_text = ", ".join(reason_parts) if reason_parts else "good conditions"

            # Track storm/caution hours (simple)
            if ov_wind > 40:
                storm_hours.append(overview_time[-5:])  # HH:MM
            elif ov_wind > 30 or ov_precip > 2 or (ov_temp is not None and (ov_temp < 5 or ov_temp > 30)):
                caution_hours.append(overview_time[-5:])

            comfort_rows.append({
                "time": overview_time[-5:],
                "score": score,
                "reason": reason_text,
                "wind": ov_wind,
                "precip": ov_precip,
                "temp": ov_temp,
                "weather": ov_weather_label,     # zaten varsa kalsın
                "feels_diff": feels_diff   
            })

            # Best/Worst
            if score > best_score:
                best_score = score
                best_time = overview_time[-5:]
                best_reason = reason_text

            if score < worst_score:
                worst_score = score
                worst_time = overview_time[-5:]
                worst_reason = reason_text      

        # Sort for top/bottom
        comfort_rows_sorted_best = sorted(comfort_rows, key=lambda x: x["score"], reverse=True)
        comfort_rows_sorted_worst = sorted(comfort_rows, key=lambda x: x["score"])

        top_n = 2 if len(comfort_rows_sorted_best) >= 2 else len(comfort_rows_sorted_best)
        bottom_n = 2 if len(comfort_rows_sorted_worst) >= 2 else len(comfort_rows_sorted_worst)

        # ⭐ Recommended hour (filter: best score BUT not rainy + not storm)
        recommended = None

        # First priority: Dry and not storm
        for item in comfort_rows_sorted_best:
            if (
                item["wind"] <= 40 and
                item.get("weather") == "Dry" and
                item.get("feels_diff") is not None and
                item["feels_diff"] < 3
            ):
                recommended = item
                break

        # Second priority: not storm
        if recommended is None:
            for item in comfort_rows_sorted_best:
                if (
                    item["wind"] <= 40 and
                    item.get("feels_diff") is not None and
                    item["feels_diff"] < 3
                ):
                    recommended = item
                    break

        # Not storm
        if recommended is None:
            for item in comfort_rows_sorted_best:
                if item["wind"] <= 40:
                    recommended = item
                    break

        # Fallback: best score
        if recommended is None and comfort_rows_sorted_best:
            recommended = comfort_rows_sorted_best[0]

        print("\n🧠 Comfort Overview (Next 10 Hours)")
        print("-" * 70)
        print(f"✅ Best hour to go outside : {best_time} (Comfort {best_score}/100) — {best_reason}")
        print(f"❌ Worst hour             : {worst_time} (Comfort {worst_score}/100) — {worst_reason}")

        print("✅ Best hours to go outside:")
        if top_n == 0:
            print("  - N/A")
        else:
            for item in comfort_rows_sorted_best[:top_n]:
                print(
                    f"  - {item['time']} | "
                    f"Score {item['score']}/100 | "
                    f"{item['weather']} | "
                    f"{item['reason']}"
                )
                
        print("❌ Worst hours (least comfortable):")
        if bottom_n == 0:
            print("  - N/A")
        else:
            for item in comfort_rows_sorted_worst[:bottom_n]:
                print(f"  - {item['time']} | Comfort {item['score']}/100 — {item['reason']} | Weather: {item['weather']}")

        print("\n⭐ Recommended hour:")
        if recommended:
            print(f"  - {recommended['time']}  | Comfort {recommended['score']}/100 — {recommended['reason']}")

            reason_parts = []

            if recommended.get("weather") == "Dry":
                reason_parts.append("dry weather")
            elif recommended.get("weather"):
                reason_parts.append(recommended["weather"].lower())

            if recommended.get("feels_diff") is not None:
                reason_parts.append(f"low feels-like diff ({recommended['feels_diff']:.1f}°C)")

            if recommended.get("wind", 0) <= 20:
                reason_parts.append("calm wind")
            elif recommended.get("wind", 0) <= 40:
                reason_parts.append("moderate wind")
            else:
                reason_parts.append("very windy")

            short_reason = ", ".join(reason_parts) if reason_parts else "balanced conditions"
            print(f"    👉 Reason: {short_reason}")
        else:
            print("  - N/A")
            
        if storm_hours:
            print(f"⚠️ Storm risk hours : {', '.join(storm_hours)}")
        elif caution_hours:
            shown = caution_hours[:8]
            print(f"⚠️ Caution hours    : {', '.join(shown)}{' ...' if len(caution_hours) > 8 else ''}")
        else:
            print("✅ No storm/caution hours detected in the next 10 hours.")

            print("-" * 78) 

    else:
        print("Hourly forecast data not available.")

    # --------------------------------------------------------
    # STEP 6: Daily summary (min/max)
    # --------------------------------------------------------
    daily_dates = daily.get("time", [])
    daily_max = daily.get("temperature_2m_max", [])
    daily_min = daily.get("temperature_2m_min", [])

    if daily_dates and daily_max and daily_min:
        # Show only today (first day) summary
        d0 = daily_dates[0]
        max_val = float(daily_max[0]) if daily_max[0] is not None else None
        min_val = float(daily_min[0]) if daily_min[0] is not None else None

        max_str = f"{max_val:.1f}" if max_val is not None else "N/A"
        min_str = f"{min_val:.1f}" if min_val is not None else "N/A"

        print("\nDaily Summary (Today)")
        print("-" * 45)
        print(f"Date      : {d0}")
        print(f"Min Temp  : {min_str} °C")
        print(f"Max Temp  : {max_str} °C")
        print("-" * 45)
    else:
        print("Daily summary data not available.")
    # --------------------------------------------------------
    # STEP 6.5: Astronomy & Comfort Index
    # --------------------------------------------------------
    sunrise = daily.get("sunrise", [None])[0]
    sunset = daily.get("sunset", [None])[0]

    # Format sunrise / sunset time (YYYY-MM-DDTHH:MM -> HH:MM)
    sunrise_time = sunrise[-5:] if isinstance(sunrise, str) and len(sunrise) >= 5 else "N/A"
    sunset_time  = sunset[-5:]  if isinstance(sunset,  str) and len(sunset)  >= 5 else "N/A"

    # Current feels-like (from hourly, aligned with current time)
    current_feels_like = None
    if (
        start_hour_index is not None
        and start_hour_index < len(hourly_feels_like)
        and hourly_feels_like[start_hour_index] is not None
    ):
        current_feels_like = float(hourly_feels_like[start_hour_index])

    # Current precipitation (aligned with current hour from hourly)
    current_precip_mm = 0.0
    if (
        start_hour_index is not None
        and start_hour_index < len(hourly_precipitation)
        and hourly_precipitation[start_hour_index] is not None
    ):
        current_precip_mm = float(hourly_precipitation[start_hour_index])

    # --- Comfort Score (0–100) logic
    comfort_score = 100

    # Temperature penalty (based on actual temperature)
    if temperature_celsius is not None:
        if temperature_celsius < 0:
            comfort_score -= 50
        elif temperature_celsius < 5:
            comfort_score -= 35
        elif temperature_celsius < 10:
            comfort_score -= 20
        elif temperature_celsius > 35:
            comfort_score -= 45
        elif temperature_celsius > 30:
            comfort_score -= 30
        elif temperature_celsius > 28:
            comfort_score -= 20

    if temperature_celsius is not None and current_feels_like is not None:
        diff = abs(temperature_celsius - current_feels_like)
        if diff >= 8:
            comfort_score -= 25
        elif diff >= 5:
            comfort_score -= 15
        elif diff >= 3:
            comfort_score -= 8

        # Wind penalty
        if wind_speed_kmh > 40:
            comfort_score -= 35
        elif wind_speed_kmh > 30:
            comfort_score -= 20
        elif wind_speed_kmh > 20:
            comfort_score -= 10

        # Precipitation penalty
        if current_precip_mm > 5:
            comfort_score -= 30
        elif current_precip_mm > 2:
            comfort_score -= 18
        elif current_precip_mm > 0:
            comfort_score -= 8

        # Clamp score to 0–100
        if comfort_score < 0:
            comfort_score = 0
        elif comfort_score > 100:
            comfort_score = 100

        # --- Outdoor Suitability label
        if wind_speed_kmh > 40 or current_precip_mm > 5 or (temperature_celsius is not None and (temperature_celsius < 0 or temperature_celsius > 35)):
            suitability = "❌ Avoid"
        elif wind_speed_kmh > 30 or current_precip_mm > 2 or (temperature_celsius is not None and (temperature_celsius < 5 or temperature_celsius > 30)):
            suitability = "⚠️ Caution"
        else:
            suitability = "✅ Good"

        # --- Short comfort note
        comfort_note = "Temperature feels consistent."
        if temperature_celsius is not None and current_feels_like is not None:
            diff = abs(temperature_celsius - current_feels_like)
            if diff >= 3:
                if current_feels_like < temperature_celsius:
                    comfort_note = "Wind chill is dominant."
                else:
                    comfort_note = "Humidity makes it feel heavier."

        print(f"\n☀️  Astronomy: Sunrise at {sunrise_time} | Sunset at {sunset_time}")
        print(f"🌡️  Comfort Note : {comfort_note}")
        print(f"📊 Comfort Score : {comfort_score}/100")
        print(f"🚶 Outdoor       : {suitability}")
        print("-" * 98)
    # --------------------------------------------------------
    # STEP 7: Daily Forecast Table (Next 7 Days)
    # --------------------------------------------------------
    daily_dates = daily.get("time", [])
    daily_max = daily.get("temperature_2m_max", [])
    daily_min = daily.get("temperature_2m_min", [])

    if daily_dates and daily_max and daily_min:
        print("\n7-Day Daily Forecast (Min / Max)")
        print("-" * 55)
        print(f"{'Date':<15} {'Min (°C)':<15} {'Max (°C)':<15}")
        print("-" * 55)

        limit = 7 if len(daily_dates) >= 7 else len(daily_dates)

        for i in range(limit):
            date_str = daily_dates[i]

            min_val = float(daily_min[i]) if daily_min[i] is not None else None
            max_val = float(daily_max[i]) if daily_max[i] is not None else None

            min_str = f"{min_val:.1f}" if min_val is not None else "N/A"
            max_str = f"{max_val:.1f}" if max_val is not None else "N/A"

            print(f"{date_str:<15} {min_str:<15} {max_str:<15}")

        print("-" * 55)
    else:
        print("Daily forecast data not available.")