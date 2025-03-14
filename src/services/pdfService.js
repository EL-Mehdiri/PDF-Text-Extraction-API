const { execFile } = require("child_process");
const path = require("path");

const extractPdfData = (pdfPath) => {
    return new Promise((resolve, reject) => {
        const pythonScript = path.join(__dirname, "../scripts/extractPdf.py");

        execFile("python3", [pythonScript, pdfPath], (error, stdout, stderr) => {
            if (error) {
                reject(stderr || error);
            } else {
                try {
                    const jsonData = JSON.parse(stdout);
                    resolve(jsonData);
                } catch (parseError) {
                    reject("Error parsing JSON output");
                }
            }
        });
    });
};

module.exports = { extractPdfData };
