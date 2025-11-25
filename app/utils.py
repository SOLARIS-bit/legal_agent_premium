import pytesseract
from pdf2image import convert_from_path
from docxtpl import DocxTemplate
from docx2pdf import convert
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img, lang='fra') + "\n"
    return text

def generate_letter(data, country="FR", docx_path="lettre_generée.docx", pdf_path="lettre_generée.pdf"):
    template_path = f"app/templates/{country}/lettre_template.docx"
    doc = DocxTemplate(template_path)
    doc.render(data)
    doc.save(docx_path)
    convert(docx_path, pdf_path)
    return pdf_path

def send_email(subject, body, to_email, from_email="ton_email@example.com", smtp_server="smtp.gmail.com", smtp_port=587, password="TON_MDP"):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()
