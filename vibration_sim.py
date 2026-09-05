import json
import random
import time
import math

def calculate_rms(readings):
    return math.sqrt(sum([x**2 for x in readings]) / len(readings))

def advanced_telemetry_simulation():
    print("Initializing Advanced Tri-Axis IoT Telemetry Node...")
    time.sleep(1)
    
    # Simulated stream of (X_axis_sway, Y_axis_braking, Z_axis_vertical_jolt)
    stream_data = [
        (0.2, 0.1, 9.8),   # Normal smooth road
        (0.1, 0.0, 10.1),  # Normal road
        (0.3, 0.2, 16.5),  # Potential jolt
        (2.5, 4.1, 14.2),  # FALSE POSITIVE: Bus is braking/turning hard (High X/Y)
        (0.1, 0.0, 24.6),  # TRUE POTHOLE: Massive Z spike, stable X/Y
        (0.2, 0.1, 10.5)   # Normal road
    ]
    
    for i, (x_val, y_val, z_val) in enumerate(stream_data):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Check if motion is due to turning/braking (X or Y exceeds safe threshold)
        is_vehicle_maneuver = abs(x_val) > 1.5 or abs(y_val) > 2.0
        
        classification = "Normal Road Surface"
        severity_score = 1.0
        status = "Filtered / Logged"
        
        if is_vehicle_maneuver:
            classification = "Ignored (Vehicle Turn/Braking Artifact)"
            severity_score = 0.0
            status = "Discarded by Multi-Axis Verification"
        elif z_val > 20.0:
            classification = "Critical Structural Pothole"
            severity_score = round((z_val / 9.8) * 2.5, 2)
            status = "Verified & Queued for Command Desk"
        elif 13.0 <= z_val <= 19.9:
            classification = "Minor Speed Breaker"
            severity_score = round((z_val / 9.8) * 1.2, 2)
            status = "Classified (Non-Emergency)"

        payload = {
            "node_id": "IoT-Bus-Node-04",
            "timestamp": timestamp,
            "raw_imu": {"x": x_val, "y": y_val, "z": z_val},
            "classification": classification,
            "severity_index": severity_score,
            "verification_status": status
        }
        
        print(f"\n[Advanced Telemetry Packet #{i+1}]")
        print(json.dumps(payload, indent=2))
        time.sleep(1.5)

if __name__ == "__main__":
    advanced_telemetry_simulation()