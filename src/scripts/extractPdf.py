import sys
import json
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LTChar

# Function to convert RGB to Hex
def rgb_to_hex(rgb):
    if isinstance(rgb, (list, tuple)) and len(rgb) == 3:
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    return "#000000" 

pdf_path = sys.argv[1] 

pdf_data = {}

for page_num, page in enumerate(extract_pages(pdf_path)):
    page_info = {
        "height": page.bbox[3],
        "width": page.bbox[2],
        "data": {}
    }

    text_index = 0
    for element in page:
        if isinstance(element, (LTTextBox, LTTextLine)):
            text = element.get_text().strip()
            if not text:
                continue

            font_size = None
            font_color = "#000000"  
            is_bold = False
            is_italic = False

            # Extract font details (color, size, style)
            for text_line in element:
                for char in text_line:
                    if isinstance(char, LTChar):
                        font_size = char.size
                        font_name = char.fontname.lower()
                        is_bold = "bold" in font_name
                        is_italic = "italic" in font_name
                        
                        # Extract color (if available)
                        if hasattr(char, "graphicstate") and char.graphicstate is not None:
                            if hasattr(char.graphicstate, 'ncolor'):
                                font_color = rgb_to_hex(char.graphicstate.ncolor)
                        
                        break  

            page_info["data"][str(text_index)] = {
                "text": text,
                "left": element.bbox[0],
                "top": element.bbox[1],
                "end_left": element.bbox[2],
                "end_top": element.bbox[3],
                "font_size": font_size or 12,
                "font_color": font_color, 
                "is_bold": is_bold,
                "is_italic": is_italic
            }
            text_index += 1

    pdf_data[str(page_num)] = page_info

print(json.dumps(pdf_data))  
