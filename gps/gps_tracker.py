import h3
from datetime import datetime

def log_pothole_detection(lat, lng, confidence):
    # Updated to H3 v4 syntax ('latlng_to_cell' with 'res=')
    h3_index = h3.latlng_to_cell(lat, lng, res=12)
    
    payload = {
        "timestamp": datetime.now().isoformat(),
        "latitude": lat,
        "longitude": lng,
        "h3_cluster_id": h3_index,
        "confidence": confidence,
        "status": "Logged - Pending Dispatch"
    }
    
    print("--- [NETRA EDGE TELEMETRY TRANSMITTED] ---")
    for key, value in payload.items():
        print(f"{key}: {value}")
    print("------------------------------------------")
    return payload

log_pothole_detection(28.4744, 77.5040, confidence=0.92)