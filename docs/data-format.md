# SteamSafe Data Contract

## 1. Tujuan

Data contract menetapkan format data yang digunakan oleh
SteamSafe selama pengembangan software MVP.

Format ini menjadi acuan bersama untuk sensor simulator,
status monitoring, backend, dan dashboard.

## 2. Struktur Data

Setiap data telemetry menggunakan format JSON dengan field berikut.

| Field | Tipe Data | Keterangan |
|---|---|---|
| device_id | String | Identitas perangkat SteamSafe |
| timestamp | String | Waktu data dibuat dalam format ISO 8601 |
| water_state | String atau null | Kondisi rain sensor |
| water_status | String | Status hasil pengolahan sensor |
| teg_voltage_v | Number | Tegangan TEG dalam volt |
| teg_current_ma | Number | Arus TEG dalam miliampere |
| teg_power_mw | Number | Daya TEG dalam miliwatt |
| data_source | String | Sumber data yang digunakan |

## 3. Aturan Nilai

### water_state

- DRY: permukaan rain sensor terdeteksi kering.
- WET: permukaan rain sensor terdeteksi basah.
- null: pembacaan sensor tidak tersedia.

### water_status

- NORMAL: rain sensor terdeteksi kering.
- OVERFLOW_DETECTED: rain sensor terdeteksi basah.
- NO_DATA: pembacaan rain sensor tidak tersedia atau tidak valid.

### data_source

- SIMULATED: data dihasilkan oleh program simulasi.
- HARDWARE: data berasal dari perangkat fisik.

Selama Sprint 1, data yang digunakan adalah SIMULATED.

## 4. Aturan Timestamp

Timestamp menggunakan format ISO 8601 dan menyertakan zona waktu.
Contoh: 2026-10-22T14:00:00+07:00

## 5. Catatan Pengembangan

Nilai tegangan, arus, dan daya pada simulator merupakan data dummy,
bukan hasil pengukuran TEG secara fisik.

Rain sensor digunakan sebagai indikator kebasahan permukaan
untuk simulasi indikasi luapan. Sensor ini tidak mengukur
ketinggian air boiler secara langsung.