import streamlit as st
import os
import base64

st.set_page_config(page_title="刘清泉的简历", layout="wide")

# ========== 照片路径 ==========
PHOTO_PATH = "photo.jpg"

# ========== 自定义样式 ==========
st.markdown("""
<style>
/* 全局基础设置 */
html, body {
    color-scheme: light only !important;
    background-color: #fafbfc !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    letter-spacing: 0.3px;
}

/* 平滑滚动 + 锚点偏移 */
html {
    scroll-behavior: smooth !important;
    scroll-padding-top: 60px !important;
}

/* 隐藏原生控件：顶部栏、右上角菜单、部署按钮 */
[data-testid="stHeader"], 
[data-testid="stToolbar"],
.stDeployButton, .stSidebarCollapseButton {
    display: none !important;
}

:root, [data-theme="dark"], [data-theme="light"] {
    color-scheme: light !important;
    --background-color: #fafbfc !important;
    --text-color: #2c3e50 !important;
}

/* 加载动画 */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
.stApp {
    animation: fadeIn 0.6s ease-out;
    background: linear-gradient(180deg, #fafbfc 0%, #f0f2f5 100%);
}

/* 全局间距标准化 */
.block-container {
    padding: 2rem 1.5rem 3rem 1.5rem !important;
    max-width: 1200px;
}

/* 板块分割装饰线 */
.section-divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #c8cdd8, transparent);
    margin: 2rem 0;
}

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
    --section-gap: 2rem;
    --card-gap: 1.2rem;
}

/* ===== 左侧整体容器（sticky） ===== */
.left-col {
    position: sticky;
    top: 2rem;
    height: fit-content;
}

/* ===== 左侧横幅 ===== */
.hero-banner-left {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 40%, #1a1a2e 100%);
    border-radius: 16px;
    padding: 1.5rem 1.2rem;
    margin-bottom: var(--card-gap);
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
    text-shadow: 0 2px 8px rgba(0,0,0,0.2);
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

/* ===== 左侧照片容器 ===== */
.photo-container-left {
    width: 100%;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    border: 3px solid #ffffff;
    background: #e8eaef;
    margin-bottom: var(--card-gap);
    text-align: center;
    transition: transform 0.25s ease;
}
.photo-container-left:hover {
    transform: translateY(-3px);
}
.photo-container-left img {
    width: 50% !important;
    height: auto !important;
    object-fit: contain !important;
    margin: 0 auto !important;
    display: block !important;
    border-radius: 8px;
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

/* ===== 分区标题 ===== */
.section-title-custom {
    font-size: 1.25rem;
    font-weight: 700;
    color: #1a1a2e;
    margin: 0 0 1rem 0;
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
    margin-bottom: var(--card-gap);
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    border: 1px solid #e8eaef;
    transition: all 0.25s ease;
}
.info-card:hover {
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transform: translateY(-2px);
}

.highlight-card {
    background: #fffef9;
    border-radius: 12px;
    padding: 1.5rem 1.8rem;
    margin-bottom: var(--card-gap);
    box-shadow: 0 2px 12px rgba(200,150,62,0.08);
    border: 1px solid #f0e4c8;
    border-left: 4px solid #c8963e;
    line-height: 1.7;
    letter-spacing: 0.4px;
}

.portfolio-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    border: 1px solid #e0e3e8;
    border-left: 4px solid #4a90d9;
    transition: all 0.25s ease;
    line-height: 1.65;
    letter-spacing: 0.3px;
}
.portfolio-card:hover {
    border-left-color: #e8b86d;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    transform: translateY(-2px);
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

/* 静态信息展示 */
.static-info-row {
    background: #fafbfc;
    border-radius: 8px;
    padding: 0.5rem 0;
    margin-bottom: 0.25rem;
    font-size: 0.95rem;
    color: #2c3e50;
}
.static-info-label {
    font-weight: 600;
    color: #1a1a2e;
    margin-right: 0.5rem;
}

/* 概要信息条 */
.info-summary-bar {
    background: #f0f4f8;
    border-radius: 8px;
    padding: 0.7rem 1.2rem;
    font-size: 0.85rem;
    color: #4a5568;
    text-align: center;
    margin: 1rem 0 var(--section-gap) 0;
    letter-spacing: 0.3px;
}
.info-summary-bar strong {
    color: #1a1a2e;
}

/* 实践经历卡片 */
.exp-project-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.5rem 1.8rem;
    margin-bottom: var(--card-gap);
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    border-left: 4px solid #4a90d9;
    transition: all 0.25s ease;
    line-height: 1.75;
    letter-spacing: 0.4px;
}
.exp-project-card:hover {
    border-left-color: #e8b86d;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    transform: translateY(-2px);
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
    line-height: 1.75;
    letter-spacing: 0.4px;
}

/* 自我评价文本优化行高字间距 */
.eval-text {
    line-height: 1.9 !important;
    letter-spacing: 0.4px !important;
    color: #2c3e50;
}

/* 作品集静态链接卡片 */
.portfolio-link-card {
    text-align:center;
    padding:1rem;
    margin-top:1rem;
    background:#f8f9fb;
    border-radius:10px;
    border:1px solid #e8eaef;
}

/* 响应式调整 */
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
        position: static;
    }
    .photo-container-left img {
        width: 70% !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# ========== 左右分栏布局 ==========
# ============================================================
left_col, right_col = st.columns([1.2, 2.8], gap="large")

# ==================== 左侧区域 ====================
with left_col:
    st.markdown('<div class="left-col">', unsafe_allow_html=True)

    # 顶部横幅
    st.markdown("""
    <div class="hero-banner-left">
        <div class="hero-name-left">刘 清 泉</div>
        <div class="hero-title-left">🎯 UE蓝图开发工程师 · 技术美术</div>
    </div>
    """, unsafe_allow_html=True)

    # 照片
    if os.path.exists(PHOTO_PATH):
        with open(PHOTO_PATH, "rb") as img_file:
            img_bytes = img_file.read()
        img_b64 = base64.b64encode(img_bytes).decode()
        st.markdown(f'''
        <div class="photo-container-left">
            <img src="data:image/jpeg;base64,{img_b64}" alt="刘清泉照片">
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('<div class="photo-container-left" style="padding:1rem; text-align:center; color:#7f8c8d;">📷<br>暂无照片<br><small>请放置 photo.jpg</small></div>',
                    unsafe_allow_html=True)

    # 导航栏
    st.markdown("""
    <div class="nav-card">
        <a style="font-size: 1.4rem; font-weight: bold;">简历导航栏(点击跳转)</a>
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
    # 基本信息
    st.markdown('<div id="basic-info"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">📋</span> 基本信息</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="static-info-row"><span class="static-info-label">姓名：</span>刘清泉</div>', unsafe_allow_html=True)
        st.markdown('<div class="static-info-row"><span class="static-info-label">电话：</span>13550768834</div>', unsafe_allow_html=True)
        st.markdown('<div class="static-info-row"><span class="static-info-label">现居城市：</span>宜宾</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="static-info-row"><span class="static-info-label">求职意向：</span>UE蓝图开发工程师 / 技术美术</div>', unsafe_allow_html=True)
        st.markdown('<div class="static-info-row"><span class="static-info-label">邮箱：</span>3341964836@qq.com</div>', unsafe_allow_html=True)
        st.markdown('<div class="static-info-row"><span class="static-info-label">学历：</span>本科 · 数字媒体技术</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-summary-bar">
        <strong>刘清泉</strong> ｜ 📞 13550768834 ｜ ✉️ 3341964836@qq.com ｜ 📍 宜宾 ｜ 🎓 本科 · 数字媒体技术 ｜ 🎯 <strong>UE蓝图开发工程师 / 技术美术</strong>
    </div>
    """, unsafe_allow_html=True)

    # 分割线
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

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

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

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

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

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

    # 已改为静态展示，移除输入框
    st.markdown("""
    <div class="portfolio-link-card">
        🔗 作品集可提供：站酷 / GitHub / 个人演示视频链接，面试可现场展示项目源码与演示效果
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # 荣誉奖项
    st.markdown('<div id="awards"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title-custom"><span class="icon">🏆</span> 荣誉奖项</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-card">
        <div style="padding:0.5rem 0; font-weight:500; color:#2c3e50;">🏅 蓝桥杯全国软件和信息技术专业人才大赛 二等奖（C++方向）</div>
        <div style="padding:0.5rem 0; font-weight:500; color:#2c3e50;">📜 英语 CET-4</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

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

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

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
        <p class="eval-text">{self_eval_text}</p>
    </div>
    """, unsafe_allow_html=True)

    # 页脚
    st.markdown("""
    <div style="text-align:center;color:#aab4c0;font-size:0.8rem;padding:1rem 0;margin-top:2rem;">
        📄 刘清泉的个人简历 · 感谢您花时间阅读 · 期待与您交流
    </div>
    """, unsafe_allow_html=True)