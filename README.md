# RPA-Based Invoice Processing Automation

This project automates invoice processing using Python and UiPath. It extracts data from PDF and image-based invoices, saves structured data into a CSV file, and sends email notifications. Additionally, UiPath is used for further automation workflows.

## Features
- ✅ Extracts text from PDF invoices using `PyPDF2`
- ✅ Uses `pytesseract` for OCR-based extraction from image invoices
- ✅ Extracts invoice details such as **Invoice Number, Date, and Total Amount**
- ✅ Saves extracted data into a **CSV file**
- ✅ Sends email notifications upon invoice processing
- ✅ **Integrates UiPath** for advanced automation workflows

## Technologies Used
- Python 🐍
- `PyPDF2` for PDF text extraction
- `pytesseract` and `OpenCV` for OCR processing
- `pandas` for data handling
- `smtplib` for email notifications
- `UiPath` for RPA automation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rpa-invoice-processing.git
   cd rpa-invoice-processing
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python pytesseract pandas PyPDF2
   ```

3. Set up `Tesseract OCR` (if not installed already):
   - Download and install from: [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - Update the path in the script if necessary.

4. Update email credentials in `send_email_notification()`.
5. Specify the correct **UiPath workflow path** inside `execute_uipath_workflow()`.

## Usage

Run the script with an invoice file:
```bash
python invoice_processing.py sample_invoice.pdf
```

The extracted invoice details will be saved to `invoices.csv`, and an email notification will be sent.

## UiPath Integration
Ensure your UiPath workflow (`.xaml` file) is correctly referenced in the script. You can modify the path in:
```python
execute_uipath_workflow("path/to/uipath/workflow.xaml")
```

## Future Enhancements 🚀
- ✅ Store invoice data in a **database** (PostgreSQL/MySQL)
- ✅ Implement **GUI** for better usability
- ✅ Add **multi-file processing** capability

## License
This project is licensed under the MIT License.


