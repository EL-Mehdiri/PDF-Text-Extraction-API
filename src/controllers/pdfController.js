const { extractPdfData } = require("../services/pdfService");

const uploadPDF = async (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).json({ success: false, message: "No file uploaded" });
        }

        const filePath = req.file.path;
        const extractedData = await extractPdfData(filePath);
        res.json({ success: true, data: extractedData });

    } catch (error) {
        res.status(500).json({ success: false, message: "Error processing file", error });
    }
};

module.exports = { uploadPDF };
