def determine_water_status(water_state: str | None) -> str:
    """
    Menentukan status pemantauan air berdasarkan pembacaan rain sensor.

    DRY  -> NORMAL
    WET  -> OVERFLOW_DETECTED
    None atau nilai tidak valid -> NO_DATA

    Fungsi ini menggunakan data sensor yang disimulasikan maupun
    data perangkat, selama inputnya mengikuti format yang ditentukan.
    """

    # Tidak ada pembacaan sensor
    if water_state is None:
        return "NO_DATA"

    # Menyeragamkan huruf dan menghapus spasi
    state = water_state.strip().upper()

    # Permukaan sensor kering
    if state == "DRY":
        return "NORMAL"

    # Permukaan sensor basah
    if state == "WET":
        return "OVERFLOW_DETECTED"

    # Nilai yang tidak dikenali
    return "NO_DATA"