# """
# Ishaan Dawra — Personal Portfolio
# Run: streamlit run portfolio_app.py
# """

# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px
# import re
# from datetime import datetime

# # ─────────────────────────────────────────────────────────────────────────────
# # PAGE CONFIG
# # ─────────────────────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="Ishaan Dawra · Data Scientist",
#     page_icon="🔷",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ─────────────────────────────────────────────────────────────────────────────
# # SESSION STATE — contact form submissions
# # ─────────────────────────────────────────────────────────────────────────────
# if "submissions" not in st.session_state:
#     st.session_state.submissions = []
# if "form_sent" not in st.session_state:
#     st.session_state.form_sent = False

# # ─────────────────────────────────────────────────────────────────────────────
# # GLOBAL CSS — Apple-inspired design system
# # ─────────────────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# /* ── FONTS & BASE ── */
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

# html, body, [class*="css"], .stApp {
#   font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
#   background: #ffffff;
#   color: #1d1d1f;
#   -webkit-font-smoothing: antialiased;
# }

# /* ── HIDE STREAMLIT CHROME ── */
# header[data-testid="stHeader"]          { display: none !important; }
# .stDeployButton                          { display: none !important; }
# footer                                   { display: none !important; }
# #MainMenu                                { display: none !important; }
# .block-container {
#   padding: 0 !important;
#   max-width: 100% !important;
# }
# section[data-testid="stSidebar"]        { display: none !important; }

# /* ── TOKENS ── */
# :root {
#   --ink:        #1d1d1f;
#   --ink-muted:  #6e6e73;
#   --ink-faint:  #aeaeb2;
#   --bg:         #ffffff;
#   --bg-alt:     #f5f5f7;
#   --border:     #d2d2d7;
#   --accent:     #0066cc;
#   --accent-lt:  #e8f0fb;
#   --radius-sm:  12px;
#   --radius-md:  18px;
#   --radius-lg:  24px;
#   --shadow-sm:  0 2px 8px rgba(0,0,0,.06);
#   --shadow-md:  0 8px 32px rgba(0,0,0,.10);
#   --shadow-lg:  0 20px 60px rgba(0,0,0,.14);
# }

# /* ── NAVBAR ── */
# .navbar {
#   position: sticky; top: 0; z-index: 9999;
#   backdrop-filter: saturate(180%) blur(24px);
#   -webkit-backdrop-filter: saturate(180%) blur(24px);
#   background: rgba(255,255,255,0.88);
#   border-bottom: 1px solid rgba(0,0,0,.09);
#   display: flex; align-items: center; justify-content: space-between;
#   padding: 0 48px; height: 56px;
# }
# .nav-brand {
#   display: flex; align-items: center; gap: 10px;
#   text-decoration: none;
# }
# .nav-logo-mark {
#   width: 32px; height: 32px;
#   background: var(--ink);
#   border-radius: 8px;
#   display: flex; align-items: center; justify-content: center;
#   font-size: 13px; font-weight: 800; color: #fff;
#   letter-spacing: -1px;
#   flex-shrink: 0;
# }
# .nav-brand-name {
#   font-size: 15px; font-weight: 600; color: var(--ink); letter-spacing: -.3px;
# }
# .nav-links { display: flex; gap: 28px; list-style: none; }
# .nav-links a {
#   font-size: 14px; font-weight: 400; color: var(--ink);
#   text-decoration: none; opacity: .75; transition: opacity .18s;
# }
# .nav-links a:hover { opacity: 1; }
# .nav-cta {
#   background: var(--ink) !important; color: #fff !important;
#   border-radius: 980px !important; padding: 7px 18px !important;
#   font-size: 13px !important; font-weight: 500 !important; opacity: 1 !important;
# }

# /* ── HERO ── */
# .hero-wrap {
#   background: linear-gradient(160deg, #eef3ff 0%, #f5f5f7 55%, #ffffff 100%);
#   padding: 96px 48px 88px;
#   display: flex; flex-direction: column; align-items: center; text-align: center;
# }
# .hero-avatar-ring {
#   width: 128px; height: 128px; border-radius: 50%;
#   background: linear-gradient(135deg, #1d1d1f 0%, #4a4a4f 100%);
#   display: flex; align-items: center; justify-content: center;
#   font-size: 68px; margin-bottom: 28px;
#   box-shadow: var(--shadow-md);
# }
# .hero-eyebrow {
#   font-size: 12px; font-weight: 600; letter-spacing: 2.5px;
#   text-transform: uppercase; color: var(--accent); margin-bottom: 14px;
# }
# .hero-name {
#   font-size: 68px; font-weight: 800; letter-spacing: -2.5px; line-height: 1.0;
#   color: var(--ink); margin-bottom: 14px;
# }
# .hero-role {
#   font-size: 22px; font-weight: 300; color: var(--ink-muted);
#   margin-bottom: 20px; letter-spacing: -.3px;
# }
# .hero-tagline {
#   font-size: 17px; font-weight: 400; color: var(--ink-muted);
#   max-width: 560px; line-height: 1.65; margin-bottom: 36px;
# }
# .hero-badges { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-bottom: 40px; }
# .badge {
#   background: rgba(255,255,255,.92); border: 1px solid var(--border);
#   border-radius: 980px; padding: 6px 16px;
#   font-size: 13px; font-weight: 500; color: var(--ink);
# }
# .hero-cta-row { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
# .btn-primary {
#   background: var(--ink); color: #fff;
#   border-radius: 980px; padding: 12px 28px;
#   font-size: 15px; font-weight: 500; text-decoration: none;
#   transition: box-shadow .2s, transform .15s; display: inline-block;
# }
# .btn-primary:hover { box-shadow: var(--shadow-md); transform: translateY(-1px); }
# .btn-secondary {
#   background: transparent; color: var(--ink);
#   border: 1px solid var(--border); border-radius: 980px; padding: 12px 28px;
#   font-size: 15px; font-weight: 500; text-decoration: none;
#   display: inline-block; transition: border-color .2s;
# }
# .btn-secondary:hover { border-color: var(--ink); }

# /* ── STAT STRIP ── */
# .stat-strip {
#   background: var(--ink); color: #fff;
#   display: flex; justify-content: center; flex-wrap: wrap;
# }
# .stat-item {
#   flex: 1; min-width: 150px; max-width: 220px;
#   padding: 30px 20px; text-align: center;
#   border-right: 1px solid rgba(255,255,255,.12);
# }
# .stat-item:last-child { border-right: none; }
# .stat-num  { font-size: 34px; font-weight: 700; letter-spacing: -1px; color: #fff; }
# .stat-desc { font-size: 13px; font-weight: 400; color: rgba(255,255,255,.5); margin-top: 4px; }

# /* ── SECTION LAYOUT ── */
# .section { max-width: 1080px; margin: 0 auto; padding: 80px 48px; }
# .section-eyebrow {
#   font-size: 12px; font-weight: 600; letter-spacing: 2.5px;
#   text-transform: uppercase; color: var(--accent); margin-bottom: 10px;
# }
# .section-heading {
#   font-size: 44px; font-weight: 700; letter-spacing: -1.5px;
#   color: var(--ink); line-height: 1.1; margin-bottom: 12px;
# }
# .section-sub {
#   font-size: 18px; font-weight: 400; color: var(--ink-muted);
#   line-height: 1.6; max-width: 600px; margin-bottom: 0;
# }
# .divider { border: none; border-top: 1px solid var(--border); margin: 0; }

# /* ── ABOUT ── */
# .about-body {
#   font-size: 16px; font-weight: 400; color: var(--ink-muted);
#   line-height: 1.8; margin-bottom: 20px;
# }
# .about-body strong { color: var(--ink); font-weight: 600; }

# /* ── EDU TABLE ── */
# .edu-table { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 16px; overflow: hidden; border: 1px solid var(--border); }
# .edu-table thead tr { background: var(--ink); }
# .edu-table thead th { padding: 12px 18px; font-size: 11px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(255,255,255,.7); text-align: left; }
# .edu-table tbody tr { background: var(--bg); border-bottom: 1px solid var(--bg-alt); transition: background .15s; }
# .edu-table tbody tr:last-child { border-bottom: none; }
# .edu-table tbody tr:hover { background: var(--bg-alt); }
# .edu-table td { padding: 16px 18px; font-size: 14px; color: var(--ink-muted); vertical-align: top; }
# .edu-table td:first-child { font-weight: 600; color: var(--ink); }
# .edu-year { display: inline-block; background: var(--accent-lt); color: var(--accent); border-radius: 980px; padding: 2px 10px; font-size: 12px; font-weight: 600; }

# /* ── EXPERIENCE CARDS ── */
# .exp-card {
#   background: var(--bg); border: 1px solid var(--border);
#   border-radius: var(--radius-lg); padding: 32px 36px;
#   margin-bottom: 20px;
#   transition: box-shadow .2s;
# }
# .exp-card:hover { box-shadow: var(--shadow-md); }
# .exp-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 4px; }
# .exp-company { font-size: 20px; font-weight: 700; color: var(--ink); }
# .exp-dates   { font-size: 13px; font-weight: 500; color: var(--ink-muted); background: var(--bg-alt); border-radius: 980px; padding: 4px 12px; white-space: nowrap; }
# .exp-role    { font-size: 15px; font-weight: 500; color: var(--accent); margin-bottom: 3px; }
# .exp-loc     { font-size: 13px; color: var(--ink-faint); margin-bottom: 18px; }
# .exp-bullets { list-style: none; padding: 0; }
# .exp-bullets li {
#   font-size: 14px; color: var(--ink-muted); line-height: 1.65;
#   padding: 5px 0 5px 22px; position: relative;
# }
# .exp-bullets li::before {
#   content: '→'; position: absolute; left: 0;
#   color: var(--accent); font-weight: 600;
# }

# /* ── PROJECT CARDS ── */
# .proj-card {
#   background: var(--bg); border: 1px solid var(--border);
#   border-radius: var(--radius-lg); overflow: hidden;
#   transition: transform .22s, box-shadow .22s;
#   display: flex; flex-direction: column; height: 100%;
# }
# .proj-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-lg); }
# .proj-thumb {
#   width: 100%; aspect-ratio: 16/9;
#   display: flex; align-items: center; justify-content: center;
#   font-size: 56px;
# }
# .proj-body { padding: 22px 26px 26px; flex: 1; display: flex; flex-direction: column; }
# .proj-metric {
#   display: inline-block;
#   background: var(--accent-lt); color: var(--accent);
#   border-radius: 980px; padding: 3px 12px;
#   font-size: 11px; font-weight: 600; letter-spacing: .3px;
#   margin-bottom: 10px;
# }
# .proj-tag {
#   font-size: 11px; font-weight: 600; letter-spacing: 1.8px;
#   text-transform: uppercase; color: var(--ink-muted); margin-bottom: 8px;
# }
# .proj-title { font-size: 18px; font-weight: 700; color: var(--ink); margin-bottom: 10px; letter-spacing: -.3px; }
# .proj-desc  { font-size: 13px; color: var(--ink-muted); line-height: 1.65; margin-bottom: 16px; flex: 1; }
# .proj-pills { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 18px; }
# .pill {
#   background: var(--bg-alt); border: 1px solid var(--border);
#   border-radius: var(--radius-sm); padding: 3px 9px;
#   font-size: 11px; font-weight: 500; color: var(--ink);
# }
# .proj-links { display: flex; gap: 8px; margin-top: auto; }
# .proj-link {
#   font-size: 13px; font-weight: 500; color: var(--ink);
#   text-decoration: none; border: 1px solid var(--border);
#   border-radius: 980px; padding: 6px 16px;
#   transition: background .18s, border-color .18s;
# }
# .proj-link:hover { background: var(--bg-alt); border-color: var(--ink); }
# .proj-link-fill {
#   background: var(--ink); color: #fff !important; border-color: var(--ink) !important;
# }
# .proj-link-fill:hover { background: #333 !important; }

# /* ── CONTACT ── */
# .contact-info h3 { font-size: 24px; font-weight: 700; color: var(--ink); margin-bottom: 14px; }
# .contact-info p  { font-size: 16px; color: var(--ink-muted); line-height: 1.65; margin-bottom: 28px; }
# .contact-detail { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }
# .contact-detail-icon { font-size: 20px; }
# .contact-detail-text { font-size: 15px; color: var(--ink); font-weight: 500; }
# .contact-detail-text a { color: var(--accent); text-decoration: none; }
# .contact-detail-text a:hover { text-decoration: underline; }
# .form-success {
#   background: #ecfdf5; border: 1px solid #6ee7b7;
#   border-radius: var(--radius-md); padding: 18px 22px;
#   font-size: 15px; color: #065f46; font-weight: 500; margin-top: 12px;
# }
# .form-error {
#   background: #fef2f2; border: 1px solid #fca5a5;
#   border-radius: var(--radius-sm); padding: 9px 14px;
#   font-size: 13px; color: #991b1b; margin-bottom: 6px;
# }

# /* ── FOOTER ── */
# .footer {
#   background: var(--ink); color: rgba(255,255,255,.5);
#   padding: 28px 48px; font-size: 13px;
# }
# .footer-inner {
#   display: flex; justify-content: space-between; align-items: center;
#   max-width: 1080px; margin: 0 auto;
# }
# .footer a { color: rgba(255,255,255,.7); text-decoration: none; }
# .footer a:hover { color: #fff; }

# /* ── STREAMLIT WIDGET TWEAKS ── */
# .stSelectbox label, .stSlider label, .stTextInput label, .stTextArea label,
# .stMultiSelect label, .stRadio label {
#   font-size: 13px !important; font-weight: 600 !important;
#   color: var(--ink) !important; letter-spacing: .2px !important;
# }
# div[data-testid="stSelectbox"] > div > div {
#   border-radius: var(--radius-sm) !important; border-color: var(--border) !important;
# }
# .stTextInput input, .stTextArea textarea {
#   border-radius: var(--radius-sm) !important;
#   border-color: var(--border) !important;
#   font-family: inherit !important; font-size: 14px !important;
# }
# .stButton > button {
#   background: var(--ink) !important; color: #fff !important;
#   border: none !important; border-radius: 980px !important;
#   font-size: 15px !important; font-weight: 500 !important;
#   padding: 10px 28px !important; font-family: inherit !important;
# }
# .stButton > button:hover { background: #333 !important; }
# </style>
# """, unsafe_allow_html=True)


# # ─────────────────────────────────────────────────────────────────────────────
# # DATA
# # ─────────────────────────────────────────────────────────────────────────────
# PROJECTS = [
#     {
#         "tag":    "Machine Learning · Finance",
#         "title":  "Client Dormancy Risk Model",
#         "desc":   "Risk-based predictive ML model identifying client segments at-risk of dormancy. Covers 23% of revenue built on 24 months of multi-source transaction & behavioural data across 340K+ active clients.",
#         "tech":   ["Python", "XGBoost", "SQL", "Tableau", "Pandas"],
#         "color":  "#e8f0fb", "emoji": "🏦", "metric": "23% revenue covered",
#         "github": None, "live": None, "wip": True,
#     },
#     {
#         "tag":    "Healthcare · Process Mining",
#         "title":  "Emergency Department Optimisation",
#         "desc":   "Dual gradient boosting classifiers (AUC ~0.85) on 90K+ ED event logs to predict admission and walkout risk. Streamlit deployment captures 53% of walkouts in the top decile.",
#         "tech":   ["Scikit-learn", "Causal Inference", "Plotly", "Streamlit"],
#         "color":  "#fdf2f8", "emoji": "🏥", "metric": "AUC ~0.85",
#         "github": "https://github.com/2002-ishaan/Healthcare_Process-Optimisation", "live": None, "wip": False,
#     },
#     {
#         "tag":    "Public Safety · Geospatial",
#         "title":  "Toronto Police Risk Platform",
#         "desc":   "Crime-risk dashboard across 316K+ incidents at 73 TTC stations for the 2026 FIFA World Cup. Generated ranked risk profiles for 15 priority stations. Finalist (Top 5) in TPS Case Competition.",
#         "tech":   ["GeoPandas", "Streamlit", "NumPy", "Anomaly Detection"],
#         "color":  "#f0fdf4", "emoji": "🗺️", "metric": "316K+ incidents",
#         "github": "https://github.com/2002-ishaan/Toronto_Police-Case_Competition", "live": None, "wip": False,
#     },
#     {
#         "tag":    "Time Series · EV · ML",
#         "title":  "SmartCharge",
#         "desc":   "Time series ML model on 22K+ EV charging sessions to forecast energy demand for proactive grid management. LightGBM with Meteostat weather data improved R² from 0.14 to 0.415 and reduced MAE by 31.6%.",
#         "tech":   ["Python", "Scikit-learn", "LightGBM", "Seaborn", "Feature Engineering"],
#         "color":  "#f0f9ff", "emoji": "⚡", "metric": "MAE ↓ 31.6%",
#         "github": "https://github.com/2002-ishaan", "live": None, "wip": False,
#     },
#     {
#         "tag":    "GenAI · Recommendation · AWS",
#         "title":  "GoVacay",
#         "desc":   "Hybrid recommendation system combining content-based filtering with LLM-generated synthetic user profiles via OpenRouter API. Reduced inference time by 67%, filtered 80% of irrelevant results. Deployed on AWS Bedrock.",
#         "tech":   ["Python", "NumPy", "GenAI", "AWS Bedrock", "API Integration"],
#         "color":  "#fefce8", "emoji": "✈️", "metric": "67% faster inference",
#         "github": "https://github.com/2002-ishaan", "live": None, "wip": False,
#     },
#     {
#         "tag":    "Statistics · Airline Analytics",
#         "title":  "SkyMetrics",
#         "desc":   "Analysed 6 years of airline operational data comparing Air Canada vs WestJet. Found Air Canada consumed 12% more fuel per passenger-km despite similar load factors (~83%). Created AWS QuickSight dashboard.",
#         "tech":   ["Python", "Statistics", "Pandas", "Matplotlib", "AWS QuickSight"],
#         "color":  "#fff1f2", "emoji": "📊", "metric": "6 yrs of data",
#         "github": "https://github.com/2002-ishaan", "live": None, "wip": False,
#     },
# ]

# SKILLS_DB = {
#     "Programming & Data Engineering": {
#         "Python (Pandas / NumPy)": 95, "SQL": 90, "R": 75,
#         "Apache Airflow": 70, "AWS S3": 72, "Git / GitHub": 85, "Data Wrangling": 88,
#     },
#     "Machine Learning & Analytics": {
#         "Gradient Boosting (XGB/LGBM)": 90, "Supervised Learning": 92,
#         "Unsupervised Learning": 80, "NLP": 78, "Causal Inference": 75,
#         "A/B Testing": 82, "Anomaly Detection": 78,
#     },
#     "Visualisation & Deployment": {
#         "Tableau": 88, "Streamlit": 85, "Plotly": 80,
#         "Matplotlib / Seaborn": 85, "Geospatial Mapping": 72,
#     },
# }

# EXPERIENCES = [
#     {
#         "company":  "Meridian Credit Union",
#         "role":     "Data Scientist Co-op",
#         "dates":    "Jan 2026 – Present",
#         "location": "Toronto, ON, Canada",
#         "bullets":  [
#             "Engineered a risk-based predictive ML model identifying client segments at-risk of dormancy, covering 23% of revenue across 340K+ active clients.",
#             "Architected a scalable Python / SQL pipeline compressing 8M+ records into 1.4M half-year snapshots — 6× faster segmentation & retention analysis.",
#             "Designed and deployed an interactive Tableau dashboard prioritising high-value and at-risk client segments for the marketing team.",
#             "Presented complex analytical findings to executive leadership and an audience of 100+, translating models into actionable business strategy.",
#         ],
#         "tech": ["Python", "SQL", "XGBoost", "Tableau", "AWS S3", "Pandas"],
#     },
#     {
#         "company":  "Genpact",
#         "role":     "Data Scientist Co-op",
#         "dates":    "Feb 2024 – Aug 2024",
#         "location": "Karnataka, India",
#         "bullets":  [
#             "Built a churn prediction model (72% recall) with automated APIs and AWS S3 ingestion via Apache Airflow, enabling production-ready churn monitoring.",
#             "Analysed A/B test results and 3.9K+ customer reviews using NLP to identify key churn drivers and inform targeted retention strategies.",
#         ],
#         "tech": ["Python", "NLP", "Apache Airflow", "AWS S3", "A/B Testing"],
#     },
# ]


# # ─────────────────────────────────────────────────────────────────────────────
# # HELPERS
# # ─────────────────────────────────────────────────────────────────────────────
# def pills_html(tech_list, cls="pill"):
#     return "".join(f'<span class="{cls}">{t}</span>' for t in tech_list)

# def is_valid_email(email):
#     return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


# # =============================================================================
# # ① NAVBAR
# # =============================================================================
# st.markdown("""
# <div class="navbar">
#   <a class="nav-brand" href="#">
#     <div class="nav-logo-mark">ID</div>
#     <span class="nav-brand-name">Ishaan Dawra</span>
#   </a>
#   <nav>
#     <ul class="nav-links">
#       <li><a href="#about">About</a></li>
#       <li><a href="#skills">Skills</a></li>
#       <li><a href="#experience">Experience</a></li>
#       <li><a href="#projects">Projects</a></li>
#       <li><a href="#contact" class="nav-cta">Contact</a></li>
#     </ul>
#   </nav>
# </div>
# """, unsafe_allow_html=True)


# # =============================================================================
# # ② HERO
# # =============================================================================
# st.markdown("""
# <div class="hero-wrap">
#   <div class="hero-avatar-ring">👨🏽‍💻</div>
#   <div class="hero-eyebrow">Data Scientist &nbsp;·&nbsp; MMA Candidate &nbsp;·&nbsp; University of Toronto</div>
#   <h1 class="hero-name">Ishaan Dawra</h1>
#   <p class="hero-role">Turning raw data into decisions that matter.</p>
#   <p class="hero-tagline">
#     I enjoy solving problems where understanding the question matters as much as finding the answer.
#     Asking the right question matters just as much as building the model.
#     Data problems are just like my favourite game Lego, where thousands of pieces come together to form a clear outcome.
#   </p>
#   <div class="hero-badges">
#     <span class="badge">🐍 Python</span>
#     <span class="badge">🤖 Machine Learning</span>
#     <span class="badge">📊 Analytics</span>
#     <span class="badge">☁️ AWS Certified</span>
#     <span class="badge">🗺️ Geospatial</span>
#     <span class="badge">🔬 NLP</span>
#   </div>
#   <div class="hero-cta-row">
#     <a class="btn-primary" href="#projects">View Projects ↓</a>
#     <a class="btn-secondary" href="#contact">Get in Touch</a>
#   </div>
# </div>
# """, unsafe_allow_html=True)


# # =============================================================================
# # ③ STAT STRIP
# # =============================================================================
# st.markdown("""
# <div class="stat-strip">
#   <div class="stat-item"><div class="stat-num">2</div><div class="stat-desc">Co-op internships completed</div></div>
#   <div class="stat-item"><div class="stat-num">6+</div><div class="stat-desc">End-to-end projects built</div></div>
#   <div class="stat-item"><div class="stat-num">2×</div><div class="stat-desc">Case competition top-2 finish</div></div>
#   <div class="stat-item"><div class="stat-num">2</div><div class="stat-desc">AWS certifications (2025)</div></div>
#   <div class="stat-item"><div class="stat-num">5+</div><div class="stat-desc">Years building with Python & ML</div></div>
# </div>
# """, unsafe_allow_html=True)


# # =============================================================================
# # ④ ABOUT
# # =============================================================================
# st.markdown('<a id="about"></a>', unsafe_allow_html=True)
# st.markdown('<div style="background:#ffffff"><div class="section">', unsafe_allow_html=True)
# st.markdown('<div class="section-eyebrow">About Me</div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Background</div>', unsafe_allow_html=True)

# c1, c2 = st.columns([1, 1], gap="large")
# with c1:
#     st.markdown("""
#     <p class="about-body">
#       I am a <strong>Data Scientist</strong> with hands-on co-op experience at
#       <strong>Meridian Credit Union</strong> and <strong>Genpact</strong>, currently completing a
#       <strong>Master of Management Analytics</strong> at Rotman School of Management,
#       University of Toronto (2026).
#     </p>
#     <p class="about-body">
#       My expertise spans <strong>predictive modelling, NLP, causal inference,
#       A/B testing, and large-scale data engineering</strong>. I am equally comfortable
#       designing XGBoost pipelines, writing production SQL, and presenting findings
#       to a C-suite audience.
#     </p>
#     <p class="about-body">
#       I hold a <strong>B.E. in Computer &amp; Electronics Engineering</strong> from
#       Thapar Institute of Engineering &amp; Technology (2024), and dual AWS certifications:
#       Cloud Practitioner and AI Practitioner — both 2025.
#     </p>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown("""
#     <table class="edu-table">
#       <thead>
#         <tr>
#           <th>Degree</th>
#           <th>Institution</th>
#           <th>Year</th>
#         </tr>
#       </thead>
#       <tbody>
#         <tr>
#           <td>Master of Management Analytics</td>
#           <td>Rotman School of Management<br><span style="font-size:12px;color:var(--ink-faint)">University of Toronto</span></td>
#           <td><span class="edu-year">2026</span></td>
#         </tr>
#         <tr>
#           <td>B.E. Computer &amp; Electronics Engineering</td>
#           <td>Thapar Institute of Engineering &amp; Technology<br><span style="font-size:12px;color:var(--ink-faint)">Punjab, India</span></td>
#           <td><span class="edu-year">2024</span></td>
#         </tr>
#       </tbody>
#     </table>
#     """, unsafe_allow_html=True)

# st.markdown("</div></div>", unsafe_allow_html=True)


# # =============================================================================
# # ⑤ SKILLS — widgets 1, 2, 3
# # =============================================================================
# st.markdown('<hr class="divider"><div style="background:#f5f5f7"><div class="section">', unsafe_allow_html=True)
# st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
# st.markdown('<div class="section-eyebrow">Technical Skills</div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">What I work with.</div>', unsafe_allow_html=True)

# ctrl_col, chart_col = st.columns([1, 2], gap="large")

# with ctrl_col:
#     # Widget 1 — category selectbox
#     category = st.selectbox(
#         "Skill category",
#         list(SKILLS_DB.keys()),
#         key="skill_cat",
#     )
#     # Widget 2 — proficiency slider
#     min_prof = st.slider("Minimum proficiency (%)", 0, 100, 0, 5, key="min_prof")
#     # Widget 3 — chart style radio
#     chart_type = st.radio(
#         "Chart style",
#         ["Horizontal bars", "Radar chart"],
#         key="chart_type",
#         horizontal=True,
#     )

# with chart_col:
#     chosen = {k: v for k, v in SKILLS_DB[category].items() if v >= min_prof}
#     if chosen:
#         if chart_type == "Horizontal bars":
#             sorted_items = dict(sorted(chosen.items(), key=lambda x: x[1]))
#             fig = go.Figure(go.Bar(
#                 x=list(sorted_items.values()),
#                 y=list(sorted_items.keys()),
#                 orientation="h",
#                 marker=dict(
#                     color=list(sorted_items.values()),
#                     colorscale=[[0, "#d2d2d7"], [0.5, "#6e6e73"], [1, "#1d1d1f"]],
#                     line=dict(width=0),
#                 ),
#                 text=[f"{v}%" for v in sorted_items.values()],
#                 textposition="outside",
#                 cliponaxis=False,
#             ))
#             fig.update_layout(
#                 paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
#                 margin=dict(l=0, r=60, t=10, b=10),
#                 height=max(280, len(chosen) * 50),
#                 xaxis=dict(range=[0, 115], showgrid=False, visible=False),
#                 yaxis=dict(tickfont=dict(size=13, family="Inter"), automargin=True),
#                 font=dict(family="Inter"),
#             )
#         else:
#             cats  = list(chosen.keys())
#             vals  = list(chosen.values())
#             cats += [cats[0]]; vals += [vals[0]]
#             fig = go.Figure(go.Scatterpolar(
#                 r=vals, theta=cats, fill="toself",
#                 fillcolor="rgba(0,102,204,0.12)",
#                 line=dict(color="#0066cc", width=2),
#                 marker=dict(size=6, color="#0066cc"),
#             ))
#             fig.update_layout(
#                 paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
#                 polar=dict(
#                     radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=10)),
#                     angularaxis=dict(tickfont=dict(size=11, family="Inter")),
#                 ),
#                 margin=dict(l=30, r=30, t=30, b=30),
#                 height=380, font=dict(family="Inter"),
#             )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.info("No skills match that threshold.")

# st.markdown("</div></div>", unsafe_allow_html=True)


# # =============================================================================
# # ⑥ EXPERIENCE
# # =============================================================================
# st.markdown('<hr class="divider"><div style="background:#ffffff"><div class="section">', unsafe_allow_html=True)
# st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
# st.markdown('<div class="section-eyebrow">Professional Experience</div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Where I\'ve worked.</div>', unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)

# for exp in EXPERIENCES:
#     bullets_li = "".join(f"<li>{b}</li>" for b in exp["bullets"])
#     st.markdown(f"""
#     <div class="exp-card">
#       <div class="exp-header">
#         <div>
#           <div class="exp-company">{exp['company']}</div>
#           <div class="exp-role">{exp['role']}</div>
#           <div class="exp-loc">📍 {exp['location']}</div>
#         </div>
#         <div class="exp-dates">{exp['dates']}</div>
#       </div>
#       <ul class="exp-bullets">{bullets_li}</ul>
#       <div style="margin-top:16px;display:flex;flex-wrap:wrap;gap:6px">{pills_html(exp['tech'])}</div>
#     </div>
#     """, unsafe_allow_html=True)

# # Timeline chart
# st.markdown("<br>", unsafe_allow_html=True)
# timeline_df = pd.DataFrame([
#     dict(Task="Meridian Credit Union", Start="2026-01-01", Finish="2026-09-01", Type="Industry"),
#     dict(Task="Genpact",               Start="2024-02-01", Finish="2024-08-01", Type="Industry"),
#     dict(Task="MMA @ Rotman",          Start="2025-09-01", Finish="2026-08-01", Type="Education"),
#     dict(Task="B.E. @ Thapar",         Start="2020-08-01", Finish="2024-06-01", Type="Education"),
# ])
# fig_tl = px.timeline(
#     timeline_df, x_start="Start", x_end="Finish", y="Task", color="Type",
#     color_discrete_map={"Industry": "#1d1d1f", "Education": "#6e6e73"},
#     title="Career & Education Timeline",
# )
# fig_tl.update_yaxes(autorange="reversed")
# fig_tl.update_layout(
#     paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
#     margin=dict(l=0, r=0, t=36, b=0), height=200,
#     font=dict(family="Inter", size=13),
#     legend=dict(orientation="h", y=-0.4),
#     title_font=dict(size=15, family="Inter"),
#     xaxis=dict(showgrid=False), yaxis=dict(showgrid=False),
# )
# st.plotly_chart(fig_tl, use_container_width=True)
# st.markdown("</div></div>", unsafe_allow_html=True)


# # Certifications
# st.markdown('<hr class="divider"><div style="background:#f5f5f7"><div class="section">', unsafe_allow_html=True)
# st.markdown('<div class="section-eyebrow">Certifications</div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Credentials.</div>', unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)
# cert_df = pd.DataFrame({
#     "Certification":   ["AWS Certified Cloud Practitioner", "AWS Certified AI Practitioner"],
#     "Issuer":          ["Amazon Web Services",               "Amazon Web Services"],
#     "Year":            [2025,                                 2025],
#     "Status":          ["✅ Active",                          "✅ Active"],
#     "Relevance":       ["Cloud infrastructure, S3, scalable deployment",
#                         "AI/ML services, model deployment on AWS"],
# })
# st.dataframe(cert_df, use_container_width=True, hide_index=True)
# st.markdown("</div></div>", unsafe_allow_html=True)


# # =============================================================================
# # ⑦ PROJECTS
# # =============================================================================
# st.markdown('<hr class="divider"><div style="background:#ffffff"><div class="section">', unsafe_allow_html=True)
# st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
# st.markdown('<div class="section-eyebrow">Technical Projects</div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Things I\'ve built.</div>', unsafe_allow_html=True)
# st.markdown('<p class="section-sub">ML systems, data tools, and analytics deployments from co-ops and competitions.</p>', unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)

# # Widget 4 — tech filter multiselect
# all_tech = sorted({t for p in PROJECTS for t in p["tech"]})
# filter_tech = st.multiselect(
#     "Filter by technology",
#     all_tech,
#     default=[],
#     key="proj_filter",
#     placeholder="Show all projects...",
# )

# filtered = PROJECTS if not filter_tech else [
#     p for p in PROJECTS if any(t in p["tech"] for t in filter_tech)
# ]

# rows = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
# for row in rows:
#     cols = st.columns(len(row), gap="medium")
#     for col, proj in zip(cols, row):
#         with col:
#             if proj["wip"]:
#                 gh = '<span style="font-size:12px;font-weight:500;color:var(--ink-muted);border:1px solid var(--border);border-radius:980px;padding:6px 14px;">🔒 Practicum project, in progress</span>'
#             elif proj["github"]:
#                 gh = f'<a class="proj-link proj-link-fill" href="{proj["github"]}" target="_blank">GitHub ↗</a>'
#             else:
#                 gh = ""
#             live = f'<a class="proj-link" href="{proj["live"]}" target="_blank">Live ↗</a>' if proj["live"] else ""
#             st.markdown(f"""
#             <div class="proj-card">
#               <div class="proj-thumb" style="background:{proj['color']}">{proj['emoji']}</div>
#               <div class="proj-body">
#                 <div class="proj-metric">{proj['metric']}</div>
#                 <div class="proj-tag">{proj['tag']}</div>
#                 <div class="proj-title">{proj['title']}</div>
#                 <p class="proj-desc">{proj['desc']}</p>
#                 <div class="proj-pills">{pills_html(proj['tech'])}</div>
#                 <div class="proj-links">{gh}{live}</div>
#               </div>
#             </div>
#             """, unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)

# if not filtered:
#     st.info("No projects match the selected filters.")

# st.markdown("</div></div>", unsafe_allow_html=True)


# # =============================================================================
# # ⑧ CONTACT — validation + stored submissions
# # =============================================================================
# st.markdown('<hr class="divider"><div style="background:#f5f5f7"><div class="section">', unsafe_allow_html=True)
# st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
# st.markdown('<div class="section-eyebrow">Contact</div>', unsafe_allow_html=True)
# st.markdown('<div class="section-heading">Let\'s connect.</div>', unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)

# left, right = st.columns([1, 1], gap="large")

# with left:
#     st.markdown("""
#     <div class="contact-info">
#       <h3>Open to opportunities</h3>
#       <p>
#         I am actively looking for full-time Data Science roles starting Summer / Fall 2026.
#         Whether you have a role, a collaboration, or just want to talk ML — I would love to hear from you.
#       </p>
#       <div class="contact-detail">
#         <span class="contact-detail-icon">✉️</span>
#         <span class="contact-detail-text">
#           <a href="mailto:ishaan.dawra@rotman.utoronto.ca">ishaan.dawra@rotman.utoronto.ca</a>
#         </span>
#       </div>
#       <div class="contact-detail">
#         <span class="contact-detail-icon">📞</span>
#         <span class="contact-detail-text">(431) 554-4482</span>
#       </div>
#       <div class="contact-detail">
#         <span class="contact-detail-icon">📍</span>
#         <span class="contact-detail-text">Toronto, Ontario, Canada</span>
#       </div>
#       <div class="contact-detail">
#         <span class="contact-detail-icon">💼</span>
#         <span class="contact-detail-text">
#           <a href="https://linkedin.com" target="_blank">LinkedIn Profile</a>
#         </span>
#       </div>
#       <div class="contact-detail">
#         <span class="contact-detail-icon">🐙</span>
#         <span class="contact-detail-text">
#           <a href="https://github.com/2002-ishaan" target="_blank">GitHub Profile</a>
#         </span>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

# with right:
#     cf_name    = st.text_input("Full Name *",     placeholder="Jane Smith",                              key="cf_name")
#     cf_email   = st.text_input("Email Address *", placeholder="jane@company.com",                        key="cf_email")
#     cf_subject = st.text_input("Subject",         placeholder="Hiring inquiry / Collaboration / Other",  key="cf_subject")
#     cf_message = st.text_area ("Message *",       placeholder="Tell me about the opportunity or what you'd like to discuss...", height=150, key="cf_message")

#     errors = []
#     if st.button("Send Message →", key="send_btn"):
#         if not cf_name.strip():
#             errors.append("Name is required.")
#         if not cf_email.strip():
#             errors.append("Email is required.")
#         elif not is_valid_email(cf_email.strip()):
#             errors.append("Please enter a valid email address (e.g. name@domain.com).")
#         if not cf_message.strip():
#             errors.append("Message cannot be empty.")

#         if errors:
#             for e in errors:
#                 st.markdown(f'<div class="form-error">⚠️ {e}</div>', unsafe_allow_html=True)
#         else:
#             st.session_state.submissions.append({
#                 "name":      cf_name.strip(),
#                 "email":     cf_email.strip(),
#                 "subject":   cf_subject.strip() or "—",
#                 "message":   cf_message.strip(),
#                 "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
#             })
#             st.session_state.form_sent = True
#             st.rerun()

#     if st.session_state.form_sent:
#         st.markdown("""
#         <div class="form-success">
#           ✅ &nbsp;<strong>Message sent!</strong> Thanks for reaching out — I will get back to you soon.
#         </div>
#         """, unsafe_allow_html=True)

# st.markdown("</div></div>", unsafe_allow_html=True)

# # Admin panel — stored submissions
# if st.session_state.submissions:
#     with st.expander(f"📬 Inbox — {len(st.session_state.submissions)} submission(s)"):
#         st.dataframe(
#             pd.DataFrame(st.session_state.submissions),
#             use_container_width=True, hide_index=True,
#         )


# # =============================================================================
# # FOOTER
# # =============================================================================
# st.markdown("""
# <div class="footer">
#   <div class="footer-inner">
#     <span>© 2026 Ishaan Dawra &nbsp;·&nbsp; Built with Streamlit</span>
#     <span>
#       <a href="mailto:ishaan.dawra@rotman.utoronto.ca">Email</a> &nbsp;·&nbsp;
#       <a href="https://linkedin.com" target="_blank">LinkedIn</a> &nbsp;·&nbsp;
#       <a href="https://github.com/2002-ishaan" target="_blank">GitHub</a>
#     </span>
#   </div>
# </div>
# """, unsafe_allow_html=True)























"""
Ishaan Dawra — Personal Portfolio
Run:  pip install streamlit plotly pandas
      streamlit run portfolio_app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import re
from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ishaan Dawra · Data Scientist",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
if "submissions" not in st.session_state:
    st.session_state.submissions = []
if "form_sent" not in st.session_state:
    st.session_state.form_sent = False

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "tag": "Machine Learning · Finance",
        "title": "Client Dormancy Risk Model",
        "desc": "Risk-based predictive ML model identifying client segments at-risk of dormancy. Covers 23% of revenue built on 24 months of multi-source transaction & behavioural data across 340K+ active clients.",
        "tech": ["Python", "XGBoost", "SQL", "Tableau", "Pandas"],
        "color": "#e8f0fb", "emoji": "🏦", "metric": "23% revenue covered",
        "github": None, "live": None, "wip": True,
    },
    {
        "tag": "Healthcare · Process Mining",
        "title": "Emergency Dept Optimisation",
        "desc": "Dual gradient boosting classifiers (AUC ~0.85) on 90K+ ED event logs to predict admission and walkout risk. Streamlit deployment captures 53% of walkouts in the top decile.",
        "tech": ["Scikit-learn", "Causal Inference", "Plotly", "Streamlit"],
        "color": "#fdf2f8", "emoji": "🏥", "metric": "AUC ~0.85",
        "github": "https://github.com/2002-ishaan/Healthcare_Process-Optimisation", "live": None, "wip": False,
    },
    {
        "tag": "Public Safety · Geospatial",
        "title": "Toronto Police Risk Platform",
        "desc": "Crime-risk dashboard across 316K+ incidents at 73 TTC stations. Generated ranked risk profiles for 15 priority stations for the 2026 FIFA World Cup. Finalist (Top 5) in TPS Case Competition.",
        "tech": ["GeoPandas", "Streamlit", "NumPy", "Anomaly Detection"],
        "color": "#f0fdf4", "emoji": "🗺️", "metric": "316K+ incidents",
        "github": "https://github.com/2002-ishaan/Toronto_Police-Case_Competition", "live": None, "wip": False,
    },
    {
        "tag": "Time Series · EV · ML",
        "title": "SmartCharge",
        "desc": "Time series ML model on 22K+ EV charging sessions to forecast energy demand. LightGBM with Meteostat weather data improved R² from 0.14 → 0.415 and reduced MAE by 31.6%.",
        "tech": ["Python", "LightGBM", "Scikit-learn", "Seaborn", "Feature Engineering"],
        "color": "#f0f9ff", "emoji": "⚡", "metric": "MAE ↓ 31.6%",
        "github": "https://github.com/2002-ishaan", "live": None, "wip": False,
    },
    {
        "tag": "GenAI · Recommendation · AWS",
        "title": "GoVacay",
        "desc": "Hybrid recommendation system combining content-based filtering with LLM-generated synthetic user profiles via OpenRouter API. Reduced inference time by 67%, filtered 80% of irrelevant results. Deployed on AWS Bedrock.",
        "tech": ["Python", "NumPy", "GenAI", "AWS Bedrock", "API Integration"],
        "color": "#fefce8", "emoji": "✈️", "metric": "67% faster inference",
        "github": "https://github.com/2002-ishaan", "live": None, "wip": False,
    },
    {
        "tag": "Statistics · Airline Analytics",
        "title": "SkyMetrics",
        "desc": "Analysed 6 years of airline operational data comparing Air Canada vs WestJet. Found Air Canada consumed 12% more fuel per passenger-km despite similar load factors (~83%). Created AWS QuickSight dashboard.",
        "tech": ["Python", "Statistics", "Pandas", "Matplotlib", "AWS QuickSight"],
        "color": "#fff1f2", "emoji": "📊", "metric": "6 yrs of data",
        "github": "https://github.com/2002-ishaan", "live": None, "wip": False,
    },
]

SKILLS_DB = {
    "Programming & Data Engineering": {
        "Python (Pandas / NumPy)": 95, "SQL": 90, "R": 75,
        "Apache Airflow": 70, "AWS S3": 72, "Git / GitHub": 85, "Data Wrangling": 88,
    },
    "Machine Learning & Analytics": {
        "Gradient Boosting (XGB/LGBM)": 90, "Supervised Learning": 92,
        "Unsupervised Learning": 80, "NLP": 78, "Causal Inference": 75,
        "A/B Testing": 82, "Anomaly Detection": 78,
    },
    "Visualisation & Deployment": {
        "Tableau": 88, "Streamlit": 85, "Plotly": 80,
        "Matplotlib / Seaborn": 85, "Geospatial Mapping": 72,
    },
}

EXPERIENCES = [
    {
        "company": "Meridian Credit Union",
        "role": "Data Scientist Co-op",
        "dates": "Jan 2026 – Present",
        "location": "Toronto, ON, Canada",
        "bullets": [
            "Engineered a risk-based predictive ML model identifying client segments at-risk of dormancy, covering 23% of revenue across 340K+ active clients.",
            "Architected a scalable Python / SQL pipeline compressing 8M+ records into 1.4M half-year snapshots — 6× faster segmentation & retention analysis.",
            "Designed and deployed an interactive Tableau dashboard prioritising high-value and at-risk client segments for the marketing team.",
            "Presented complex analytical findings to executive leadership and an audience of 100+, translating models into actionable business strategy.",
        ],
        "tech": ["Python", "SQL", "XGBoost", "Tableau", "AWS S3", "Pandas"],
    },
    {
        "company": "Genpact",
        "role": "Data Scientist Co-op",
        "dates": "Feb 2024 – Aug 2024",
        "location": "Karnataka, India",
        "bullets": [
            "Built a churn prediction model (72% recall) with automated APIs and AWS S3 ingestion via Apache Airflow, enabling production-ready churn monitoring.",
            "Analysed A/B test results and 3.9K+ customer reviews using NLP to identify key churn drivers and inform targeted retention strategies.",
        ],
        "tech": ["Python", "NLP", "Apache Airflow", "AWS S3", "A/B Testing"],
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def pills(items):
    return "".join(f'<span class="pill">{t}</span>' for t in items)

def valid_email(e):
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", e))

# ─────────────────────────────────────────────────────────────────────────────
# CSS  — single injection, no background wrappers, scroll-reveal animations
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"], .stApp {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #ffffff; color: #1d1d1f;
  -webkit-font-smoothing: antialiased;
}

/* ── HIDE STREAMLIT CHROME ── */
header[data-testid="stHeader"], .stDeployButton, #MainMenu,
section[data-testid="stSidebar"], footer { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
/* kill the extra vertical space streamlit injects between elements */
div[data-testid="stVerticalBlock"] > div { gap: 0 !important; }
div.element-container { margin: 0 !important; padding: 0 !important; }

/* ── TOKENS ── */
:root {
  --ink: #1d1d1f; --ink-2: #6e6e73; --ink-3: #aeaeb2;
  --bg: #ffffff; --bg-2: #f5f5f7; --border: #d2d2d7;
  --blue: #0066cc; --blue-lt: #e8f0fb;
  --r-sm: 12px; --r-md: 18px; --r-lg: 24px;
  --sh-sm: 0 2px 8px rgba(0,0,0,.06);
  --sh-md: 0 8px 32px rgba(0,0,0,.10);
  --sh-lg: 0 24px 64px rgba(0,0,0,.14);
}

/* ── SCROLL-REVEAL ANIMATION ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(32px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; } to { opacity: 1; }
}
@keyframes scaleIn {
  from { opacity: 0; transform: scale(.96); }
  to   { opacity: 1; transform: scale(1); }
}
@keyframes slideRight {
  from { opacity: 0; transform: translateX(-24px); }
  to   { opacity: 1; transform: translateX(0); }
}
.anim-fadeup  { animation: fadeUp  .7s cubic-bezier(.22,1,.36,1) both; }
.anim-fadein  { animation: fadeIn  .6s ease both; }
.anim-scale   { animation: scaleIn .55s cubic-bezier(.22,1,.36,1) both; }
.anim-slide   { animation: slideRight .6s cubic-bezier(.22,1,.36,1) both; }
.delay-1 { animation-delay: .1s; }
.delay-2 { animation-delay: .2s; }
.delay-3 { animation-delay: .3s; }
.delay-4 { animation-delay: .4s; }
.delay-5 { animation-delay: .5s; }
.delay-6 { animation-delay: .6s; }

/* ── NAVBAR ── */
.navbar {
  position: sticky; top: 0; z-index: 9999;
  backdrop-filter: saturate(180%) blur(24px);
  -webkit-backdrop-filter: saturate(180%) blur(24px);
  background: rgba(255,255,255,.88);
  border-bottom: 1px solid rgba(0,0,0,.08);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 52px; height: 54px;
}
.nav-brand { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.nav-logo {
  width: 30px; height: 30px; background: var(--ink); border-radius: 7px;
  display: flex; align-items: center; justify-content: center;
  font-size: 12px; font-weight: 800; color: #fff; letter-spacing: -.5px;
  flex-shrink: 0; transition: transform .2s;
}
.nav-logo:hover { transform: rotate(-5deg) scale(1.08); }
.nav-name { font-size: 15px; font-weight: 600; color: var(--ink); letter-spacing: -.3px; }
.nav-links { display: flex; gap: 28px; list-style: none; }
.nav-links a {
  font-size: 14px; font-weight: 400; color: var(--ink);
  text-decoration: none; opacity: .7; transition: opacity .18s;
}
.nav-links a:hover { opacity: 1; }
.nav-pill {
  background: var(--ink) !important; color: #fff !important;
  border-radius: 980px !important; padding: 6px 18px !important;
  font-size: 13px !important; font-weight: 500 !important; opacity: 1 !important;
  transition: background .2s !important;
}
.nav-pill:hover { background: #333 !important; }

/* ── HERO ── */
.hero {
  background: linear-gradient(165deg, #eef3ff 0%, #f5f5f7 52%, #fff 100%);
  padding: 100px 52px 92px;
  display: flex; flex-direction: column; align-items: center; text-align: center;
}
.hero-avatar {
  width: 120px; height: 120px; border-radius: 50%;
  background: linear-gradient(135deg, #1d1d1f, #4a4a4f);
  display: flex; align-items: center; justify-content: center;
  font-size: 64px; margin-bottom: 28px; box-shadow: var(--sh-md);
  transition: transform .3s, box-shadow .3s;
}
.hero-avatar:hover { transform: scale(1.05); box-shadow: var(--sh-lg); }
.hero-eyebrow {
  font-size: 11px; font-weight: 600; letter-spacing: 2.8px;
  text-transform: uppercase; color: var(--blue); margin-bottom: 14px;
}
.hero-name {
  font-size: 72px; font-weight: 800; letter-spacing: -2.8px; line-height: 1.0;
  color: var(--ink); margin-bottom: 14px;
}
.hero-role {
  font-size: 22px; font-weight: 300; color: var(--ink-2);
  letter-spacing: -.3px; margin-bottom: 18px;
}
.hero-tagline {
  font-size: 17px; font-weight: 400; color: var(--ink-2);
  max-width: 580px; line-height: 1.7; margin-bottom: 36px;
}
.hero-badges { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-bottom: 40px; }
.badge {
  background: rgba(255,255,255,.9); border: 1px solid var(--border);
  border-radius: 980px; padding: 6px 16px;
  font-size: 13px; font-weight: 500; color: var(--ink);
  transition: border-color .2s, transform .2s;
}
.badge:hover { border-color: var(--ink); transform: translateY(-2px); }
.btn-row { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.btn-dark {
  background: var(--ink); color: #fff; border-radius: 980px; padding: 13px 30px;
  font-size: 15px; font-weight: 500; text-decoration: none; display: inline-block;
  transition: transform .2s, box-shadow .2s;
}
.btn-dark:hover { transform: translateY(-2px); box-shadow: var(--sh-md); }
.btn-outline {
  background: transparent; color: var(--ink);
  border: 1.5px solid var(--border); border-radius: 980px; padding: 13px 30px;
  font-size: 15px; font-weight: 500; text-decoration: none; display: inline-block;
  transition: border-color .2s;
}
.btn-outline:hover { border-color: var(--ink); }

/* ── STAT STRIP ── */
.stat-strip {
  background: var(--ink);
  display: flex; justify-content: center; flex-wrap: wrap;
  border-top: 1px solid rgba(255,255,255,.06);
}
.stat-item {
  flex: 1; min-width: 150px; max-width: 210px;
  padding: 28px 20px; text-align: center;
  border-right: 1px solid rgba(255,255,255,.1);
  transition: background .2s;
}
.stat-item:last-child { border-right: none; }
.stat-item:hover { background: rgba(255,255,255,.05); }
.stat-num  { font-size: 32px; font-weight: 700; letter-spacing: -1px; color: #fff; }
.stat-lbl  { font-size: 12px; color: rgba(255,255,255,.45); margin-top: 4px; }

/* ── SECTION WRAPPER — single clean approach, alternating via class ── */
.sec {
  padding: 88px 52px;
  position: relative;
}
.sec-inner { max-width: 1080px; margin: 0 auto; }
.sec-alt { background: var(--bg-2); }

.sec-eye {
  font-size: 11px; font-weight: 600; letter-spacing: 2.8px;
  text-transform: uppercase; color: var(--blue); margin-bottom: 10px;
}
.sec-head {
  font-size: 44px; font-weight: 700; letter-spacing: -1.6px;
  color: var(--ink); line-height: 1.1; margin-bottom: 12px;
}
.sec-sub {
  font-size: 18px; font-weight: 400; color: var(--ink-2);
  line-height: 1.6; max-width: 580px;
}
.divider { border: none; border-top: 1px solid var(--border); }

/* ── ABOUT ── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 56px; align-items: start; margin-top: 44px; }
.about-p { font-size: 16px; color: var(--ink-2); line-height: 1.8; margin-bottom: 18px; }
.about-p strong { color: var(--ink); font-weight: 600; }
.edu-tbl { width: 100%; border-collapse: separate; border-spacing: 0; border-radius: 16px; overflow: hidden; border: 1px solid var(--border); }
.edu-tbl thead th { background: var(--ink); padding: 12px 18px; font-size: 10px; font-weight: 600; letter-spacing: 1.8px; text-transform: uppercase; color: rgba(255,255,255,.6); text-align: left; }
.edu-tbl tbody td { padding: 18px 18px; font-size: 14px; color: var(--ink-2); border-bottom: 1px solid var(--bg-2); transition: background .15s; }
.edu-tbl tbody tr:last-child td { border-bottom: none; }
.edu-tbl tbody tr:hover td { background: var(--bg-2); }
.edu-tbl td:first-child { font-weight: 600; color: var(--ink); }
.yr { display: inline-block; background: var(--blue-lt); color: var(--blue); border-radius: 980px; padding: 2px 10px; font-size: 11px; font-weight: 600; }

/* ── SKILL PILLS ── */
.pill {
  display: inline-block; background: var(--bg-2); border: 1px solid var(--border);
  border-radius: 10px; padding: 3px 10px;
  font-size: 11px; font-weight: 500; color: var(--ink); margin: 2px;
  transition: background .15s, border-color .15s;
}
.pill:hover { background: #fff; border-color: var(--ink); }

/* ── EXPERIENCE CARDS ── */
.exp-card {
  background: #fff; border: 1px solid var(--border); border-radius: var(--r-lg);
  padding: 32px 36px; margin-bottom: 18px;
  transition: box-shadow .25s, transform .25s;
  position: relative; overflow: hidden;
}
.exp-card::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0;
  width: 3px; background: var(--blue);
  border-radius: 3px 0 0 3px;
  transform: scaleY(0); transition: transform .3s cubic-bezier(.22,1,.36,1);
}
.exp-card:hover { box-shadow: var(--sh-md); transform: translateY(-3px); }
.exp-card:hover::before { transform: scaleY(1); }
.exp-hdr { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 4px; }
.exp-co   { font-size: 19px; font-weight: 700; color: var(--ink); }
.exp-date { font-size: 12px; font-weight: 500; color: var(--ink-2); background: var(--bg-2); border-radius: 980px; padding: 4px 12px; white-space: nowrap; }
.exp-role { font-size: 14px; font-weight: 500; color: var(--blue); margin-bottom: 2px; }
.exp-loc  { font-size: 12px; color: var(--ink-3); margin-bottom: 16px; }
.exp-list { list-style: none; padding: 0; }
.exp-list li { font-size: 14px; color: var(--ink-2); line-height: 1.65; padding: 4px 0 4px 22px; position: relative; }
.exp-list li::before { content: '→'; position: absolute; left: 0; color: var(--blue); font-weight: 600; }

/* ── CERT CARDS ── */
.cert-row { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 36px; }
.cert-card {
  background: #fff; border: 1px solid var(--border); border-radius: var(--r-lg);
  padding: 24px 28px; display: flex; align-items: center; gap: 18px;
  transition: box-shadow .22s, transform .22s;
}
.cert-card:hover { box-shadow: var(--sh-md); transform: translateY(-3px); }
.cert-icon { font-size: 36px; flex-shrink: 0; }
.cert-name { font-size: 15px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
.cert-meta { font-size: 12px; color: var(--ink-3); }
.cert-badge { margin-top: 6px; display: inline-block; background: #ecfdf5; color: #065f46; border-radius: 980px; padding: 2px 10px; font-size: 11px; font-weight: 600; }

/* ── PROJECT CARDS ── */
.proj-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; margin-top: 40px; }
.proj-card {
  background: #fff; border: 1px solid var(--border); border-radius: var(--r-lg);
  overflow: hidden; display: flex; flex-direction: column;
  transition: transform .25s cubic-bezier(.22,1,.36,1), box-shadow .25s;
}
.proj-card:hover { transform: translateY(-6px); box-shadow: var(--sh-lg); }
.proj-thumb {
  width: 100%; aspect-ratio: 16/9;
  display: flex; align-items: center; justify-content: center;
  font-size: 52px; position: relative; overflow: hidden;
  transition: filter .25s;
}
.proj-card:hover .proj-thumb { filter: brightness(.92); }
.proj-body { padding: 20px 24px 24px; flex: 1; display: flex; flex-direction: column; }
.proj-metric { display: inline-block; background: var(--blue-lt); color: var(--blue); border-radius: 980px; padding: 2px 12px; font-size: 11px; font-weight: 600; margin-bottom: 8px; }
.proj-tag { font-size: 10px; font-weight: 600; letter-spacing: 1.8px; text-transform: uppercase; color: var(--ink-3); margin-bottom: 6px; }
.proj-title { font-size: 17px; font-weight: 700; color: var(--ink); margin-bottom: 8px; letter-spacing: -.3px; }
.proj-desc { font-size: 13px; color: var(--ink-2); line-height: 1.65; flex: 1; margin-bottom: 14px; }
.proj-pills { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 16px; }
.proj-links { display: flex; gap: 8px; margin-top: auto; }
.proj-btn {
  font-size: 12px; font-weight: 500; color: var(--ink);
  text-decoration: none; border: 1px solid var(--border);
  border-radius: 980px; padding: 5px 14px;
  transition: background .18s, border-color .18s;
}
.proj-btn:hover { background: var(--bg-2); border-color: var(--ink); }
.proj-btn-dark { background: var(--ink) !important; color: #fff !important; border-color: var(--ink) !important; }
.proj-btn-dark:hover { background: #333 !important; }
.proj-wip { font-size: 12px; font-weight: 500; color: var(--ink-2); border: 1px solid var(--border); border-radius: 980px; padding: 5px 14px; display: inline-block; }

/* ── CONTACT ── */
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; margin-top: 44px; align-items: start; }
.contact-h3 { font-size: 22px; font-weight: 700; color: var(--ink); margin-bottom: 12px; }
.contact-p  { font-size: 15px; color: var(--ink-2); line-height: 1.7; margin-bottom: 28px; }
.contact-row { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }
.contact-ico  { font-size: 18px; }
.contact-txt  { font-size: 14px; color: var(--ink); font-weight: 500; }
.contact-txt a { color: var(--blue); text-decoration: none; }
.contact-txt a:hover { text-decoration: underline; }
.form-ok  { background: #ecfdf5; border: 1px solid #6ee7b7; border-radius: var(--r-md); padding: 16px 20px; font-size: 14px; color: #065f46; font-weight: 500; margin-top: 10px; }
.form-err { background: #fef2f2; border: 1px solid #fca5a5; border-radius: var(--r-sm); padding: 8px 14px; font-size: 13px; color: #991b1b; margin-bottom: 6px; }

/* ── FOOTER ── */
.footer { background: var(--ink); padding: 26px 52px; font-size: 13px; }
.footer-in { display: flex; justify-content: space-between; align-items: center; max-width: 1080px; margin: 0 auto; }
.footer-in span { color: rgba(255,255,255,.45); }
.footer-in a { color: rgba(255,255,255,.65); text-decoration: none; margin-left: 16px; transition: color .18s; }
.footer-in a:hover { color: #fff; }

/* ── WIDGET POLISH ── */
.stSelectbox label, .stSlider label, .stTextInput label,
.stTextArea label, .stMultiSelect label, .stRadio label {
  font-size: 12px !important; font-weight: 600 !important;
  letter-spacing: .4px !important; text-transform: uppercase !important;
  color: var(--ink-2) !important;
}
div[data-testid="stSelectbox"] > div > div { border-radius: var(--r-sm) !important; border-color: var(--border) !important; }
.stTextInput input, .stTextArea textarea {
  border-radius: var(--r-sm) !important; border-color: var(--border) !important;
  font-family: inherit !important; font-size: 14px !important;
  transition: border-color .2s, box-shadow .2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--blue) !important;
  box-shadow: 0 0 0 3px var(--blue-lt) !important;
}
.stButton > button {
  background: var(--ink) !important; color: #fff !important;
  border: none !important; border-radius: 980px !important;
  font-size: 14px !important; font-weight: 500 !important;
  padding: 10px 28px !important; font-family: inherit !important;
  transition: background .2s, transform .15s !important;
}
.stButton > button:hover { background: #333 !important; transform: translateY(-1px) !important; }
/* Slider accent */
div[data-testid="stSlider"] div[role="slider"] { background: var(--ink) !important; }
div[data-testid="stSlider"] .stSlider > div > div > div { background: var(--ink) !important; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# NAVBAR
# =============================================================================
st.markdown("""
<div class="navbar anim-fadein">
  <a class="nav-brand" href="#">
    <div class="nav-logo">ID</div>
    <span class="nav-name">Ishaan Dawra</span>
  </a>
  <nav>
    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#experience">Experience</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#contact" class="nav-pill">Contact</a></li>
    </ul>
  </nav>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# HERO
# =============================================================================
st.markdown("""
<div class="hero">
  <div class="hero-avatar anim-scale">👨🏽‍💻</div>
  <div class="hero-eyebrow anim-fadeup delay-1">Data Scientist &nbsp;·&nbsp; MMA Candidate &nbsp;·&nbsp; University of Toronto</div>
  <h1 class="hero-name anim-fadeup delay-2">Ishaan Dawra</h1>
  <p class="hero-role anim-fadeup delay-3">Turning raw data into decisions that matter.</p>
  <p class="hero-tagline anim-fadeup delay-4">
    I enjoy solving problems where understanding the question matters as much as finding the answer.
    Asking the right question matters just as much as building the model.
    Data problems are just like my favourite game Lego — thousands of pieces coming together to form a clear outcome.
  </p>
  <div class="hero-badges anim-fadeup delay-5">
    <span class="badge">🐍 Python</span>
    <span class="badge">🤖 Machine Learning</span>
    <span class="badge">📊 Analytics</span>
    <span class="badge">☁️ AWS Certified</span>
    <span class="badge">🗺️ Geospatial</span>
    <span class="badge">🔬 NLP</span>
  </div>
  <div class="btn-row anim-fadeup delay-6">
    <a class="btn-dark" href="#projects">View Projects ↓</a>
    <a class="btn-outline" href="#contact">Get in Touch</a>
  </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# STAT STRIP
# =============================================================================
st.markdown("""
<div class="stat-strip">
  <div class="stat-item anim-fadeup delay-1">
    <div class="stat-num">2</div><div class="stat-lbl">Co-op internships</div>
  </div>
  <div class="stat-item anim-fadeup delay-2">
    <div class="stat-num">6+</div><div class="stat-lbl">End-to-end projects</div>
  </div>
  <div class="stat-item anim-fadeup delay-3">
    <div class="stat-num">2×</div><div class="stat-lbl">Case competition top-2</div>
  </div>
  <div class="stat-item anim-fadeup delay-4">
    <div class="stat-num">2</div><div class="stat-lbl">AWS certifications</div>
  </div>
  <div class="stat-item anim-fadeup delay-5">
    <div class="stat-num">3+</div><div class="stat-lbl">Years with Python & ML</div>
  </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# ABOUT
# =============================================================================
st.markdown('<div class="sec"><div class="sec-inner">', unsafe_allow_html=True)
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="anim-fadeup">
  <div class="sec-eye">About Me</div>
  <div class="sec-head">Background</div>
</div>
<div class="about-grid">
  <div class="anim-slide delay-2">
    <p class="about-p">
      I am a <strong>Data Scientist</strong> with hands-on co-op experience at
      <strong>Meridian Credit Union</strong> and <strong>Genpact</strong>, currently completing a
      <strong>Master of Management Analytics</strong> at Rotman School of Management,
      University of Toronto (2026).
    </p>
    <p class="about-p">
      My expertise spans <strong>predictive modelling, NLP, causal inference,
      A/B testing, and large-scale data engineering</strong>. I am equally comfortable
      designing XGBoost pipelines, writing production SQL, and presenting findings
      to a C-suite audience of 100+.
    </p>
    <p class="about-p">
      I hold a <strong>B.E. in Computer &amp; Electronics Engineering</strong> from
      Thapar Institute (2024) and dual AWS certifications:
      Cloud Practitioner and AI Practitioner — both earned in 2025.
    </p>
  </div>
  <div class="anim-scale delay-3">
    <table class="edu-tbl">
      <thead><tr><th>Degree</th><th>Institution</th><th>Year</th></tr></thead>
      <tbody>
        <tr>
          <td>Master of Management Analytics</td>
          <td>Rotman School of Management<br><span style="font-size:11px;color:var(--ink-3)">University of Toronto</span></td>
          <td><span class="yr">2026</span></td>
        </tr>
        <tr>
          <td>B.E. Computer &amp; Electronics Engineering</td>
          <td>Thapar Institute of Engg. &amp; Technology<br><span style="font-size:11px;color:var(--ink-3)">Punjab, India</span></td>
          <td><span class="yr">2024</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================
# SKILLS — widgets 1, 2, 3
# =============================================================================
st.markdown('<div class="sec sec-alt"><div class="sec-inner">', unsafe_allow_html=True)
st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="anim-fadeup">
  <div class="sec-eye">Technical Skills</div>
  <div class="sec-head">What I work with.</div>
</div>
""", unsafe_allow_html=True)

ctrl, chart = st.columns([1, 2], gap="large")
with ctrl:
    cat = st.selectbox("Skill category", list(SKILLS_DB.keys()), key="s_cat")       # widget 1
    mn  = st.slider("Min proficiency (%)", 0, 100, 0, 5, key="s_min")               # widget 2
    ct  = st.radio("Chart type", ["Horizontal bars", "Radar"], key="s_ct", horizontal=True)  # widget 3

with chart:
    chosen = {k: v for k, v in SKILLS_DB[cat].items() if v >= mn}
    if chosen:
        if ct == "Horizontal bars":
            si = dict(sorted(chosen.items(), key=lambda x: x[1]))
            fig = go.Figure(go.Bar(
                x=list(si.values()), y=list(si.keys()), orientation="h",
                marker=dict(
                    color=list(si.values()),
                    colorscale=[[0, "#d2d2d7"], [0.5, "#6e6e73"], [1, "#1d1d1f"]],
                    line=dict(width=0),
                ),
                text=[f"{v}%" for v in si.values()], textposition="outside", cliponaxis=False,
            ))
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=0, r=60, t=8, b=8),
                height=max(280, len(chosen) * 50),
                xaxis=dict(range=[0, 115], showgrid=False, visible=False),
                yaxis=dict(tickfont=dict(size=13, family="Inter"), automargin=True),
                font=dict(family="Inter"),
            )
        else:
            cats = list(chosen.keys()) + [list(chosen.keys())[0]]
            vals = list(chosen.values()) + [list(chosen.values())[0]]
            fig = go.Figure(go.Scatterpolar(
                r=vals, theta=cats, fill="toself",
                fillcolor="rgba(0,102,204,.12)",
                line=dict(color="#0066cc", width=2),
                marker=dict(size=6, color="#0066cc"),
            ))
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=10)),
                    angularaxis=dict(tickfont=dict(size=11, family="Inter")),
                ),
                margin=dict(l=30, r=30, t=30, b=30), height=380,
                font=dict(family="Inter"),
            )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No skills meet that threshold.")

st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================
# EXPERIENCE
# =============================================================================
st.markdown('<div class="sec"><div class="sec-inner">', unsafe_allow_html=True)
st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="anim-fadeup">
  <div class="sec-eye">Professional Experience</div>
  <div class="sec-head">Where I\'ve worked.</div>
</div>
<br>
""", unsafe_allow_html=True)

for i, exp in enumerate(EXPERIENCES):
    bl = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    delay = f"delay-{i+1}"
    st.markdown(f"""
    <div class="exp-card anim-fadeup {delay}">
      <div class="exp-hdr">
        <div>
          <div class="exp-co">{exp['company']}</div>
          <div class="exp-role">{exp['role']}</div>
          <div class="exp-loc">📍 {exp['location']}</div>
        </div>
        <div class="exp-date">{exp['dates']}</div>
      </div>
      <ul class="exp-list">{bl}</ul>
      <div style="margin-top:16px;display:flex;flex-wrap:wrap;gap:6px">{pills(exp['tech'])}</div>
    </div>
    """, unsafe_allow_html=True)

# Timeline chart
st.markdown("<br>", unsafe_allow_html=True)
tl = pd.DataFrame([
    dict(Task="Meridian Credit Union", Start="2026-01-01", Finish="2026-09-01", Type="Industry"),
    dict(Task="Genpact",               Start="2024-02-01", Finish="2024-08-01", Type="Industry"),
    dict(Task="MMA @ Rotman",          Start="2025-09-01", Finish="2026-08-01", Type="Education"),
    dict(Task="B.E. @ Thapar",         Start="2020-08-01", Finish="2024-06-01", Type="Education"),
])
fig_tl = px.timeline(tl, x_start="Start", x_end="Finish", y="Task", color="Type",
    color_discrete_map={"Industry": "#1d1d1f", "Education": "#6e6e73"},
    title="Career & Education Timeline",
)
fig_tl.update_yaxes(autorange="reversed")
fig_tl.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=36, b=0), height=200,
    font=dict(family="Inter", size=13),
    legend=dict(orientation="h", y=-0.45),
    title_font=dict(size=14, family="Inter"),
    xaxis=dict(showgrid=False), yaxis=dict(showgrid=False),
)
st.plotly_chart(fig_tl, use_container_width=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================
# CERTIFICATIONS
# =============================================================================
st.markdown('<div class="sec sec-alt"><div class="sec-inner">', unsafe_allow_html=True)
st.markdown("""
<div class="anim-fadeup">
  <div class="sec-eye">Certifications</div>
  <div class="sec-head">Credentials.</div>
</div>
<div class="cert-row anim-fadeup delay-2">
  <div class="cert-card">
    <div class="cert-icon">☁️</div>
    <div>
      <div class="cert-name">AWS Certified Cloud Practitioner</div>
      <div class="cert-meta">Amazon Web Services &nbsp;·&nbsp; 2025</div>
      <span class="cert-badge">✅ Active</span>
    </div>
  </div>
  <div class="cert-card">
    <div class="cert-icon">🤖</div>
    <div>
      <div class="cert-name">AWS Certified AI Practitioner</div>
      <div class="cert-meta">Amazon Web Services &nbsp;·&nbsp; 2025</div>
      <span class="cert-badge">✅ Active</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Certifications dataframe (satisfies "at least one table" requirement)
cert_df = pd.DataFrame({
    "Certification": ["AWS Certified Cloud Practitioner", "AWS Certified AI Practitioner"],
    "Issuer": ["Amazon Web Services", "Amazon Web Services"],
    "Year": [2025, 2025],
    "Status": ["✅ Active", "✅ Active"],
    "Relevance": ["Cloud infra, S3, scalable deployment", "AI/ML services, model deployment on AWS"],
})
st.markdown("<br>", unsafe_allow_html=True)
st.dataframe(cert_df, use_container_width=True, hide_index=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================
# PROJECTS  — widget 4: multiselect filter
# =============================================================================
st.markdown('<div class="sec"><div class="sec-inner">', unsafe_allow_html=True)
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="anim-fadeup">
  <div class="sec-eye">Technical Projects</div>
  <div class="sec-head">Things I\'ve built.</div>
  <p class="sec-sub">ML systems, analytics tools and deployments from co-ops and competitions.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

all_tech = sorted({t for p in PROJECTS for t in p["tech"]})
ft = st.multiselect("Filter by technology", all_tech, default=[], key="pf",
                    placeholder="Show all projects…")   # widget 4

filtered = PROJECTS if not ft else [p for p in PROJECTS if any(t in p["tech"] for t in ft)]

if not filtered:
    st.info("No projects match the selected filters.")
else:
    rows = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
    for row in rows:
        cols = st.columns(len(row), gap="medium")
        for col, proj in zip(cols, row):
            with col:
                if proj["wip"]:
                    cta = '<span class="proj-wip">🔒 Practicum project, in progress</span>'
                elif proj["github"]:
                    cta = f'<a class="proj-btn proj-btn-dark" href="{proj["github"]}" target="_blank">GitHub ↗</a>'
                else:
                    cta = ""
                live_btn = f'<a class="proj-btn" href="{proj["live"]}" target="_blank">Live ↗</a>' if proj["live"] else ""
                st.markdown(f"""
                <div class="proj-card anim-scale">
                  <div class="proj-thumb" style="background:{proj['color']}">{proj['emoji']}</div>
                  <div class="proj-body">
                    <div class="proj-metric">{proj['metric']}</div>
                    <div class="proj-tag">{proj['tag']}</div>
                    <div class="proj-title">{proj['title']}</div>
                    <p class="proj-desc">{proj['desc']}</p>
                    <div class="proj-pills">{pills(proj['tech'])}</div>
                    <div class="proj-links">{cta}{live_btn}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# =============================================================================
# CONTACT — validation + stored submissions
# =============================================================================
st.markdown('<div class="sec sec-alt"><div class="sec-inner">', unsafe_allow_html=True)
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="anim-fadeup">
  <div class="sec-eye">Contact</div>
  <div class="sec-head">Let\'s connect.</div>
</div>
<div class="contact-grid">
  <div class="anim-slide delay-2">
    <div class="contact-h3">Open to opportunities</div>
    <p class="contact-p">
      I am actively looking for full-time Data Science roles starting Summer / Fall 2026.
      Whether you have a role, a collaboration, or just want to talk ML — I would love to hear from you.
    </p>
    <div class="contact-row"><span class="contact-ico">✉️</span>
      <span class="contact-txt"><a href="mailto:ishaan.dawra@rotman.utoronto.ca">ishaan.dawra@rotman.utoronto.ca</a></span>
    </div>
    <div class="contact-row"><span class="contact-ico">📞</span>
      <span class="contact-txt">(431) 554-4482</span>
    </div>
    <div class="contact-row"><span class="contact-ico">📍</span>
      <span class="contact-txt">Toronto, Ontario, Canada</span>
    </div>
    <div class="contact-row"><span class="contact-ico">💼</span>
      <span class="contact-txt"><a href="https://linkedin.com" target="_blank">LinkedIn Profile</a></span>
    </div>
    <div class="contact-row"><span class="contact-ico">🐙</span>
      <span class="contact-txt"><a href="https://github.com/2002-ishaan" target="_blank">github.com/2002-ishaan</a></span>
    </div>
  </div>
  <div style="padding-top:4px">
""", unsafe_allow_html=True)

# Form inside the right column — Streamlit widgets must be outside raw HTML
cf_name    = st.text_input("Full Name *",     placeholder="Jane Smith",                              key="cf_name")
cf_email   = st.text_input("Email Address *", placeholder="jane@company.com",                        key="cf_email")
cf_subject = st.text_input("Subject",         placeholder="Hiring / Collaboration / Other",           key="cf_subj")
cf_msg     = st.text_area("Message *",        placeholder="Tell me about the opportunity…",           height=140, key="cf_msg")

errors = []
if st.button("Send Message →", key="send_btn"):
    if not cf_name.strip():         errors.append("Name is required.")
    if not cf_email.strip():        errors.append("Email is required.")
    elif not valid_email(cf_email): errors.append("Enter a valid email address.")
    if not cf_msg.strip():          errors.append("Message cannot be empty.")
    if errors:
        for e in errors:
            st.markdown(f'<div class="form-err">⚠️ {e}</div>', unsafe_allow_html=True)
    else:
        st.session_state.submissions.append({
            "name": cf_name.strip(), "email": cf_email.strip(),
            "subject": cf_subject.strip() or "—", "message": cf_msg.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })
        st.session_state.form_sent = True
        st.rerun()

if st.session_state.form_sent:
    st.markdown('<div class="form-ok">✅ &nbsp;<strong>Message sent!</strong> I\'ll get back to you soon.</div>',
                unsafe_allow_html=True)

st.markdown('</div></div></div></div>', unsafe_allow_html=True)

if st.session_state.submissions:
    with st.expander(f"📬 Inbox — {len(st.session_state.submissions)} submission(s)"):
        st.dataframe(pd.DataFrame(st.session_state.submissions), use_container_width=True, hide_index=True)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("""
<div class="footer">
  <div class="footer-in">
    <span>© 2026 Ishaan Dawra &nbsp;·&nbsp; Built with Streamlit</span>
    <span>
      <a href="mailto:ishaan.dawra@rotman.utoronto.ca">Email</a>
      <a href="https://linkedin.com" target="_blank">LinkedIn</a>
      <a href="https://github.com/2002-ishaan" target="_blank">GitHub</a>
    </span>
  </div>
</div>
""", unsafe_allow_html=True)