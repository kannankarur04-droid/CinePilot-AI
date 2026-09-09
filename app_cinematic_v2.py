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
# CINEMATIC CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(circle at 82% 16%, rgba(220, 30, 30, 0.20), transparent 25%),
        radial-gradient(circle at 12% 78%, rgba(255, 170, 55, 0.10), transparent 28%),
        radial-gradient(circle at 50% -10%, rgba(255,255,255,0.07), transparent 22%),
        repeating-linear-gradient(90deg, transparent 0px, transparent 118px, rgba(255,255,255,0.018) 119px, transparent 121px),
        linear-gradient(145deg, #010102 0%, #08090c 38%, #100708 68%, #020203 100%);
    color: #f5f5f5;
}

/* Cinematic pipeline tabs */
.stTabs [data-baseweb="tab"] {
    color: #f2f2f2 !important;
    opacity: 1 !important;
    font-weight: 600 !important;
}
.stTabs [data-baseweb="tab"] p {
    color: #f2f2f2 !important;
}
.stTabs [data-baseweb="tab"]:hover p {
    color: #ff4b4b !important;
}
.stTabs [aria-selected="true"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
}
.stTabs [aria-selected="true"] {
    color: #ffffff !important;
}

/* Fix Streamlit idea input visibility */
[data-testid="stTextArea"] textarea {
    color: #111111 !important;
    background-color: #ffffff !important;
    caret-color: #111111 !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #666666 !important;
    opacity: 1 !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* Hero */
.hero {
    text-align: center;
    padding: 30px 20px 25px 20px;
    margin-bottom: 25px;
    border-radius: 22px;
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.02)
        );
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 20px 60px rgba(0,0,0,0.45);
}

.hero h1 {
    font-size: 3.2rem;
    margin-bottom: 12px;
    font-weight: 800;
    letter-spacing: 1px;
}

.hero p {
    margin: 7px 0;
    color: #d0d0d0;
    font-size: 1.15rem;
}

.hero .tagline {
    font-size: 1.35rem;
    font-weight: 600;
    color: #ffffff;
}

.hero .pipeline {
    font-size: 0.98rem;
    color: #aaaaaa;
}

/* Idea card */
.idea-card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.10);
    margin-bottom: 20px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    min-height: 52px;
    border-radius: 12px;
    font-size: 1.05rem;
    font-weight: 700;
    border: 1px solid rgba(255,255,255,0.18);
    background: linear-gradient(
        135deg,
        #ffffff,
        #d8d8d8
    );
    color: #050505;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(255,255,255,0.15);
}

/* Text area */
textarea {
    border-radius: 12px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 5px;
    background: rgba(255,255,255,0.025);
    padding: 8px;
    border-radius: 14px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 10px 14px;
    color: #ffffff !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #ffffff !important;
}

.stTabs [data-baseweb="tab"] p,
.stTabs [data-baseweb="tab"] span {
    color: #ffffff !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* Output */
.output-box {
    padding: 22px;
    border-radius: 16px;
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.09);
    margin-top: 15px;
}

/* Status cards */
.status-card {
    padding: 18px;
    border-radius: 14px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
}

.footer {
    text-align: center;
    color: #777777;
    padding-top: 30px;
    font-size: 0.9rem;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.html(
    """
<div class="hero">

    <h1>🎬 CINEPILOT AI</h1>

    <p class="tagline">
        From One Idea to a Production-Ready Film
    </p>

    <p>
        🤖 Autonomous AI Film Production Factory
    </p>

    <p class="pipeline">
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
    """Display generated stage output."""

    st.subheader(title)

    value = get_value(result, key)

    if value.strip():

        st.markdown(
            '<div class="output-box">',
            unsafe_allow_html=True
        )

        st.text(value)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.info(
            "No output available for this stage."
        )


# ============================================================
# FILM IDEA INPUT
# ============================================================

st.html(
    """
<div class="idea-card">

    <h3>🎞️ Start Your Film</h3>

    <p style="color:#aaaaaa;">
        Enter any film idea. CinePilot will transform it into a
        complete production-ready film plan.
    </p>

</div>
"""
)

# IMPORTANT:
# EMPTY BY DEFAULT — NO OLD FILM IDEA

film_idea = st.text_area(
    "Enter any film idea",
    value="",
    height=140,
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
# GENERATE
# ============================================================

if generate:

    if not film_idea.strip():

        st.warning(
            "🎬 Please enter a film idea before starting the Film Factory."
        )

        st.stop()

    if not RUNTIME_AVAILABLE:

        st.error(
            "❌ CinePilot runtime could not be loaded."
        )

        st.code(
            RUNTIME_ERROR,
            language="text"
        )

        st.stop()

    # Clear previous session result
    if "cinepilot_result" in st.session_state:
        del st.session_state["cinepilot_result"]

    st.markdown("---")

    st.info(
        "🎬 CinePilot Film Factory is generating a new production..."
    )

    progress_placeholder = st.empty()

    progress_placeholder.markdown(
        """
        ### 🤖 Autonomous Pipeline Running

        🔎 Parallel Research + Director Agent  
        ✍️ Screenplay Agent  
        🎞️ Scene Breakdown Agent  
        📷 Shot Design Agent  
        🏭 Production Plan Agent  
        🎥 Video Prompt Agent  
        ✨ Cinematic Preview Agent
        """
    )

    try:

        # ====================================================
        # REAL CINEPILOT RUNTIME
        # ====================================================

        generated_result = cinepilot_film_factory(
            film_idea.strip()
        )

        # Save fresh result
        save_result(generated_result)

        # Store current result
        st.session_state["cinepilot_result"] = generated_result

        st.success(
            "🎉 Film Factory completed successfully!"
        )

        # Reload saved result
        fresh_result = load_saved_result()

        if fresh_result is not None:
            st.session_state["cinepilot_result"] = fresh_result

        st.rerun()

    except Exception as e:

        st.error(
            f"❌ Film Factory failed: {e}"
        )

        st.exception(e)

        st.stop()


# ============================================================
# RESULT SELECTION
# ============================================================

# IMPORTANT:
# DO NOT AUTO-LOAD cinepilot_result.json ON FRESH START.
# Only use the result generated during the current session.

result = st.session_state.get("cinepilot_result")

if result is None:
    result = None


# ============================================================
# RESULT VIEW
# ============================================================

if result:

    st.markdown("---")

    # --------------------------------------------------------
    # Current Film Idea
    # --------------------------------------------------------

    current_idea = get_value(
        result,
        "film_idea"
    )

    if current_idea:

        st.html(
            f"""
<div class="idea-card">

    <h3>🎬 Current Film Idea</h3>

    <p style="color:#dddddd; font-size:1.05rem;">
        {current_idea}
    </p>

</div>
"""
        )

    # --------------------------------------------------------
    # Pipeline Status
    # --------------------------------------------------------

    cols = st.columns(4)

    with cols[0]:

        st.metric(
            "🔎 Research",
            "READY"
            if get_value(
                result,
                "research_context"
            )
            else "—"
        )

    with cols[1]:

        st.metric(
            "🎬 Story",
            "READY"
            if get_value(
                result,
                "film_concept"
            )
            else "—"
        )

    with cols[2]:

        st.metric(
            "🏭 Production",
            "READY"
            if get_value(
                result,
                "production_plan"
            )
            else "—"
        )

    with cols[3]:

        st.metric(
            "✨ Preview",
            "READY"
            if get_value(
                result,
                "cinematic_preview"
            )
            else "—"
        )

    st.markdown("---")

    # ========================================================
    # OUTPUT TABS
    # ========================================================

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

    # --------------------------------------------------------
    # Research
    # --------------------------------------------------------

    with tabs[0]:

        show_output(
            result,
            "research_context",
            "🔎 Parallel Research"
        )

        st.caption(
            "Research generated through the CinePilot research pipeline."
        )

    # --------------------------------------------------------
    # Director
    # --------------------------------------------------------

    with tabs[1]:

        show_output(
            result,
            "film_concept",
            "🎬 Director Vision"
        )

    # --------------------------------------------------------
    # Screenplay
    # --------------------------------------------------------

    with tabs[2]:

        show_output(
            result,
            "screenplay",
            "✍️ Screenplay"
        )

    # --------------------------------------------------------
    # Scenes
    # --------------------------------------------------------

    with tabs[3]:

        show_output(
            result,
            "scene_breakdown",
            "🎞️ Scene Breakdown"
        )

    # --------------------------------------------------------
    # Shots
    # --------------------------------------------------------

    with tabs[4]:

        show_output(
            result,
            "shot_breakdown",
            "📷 Shot Breakdown"
        )

    # --------------------------------------------------------
    # Lighting
    # --------------------------------------------------------

    with tabs[5]:

        st.subheader(
            "💡 Cinematic Lighting & Visual Direction"
        )

        st.info(
            "Lighting direction is contained within the generated "
            "shot breakdown and cinematic visual design."
        )

        shot_data = get_value(
            result,
            "shot_breakdown"
        )

        if shot_data:

            st.text(shot_data)

        else:

            st.info(
                "No lighting/visual direction available."
            )

    # --------------------------------------------------------
    # Production
    # --------------------------------------------------------

    with tabs[6]:

        show_output(
            result,
            "production_plan",
            "🏭 Production Plan"
        )

    # --------------------------------------------------------
    # Video Prompts
    # --------------------------------------------------------

    with tabs[7]:

        show_output(
            result,
            "video_prompt_package",
            "🎥 Video Prompt Package"
        )

    # --------------------------------------------------------
    # Cinematic Preview
    # --------------------------------------------------------

    with tabs[8]:

        show_output(
            result,
            "cinematic_preview",
            "✨ Cinematic Preview"
        )

    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.markdown("---")

    json_data = json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )

    st.download_button(
        label="📦 Download Complete CinePilot Result",
        data=json_data,
        file_name="cinepilot_result.json",
        mime="application/json",
        use_container_width=True
    )


# ============================================================
# EMPTY STATE
# ============================================================

else:

    st.markdown("---")

    st.html(
        """
<div class="idea-card" style="text-align:center;">

    <h2>🎬 Your Film Factory is Ready</h2>

    <p style="color:#aaaaaa;">
        Enter a film idea above and let CinePilot build
        the complete production pipeline.
    </p>

    <p style="color:#888888;">
        Idea → Research → Director → Screenplay → Scenes
        → Shots → Production → Video Prompts → Preview
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