#!/usr/bin/env python3
"""
Weather API - 基于 Open-Meteo 的免费天气 API
可部署到 Render 变现
"""
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI(
    title="Weather API",
    description="基于 Open-Meteo 的免费天气 API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Weather API is running!",
        "docs": "/docs",
        "endpoints": ["/weather", "/forecast"]
    }

@app.get("/weather")
def get_weather(
    latitude: float = Query(39.9, description="纬度"),
    longitude: float = Query(116.4, description="经度")
):
    """获取当前天气"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,wind_speed_10m",
        "timezone": "auto"
    }
    
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        
        return {
            "success": True,
            "location": {"lat": latitude, "lon": longitude},
            "current": data.get("current", {}),
            "timezone": data.get("timezone")
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/forecast")
def get_forecast(
    latitude: float = Query(39.9, description="纬度"),
    longitude: float = Query(116.4, description="经度"),
    days: int = Query(7, ge=1, le=14, description="预报天数")
):
    """获取天气预报"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,weather_code,sunrise,sunset",
        "timezone": "auto",
        "forecast_days": days
    }
    
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()
        
        return {
            "success": True,
            "location": {"lat": latitude, "lon": longitude},
            "forecast": data.get("daily", {}),
            "timezone": data.get("timezone")
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
