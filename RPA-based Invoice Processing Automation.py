import os
import cv2
import pytesseract
import pandas as pd
import PyPDF2
import re
import smtplib
from email.mime.text import MIMEText
import uipath

# Set up Tesseract OCR path (Change this based on your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Extract text from image invoices using OCR
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Process extracted text to fetch invoice details
def extract_invoice_details(text):
    invoice_no = re.search(r'Invoice[\s:]*(\d+)', text)
    date = re.search(r'Date[\s:]*(\d{2}/\d{2}/\d{4})', text)
    total_amount = re.search(r'Total[\s:]*(\d+\.\d{2})', text)
    
    return {
        "Invoice Number": invoice_no.group(1) if invoice_no else "N/A",
        "Date": date.group(1) if date else "N/A",
        "Total Amount": total_amount.group(1) if total_amount else "N/A"
    }

# Save extracted data to CSV
def save_to_csv(data, filename="invoices.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, mode='a', header=not os.path.exists(filename))
    print(f"Data saved to {filename}")

# Send email notification
def send_email_notification(recipient, invoice_data):
    sender = "your-email@example.com"
    password = "your-email-password"
    subject = "New Invoice Processed"
    body = f"Invoice Processed: {invoice_data}"
    
    msg = MIMEText(body)
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", e)

# Integrate UiPath workflow
def execute_uipath_workflow(workflow_path):
    try:
        uipath.run_workflow(workflow_path)
        print("UiPath workflow executed successfully")
    except Exception as e:
        print("Error executing UiPath workflow:", e)

# Main execution
def process_invoice(file_path):
    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)
    
    invoice_details = extract_invoice_details(text)
    save_to_csv([invoice_details])
    send_email_notification("recipient@example.com", invoice_details)
    execute_uipath_workflow("path/to/uipath/workflow.xaml")

# Example usage
if __name__ == "__main__":
    process_invoice("sample_invoice.pdf")
