# SteamSafe — Sprint 1 Software MVP

SteamSafe merupakan rancangan sistem pemantauan untuk mendukung
pengawasan kondisi pada penggunaan setrika uap laundry kiloan.

Pada Sprint 1, data sensor masih disimulasikan karena hardware
belum tersedia dan belum dilakukan pengukuran fisik.

## User Stories

- US-01: Menentukan format data telemetry bersama.
- US-02: Membuat simulator data sensor.
- US-05: Menentukan status monitoring dari pembacaan sensor.

## Struktur Proyek

- docs/data-format.md: dokumentasi data contract.
- data/sample-data.json: contoh payload telemetry.
- src/sensor_simulator.py: simulator data sensor.
- src/status_logic.py: logika penentuan status.
- tests/test_status_logic.py: pengujian logika status.

## Menjalankan Simulator

```bash
python src/sensor_simulator.py