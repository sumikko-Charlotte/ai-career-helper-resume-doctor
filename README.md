# AI 职业助手 - 简历医生模块

## 📖 功能介绍

这是 AI 职业助手项目的简历医生模块，基于 Streamlit 构建，提供独立的简历诊断与优化服务：

- 📄 PDF 简历上传与解析
- 🔍 AI 智能简历诊断（评分 + 建议）
- ✍️ AI 简历优化生成
- 📊 详细的诊断报告
- 💡 循证修改建议

## 🚀 本地运行

### 前置要求

- Python >= 3.10

### 安装依赖

```bash
pip install -r requirements.txt
```

### 环境变量配置

创建 `.env` 文件（或在系统环境变量中设置）：

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 启动服务

```bash
streamlit run streamlit_app.py
```

访问地址：http://localhost:8501

## 📦 部署到 Streamlit Community Cloud

### 步骤一：准备代码

1. 确保所有文件已提交到 Git 仓库

2. 检查项目结构：
   - `streamlit_app.py` - 主应用文件
   - `requirements.txt` - Python 依赖
   - `.streamlit/config.toml` - Streamlit 配置（可选）

### 步骤二：创建 Streamlit Cloud 应用

1. 访问 [Streamlit Community Cloud](https://share.streamlit.io/)

2. 使用 GitHub 账号登录

3. 点击 "New app"

4. 配置应用：
   - **Repository**: 选择你的 GitHub 仓库
   - **Branch**: `main` 或 `master`
   - **Main file path**: `streamlit_app.py`
   - **App URL**: 自定义（如：`ai-career-resume-doctor`）

### 步骤三：配置环境变量

在 Streamlit Cloud 应用设置中添加：

- `DEEPSEEK_API_KEY`: 你的 DeepSeek API Key

### 步骤四：部署

点击 "Deploy"，Streamlit Cloud 会自动：

1. 克隆代码
2. 安装依赖
3. 启动应用

部署完成后，你会获得一个类似 `https://ai-career-resume-doctor.streamlit.app` 的 URL。

## 📁 项目结构

```
ai-career-helper-resume-doctor/
├── streamlit_app.py      # Streamlit 主应用
├── resume_parser.py      # PDF 解析模块
├── ai_advisor.py         # AI 服务模块
├── requirements.txt      # Python 依赖
├── .streamlit/           # Streamlit 配置目录
│   └── config.toml       # 配置文件
└── .env                  # 环境变量（不提交到 Git）
```

## 🔧 依赖说明

### 核心依赖

- `streamlit>=1.28.0` - Streamlit 框架
- `pypdf>=3.0.0` - PDF 解析库
- `openai>=1.0.0` - OpenAI API 客户端（用于 DeepSeek）
- `python-dotenv>=1.0.0` - 环境变量管理

## 🎯 功能说明

### 1. 简历上传

支持上传 PDF 格式的简历文件，系统会自动提取文本内容。

### 2. AI 诊断

- **评分**：0-100 分综合评分
- **评分理由**：详细说明评分依据
- **优势分析**：识别简历亮点
- **不足分析**：指出需要改进的地方
- **修改建议**：提供具体的优化建议（含证据定位）
- **岗位推荐**：基于简历内容推荐匹配岗位

### 3. 简历生成

根据诊断结果，AI 自动生成优化后的 Markdown 格式简历，可直接下载使用。

## 📝 注意事项

1. **API Key 安全**：不要将 API Key 提交到代码仓库，使用环境变量或 Streamlit Secrets

2. **文件大小限制**：Streamlit 默认限制上传文件大小为 200MB，PDF 文件建议控制在 10MB 以内

3. **PDF 格式**：目前仅支持文本型 PDF，扫描版 PDF 需要先进行 OCR 处理

4. **Streamlit Secrets**：在 Streamlit Cloud 中，可以使用 Secrets 功能管理敏感信息：
   - 在应用设置中点击 "Secrets"
   - 添加 `DEEPSEEK_API_KEY` 键值对
   - 代码中使用 `st.secrets["DEEPSEEK_API_KEY"]` 访问

## 🆘 常见问题

**Q: 上传 PDF 后无法解析？**  
A: 检查 PDF 是否为文本型（非扫描版），或尝试重新生成 PDF

**Q: AI 诊断失败？**  
A: 检查环境变量 `DEEPSEEK_API_KEY` 是否配置正确，以及 API 额度是否充足

**Q: 部署后页面无法访问？**  
A: 检查 Streamlit Cloud 日志，确认依赖安装是否成功

**Q: 如何本地测试？**  
A: 运行 `streamlit run streamlit_app.py`，确保 `.env` 文件存在且包含正确的 API Key

## 🔗 相关链接

- [Streamlit 文档](https://docs.streamlit.io/)
- [Streamlit Community Cloud](https://share.streamlit.io/)
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs/)

## 📄 许可证

本项目仅供学习使用。
