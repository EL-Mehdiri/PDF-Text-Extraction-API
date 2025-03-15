# PDF Text Extraction API

## Overview

This project provides a **REST API** to extract structured text from PDF files, including:

- **Text Content**
- **Font Size**
- **Font Color (HEX)**
- **Bold & Italic Styles**
- **Text Position (X, Y, Width, Height)**
- **Page Dimensions**

The API processes PDFs using **Node.js (Express.js)** and calls a **Python script** (`pdfminer.six`) to extract detailed font information.

---

## Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-repo/pdf-extractor-api.git
cd pdf-extractor-api
```

### 2️⃣ Install Node.js Dependencies

```sh
npm install
```

### 3️⃣ Set Up Python Environment

Ensure you have Python 3 installed. Then create a virtual environment and install dependencies:

```sh
python3 -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Linux/macOS)
venv\Scripts\activate  # Activate (Windows)
pip install -r requirements.txt  # Install dependencies
```

### 4️⃣ Start the API Server

```sh
node src/app.js
```

---

## API Usage

### **Upload a PDF for Extraction**

**Endpoint:** `POST /api/pdf/upload`

#### **Example Request (cURL)**

```sh
curl -X POST -F "pdfFile=@sample.pdf" http://localhost:5100/api/pdf/upload
```

#### **Example Response**

```json
{
  "success": true,
  "data": {
    "0": {
      "height": 841.89,
      "width": 595.276,
      "data": {
        "1": {
          "text": "Retirement Plan",
          "left": 50,
          "top": 700,
          "end_left": 250,
          "end_top": 730,
          "font_size": 14,
          "font_color": "#000000",
          "is_bold": true,
          "is_italic": false
        }
      }
    }
  }
}
```

---

## **Project Structure**

```
pdf-extractor-api/
├── src/
│   ├── controllers/
│   │   ├── pdfController.js
│   ├── services/
│   │   ├── pdfService.js
│   ├── routes/
│   │   ├── pdfRoutes.js
│   ├── middleware/
│   │   ├── multerMiddleware.js
│   ├── scripts/
│   │   ├── extractPdf.py
│   ├── app.js
├── uploads/
├── package.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## **Environment Variables**

Create a `.env` file in the project root:

```ini
PORT=5100
```

---

## **Deployment**

### **Run with Nodemon (for Development)**

```sh
npm install -g nodemon
nodemon src/app.js
```

### **Run as a Production Service**

```sh
node src/app.js &
```

---

## **Troubleshooting**

**Error: Cannot find module 'dotenv'**

```sh
npm install dotenv
```

**Error: Python script not found**
Ensure `extractPdf.py` is in `src/scripts/` and `requirements.txt` is installed.

```sh
pip install -r requirements.txt
```

**Error: Module 'pdfminer.six' not found**

```sh
pip install pdfminer.six
```

---

## **License**

This project is licensed under the MIT License.
