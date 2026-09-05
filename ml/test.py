from pathlib import Path
from ultralytics import YOLO
import cv2

# This automatically finds best.pt right next to test.py, no matter where the terminal is
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / 'best.pt'

model = YOLO(str(model_path))
results = model(r'C:\Users\NANDINI BHARDWAJ\OneDrive\Desktop\NETRA\ml\dataset-roboflow\valid\images\images_002.jpg', show=True)

#print("Check the pop-up window! Press any key on your keyboard to close it.")
cv2.waitKey(0)
cv2.destroyAllWindows()