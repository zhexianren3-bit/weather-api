# Weather API

基于 Open-Meteo 的免费天气 API，可直接部署到 Render。

## 接口

- `GET /weather?latitude=39.9&longitude=116.4` - 获取当前天气
- `GET /forecast?latitude=39.9&longitude=116.4&days=7` - 获取预报

## 部署

```bash
pip install -r requirements.txt
python main.py
```

## 示例

```json
{
  "success": true,
  "location": {"lat": 39.9, "lon": 116.4},
  "current": {"temperature_2m": 20, "weather_code": 0}
}
```
