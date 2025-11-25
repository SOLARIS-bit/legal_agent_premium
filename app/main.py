from flask import Flask, request, render_template, send_file
from .utils import extract_text_from_pdf, generate_letter, send_email
from .nlp_module import detect_infractions, classify_recours
from .db import Session, Dossier
from datetime import datetime
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""
    detected_motif = ""
    if request.method == "POST":
        pdf = request.files["pdf"]
        user_email = request.form.get("email")
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(pdf_path)

        extracted_text = extract_text_from_pdf(pdf_path)
        infractions = detect_infractions(extracted_text)
        detected_motif = classify_recours(extracted_text)

        # Sauvegarde dans SQLite
        session = Session()
        dossier = Dossier(nom="M. Dupont", date=datetime.utcnow(), motif=detected_motif)
        session.add(dossier)
        session.commit()
        session.close()

        # Génération PDF et envoi email
        data = {"nom": "M. Dupont", "date": datetime.today().strftime("%d/%m/%Y"), "motif": detected_motif}
        pdf_generated = generate_letter(data, country="FR")
        if user_email:
            send_email(
                subject="Votre document généré",
                body="Bonjour, veuillez trouver ci-joint le document généré.",
                to_email=user_email
            )

    return render_template("index.html", extracted_text=extracted_text, detected_motif=detected_motif, date=datetime.today().strftime("%d/%m/%Y"))

@app.route("/generate", methods=["POST"])
def generate():
    data = {
        "nom": request.form.get("nom", "M. Dupont"),
        "date": request.form.get("date", "24/11/2025"),
        "motif": request.form.get("motif", "Non spécifié")
    }
    pdf_path = generate_letter(data, country="FR")
    return send_file(pdf_path, as_attachment=True)

@app.route("/history")
def history():
    session = Session()
    dossiers = session.query(Dossier).all()
    session.close()
    return render_template("history.html", dossiers=dossiers)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)  # debug=True

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
