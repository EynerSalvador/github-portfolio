# run.py
import sys
from pathlib import Path

# Añade el directorio raíz al path de Python
sys.path.append(str(Path(__file__).parent))

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
