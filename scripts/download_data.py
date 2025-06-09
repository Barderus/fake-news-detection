import os
from dotenv import load_dotenv
import json
from pathlib import Path


load_dotenv()
API_KEY = os.getenv("KAGGLE_API_KEY")
USERNAME=os.getenv("KAGGLE_USERNAME")

# Create kaggle.json in the right place
kaggle_dir = Path.home() / ".kaggle"
kaggle_dir.mkdir(exist_ok=True)

with open(kaggle_dir / "kaggle.json", "w") as f:
    json.dump({"username": USERNAME, "key": API_KEY}, f)

# Set permissions (especially for Linux/macOS)
os.chmod(kaggle_dir / "kaggle.json", 0o600)

import subprocess
from pathlib import Path

def download_kaggle_dataset(dataset_name, base_dest=r"C:\Users\Owner\PycharmProjects\fake-news-detection\data\raw"):
    subfolder = dataset_name.split("/")[-1]
    full_path = Path(base_dest) / subfolder
    full_path.mkdir(parents=True, exist_ok=True)

    result = subprocess.run([
        "kaggle", "datasets", "download",
        "-d", dataset_name,
        "-p", str(full_path),
        "--unzip"
    ], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Downloaded and extracted: {dataset_name}")
    else:
        print(f"Error downloading {dataset_name}:\n{result.stderr}")



download_kaggle_dataset("algord/fake-news")
download_kaggle_dataset("saurabhshahane/fake-news-classification")
download_kaggle_dataset("bhavikjikadara/fake-news-detection")
download_kaggle_dataset("hassanamin/textdb3")
download_kaggle_dataset("mrisdal/fake-news")

