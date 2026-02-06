import json
import os
import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# ==========================================
# 🛠️ 修复 1: 强制 Windows 输出 UTF-8 (解决报错核心)
# ==========================================
# 这一行是解决 'ascii' codec can't encode... 的关键
sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# 📂 配置路径与 Key (适配独立部署)
# ==========================================
# 1. 使用当前文件所在目录作为项目根目录
project_root = Path(__file__).parent
env_path = project_root / ".env"

# 2. 加载环境变量（优先从当前目录，其次从系统环境变量）
load_dotenv(dotenv_path=env_path, override=True)

# 3. 获取 API Key
api_key = os.getenv("DEEPSEEK_API_KEY")

# 4. 检查 Key
if not api_key:
    # 尝试找一下 .env.txt 这种常见错误
    if (project_root / ".env.txt").exists():
        print("⚠️ 警告: 发现了 .env.txt，请重命名为 .env")
    print(f"❌ [AI Advisor] 错误: 未找到 API Key，请检查环境变量 DEEPSEEK_API_KEY 或 {env_path}")
else:
    print(f"✅ [AI Advisor] API Key 加载成功")

# 5. 初始化 OpenAI Client
client = OpenAI(
    api_key=api_key, 
    base_url="https://api.deepseek.com" 
)

# ==========================================
# 🧹 工具函数
# ==========================================
def clean_ai_response(raw_response):
    """清洗 AI 返回的 Markdown 格式，提取纯 JSON"""
    if not raw_response:
        return ""
    clean_text = raw_response.replace("```json", "").replace("```", "")
    return clean_text.strip()

# ==========================================
# 🧠 核心功能 1: 简历诊断 (含评分理由)
# ==========================================
def analyze_resume(resume_text):
    """
    分析简历，返回包含 score_rationale 的完整 JSON
    """
    print("🚀 [AI Advisor] 正在调用 DeepSeek 进行深度诊断...")
    
    # 这个 Prompt 保留了你要求的所有字段
    system_prompt = """
    你是一位资深技术面试官。请分析简历并严格输出纯 JSON 格式。
    
    【核心要求】
    1. "score_rationale": 必须用一句话解释为什么给这个分数（这是核心功能，必填）。
    2. "suggestions": 提建议时，必须在 "evidence" 字段指出简历原文的问题。

    返回格式（纯JSON）：
    {
        "score": (0-100整数),
        "score_rationale": "评分依据",
        "summary": "综合点评",
        "pros": ["亮点1", "亮点2"],
        "cons": ["不足1", "不足2"],
        "suggestions": [
            {
                "advice": "修改建议",
                "evidence": "简历原文引用"
            }
        ],
        "matched_jobs": ["推荐岗位1", "推荐岗位2"]
    }
    """
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"这是我的简历内容：\n{resume_text}"}
            ],
            temperature=0.2,
            response_format={ "type": "json_object" } 
        )
        
        raw_result = response.choices[0].message.content
        clean_result = clean_ai_response(raw_result)
        
        # 解析 JSON
        return json.loads(clean_result)
            
    except Exception as e:
        # 使用 repr() 防止中文报错炸毁整个程序
        print(f"❌ 分析过程出错: {repr(e)}")
        return None

# ==========================================
# ✍️ 核心功能 2: 简历生成 (你的新功能)
# ==========================================
def generate_resume_markdown(prompt: str, temperature: float = 0.6) -> str:
    """
    生成/优化简历内容（返回 Markdown 文本）
    """
    print("✍️ [AI Advisor] 正在调用 DeepSeek 生成优化版简历...")
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是严谨的简历优化专家，请直接输出 Markdown 格式的简历内容，不要包含 ```markdown 标记。"},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ 生成过程出错: {repr(e)}")
        return f"AI 生成服务暂时不可用: {str(e)}"