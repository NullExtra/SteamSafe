CREATE TABLE IF NOT EXISTS sensor_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp VARCHAR(50) NOT NULL,
    water_state VARCHAR(20) NOT NULL,
    water_status VARCHAR(50) NOT NULL,
    teg_voltage_v FLOAT NOT NULL,
    teg_current_ma FLOAT NOT NULL,
    teg_power_mw FLOAT NOT NULL,
    data_source VARCHAR(20) NOT NULL
);
