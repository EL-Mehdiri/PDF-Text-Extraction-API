const express = require("express");
const { uploadPDF } = require("../controllers/pdfController");
const { upload } = require("../middleware/multerMiddleware");

const router = express.Router();

router.post("/upload", upload.single("pdfFile"), uploadPDF);

module.exports = router;
