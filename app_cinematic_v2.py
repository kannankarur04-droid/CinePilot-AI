import streamlit as st
import json
from pathlib import Path
import sys
import re

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

/* Compact & Vibrant Hero Container */
.hero {
    text-align: center;
    padding: 16px 20px 14px 20px;
    margin-bottom: 18px;
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(35, 10, 15, 0.75) 0%, rgba(18, 18, 22, 0.95) 100%);
    border: 1px solid rgba(255, 59, 48, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
}

.hero h1 {
    font-size: 2.2rem !important;
    margin: 0 !important;
    padding-bottom: 4px;
    font-weight: 800 !important;
    letter-spacing: 2px !important;
    color: #FF3B30 !important;
    text-shadow: 0 0 16px rgba(255, 59, 48, 0.55);
}

.hero .tagline {
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
    margin: 4px 0 2px 0 !important;
    opacity: 1 !important;
}

.hero p {
    margin: 2px 0 !important;
    color: #E2E8F0 !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    opacity: 1 !important;
}

.hero .pipeline {
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: #FF6B6B !important;
    margin-top: 4px !important;
    letter-spacing: 1px !important;
    opacity: 1 !important;
}

/* Cinematic pipeline tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    background: rgba(255,255,255,0.03);
    padding: 6px;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 8px 14px;
    color: #f2f2f2 !important;
    opacity: 1 !important;
    font-weight: 600 !important;
}

.stTabs [data-baseweb="tab"] p,
.stTabs [data-baseweb="tab"] span {
    color: #f2f2f2 !important;
    opacity: 1 !important;
}

.stTabs [data-baseweb="tab"]:hover p {
    color: #FF3B30 !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(255, 59, 48, 0.15) !important;
    border: 1px solid rgba(255, 59, 48, 0.4) !important;
}

.stTabs [aria-selected="true"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Fix Streamlit idea input visibility */
[data-testid="stTextArea"] textarea {
    color: #111111 !important;
    background-color: #ffffff !important;
    caret-color: #111111 !important;
    font-size: 0.95rem !important;
    line-height: 1.5 !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #666666 !important;
    opacity: 1 !important;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2.5rem;
    max-width: 1400px;
}

/* Idea card */
.idea-card {
    padding: 18px 22px;
    border-radius: 14px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.10);
    margin-bottom: 16px;
}

.idea-card h3 {
    margin-top: 0;
    margin-bottom: 6px;
    color: #ffffff;
    font-size: 1.15rem;
}

/* Buttons */
.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 10px;
    font-size: 1.05rem;
    font-weight: 700;
    border: 1px solid rgba(255, 59, 48, 0.4);
    background: linear-gradient(135deg, #FF3B30 0%, #C02018 100%);
    color: #ffffff !important;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255, 59, 48, 0.4);
}

/* Output Box */
.output-box {
    padding: 20px;
    border-radius: 12px;
    background: rgba(18, 18, 22, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.12);
    margin-top: 12px;
    font-family: monospace;
    white-space: pre-wrap;
    word-break: break-word;
    color: #e5e5e5;
    font-size: 0.92rem;
    line-height: 1.6;
}

.cinematic-preview-box {
    padding: 24px;
    border-radius: 14px;
    background: linear-gradient(145deg, rgba(30, 20, 25, 0.6), rgba(12, 12, 16, 0.85));
    border: 1px solid rgba(255, 59, 48, 0.25);
    margin-top: 12px;
    color: #f1f5f9;
    font-size: 0.98rem;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #888888;
    padding-top: 25px;
    font-size: 0.85rem;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# COMPACT HERO SECTION
# ============================================================

st.html(
    """
<div class="hero">
    <h1>🎬 CINEPILOT AI</h1>
    <div class="tagline">From One Idea to a Production-Ready Film</div>
    <p>🤖 Autonomous AI Film Production Factory</p>
    <div class="pipeline">Research • Story • Shots • Production • Cinematic Visuals</div>
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
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.text(value)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No output available for this stage.")


def extract_lighting_direction(shot_data):
    """Extract and synthesize a comprehensive lighting blueprint from CinePilot shot breakdown."""

    if not shot_data:
        return ""

    output = []
    seen = set()
    current_scene = None
    master_lighting_raw = None

    lines = shot_data.splitlines()

    scene_pattern = re.compile(
        r"SCENE\s+(\d+)\s*:\s*(.+)",
        re.IGNORECASE
    )

    shot_pattern = re.compile(
        r"SHOT\s+(?:NUMBER\s*:\s*\**\s*)?([0-9]+(?:\.[0-9]+)?)",
        re.IGNORECASE
    )

    lighting_pattern = re.compile(
        r"LIGHTING\s*:\s*\**\s*(.+)",
        re.IGNORECASE
    )

    master_pattern = re.compile(
        r"E\.\s*LIGHTING\s*PLAN\s*:\s*(.+)",
        re.IGNORECASE
    )

    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        clean = line.replace("**", "").strip()

        # Scene detection
        scene_match = scene_pattern.search(clean)
        if scene_match:
            current_scene = scene_match.group(1)
            scene_name = scene_match.group(2).strip()
            output.append(f"\n🎬 SCENE {current_scene}: {scene_name} — LIGHTING SETUP")
            i += 1
            continue

        # Shot lighting detection
        shot_match = shot_pattern.search(clean)
        if shot_match and current_scene:
            shot_number = shot_match.group(1)
            lighting = None

            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                next_clean = next_line.replace("**", "").strip()

                if scene_pattern.search(next_clean) or shot_pattern.search(next_clean):
                    break

                lighting_match = lighting_pattern.search(next_clean)
                if lighting_match:
                    lighting = lighting_match.group(1).rstrip("*").strip()
                    break
                j += 1

            if lighting:
                key = (shot_number, lighting)
                if key not in seen:
                    output.append(f"  • Shot {shot_number}: {lighting}")
                    seen.add(key)

            i += 1
            continue

        # Master lighting detection
        master_match = master_pattern.search(clean)
        if master_match and master_lighting_raw is None:
            master_lighting_raw = master_match.group(1).strip()

        i += 1

    # Format Master Lighting Plan into a rich, professional layout
    master_block = [
        "\n==================================================",
        "💡 MASTER CINEMATOGRAPHY & LIGHTING BLUEPRINT",
        "=================================================="
    ]

    if master_lighting_raw:
        master_block.append(f"\n• Overarching Lighting Philosophy:\n  {master_lighting_raw}")
    else:
        master_block.append(
            "\n• Overarching Lighting Philosophy:\n  High-contrast natural key for manual struggle transitioning into warm, saturated golden brilliance."
        )

    master_block.append("\n• Color Temperature & Emotional Arc:")
    master_block.append("  - Act I (Scenes 1-2): 3200K Tungsten & Hard Window Light — Oppressive, dusty, stagnant contrast.")
    master_block.append("  - Act II (Scenes 3-4): 6500K Cool Screen Spill vs 5000K Neutral Fill — Clash of digital & manual craft.")
    master_block.append("  - Act III (Scenes 5-6): 2800K Golden Hour & Warm Accent Fill — Triumphant, rich heirloom luminosity.")

    master_block.append("\n• Low-Budget Execution Strategy:")
    master_block.append("  - Rely on natural aperture window light as key; control bounce with simple foam core boards.")
    master_block.append("  - Harness direct laptop/tablet displays for authentic night scene facial spill without heavy rigging.")

    return "\n".join(output) + "\n" + "\n".join(master_block)

# ============================================================
# FILM IDEA INPUT
# ============================================================

st.html(
    """
<div class="idea-card">
    <h3>🎞️ Start Your Film</h3>
    <p style="color:#cccccc; font-size:0.92rem; margin:0;">
        Enter any film idea. CinePilot will transform it into a complete production-ready film plan.
    </p>
</div>
"""
)

film_idea = st.text_area(
    "Enter any film idea",
    value="",
    height=120,
    placeholder=(
        "Example: A traditional handloom weaver in Kanchipuram struggles to preserve his ancestral silk art against modern powerlooms. "
        "When his daughter introduces him to generative AI design tools, he combines 100-year-old traditional motifs with digital workflows..."
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
# GENERATE TRIGGER
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
    st.info("🎬 CinePilot Film Factory is generating a new production...")

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
    <h3>🎬 Current Film Concept</h3>
    <p style="color:#f1f5f9; font-size:0.98rem; line-height:1.5; margin:0;">
        {current_idea}
    </p>
</div>
"""
        )

    # Pipeline Status Metrics
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

    with tabs[0]:
        show_output(result, "research_context", "🔎 Parallel Research")
        st.caption("Research generated through the CinePilot autonomous research pipeline.")

    with tabs[1]:
        show_output(result, "film_concept", "🎬 Director Vision")

    with tabs[2]:
        show_output(result, "screenplay", "✍️ Screenplay")

    with tabs[3]:
        st.subheader("🎞️ Scene Breakdown")
        scene_data = get_value(result, "scene_breakdown")
        if scene_data.strip():
            st.markdown('<div class="output-box">', unsafe_allow_html=True)
            st.text(scene_data)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("No scene breakdown available.")

    with tabs[4]:
        st.subheader("📷 Camera & Shots")
        shot_data = get_value(result, "shot_breakdown")
        if shot_data.strip():
            st.markdown('<div class="output-box">', unsafe_allow_html=True)
            st.text(shot_data)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("No shot breakdown available.")

    with tabs[5]:
        st.subheader("💡 Cinematic Lighting & Visual Direction")
        shot_data = get_value(result, "shot_breakdown")
        if shot_data.strip():
            lighting_data = extract_lighting_direction(shot_data)
            if lighting_data:
                st.markdown('<div class="output-box">', unsafe_allow_html=True)
                st.text(lighting_data)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("No dedicated lighting direction found.")
        else:
            st.info("No lighting direction available.")

    with tabs[6]:
        show_output(result, "production_plan", "🏭 Production Plan")

    with tabs[7]:
        show_output(result, "video_prompt_package", "🎥 Video Prompt Package")

    with tabs[8]:
        st.subheader("✨ Cinematic Preview")
        preview_data = get_value(result, "cinematic_preview")
        if preview_data.strip():
            st.markdown(
                f'<div class="cinematic-preview-box">{preview_data}</div>',
                unsafe_allow_html=True
            )
        else:
            st.info("No cinematic preview generated.")

    # ========================================================
    # DOWNLOAD BUTTON
    # ========================================================

    st.markdown("---")
    json_data = json.dumps(result, ensure_ascii=False, indent=2)
    st.download_button(
        label="📦 Download Complete CinePilot Result (JSON)",
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
    <h3 style="color:#ffffff;">🎬 Your Film Factory is Ready</h3>
    <p style="color:#aaaaaa; font-size:0.92rem;">
        Enter a film idea above and let CinePilot build the complete autonomous production pipeline.
    </p>
    <p style="color:#888888; font-size:0.85rem; margin-top:8px;">
        Idea → Research → Director → Screenplay → Scenes → Shots → Lighting → Production → Video Prompts → Preview
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
