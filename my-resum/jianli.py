import streamlit as st
import os
import base64

st.set_page_config(page_title="刘清泉的简历", layout="wide", page_icon="🎮")

# ========== 照片路径 ==========
PHOTO_PATH = "my-resum/photo.jpg"

# ========== 自定义样式 ==========
st.markdown("""
<style>
    /* ===== 全局字体与变量 ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    :root {
        --primary: #1a1a2e;
        --accent: #e8b86d;
        --accent2: #4a90d9;
        --card-bg: #f8f9fb;
        --border: #e0e3e8;
        --text: #2c3e50;
        --text-light: #5a6c7d;
        --tag-ue: #1a3a5c;
        --tag-unity: #2d2d2d;
        --tag-python: #1e4a3a;
        --tag-cpp: #3d1f5c;
        --tag-art: #5c2d1a;
        --golden: #c8963e;
        --highlight-bg: #fffdf5;
    }

    /* ===== 页面背景 ===== */
    .stApp {
        background: linear-gradient(180deg, #fafbfc 0%, #f0f2f5 100%);
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px; /* 适度放宽，配合宽屏模式 */
    }

    /* ===== 左侧整体容器（sticky） ===== */
    .left-col {
        position: sticky;
        top: 2rem;
        height: fit-content;
    }

    /* ===== 左侧横幅（缩小版） ===== */
    .hero-banner-left {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 40%, #1a1a2e 100%);
        border-radius: 16px;
        padding: 1.5rem 1.2rem;
        margin-bottom: 1.2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(26, 26, 46, 0.25);
        position: relative;
        overflow: hidden;
    }
    .hero-banner-left::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 50%, rgba(232,184,109,0.08) 0%, transparent 60%),
                    radial-gradient(circle at 70% 30%, rgba(74,144,217,0.06) 0%, transparent 50%);
        pointer-events: none;
    }
    .hero-name-left {
        font-size: 1.8rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
    }
    .hero-title-left {
        display: inline-block;
        background: rgba(232,184,109,0.15);
        border: 1px solid rgba(232,184,109,0.35);
        color: #e8b86d;
        font-size: 0.8rem;
        font-weight: 500;
        padding: 0.35rem 1rem;
        border-radius: 30px;
        letter-spacing: 0.5px;
        position: relative;
        z-index: 1;
    }

    /* ===== 左侧照片（变大） ===== */
    .photo-container-left {
        width: 100%;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
        border: 3px solid #ffffff;
        background: #e8eaef;
        margin-bottom: 1.2rem;
    }
    .photo-container-left img {
        width: 100%;
        display: block;
        object-fit: cover;
    }

    /* ===== 左侧导航栏 ===== */
    .nav-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border: 1px solid #e8eaef;
    }
    .nav-card a {
        display: block;
        padding: 0.5rem 0.8rem;
        margin: 0.2rem 0;
        border-radius: 8px;
        color: #2c3e50;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: background 0.15s;
    }
    .nav-card a:hover {
        background: #f0f4f8;
        color: #1a1a2e;
    }

    /* ===== 分区标题（右侧主体） ===== */
    .section-title-custom {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid transparent;
        border-image: linear-gradient(90deg, #e8b86d 0%, #4a90d9 100%) 1;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .section-title-custom .icon {
        font-size: 1.3rem;
    }

    /* ===== 卡片容器 ===== */
    .info-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border: 1px solid #e8eaef;
        transition: box-shadow 0.2s;
    }
    .info-card:hover {
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }

    .highlight-card {
        background: #fffef9;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(200,150,62,0.08);
        border: 1px solid #f0e4c8;
        border-left: 4px solid #c8963e;
    }

    .portfolio-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border: 1px solid #e0e3e8;
        border-left: 4px solid #4a90d9;
        transition: all 0.2s;
    }
    .portfolio-card:hover {
        border-left-color: #e8b86d;
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    }
    .portfolio-card .p-title {
        font-weight: 600;
        color: #1a1a2e;
        font-size: 1rem;
    }
    .portfolio-card .p-desc {
        color: #5a6c7d;
        font-size: 0.9rem;
        margin-top: 0.3rem;
    }

    /* ===== 技能标签云 ===== */
    .skill-tags-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 0.8rem 0;
    }
    .skill-tag {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.3px;
        transition: transform 0.15s, box-shadow 0.15s;
        cursor: default;
    }
    .skill-tag:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .tag-ue { background: #1a3a5c; color: #e8f4ff; }
    .tag-unity { background: #2d2d2d; color: #e0e0e0; }
    .tag-python { background: #1e4a3a; color: #d4f5e8; }
    .tag-cpp { background: #3d1f5c; color: #f0e0ff; }
    .tag-art { background: #5c2d1a; color: #ffe8d8; }
    .tag-general { background: #3a4a5c; color: #e8f0f8; }
    .tag-core {
        background: linear-gradient(135deg, #c8963e, #e8b86d);
        color: #1a1a2e;
        font-weight: 700;
        font-size: 0.9rem;
        padding: 0.5rem 1.1rem;
        box-shadow: 0 3px 10px rgba(200,150,62,0.3);
    }

    /* ===== 输入框美化 ===== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 8px !important;
        border: 1px solid #dde0e5 !important;
        background: #fafbfc !important;
        transition: all 0.2s !important;
        font-size: 0.95rem !important;
        color: #2c3e50 !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #4a90d9 !important;
        box-shadow: 0 0 0 3px rgba(74,144,217,0.1) !important;
        background: #ffffff !important;
    }
    .stTextInput > label, .stTextArea > label {
        font-weight: 500 !important;
        color: #4a5568 !important;
        font-size: 0.85rem !important;
    }

    /* ===== 分割线 ===== */
    .divider-custom {
        height: 1px;
        background: linear-gradient(90deg, transparent, #c8cdd5, transparent);
        margin: 1.5rem 0;
        border: none;
    }

    /* ===== 概要信息条 ===== */
    .info-summary-bar {
        background: #f0f4f8;
        border-radius: 8px;
        padding: 0.7rem 1.2rem;
        font-size: 0.85rem;
        color: #4a5568;
        text-align: center;
        margin-top: 0.8rem;
        letter-spacing: 0.3px;
    }
    .info-summary-bar strong {
        color: #1a1a2e;
    }

    /* ===== 实践经历卡片 ===== */
    .exp-project-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border-left: 4px solid #4a90d9;
        transition: all 0.2s;
    }
    .exp-project-card:hover {
        border-left-color: #e8b86d;
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    }
    .exp-project-card .exp-title {
        font-weight: 600;
        color: #1a1a2e;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
    .exp-project-card .exp-meta {
        font-size: 0.85rem;
        color: #5a6c7d;
        margin-bottom: 0.8rem;
    }
    .exp-project-card .exp-desc {
        font-size: 0.9rem;
        color: #2c3e50;
        line-height: 1.6;
    }

    /* ===== 响应式调整 ===== */
    @media (max-width: 768px) {
        .hero-name-left {
            font-size: 1.4rem;
        }
        .hero-title-left {
            font-size: 0.7rem;
        }
        .main .block-container {
            padding-top: 1rem;
        }
        .left-col {
            position: static; /* 小屏幕取消吸顶 */
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# ========== 左右分栏布局（左侧更宽） ==========
# ============================================================
left_col, right_col = st.columns([1.2, 2.8], gap="large")

# ==================== 左侧区域（sticky容器） ====================
with left_col:
    st.markdown('<div class="left-col">', unsafe_allow_html=True)

    # 顶部横幅（缩小版）
    st.markdown("""
    <div class="hero-banner-left">
        <div class="hero-name-left">刘 清 泉</div>
        <div class="hero-title-left">🎯 UE蓝图开发工程师 · 技术美术</div>
    </div>
    """, unsafe_allow_html=True)

    # 照片（变大，占满宽度）
    if os.path.exists(PHOTO_PATH):
        with open(PHOTO_PATH, "rb") as img_file:
            img_bytes = img_file.read()
        img_b64 = base64.b64encode(img_bytes).decode()
        st.markdown(f'''
        <div class="photo-container-left">
            <img src="data:image/jpeg;base64,{img_b64}" alt="照片">
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="photo-placeholder-custom">📷<br>请上传照片<br><small>my-resum/photo.jpg</small></div>',
                    unsafe_allow_html=True)

    # 导航栏
    st.markdown("""
    <div class="nav-card">
        <a href="#basic-info">📋 基本信息</a>
        <a href="#intent">🎯 求职意向</a>
        <a href="#skills">🛠 专业技能</a>
        <a href="#portfolio">📁 作品集展示</a>
        <a href="#awards">🏆 荣誉奖项</a>
        <a href="#experience">💼 实践经历</a>
        <a href="#self-eval">💡 自我评价</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 右侧主体内容 ====================
with right_col:
    # 基本信息（含输入框）
    st.markdown('<div id="basic-info"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">📋</span> 基本信息</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        name_val = st.text_input("姓名", value="刘清泉", key="name")
        phone_val = st.text_input("电话", value="13550768834", key="phone")
        location_val = st.text_input("现居城市", value="宜宾", key="location")
    with col_b:
        job_title_val = st.text_input("求职意向", value="UE蓝图开发工程师 / 技术美术", key="job_title")
        email_val = st.text_input("邮箱", value="3341964836@qq.com", key="email")
        degree_val = st.text_input("学历", value="本科 · 数字媒体技术", key="degree_summary")

    st.markdown(f"""
    <div class="info-summary-bar">
        <strong>{name_val}</strong> ｜ 📞 {phone_val} ｜ ✉️ {email_val} ｜ 📍 {location_val} ｜ 🎓 {degree_val} ｜ 🎯 <strong>{job_title_val}</strong>
    </div>
    """, unsafe_allow_html=True)

    # 求职意向
    st.markdown('<div id="intent"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">🎯</span> 求职意向</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-card">
        <p style="margin:0; font-weight:500; color:#2c3e50;">核心意向：UE蓝图开发工程师、技术美术（游戏方向）</p>
        <p style="margin:0.5rem 0 0 0; color:#5a6c7d;">可接受岗位：游戏开发助理、Unity开发助理</p>
        <p style="margin-top:0.8rem; color:#2c3e50;">聚焦游戏研发环节，擅长通过技术与美术结合，优化游戏交互体验、实现蓝图逻辑与脚本开发，助力游戏项目落地。</p>
    </div>
    """, unsafe_allow_html=True)

    # 专业技能
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">🛠</span> 专业技能</div>', unsafe_allow_html=True)

    fixed_skills = """【游戏引擎操作】
Unreal Engine (UE) - 精通蓝图可视化编程
Unity引擎 - 场景搭建与交互开发
【编程语言】
Python - 辅助脚本、自动化测试
C++ - 游戏逻辑开发、引擎接口调用
【美术与技术结合】
场景建模、材质绘制、UI设计
美术资源优化、技术美术适配
【其他技能】
游戏开发全流程（需求分析→原型→调试上线）
逻辑思维与问题排查能力
团队协作与快速学习能力"""

    def generate_skill_tags(skills_text):
        lines = [l.strip() for l in skills_text.split('\n') if l.strip()]
        tags_html = []
        category_colors = {
            'ue': 'tag-ue', 'unreal': 'tag-ue', '虚幻': 'tag-ue',
            'unity': 'tag-unity',
            'python': 'tag-python', 'py': 'tag-python',
            'c++': 'tag-cpp', 'cpp': 'tag-cpp', 'c语言': 'tag-cpp',
            '美术': 'tag-art', '建模': 'tag-art', '材质': 'tag-art', 'ui': 'tag-art', '设计': 'tag-art',
        }
        core_keywords = ['蓝图', 'ue蓝图', '蓝图可视化', '技术美术', 'ue蓝图开发']

        for line in lines:
            if line.startswith('【') and line.endswith('】'):
                tags_html.append(
                    f'<div style="width:100%;margin-top:0.5rem;font-weight:700;color:#1a1a2e;font-size:0.9rem;">{line[1:-1]}</div>')
                continue
            clean_line = line.lstrip('-•·➤▸●○◆◇▪▫').strip()
            if not clean_line:
                continue
            if ' - ' in clean_line:
                parts = clean_line.split(' - ', 1)
                skill_name = parts[0].strip()
                skill_desc = parts[1].strip()
            elif '：' in clean_line:
                parts = clean_line.split('：', 1)
                skill_name = parts[0].strip()
                skill_desc = parts[1].strip()
            else:
                skill_name = clean_line
                skill_desc = ''
            color_class = 'tag-general'
            for kw, cls in category_colors.items():
                if kw.lower() in skill_name.lower():
                    color_class = cls
                    break
            is_core = any(core_kw in skill_name.lower() for core_kw in core_keywords)
            if is_core:
                color_class = 'tag-core'
            display_text = skill_name if len(skill_name) <= 18 else skill_name[:16] + '...'
            tags_html.append(f'<span class="skill-tag {color_class}" title="{skill_desc}">{display_text}</span>')
        return ''.join(tags_html)

    skills_display = generate_skill_tags(fixed_skills)
    st.markdown(f"""
    <div class="info-card">
        <p style="font-weight:600;color:#1a1a2e;margin-bottom:0.5rem;">🏷️ 技能标签云</p>
        <div class="skill-tags-container">
            {skills_display}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 作品集展示
    st.markdown('<div id="portfolio"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title-custom"><span class="icon">📁</span> 作品集展示 <span style="font-size:0.8rem;color:#c8963e;font-weight:500;">— 核心亮点</span></div>',
        unsafe_allow_html=True)

    portfolio_items = [
        ("UE蓝图交互项目", "独立完成的蓝图交互项目：角色控制、场景触发事件、UI交互逻辑，展示蓝图编程能力与逻辑搭建思路"),
        ("Unity游戏原型", "2D/3D小游戏原型开发：场景搭建、角色动画、基础交互逻辑，体现Unity引擎实操能力"),
        ("Python/C++辅助脚本", "游戏开发辅助脚本：资源批量导入、自动化测试、场景优化，附代码片段与功能说明"),
        ("场景建模与UI设计", "场景建模、材质绘制、UI设计作品，展示美术基础与技术美术双重能力")
    ]

    portfolio_cards_html = ""
    for title, desc in portfolio_items:
        portfolio_cards_html += f"""
        <div class="portfolio-card">
            <div class="p-title">🎮 {title}</div>
            <div class="p-desc">{desc}</div>
        </div>
        """

    st.markdown(portfolio_cards_html, unsafe_allow_html=True)

    portfolio_link = st.text_input("作品集链接（在线地址）", value="", key="portfolio_link",
                                   placeholder="如：站酷 / GitHub / 个人网站链接")
    if portfolio_link:
        st.markdown(f"""
        <div class="info-card" style="text-align:center;margin-top:0.5rem;">
            🔗 <strong>在线作品集：</strong><a href="{portfolio_link}" target="_blank" style="color:#4a90d9;">{portfolio_link}</a>
        </div>
        """, unsafe_allow_html=True)

    # 荣誉奖项
    st.markdown('<div id="awards"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">🏆</span> 荣誉奖项</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-card">
        <div style="padding:0.5rem 0; font-weight:500; color:#2c3e50;">🏅 蓝桥杯全国软件和信息技术专业人才大赛 二等奖（Python/C++方向）</div>
        <div style="padding:0.5rem 0; font-weight:500; color:#2c3e50;">📜 英语 CET-4</div>
    </div>
    """, unsafe_allow_html=True)

    # 实践经历
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title-custom"><span class="icon">💼</span> 实践经历 <span style="font-size:0.8rem;color:#888;font-weight:400;">— 个人项目 / 课程实践</span></div>',
        unsafe_allow_html=True)

    experiences = [
        {
            "title": "个人游戏开发项目（UE/Unity）",
            "meta": "独立开发 | 2024.06 - 2024.09",
            "desc": "独立完成一款2D/3D游戏原型，使用UE/Unity引擎搭建场景，编写蓝图逻辑与C++脚本，实现角色控制、交互效果与关卡设计。同时负责场景建模、材质绘制等美术资源制作，项目已形成完整演示视频与文档，收录于个人作品集。"
        },
        {
            "title": "课程设计：基于Unity的3D场景漫游系统",
            "meta": "团队项目（核心开发） | 2024.03 - 2024.06",
            "desc": "作为核心技术成员，负责Unity场景搭建、角色动画配置与交互逻辑开发。运用C#脚本实现场景切换、UI交互与物理效果，结合3Ds Max进行简单场景建模。项目获得校级优秀课程设计，体现了团队协作与全流程开发能力。"
        }
    ]

    for exp in experiences:
        st.markdown(f"""
        <div class="exp-project-card">
            <div class="exp-title">{exp['title']}</div>
            <div class="exp-meta">{exp['meta']}</div>
            <div class="exp-desc">{exp['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    # 自我评价
    st.markdown('<div id="self-eval"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">💡</span> 自我评价</div>', unsafe_allow_html=True)

    self_eval_text = (
        "数字媒体技术专业背景，聚焦游戏开发（UE蓝图、技术美术）方向，具备扎实的技术基础与清晰的职业规划。"
        "熟练掌握UE、Unity引擎操作，精通蓝图编程，具备Python、C++编程能力，且有蓝桥杯奖项佐证，"
        "能够将编程技能与游戏开发实际需求结合，编写辅助脚本、实现游戏逻辑。\n\n"
        "拥有完整的个人作品集，融合美术与代码能力，能够快速适配UE蓝图开发、技术美术岗位的工作需求；"
        "具备较强的学习能力、逻辑思维与问题解决能力，对待工作认真负责，善于主动探索新技术、新方法。\n\n"
        "渴望加入游戏研发团队，从基础岗位做起，将专业技能转化为实际工作价值，同时不断提升自身能力，助力项目发展。"
    )

    st.markdown(f"""
    <div class="info-card">
        <p style="color:#2c3e50; line-height:1.8;">{self_eval_text}</p>
    </div>
    """, unsafe_allow_html=True)

    # 页脚
    st.markdown("""
    <div class="divider-custom"></div>
    <div style="text-align:center;color:#aab4c0;font-size:0.8rem;padding:1rem 0;">
        📄 刘清泉的个人简历 · 感谢您花时间阅读 · 期待与您交流
    </div>
    """, unsafe_allow_html=True)