---

# **Algorithme Défenseur – Legal Agent Premium**

## **Description**

**Algorithme Défenseur** is a digital legal assistant for citizens.
It allows you to **automatically detect administrative offences or rights violations**, **generate official appeals**, and **track the progress of cases**.

This includes:

* Modern Flask web interface
* Multi-document PDF upload and processing
* French OCR via **Tesseract**
* Legal NLP with **CamemBERT / Legal-BERT**
* Automatic classification of appeal types
* Professional PDF/Word generation
* File history in SQLite or PostgreSQL
* Automatic email notifications
* Multi-jurisdictional (adapted to France, extensible)
* ARM64 Dockerisation for Chromebook or server

---

## **Main features**

1. **PDF upload & extraction**

   * Text extraction from PDFs or scanned images
   * Multilingual OCR (French priority)

2. **Automated legal analysis**

   * Detection of infringements or administrative errors
   * Classification of the type of appeal (litigation, mediation, informal appeal, etc.)

3. **Automatic document drafting**

   * Letters, forms, notifications compliant with administrative standards
   * PDF/Word generation via `docx2pdf` or `WeasyPrint`

4. **Case history**

   * Saving cases in **SQLite** or **PostgreSQL**
   * Consultation and monitoring via interface

5. **Notifications & Monitoring**

   * Automatic emails (via `smtplib` or SendGrid)
   * Alerts for legal deadlines
   * Feedback on case progress

6. **Multi-jurisdictional**

   * Adaptation of NLP templates and forms according to country
   * Current version optimised for France

7. **ARM64 Dockerisation**

   * Lightweight container for Chromebook Linux or ARM64 server
   * Isolated and reproducible environment

---

## **Installation**

### Prerequisites

* Python 3.11+
* Tesseract OCR with French language support:

```bash
sudo apt install tesseract-ocr tesseract-ocr-fra -y
```

* Virtualenv recommended

### Installation locale

```bash
git clone https://github.com/SOLARIS-bit/legal_agent_premium.git
cd legal_agent_premium
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Configuration

* Définir la variable pour Tesseract :

```bash
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/
```

* Configuration SMTP pour notifications (optionnel) :

```python
EMAIL_USER = "votre.email@example.com"
EMAIL_PASSWORD = "votre_mot_de_passe"
```

---

## **Lancer l’application**

```bash
export FLASK_APP=app.main
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5001
```

* Accéder à l’interface : `http://localhost:5001`
* Upload PDF → extraction → analyse → génération de document

---

## **Docker**

### Build

```bash
docker build -t legal_agent_premium:latest .
```

### Run

```bash
docker run -d -p 5001:5001 legal_agent_premium:latest
```

* Compatible **ARM64** (Chromebook / Raspberry Pi / serveur ARM)

---

## **Structure du projet**

```
legal_agent_premium/
├─ app/
│  ├─ main.py           # Flask app principale
│  ├─ utils.py          # Fonctions utilitaires (PDF, lettres)
│  ├─ nlp_module.py     # NLP CamemBERT / Legal-BERT
│  ├─ templates/        # Templates HTML
│  ├─ static/           # CSS, JS
│  └─ db.py             # Gestion de l’historique des dossiers
├─ Dockerfile
├─ requirements.txt
├─ README.md
└─ .gitignore
```

---

## **Example of use**

1. The user uploads a PDF or scanned document.
2. The agent reads the document via OCR.
3. The agent detects infringements and suggests the type of remedy.
4. The official document is generated in PDF format and sent by email if configured.
5. The file is saved for future follow-up.

---

## **Future improvements**

* Fine-tuning of the legal NLP model for better predictions
* Multi-country and multi-jurisdiction support
* Advanced dashboard to view history and statistics
* React or Vue interface for a more modern UX

---
