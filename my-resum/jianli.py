import streamlit as st
import os

st.set_page_config(page_title="刘清泉的简历", layout="centered")

# ========== 照片设置 ==========
PHOTO_PATH = "photo.jpg"   # 把你的照片放在同目录，改名与此一致即可

# ========== 轻量自定义样式 ==========
st.markdown("""
<style>
    .resume-header {
        font-size: 2.2rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
    }
    .resume-subheader {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .section-title {
        font-size: 1.2rem;
        font-weight: 600;
        border-bottom: 2px solid #333;
        padding-bottom: 0.2rem;
        margin-top: 1.8rem;
        margin-bottom: 0.8rem;
    }
    .item-date {
        font-weight: 500;
        color: #444;
    }
    hr {
        margin: 1rem 0;
    }
    .photo-placeholder {
        width: 150px;
        height: 180px;
        background: #eee;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        color: #999;
        font-size: 0.9rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("📄 刘清泉的简历")
st.caption("")

# ========== 基本信息（含照片） ==========
st.subheader("📝 基本信息")
col_photo, col_info = st.columns([1, 3], gap="medium")

with col_photo:
    # 通过添加空行使照片下移
    st.markdown("<br><br>", unsafe_allow_html=True)
    if os.path.exists(PHOTO_PATH):
        st.image(PHOTO_PATH, width=150)
    else:
        st.markdown('<div class="photo-placeholder">', unsafe_allow_html=True)

with col_info:
    name = st.text_input("姓名", value="刘清泉")
    title = st.text_input("意向职位", value="xxxxx")
    phone = st.text_input("电话", value="13550768834")
    email = st.text_input("邮箱", value="3341964836@qq.com")
    location = st.text_input("现居城市", value="宜宾")

# ========== 教育背景 ==========
st.subheader("🎓 教育背景")
edu_school = st.text_input("毕业学校", value="成都理工大学")
edu_degree = st.text_input("学位/专业", value="数字媒体技术 本科")
edu_year = st.text_input("起止时间", value="2023.09 - 2027.06")

# ========== 工作经历 ==========
st.subheader("💼 工作经历")
st.caption("多条用 | 分隔")
exp_company = st.text_input("公司/组织", value="")
exp_role = st.text_input("职位", value="")
exp_duration = st.text_input("时间", value="")
exp_desc = st.text_area("工作描述", value="")

# ========== 技能 ==========
st.subheader("🛠 技能")
skills = st.text_area("技能列表（一行一项）", value="UE游戏制作\nunity游戏制作\n游戏建模\n")

# ========== 语言 / 证书 ==========
st.subheader("🌐 语言 / 证书")
languages = st.text_area("语言与证书", value="英语 CET-4\n蓝桥杯省二等奖")

# ========== 作品集 ==========
st.subheader("📁 作品集")
portfolio = st.text_area("作品链接（一行一个）", value="", placeholder="")