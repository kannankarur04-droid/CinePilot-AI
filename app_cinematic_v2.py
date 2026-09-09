import streamlit as st
import json
from pathlib import Path
import sys

# ============================================================
# CINEPILOT AI — CINEMATIC FILM FACTORY UI
# ============================================================

st.set_page_config(
    page_title="CinePilot AI — Film Factory",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LOCAL PATH
# ============================================================

APP_DIR = Path(__file__).resolve().parent

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

RESULT_PATH = APP_DIR / "cinepilot_result.json"

# ============================================================
# RUNTIME IMPORT
# ============================================================

try:
    from cinepilot_runtime import cinepilot_film_factory
    RUNTIME_AVAILABLE = True
except Exception as e:
    cinepilot_film_factory = None
    RUNTIME_AVAILABLE = False
    RUNTIME_ERROR = str(e)

# ============================================================
# CINEMATIC DARK CSS (WITH FILM SET BACKGROUND OVERLAY)
# ============================================================

st.markdown(
    """
<style>
/* 1. Clean Cinema Background with Built-in Camera Silhouette */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #07090e !important;
    background-image: 
        radial-gradient(circle at 50% 8%, rgba(220, 38, 38, 0.18) 0%, transparent 40%),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64' fill='none' stroke='rgba(255,255,255,0.08)' stroke-width='1.5'%3E%3Cpath d='M4 20h40v30H4zM44 28l16-8v24l-16-8z'/%3E%3Ccircle cx='18' cy='35' r='7'/%3E%3Ccircle cx='14' cy='14' r='6'/%3E%3Ccircle cx='28' cy='14' r='6'/%3E%3C/svg%3E") !important;
    background-repeat: no-repeat !important;
    background-position: center 30% !important;
    background-size: 380px 380px !important;
    background-attachment: fixed !important;
    color: #ffffff !important;
}

/* 2. Absolute Crisp Visibility for Standard Text, Markdown, and Output Boxes */
.stApp p, .stApp span, .stApp label, .stApp li, .stApp div,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span {
    color: #f0f6fc !important;
    opacity: 1 !important;
    font-size: 1.02rem;
    line-height: 1.6;
}

/* 3. Screenplay Titles & Headings */
h1, h2, h3, h4, h5, h6,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #ffffff !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px;
}

/* 4. Bold Accents in Warm Screenplay Gold */
strong, b, [data-testid="stMarkdownContainer"] strong {
    color: #ffca85 !important;
    font-weight: 700 !important;
}

/* 5. Fix Output Boxes (Sharp, Readable Markdown) */
pre, .stText, [data-testid="stText"] {
    background-color: #0b0e14 !important;
    color: #f0f6fc !important;
    -webkit-text-fill-color: #f0f6fc !important;
    border: 1px solid #30363d !important;
    border-radius: 8px !important;
    padding: 16px !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    white-space: pre-wrap !important;
    word-break: break-word !important;
}

/* 6. High-Contrast Studio Text Input */
[data-testid="stTextArea"] textarea {
    color: #ffffff !important;
    background-color: #0e1219 !important;
    caret-color: #ff4b4b !important;
    -webkit-text-fill-color: #ffffff !important;
    border: 1.5px solid #ff4b4b !important;
    border-radius: 12px !important;
    font-size: 1.05rem !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #8b949e !important;
    opacity: 1 !important;
}

/* 7. Film Studio Compact Hero Card */
.hero {
    text-align: center;
    padding: 12px 16px !important;
    margin-bottom: 12px !important;
    border-radius: 14px !important;
    background: rgba(18, 23, 31, 0.85) !important;
    border: 1px solid rgba(255, 75, 75, 0.35) !important;
    box-shadow: 0 8px 24px rgba(0,0,0,0.6) !important;
    backdrop-filter: blur(10px) !important;
}

.hero h1 {
    font-size: 2.1rem !important;
    margin-bottom: 2px !important;
    margin-top: 0 !important;
    letter-spacing: 1px !important;
}

.idea-card {
    padding: 18px 22px;
    border-radius: 14px;
    background: rgba(18, 23, 31, 0.75);
    border: 1px solid #30363d;
    margin-bottom: 15px;
    backdrop-filter: blur(8px);
}

.output-box {
    padding: 20px;
    border-radius: 14px;
    background: rgba(9, 12, 16, 0.9);
    border: 1px solid #21262d;
    margin-top: 15px;
}

/* 8. Studio Primary Button */
.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 700;
    border: 1px solid #ff4b4b;
    background: linear-gradient(135deg, #ff4b4b 0%, #b91c1c 100%);
    color: #ffffff !important;
    transition: 0.25s ease;
    box-shadow: 0 4px 20px rgba(255, 75, 75, 0.3);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(255, 75, 75, 0.5);
}

/* 9. Production Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(14, 18, 25, 0.85);
    padding: 10px;
    border-radius: 12px;
    border: 1px solid #21262d;
}

.stTabs [data-baseweb="tab"] {
    color: #8b949e !important;
    font-weight: 600 !important;
    padding: 10px 16px;
    border-radius: 8px;
}

.stTabs [aria-selected="true"] {
    background-color: rgba(255, 75, 75, 0.15) !important;
    border-bottom: 2px solid #ff4b4b !important;
}

.stTabs [aria-selected="true"] p,
.stTabs [aria-selected="true"] span {
    color: #ff4b4b !important;
    font-weight: 700 !important;
}

/* 10. Metric Cards */
[data-testid="stMetricValue"] {
    color: #ffca85 !important;
    font-weight: 800 !important;
}

.footer {
    text-align: center;
    color: #8b949e;
    padding-top: 30px;
    font-size: 0.92rem;
}
</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# COMPACT HERO
# ============================================================

st.html(
    """
<div class="hero">
    <h1>🎬 CINEPILOT AI</h1>
    <p style="font-size: 1.1rem; font-weight: 600; color: #ffffff; margin: 2px 0;">
        From One Idea to a Production-Ready Film
    </p>
    <p style="color: #ffca85; font-size: 0.92rem; margin: 2px 0;">
        🤖 Autonomous AI Film Production Factory
    </p>
    <p style="font-size: 0.82rem; color: #8b949e; margin-top: 4px; margin-bottom: 0;">
        Research • Story • Shots • Production • Cinematic Visuals
    </p>
</div>
"""
)

# ============================================================
# HELPERS
# ============================================================

def load_saved_result():
    """Load the latest generated CinePilot JSON result."""
    if not RESULT_PATH.exists():
        return None

    try:
        with open(RESULT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save_result(result):
    """Persist result locally."""
    try:
        with open(RESULT_PATH, "w", encoding="utf-8") as f:
            json.dump(
                result,
                f,
                ensure_ascii=False,
                indent=2
            )
        return True
    except Exception:
        return False


def get_value(result, key):
    """Safely retrieve an output stage."""
    if not isinstance(result, dict):
        return ""

    value = result.get(key, "")

    if value is None:
        return ""

    if isinstance(value, (dict, list)):
        return json.dumps(
            value,
            ensure_ascii=False,
            indent=2
        )

    return str(value)


def show_output(result, key, title):
    """Display generated stage output clearly."""
    st.subheader(title)
    value = get_value(result, key)

    if value.strip():
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.markdown(value)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No output available for this stage.")


# ============================================================
# FILM IDEA INPUT (EXPANDED HEIGHT)
# ============================================================

st.html(
    """
<div class="idea-card">
    <h3 style="margin-top:0; color:#ffffff;">🎞️ Start Your Film</h3>
    <p style="color:#8b949e; margin-bottom:0;">
        Enter any film idea. CinePilot will transform it into a
        complete production-ready film plan.
    </p>
</div>
"""
)

film_idea = st.text_area(
    "Enter any film idea",
    value="",
    height=220,
    placeholder=(
        "Example: A fisherman in a coastal Tamil Nadu village "
        "discovers an abandoned lighthouse that contains a secret "
        "connected to his missing father."
    )
)

# ============================================================
# GENERATE BUTTON
# ============================================================

generate = st.button(
    "🚀 Generate Film Factory",
    type="primary",
    use_container_width=True
)

# ============================================================
# GENERATE LOGIC
# ============================================================

if generate:

    if not film_idea.strip():
        st.warning("🎬 Please enter a film idea before starting the Film Factory.")
        st.stop()

    if not RUNTIME_AVAILABLE:
        st.error("❌ CinePilot runtime could not be loaded.")
        st.code(RUNTIME_ERROR, language="text")
        st.stop()

    if "cinepilot_result" in st.session_state:
        del st.session_state["cinepilot_result"]

    st.markdown("---")

    progress_placeholder = st.empty()
    progress_placeholder.markdown(
        """
        ### 🤖 Autonomous Pipeline Running
        * 🔎 **Parallel Research** + **Director Agent**
        * ✍️ **Screenplay Agent**
        * 🎞️ **Scene Breakdown Agent**
        * 📷 **Shot Design Agent**
        * 🏭 **Production Plan Agent**
        * 🎥 **Video Prompt Agent**
        * ✨ **Cinematic Preview Agent**
        """
    )

    try:
        generated_result = cinepilot_film_factory(film_idea.strip())
        save_result(generated_result)
        st.session_state["cinepilot_result"] = generated_result

        st.success("🎉 Film Factory completed successfully!")

        fresh_result = load_saved_result()
        if fresh_result is not None:
            st.session_state["cinepilot_result"] = fresh_result

        st.rerun()

    except Exception as e:
        st.error(f"❌ Film Factory failed: {e}")
        st.exception(e)
        st.stop()


# ============================================================
# RESULT VIEW
# ============================================================

result = st.session_state.get("cinepilot_result")

if result:

    st.markdown("---")

    current_idea = get_value(result, "film_idea")
    if current_idea:
        st.html(
            f"""
<div class="idea-card">
    <h3 style="margin-top:0; color:#ffca85;">🎬 Current Film Idea</h3>
    <p style="color:#f0f6fc; font-size:1.05rem; margin-bottom:0;">
        {current_idea}
    </p>
</div>
"""
        )

    cols = st.columns(4)
    with cols[0]:
        st.metric("🔎 Research", "READY" if get_value(result, "research_context") else "—")
    with cols[1]:
        st.metric("🎬 Story", "READY" if get_value(result, "film_concept") else "—")
    with cols[2]:
        st.metric("🏭 Production", "READY" if get_value(result, "production_plan") else "—")
    with cols[3]:
        st.metric("✨ Preview", "READY" if get_value(result, "cinematic_preview") else "—")

    st.markdown("---")

    tabs = st.tabs(
        [
            "🔎 Research",
            "🎬 Director",
            "✍️ Screenplay",
            "🎞️ Scenes",
            "📷 Camera & Shots",
            "💡 Lighting",
            "🏭 Production",
            "🎥 Video Prompts",
            "✨ Cinematic Preview"
        ]
    )

    with tabs[0]:
        show_output(result, "research_context", "🔎 Parallel Research")
        st.caption("Research generated through the CinePilot research pipeline.")

    with tabs[1]:
        show_output(result, "film_concept", "🎬 Director Vision")

    with tabs[2]:
        show_output(result, "screenplay", "✍️ Screenplay")

    with tabs[3]:
        show_output(result, "scene_breakdown", "🎞️ Scene Breakdown")

    with tabs[4]:
        show_output(result, "shot_breakdown", "📷 Shot Breakdown")

    with tabs[5]:
        st.subheader("💡 Cinematic Lighting & Visual Direction")
        st.info("Lighting direction is contained within the generated shot breakdown and cinematic visual design.")
        shot_data = get_value(result, "shot_breakdown")
        if shot_data:
            st.markdown(shot_data)
        else:
            st.info("No lighting/visual direction available.")

    with tabs[6]:
        show_output(result, "production_plan", "🏭 Production Plan")

    with tabs[7]:
        show_output(result, "video_prompt_package", "🎥 Video Prompt Package")

    with tabs[8]:
        show_output(result, "cinematic_preview", "✨ Cinematic Preview")

    st.markdown("---")

    json_data = json.dumps(result, ensure_ascii=False, indent=2)
    st.download_button(
        label="📦 Download Complete CinePilot Result",
        data=json_data,
        file_name="cinepilot_result.json",
        mime="application/json",
        use_container_width=True
    )

else:
    st.markdown("---")
    st.html(
        """
<div class="idea-card" style="text-align:center;">
    <h2 style="color:#ffffff;">🎬 Your Film Factory is Ready</h2>
    <p style="color:#8b949e;">
        Enter a film idea above and let CinePilot build the complete production pipeline.
    </p>
    <p style="color:#ffca85;">
        Idea → Research → Director → Screenplay → Scenes → Shots → Production → Video Prompts → Preview
    </p>
</div>
"""
    )

# ============================================================
# FOOTER
# ============================================================

st.html(
    """
<div class="footer">
    🎬 <b>CinePilot AI</b><br>
    One Idea → Production-Ready Film Plan<br><br>
    🤖 Autonomous Film Production Factory<br>
    Research • Story • Shots • Production • Cinematic Visuals
</div>
"""
)
