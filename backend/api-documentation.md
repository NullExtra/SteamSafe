# API Documentation - SteamSafe Backend

Dokumentasi ini mencakup daftar endpoint yang tersedia pada layanan backend SteamSafe untuk menerima, memvalidasi, dan menyediakan data pemantauan boiler.

---

## 1. POST /api/telemetry
Digunakan oleh perangkat (atau simulator) untuk mengirimkan data pemantauan telemetri ke server.

* **URL:** `/api/telemetry`
* **Method:** `POST`
* **Content-Type:** `application/json`

### Contoh Request Body (JSON):
```json
{
  "timestamp": "2026-10-22T14:00:00+07:00",
  "water state": "DRY",
  "water status": "NORMAL",
  "teg_voltage_v": 1.2,
  "teg_current_ma": 25,
  "teg_power_mw": 30,
  "data source": "SIMULATED"
}
