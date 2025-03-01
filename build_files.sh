echo "BUILD START"

# Check Python version
python3.9 --version

# Upgrade pip and ensure it’s installed
python3.9 -m pip install --upgrade pip
python3.9 -m ensurepip 

# Install dependencies from requirements.txt
python3.9 -m pip install --no-cache-dir -r requirements.txt




echo "BUILD END"