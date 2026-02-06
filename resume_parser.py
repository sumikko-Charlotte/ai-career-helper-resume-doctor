from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    
    # 遍历每一页提取文本
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
            
    return full_text

# --- 测试代码 ---
# 你可以在本地随便找个 PDF 简历试试
# text = extract_text_from_pdf("test_resume.pdf")
# print(text[:500]) # 打印前500个字看看