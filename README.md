````markdown
# Algorithme Défenseur Premium

Assistant juridique numérique avec :
- Upload PDF et OCR (Tesseract français)
- Détection infractions & classification NLP (CamemBERT / Legal-BERT)
- Génération PDF Word professionnel
- Historique dossiers SQLite
- Notifications email automatiques
- Multi-juridictionnel (France par défaut)
- Docker ARM64 pour Chromebook / serveur

## Usage

### Local
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python -m app.main
````

### Docker

```bash
docker build -t legal_agent_premium .
docker run -p 5001:5001 legal_agent_premium
```

```

2. Crée un **.gitignore** pour Python / Docker :

```

**pycache**/
env/
*.pyc
*.pyo
*.pyd
*.db
uploads/
*.log
*.pdf
.env

````

---
