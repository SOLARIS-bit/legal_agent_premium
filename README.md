# **Algorithme Défenseur – Legal Agent Premium**

## **Description**

**Algorithme Défenseur** is a digital legal assistant that helps citizens manage their administrative procedures and disputes. It automatically detects infringements, suggests suitable remedies, generates official documents, and tracks the progress of the case.

This **premium** version includes: web interface, advanced legal NLP, professional PDF generation, email notifications, case history, and Dockerization for easy deployment.

---

## **Main Features**

1. **Document upload and extraction**

   * Supports PDF, DOCX, and images.
   * Advanced OCR with Tesseract for French text.

2. **Automated legal analysis**

   * NLP based on HuggingFace (CamemBERT / Legal-BERT).
   * Detection of infringements and classification of types of remedies.
   * Multi-jurisdictional (France by default, adaptable to other countries).

3. **Procedural drafting**

   * Automatic generation of letters and forms.
   * PDF export via `docx2pdf` or `WeasyPrint` for professional documents.

4. **Notifications and tracking**

   * Automatic emails via SMTP or SendGrid.
   * Alerts on legal deadlines.
   * Case history stored in SQLite / PostgreSQL.

5. **Web Interface**

   * Intuitive dashboard for uploading, tracking, and managing cases.
   * Real-time notifications and user feedback.

6. **Dockerization**

   * ARM64 container compatible with Chromebook and Linux servers.
   * Easy, isolated, and reproducible deployment.

7. **Security and auditability**

   * Human validation before sending documents.
   * Time stamping and complete logging of actions.

---

## **Installation**

### **1. Clone the repository**

```bash
git clone https://github.com/SOLARIS-bit/legal_agent_premium.git
cd legal_agent_premium
```

---
