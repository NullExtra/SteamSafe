import json
import random
from datetime import datetime, timedelta, timezone

from status_logic import determine_water_status


# Zona waktu Indonesia bagian barat (WIB).
WIB = timezone(timedelta(hours=7))


def simulate_teg_data() -> dict:
    """
    Menghasilkan data dummy tegangan, arus, dan daya TEG.

    Nilai ini hanya untuk menguji software.
    Nilainya bukan hasil pengukuran TEG SP1848 secara nyata.
    """

    voltage = round(random.uniform(0.0, 1.5), 2)
    current = round(random.uniform(0.0, 20.0), 2)

    # V x mA menghasilkan daya dalam mW.
    power = round(voltage * current, 2)

    return {
        "teg_voltage_v": voltage,
        "teg_current_ma": current,
        "teg_power_mw": power
    }


def create_telemetry(water_state: str | None) -> dict:
    """
    Membentuk satu pesan telemetry sesuai data contract SteamSafe.
    """

    telemetry = {
        "device_id": "steamsafe-001",
        "timestamp": datetime.now(WIB).isoformat(timespec="seconds"),
        "water_state": water_state,
        "water_status": determine_water_status(water_state),
        "data_source": "SIMULATED"
    }

    # Menambahkan data TEG buatan.
    telemetry.update(simulate_teg_data())

    return telemetry


def main():
    print("================================")
    print(" SteamSafe Sensor Data Simulator")
    print("================================")
    print("Semua data di bawah ini adalah SIMULATED.")

    while True:
        print("\nPilih skenario:")
        print("1. Rain sensor kering (DRY)")
        print("2. Rain sensor basah (WET)")
        print("3. Pembacaan rain sensor tidak tersedia")
        print("4. Skenario acak")
        print("0. Keluar")

        choice = input("Masukkan pilihan: ").strip()

        if choice == "0":
            print("Simulator dihentikan.")
            break

        elif choice == "1":
            water_state = "DRY"

        elif choice == "2":
            water_state = "WET"

        elif choice == "3":
            water_state = None

        elif choice == "4":
            water_state = random.choice(["DRY", "WET", None])

        else:
            print("Pilihan tidak valid. Coba lagi.")
            continue

        # Membuat data sesuai kontrak.
        telemetry = create_telemetry(water_state)

        # Menampilkan hasil dalam format JSON.
        print("\nHasil simulasi:")
        print(
            json.dumps(
                telemetry,
                indent=2,
                ensure_ascii=False
            )
        )


if __name__ == "__main__":
    main()