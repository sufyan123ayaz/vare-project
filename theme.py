"""VARE 'Threat-Ops Console' theme - drop-in UI skin for the Streamlit app.
Usage in app.py (right after st.set_page_config):
    from theme import apply_theme
    apply_theme()
"""
from datetime import datetime

import streamlit as st

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

:root{
  --bg:#060912; --panel:rgba(14,22,42,.72); --cyan:#00f0ff; --magenta:#ff2bd6; --lime:#b6ff3b;
  --amber:#ffb800; --red:#ff3b5c; --txt:#dce6f5; --mut:#7fa3c7;
}

/* ---------- background: neon glow + tactical grid ---------- */
.stApp{
  background:
    radial-gradient(1100px 560px at 85% -8%, rgba(255,43,214,.17), transparent 60%),
    radial-gradient(900px 520px at -8% 8%, rgba(0,240,255,.15), transparent 55%),
    linear-gradient(rgba(0,240,255,.04) 1px, transparent 1px) 0 0/46px 46px,
    linear-gradient(90deg, rgba(0,240,255,.04) 1px, transparent 1px) 0 0/46px 46px,
    var(--bg);
  color:var(--txt);
  font-family:'Rajdhani','JetBrains Mono',sans-serif;
}
.stApp::after{ /* CRT scan-lines */
  content:""; position:fixed; inset:0; pointer-events:none; z-index:9999;
  background:repeating-linear-gradient(0deg, rgba(0,0,0,.14) 0, rgba(0,0,0,.14) 1px, transparent 1px, transparent 3px);
  opacity:.35;
}
[data-testid="stHeader"]{background:transparent;}
#MainMenu, footer{visibility:hidden;}
.block-container{max-width:1320px; padding-top:1.2rem; animation:rise .55s cubic-bezier(.2,.8,.2,1);}
@keyframes rise{from{opacity:0; transform:translateY(14px);} to{opacity:1; transform:none;}}

/* ---------- typography ---------- */
html, body, [class*="css"], p, label, li, span{font-family:'Rajdhani','JetBrains Mono',sans-serif;}
p, li{font-size:1.06rem;}
h1{
  font-family:'Orbitron',sans-serif !important; font-weight:900 !important; letter-spacing:.04em;
  background:linear-gradient(90deg,#00f0ff,#ff2bd6,#00f0ff); background-size:220% 100%;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent;
  animation:shine 6s linear infinite; filter:drop-shadow(0 0 14px rgba(0,240,255,.35));
}
@keyframes shine{to{background-position:220% 0;}}
h2, h3, h4{font-family:'Orbitron',sans-serif !important; letter-spacing:.06em; color:#eaf6ff !important;}
h2::before, h3::before{content:"// "; color:var(--magenta); text-shadow:0 0 10px var(--magenta);}
[data-testid="stCaptionContainer"]{color:var(--mut); font-family:'JetBrains Mono',monospace; font-size:.82rem;}
code, pre{font-family:'JetBrains Mono',monospace !important;}
hr{border:none; height:1px; background:linear-gradient(90deg,transparent,var(--cyan),var(--magenta),transparent); opacity:.6;}

/* ---------- top live ticker ---------- */
.vare-ticker{
  display:flex; align-items:center; gap:14px; overflow:hidden; white-space:nowrap; margin-bottom:10px;
  padding:7px 14px; border:1px solid rgba(0,240,255,.25); border-radius:999px;
  background:linear-gradient(90deg,rgba(0,240,255,.10),rgba(255,43,214,.08));
  font-family:'JetBrains Mono',monospace; font-size:.74rem; color:var(--cyan); letter-spacing:.08em;
}
.vare-ticker .live{color:#fff; background:var(--red); padding:2px 9px; border-radius:999px; font-weight:700; animation:pulse 1.4s infinite;}
.vare-ticker .run{display:inline-block; padding-left:100%; animation:marq 32s linear infinite; color:var(--mut);}
@keyframes marq{to{transform:translateX(-100%);}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(255,59,92,.7);} 50%{box-shadow:0 0 0 7px rgba(255,59,92,0);}}

/* ---------- sidebar ---------- */
[data-testid="stSidebar"]{
  background:linear-gradient(185deg,#070c1a 0%,#0b1226 55%,#150a2b 100%);
  border-right:1px solid rgba(0,240,255,.22); box-shadow:6px 0 40px rgba(0,240,255,.06);
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] [data-testid="stCaptionContainer"]{display:none;}
.vare-brand{text-align:center; padding:8px 4px 16px;}
.vare-brand .logo{
  width:74px; height:74px; margin:2px auto 8px; display:grid; place-items:center; font-size:2rem;
  border-radius:22px 6px 22px 6px; border:1.5px solid var(--cyan);
  background:radial-gradient(circle at 30% 20%,rgba(0,240,255,.35),rgba(255,43,214,.18));
  box-shadow:0 0 26px rgba(0,240,255,.45), inset 0 0 18px rgba(255,43,214,.3); animation:float 4s ease-in-out infinite;
}
@keyframes float{50%{transform:translateY(-5px) rotate(2deg);}}
.vare-brand .name{font-family:'Orbitron',sans-serif; font-weight:900; font-size:1.55rem; letter-spacing:.32em; color:#fff; text-shadow:0 0 14px var(--cyan);}
.vare-brand .sub{font-family:'JetBrains Mono',monospace; font-size:.62rem; color:var(--mut); letter-spacing:.16em; margin-top:2px;}
.vare-brand .status{margin-top:10px; font-family:'JetBrains Mono',monospace; font-size:.68rem; color:var(--lime);}
.vare-brand .dot{display:inline-block; width:8px; height:8px; border-radius:50%; background:var(--lime); margin-right:6px; box-shadow:0 0 10px var(--lime); animation:pulse2 1.6s infinite;}
@keyframes pulse2{50%{opacity:.35;}}

/* ---------- buttons ---------- */
.stButton>button, .stDownloadButton>button{
  font-family:'Orbitron',sans-serif; font-size:.74rem; letter-spacing:.09em; text-transform:uppercase; font-weight:700;
  color:var(--cyan); background:rgba(0,240,255,.05); border:1px solid rgba(0,240,255,.55);
  border-radius:4px 16px 4px 16px; padding:.55rem 1rem; transition:all .22s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover{
  color:#fff; background:rgba(0,240,255,.16); border-color:var(--cyan);
  box-shadow:0 0 22px rgba(0,240,255,.5), inset 0 0 14px rgba(0,240,255,.18); transform:translateY(-2px);
}
.stButton>button[kind="primary"], button[data-testid="stBaseButton-primary"]{
  color:#04101a !important; border:none; background:linear-gradient(120deg,#00f0ff,#7b5cff 55%,#ff2bd6);
  box-shadow:0 0 26px rgba(123,92,255,.55);
}
.stButton>button[kind="primary"]:hover, button[data-testid="stBaseButton-primary"]:hover{filter:brightness(1.15); color:#000 !important;}
.stButton>button:disabled{opacity:.35; filter:grayscale(.6);}
[data-testid="stSidebar"] .stButton>button{width:100%; justify-content:flex-start; text-align:left; border-radius:4px 14px 4px 14px; font-size:.72rem; padding:.7rem 1rem;}
[data-testid="stSidebar"] .stButton>button[kind="secondary"], [data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"]{
  border-color:rgba(127,163,199,.25); color:var(--mut); background:rgba(255,255,255,.02);
}
[data-testid="stSidebar"] .stButton>button[kind="secondary"]:hover{border-color:var(--cyan); color:#fff; padding-left:1.4rem;}

/* ---------- metric cards ---------- */
[data-testid="stMetric"]{
  position:relative; overflow:hidden; padding:16px 18px; border-radius:16px 4px 16px 4px;
  background:linear-gradient(145deg,rgba(0,240,255,.09),rgba(255,43,214,.06)); border:1px solid rgba(0,240,255,.28);
  box-shadow:0 10px 34px rgba(0,0,0,.5), inset 0 0 0 1px rgba(255,255,255,.02); transition:all .25s ease;
}
[data-testid="stMetric"]::before{content:""; position:absolute; left:0; top:0; bottom:0; width:4px; background:linear-gradient(var(--cyan),var(--magenta));}
[data-testid="stMetric"]::after{content:""; position:absolute; right:-30px; top:-30px; width:90px; height:90px; border-radius:50%; background:radial-gradient(rgba(255,43,214,.28),transparent 70%);}
[data-testid="stMetric"]:hover{transform:translateY(-4px); box-shadow:0 0 28px rgba(0,240,255,.4);}
[data-testid="stMetricLabel"]{text-transform:uppercase; letter-spacing:.14em; font-size:.7rem; color:var(--mut); font-family:'JetBrains Mono',monospace;}
[data-testid="stMetricValue"]{font-family:'Orbitron',sans-serif; font-weight:700; color:#fff; text-shadow:0 0 16px rgba(0,240,255,.65);}

/* ---------- tabs ---------- */
[data-baseweb="tab-list"]{gap:6px; border-bottom:1px solid rgba(0,240,255,.2);}
button[data-baseweb="tab"]{font-family:'Orbitron',sans-serif; font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mut); border-radius:10px 10px 0 0; transition:all .2s;}
button[data-baseweb="tab"]:hover{color:#fff; background:rgba(0,240,255,.07);}
button[data-baseweb="tab"][aria-selected="true"]{color:var(--cyan); text-shadow:0 0 12px var(--cyan); background:rgba(0,240,255,.08);}
[data-baseweb="tab-highlight"]{height:3px !important; background:linear-gradient(90deg,var(--cyan),var(--magenta)) !important; box-shadow:0 0 14px var(--cyan);}

/* ---------- expanders, alerts, inputs ---------- */
[data-testid="stExpander"]{border:1px solid rgba(0,240,255,.22) !important; border-radius:14px 4px 14px 4px !important; background:var(--panel); backdrop-filter:blur(8px); transition:all .2s;}
[data-testid="stExpander"]:hover{border-color:var(--cyan) !important; box-shadow:0 0 18px rgba(0,240,255,.18);}
[data-testid="stExpander"] summary{font-family:'Rajdhani',sans-serif; font-weight:600; font-size:1.05rem;}
[data-testid="stAlert"]{border-radius:14px 4px 14px 4px; backdrop-filter:blur(8px); border:1px solid rgba(255,255,255,.12); box-shadow:0 0 22px rgba(0,0,0,.4);}
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"]>div{background:rgba(6,10,22,.85) !important; border-color:rgba(0,240,255,.3) !important; border-radius:10px !important;}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within{border-color:var(--cyan) !important; box-shadow:0 0 18px rgba(0,240,255,.4);}
textarea, input{font-family:'JetBrains Mono',monospace !important; font-size:.9rem !important;}
[data-testid="stFileUploaderDropzone"]{border:1.6px dashed var(--cyan); border-radius:16px 4px 16px 4px; background:rgba(0,240,255,.04); transition:all .25s;}
[data-testid="stFileUploaderDropzone"]:hover{background:rgba(0,240,255,.10); box-shadow:0 0 26px rgba(0,240,255,.3);}
[data-testid="stCheckbox"] label, [data-testid="stToggle"] label{color:var(--txt);}

/* ---------- progress, tables, code ---------- */
.stProgress>div>div>div{background:rgba(255,255,255,.07); border-radius:999px; height:10px;}
.stProgress>div>div>div>div{background-image:linear-gradient(90deg,#00f0ff,#7b5cff,#ff2bd6); box-shadow:0 0 16px rgba(0,240,255,.7); border-radius:999px;}
[data-testid="stDataFrame"]{border:1px solid rgba(0,240,255,.25); border-radius:12px; overflow:hidden; box-shadow:0 8px 30px rgba(0,0,0,.45);}
[data-testid="stCode"], .stCodeBlock{border:1px solid rgba(255,43,214,.3); border-radius:12px;}
[data-testid="stJson"]{background:rgba(6,10,22,.7); border-radius:12px; border:1px solid rgba(0,240,255,.2);}
::-webkit-scrollbar{width:9px; height:9px;} ::-webkit-scrollbar-track{background:#070b16;}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--cyan),var(--magenta)); border-radius:8px;}
"""


def apply_theme():
    """Inject the CSS skin + sidebar brand block + live ticker. Call once, right after set_page_config."""
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
    st.sidebar.markdown(
        """<div class="vare-brand"><div class="logo">🛡️</div><div class="name">VARE</div>
        <div class="sub">THREAT-OPS CONSOLE</div>
        <div class="status"><span class="dot"></span>SYSTEM ONLINE</div></div>""",
        unsafe_allow_html=True)
    now = datetime.now().strftime("%d %b %Y  %H:%M")
    st.markdown(
        f"""<div class="vare-ticker"><span class="live">LIVE</span><span>{now}</span>
        <span class="run">VIDEO FORENSICS &nbsp;•&nbsp; PROMPT-INJECTION SHIELD &nbsp;•&nbsp; WEB VULN SCANNER
        &nbsp;•&nbsp; OWASP TOP 10 &nbsp;•&nbsp; RISK SCORING &nbsp;•&nbsp; REMEDIATION PLANS &nbsp;•&nbsp; SCAN ONLY WHAT YOU ARE AUTHORIZED TO TEST</span></div>""",
        unsafe_allow_html=True)
