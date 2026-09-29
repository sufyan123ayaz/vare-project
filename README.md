# VARE - Vulnerability Assessment System (Streamlit)

## Run (Windows PowerShell, inside this folder)
    python -m pip install -r requirements.txt
    python -m streamlit run app.py
(Optional: install FFmpeg so `ffprobe` is available for the video metadata indicator.)

## Structure
- app.py                        Streamlit UI (six pages, session history)
- theme.py                      "Threat-Ops Console" UI skin (called via apply_theme() in app.py)
- .streamlit/config.toml        Dark base theme (restart the app after changing it)
- modules/video_detector.py     Original vs fake video (heuristic forensic indicators)
- modules/prompt_injection.py   Prompt-injection detector + client<->server gateway
- modules/web_scanner.py        Non-intrusive web vulnerability scanner (OWASP Top 10, risk score, remediation)

To go back to the default look, delete the two `apply_theme` lines in app.py.
Only scan systems you own or have written permission to test.
