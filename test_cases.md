Test Cases for FireCast – Wildfire & Air Quality Monitor
Test Case 1: Location Search Functionality

Test Steps:

Open the application

Enter a valid location name (e.g., "Delhi") in the search bar

Click the search button

Expected: Map zooms to that location and displays wildfire, AQI, and smoke data

Status: ✅ PASS

Test Case 2: Wildfire Marker Display

Test Steps:

Search any valid city

Click the "Wildfires" button

Expected: Red wildfire markers appear on the map and nearest fires list updates

Status: ✅ PASS

Test Case 3: AQI Data Card Rendering

Test Steps:

Search a city

Observe the AQI panel

Expected: AQI value, category, and pollutant breakdown (PM2.5, PM10, CO, NO2, etc.) display correctly

Status: ✅ PASS

Test Case 4: Smoke Forecast Chart Loading

Test Steps:

Search a city

Scroll to “Smoke Forecast (72 hours)” chart

Expected: Bar chart loads with 72-hour smoke prediction values

Status: ✅ PASS

Test Case 5: PDF Report Generation

Test Steps:

Search any location

Click “Generate PDF Report” button

Expected: PDF downloads successfully with AQI, wildfire, smoke, ozone and population data

Status: ✅ PASS
