# Dashboard Bureau

Dashboard mural élégant et minimaliste, développé avec Streamlit,
destiné à tourner en continu sur un écran vertical connecté à un
Raspberry Pi 5.

## Stack technique

- Python 3
- Streamlit
- Raspberry Pi OS Desktop (Raspberry Pi 5)

## Installation

```bash
git clone <url-du-depot> Dashboard-Bureau
cd Dashboard-Bureau
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lancement

```bash
source venv/bin/activate
streamlit run app.py
```

L'application s'ouvre sur `http://localhost:8501`.

## Structure du projet
