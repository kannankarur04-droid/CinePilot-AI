import os
import time
import json
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from parallel import Parallel
from google import genai


# ============================================================
# CINEPILOT — DYNAMIC AUTONOMOUS FILM FACTORY
# ============================================================

MODEL = "gemini-3.1-flash-lite"

parallel_client = Parallel(
    api_key=os.environ["PARALLEL_API_KEY"]
)

gemini_client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


# ============================================================
# GEMINI HELPER
# ============================================================

def _generate(prompt, retries=3):

    for attempt in range(retries):

        try:

            response = gemini_client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(
                f"⚠️ Gemini attempt "
                f"{attempt + 1}/{retries} failed: {e}"
            )

            if attempt < retries - 1:

                print("⏳ Retrying in 5 seconds...")

                time.sleep(5)

            else:

                raise


# ============================================================
# 1. DIRECTOR AGENT
# REAL PARALLEL RESEARCH — DYNAMIC
# ============================================================

def cinepilot_director_agent(film_idea):

    print("   🔎 Running REAL Parallel research...")

    research_objective = f"""
Research real-world information that can make this EXACT film idea
authentic, realistic, culturally grounded and production useful.

FILMMAKER IDEA:
{film_idea}

Research ONLY information relevant to this specific idea.

Consider:

- location
- profession
- community
- environment
- culture
- geography
- technology
- science
- social context
- practical constraints
- real-world risks
- authentic terminology
- believable production details

IMPORTANT:

Do NOT assume:

- handloom
- weaving
- agriculture
- fishing
- AI
- crime
- thriller
- romance
- supernatural
- village
- city

unless the filmmaker idea itself requires it.

Do not search for existing movie plots.

Use authoritative, local, academic, institutional,
government and reputable specialist sources where possible.
"""

    # Dynamic queries based on the actual filmmaker idea.
    search_queries = [
        film_idea,
        f"{film_idea} real world context",
        f"{film_idea} Tamil Nadu India",
        f"{film_idea} location profession culture"
    ]

    research = parallel_client.search(
        objective=research_objective,
        search_queries=search_queries
    )

    research_context = ""

    for i, result in enumerate(
        research.results[:8],
        1
    ):

        title = getattr(
            result,
            "title",
            ""
        )

        url = getattr(
            result,
            "url",
            ""
        )

        excerpts = getattr(
            result,
            "excerpts",
            []
        )

        research_context += f"""
SOURCE {i}

Title:
{title}

URL:
{url}

Evidence:
{excerpts}

"""


    # ========================================================
    # DIRECTOR PROMPT
    # ========================================================

    prompt = f"""
You are the CinePilot AI Director Agent.

The filmmaker has supplied this EXACT idea:

FILMMAKER IDEA:
{film_idea}


REAL-WORLD RESEARCH FROM PARALLEL:

{research_context}


Your task is to transform the filmmaker's idea into a completely
original production-ready film concept.

============================================================
MOST IMPORTANT RULE
============================================================

THE FILMMAKER IDEA IS THE SOURCE OF TRUTH.

You MUST preserve:

- protagonist
- profession
- setting
- central mystery
- central conflict
- relationships
- emotional premise
- genre direction
- important objects
- important locations

Do NOT replace the filmmaker's idea with another story.

Do NOT inject a previously generated story.

Do NOT use handloom/weaving unless explicitly required.

Do NOT use AI unless explicitly required.

Do NOT use agriculture unless explicitly required.

Do NOT use fishing unless explicitly required.

Do NOT use crime unless explicitly required.

Do NOT use supernatural elements unless explicitly required.

Do NOT force an inspirational technology story.

The genre should emerge naturally from the filmmaker idea.

============================================================
ORIGINALITY
============================================================

Do not copy an existing movie plot.

Create original characters and story development.

Use Parallel research only for factual authenticity.

Clearly separate researched facts from creative assumptions.

============================================================
PRODUCTION
============================================================

Make the story realistic for an independent Tamil film.

Avoid unnecessary expensive production requirements.

Technology, science, mystery and other elements must remain
believable unless the filmmaker explicitly asks for fantasy.

============================================================
CREATE
============================================================

1. TITLE

2. GENRE

3. LOGLINE

4. PROTAGONIST

5. STORY WORLD / SETTING

6. CENTRAL CONFLICT

7. SUPPORTING CHARACTERS

8. CHARACTER ARC

9. THREE-ACT STORY

10. EMOTIONAL CORE

11. VISUAL IDENTITY

12. RESEARCH-INFORMED DETAILS

13. ASSUMPTIONS

14. PRODUCTION CONSIDERATIONS

The concept should be suitable as the foundation for a
20–25 minute production-ready short film.

Return ONLY the Director Film Concept.
"""

    return (
        research_context,
        _generate(prompt)
    )


# ============================================================
# 2. SCREENPLAY AGENT
# DYNAMIC — DIRECTOR CONCEPT IS SOURCE OF TRUTH
# ============================================================

def cinepilot_script_agent(film_concept):

    prompt = f"""
You are the CinePilot AI Screenplay Agent.

Convert the following Director Agent film concept into a
production-ready Tamil short-film screenplay.

============================================================
DIRECTOR FILM CONCEPT
============================================================

{film_concept}


============================================================
CONTINUITY RULE
============================================================

The Director Agent concept is the SOURCE OF TRUTH.

Preserve exactly:

- protagonist
- profession
- setting
- supporting characters
- relationships
- central conflict
- mystery
- technology
- genre
- emotional direction
- important locations
- important objects

Do NOT replace the story with a different story.

Do NOT inject a handloom story.

Do NOT inject an AI story.

Do NOT inject agriculture.

Do NOT inject crime.

Do NOT inject thriller elements.

Do NOT inject supernatural elements.

UNLESS THEY ALREADY EXIST IN THE DIRECTOR CONCEPT.

Do not change the protagonist or family simply because another
story template is familiar.

============================================================
SCREENPLAY
============================================================

Create a cinematic but realistic 20–25 minute screenplay.

Use natural Tamil dialogue.

Simple English technical terms may be used when realistic.

Structure:

1. OPENING SCENE

2. ACT I

3. ACT II

4. ACT III

5. FINAL SCENE


For every major scene provide:

- Scene Number
- Location
- INT / EXT
- Time
- Characters
- Visual Action
- Dialogue
- Emotional Purpose
- Approximate Duration

Maintain continuity between every scene.

Return ONLY the screenplay.
"""

    return _generate(prompt)


# ============================================================
# 3. SCENE BREAKDOWN AGENT
# ============================================================

def cinepilot_scene_agent(screenplay):

    prompt = f"""
You are the CinePilot AI Scene Breakdown Agent.

Convert this screenplay into a detailed production-ready
scene breakdown.

SCREENPLAY:

{screenplay}


============================================================
RULES
============================================================

The screenplay is the SOURCE OF TRUTH.

Preserve:

- story
- characters
- locations
- profession
- genre
- conflict
- technology
- emotional direction

Do NOT rewrite the story.

Do NOT inject handloom/weaving.

Do NOT inject agriculture.

Do NOT inject AI.

Do NOT inject crime.

Do NOT inject supernatural elements.

unless already present in the screenplay.

Make every production detail practical for an independent
Tamil short film.


============================================================
FOR EVERY SCENE
============================================================

1. SCENE NUMBER

2. SCENE TITLE

3. LOCATION

4. INT / EXT

5. TIME OF DAY

6. DURATION

7. CHARACTERS

8. EXTRAS

9. KEY PROPS

10. SET / PRODUCTION DESIGN

11. COSTUME NOTES

12. LIGHTING

13. COLOR / VISUAL MOOD

14. CAMERA APPROACH

15. IMPORTANT SHOTS

16. SOUND DESIGN

17. DIALOGUE / ACTION HIGHLIGHTS

18. AI / VFX REQUIREMENTS

19. CONTINUITY NOTES

20. PRODUCTION DIFFICULTY

21. LOW-BUDGET ALTERNATIVE


============================================================
AFTER ALL SCENES
============================================================

A. TOTAL ESTIMATED RUNTIME

B. MASTER LOCATION LIST

C. MASTER CHARACTER LIST

D. MASTER PROP LIST

E. MASTER COSTUME LIST

F. MASTER VFX / AI REQUIREMENTS

G. SHOOTING PRIORITY ORDER

H. PRODUCTION RISKS

I. LOW-BUDGET PRODUCTION STRATEGY

Return ONLY the scene breakdown.
"""

    return _generate(prompt)


# ============================================================
# 4. SHOT DESIGN AGENT
# ============================================================

def cinepilot_shot_agent(scene_breakdown):

    prompt = f"""
You are the CinePilot AI Shot Design Agent.

Convert this production-ready scene breakdown into a detailed
cinematic shot list.

SCENE BREAKDOWN:

{scene_breakdown}


============================================================
RULES
============================================================

The scene breakdown is the SOURCE OF TRUTH.

Preserve the exact:

- story
- characters
- locations
- profession
- conflict
- genre
- technology
- visual world

Do NOT introduce unrelated story elements.

Do NOT inject handloom/weaving.

Do NOT inject agriculture.

Do NOT inject AI.

Do NOT inject crime.

Do NOT inject supernatural elements.

unless already required by the story.

All shots must be achievable for a low-budget independent film.


============================================================
SHOT FORMAT
============================================================

For every scene:

1. SCENE NUMBER

2. SHOT NUMBER

3. SHOT TYPE

4. CAMERA ANGLE

5. LENS SUGGESTION

6. CAMERA MOVEMENT

7. COMPOSITION

8. SUBJECT / ACTION

9. DIALOGUE

10. AUDIO / SOUND

11. ESTIMATED SHOT DURATION

12. TRANSITION

13. LIGHTING

14. VISUAL MOOD

15. AI / VFX / UI REQUIREMENT

16. CONTINUITY NOTE

17. PRODUCTION DIFFICULTY

18. LOW-BUDGET ALTERNATIVE


Use practical shot language:

EWS
WS
MS
MCU
CU
ECU
OTS
POV
INSERT


Create the visual language from the actual story.

============================================================
MASTER PLANS
============================================================

After all scenes provide:

A. MASTER SHOT COUNT

B. MASTER CAMERA PLAN

C. RECOMMENDED LENSES

D. CAMERA MOVEMENT PLAN

E. LIGHTING PLAN

F. SOUND RECORDING PLAN

G. AI / VFX SHOT LIST

H. MOST IMPORTANT HERO SHOTS

I. LOW-BUDGET CAMERA STRATEGY

J. SHOOTING ORDER RECOMMENDATION

Return ONLY the detailed shot breakdown.
"""

    return _generate(prompt)


# ============================================================
# 5. PRODUCTION PLAN AGENT
# ============================================================

def cinepilot_production_plan_agent(
    scene_breakdown,
    shot_breakdown
):

    prompt = f"""
You are the CinePilot AI Production Planning Agent.

Create a complete practical production plan from the actual
scene and shot breakdown.

============================================================
SCENE BREAKDOWN
============================================================

{scene_breakdown}


============================================================
SHOT BREAKDOWN
============================================================

{shot_breakdown}


============================================================
SOURCE OF TRUTH
============================================================

The supplied scene and shot breakdowns are the source of truth.

Do NOT invent:

- film title
- protagonist
- profession
- location
- supporting characters
- technology
- central conflict

Derive everything from the supplied material.

Do NOT inject handloom/weaving.

Do NOT inject agriculture.

Do NOT inject fishing.

Do NOT inject AI.

unless the supplied story actually requires it.


============================================================
CREATE
============================================================

1. PRODUCTION OVERVIEW

- Logline
- Genre
- Target Runtime
- Production Style
- Target Audience
- Core Visual Theme


2. MASTER CAST PLAN

For every character:

- Character
- Age if known
- Role
- Number of scenes
- Costume
- Props
- Performance notes


3. MASTER LOCATION PLAN

For every location:

- Location
- Scenes
- Required visual elements
- Time of day
- Lighting requirements
- Sound considerations
- Low-budget alternative


4. MASTER PROP PLAN

- Essential props
- Story-specific props
- Technology props if required
- Character props
- Background props


5. COSTUME PLAN

Scene-by-scene continuity.


6. CAMERA & EQUIPMENT PLAN

Include:

- Camera
- Lenses
- Tripod
- Gimbal
- Lighting
- Audio
- Reflector
- Smartphone if useful
- Backup equipment

Clearly mark:

MUST HAVE

NICE TO HAVE


7. AI / VFX / UI PRODUCTION PLAN

Only include requirements actually present in the story.

For each:

- Scene
- Shot
- Effect
- How to create
- Low-budget method
- Post-production priority


8. SOUND PLAN

Include:

- Dialogue
- Location ambience
- Story-specific sounds
- Device sounds if relevant
- Music
- Silence / emotional beats


9. SHOOTING SCHEDULE

Create a practical multi-day schedule based on the actual
scenes and locations.

Group scenes efficiently by location.

Do NOT use a fixed scene schedule.


10. DAILY CALL SHEET STYLE PLAN

For each day:

- Crew arrival
- Setup
- Shooting block 1
- Break
- Shooting block 2
- Pickups
- Backup footage
- Wrap


11. PRODUCTION RISK REGISTER

Include relevant risks such as:

- Weather
- Heat
- Crowd
- Location access
- Continuity
- Sound
- Lighting
- Equipment
- Actor availability
- Story-specific risks

For each:

RISK LEVEL + MITIGATION


12. LOW-BUDGET PRODUCTION STRATEGY


13. POST-PRODUCTION PLAN

- Editing
- Colour correction
- Sound
- Music
- VFX/UI
- Titles
- Subtitles
- Final export


14. PRODUCTION PRIORITY

A. MUST SHOOT

B. SHOULD SHOOT

C. OPTIONAL


15. FINAL PRODUCTION CHECKLIST

PRE-PRODUCTION
SHOOTING
BACKUP
POST-PRODUCTION
FINAL DELIVERY


Do not invent expensive production requirements.

Return a professional production-ready plan.
"""

    return _generate(prompt)


# ============================================================
# 6. VIDEO PROMPT PACKAGE AGENT
# ============================================================

def cinepilot_video_prompt_agent(
    scene_breakdown,
    shot_breakdown,
    production_plan
):

    prompt = f"""
You are the CinePilot AI Video Prompt Package Agent.

Create a production-ready cinematic AI video prompt package
for the EXACT film represented by the supplied production data.

============================================================
SCENE BREAKDOWN
============================================================

{scene_breakdown}


============================================================
SHOT BREAKDOWN
============================================================

{shot_breakdown}


============================================================
PRODUCTION PLAN
============================================================

{production_plan}


============================================================
CRITICAL CONTINUITY
============================================================

The supplied material is the SOURCE OF TRUTH.

Preserve:

- characters
- appearance
- costumes
- locations
- props
- profession
- story
- genre
- lighting
- camera language
- emotional tone

Do NOT introduce unrelated elements.

Do NOT inject a handloom story.

Do NOT inject agriculture.

Do NOT inject AI.

Do NOT inject crime.

Do NOT inject supernatural elements.

unless already present in the supplied material.


============================================================
FOR EACH IMPORTANT SHOT
============================================================

1. SCENE NUMBER

2. SHOT NUMBER

3. VIDEO PROMPT

4. CHARACTER DESCRIPTION

5. ACTION

6. ENVIRONMENT

7. CAMERA

8. LENS

9. CAMERA MOVEMENT

10. LIGHTING

11. COLOR / MOOD

12. SOUND

13. DURATION

14. CONTINUITY NOTES

15. NEGATIVE PROMPT


============================================================
MASTER GUIDES
============================================================

A. MASTER VISUAL STYLE

B. CHARACTER CONSISTENCY GUIDE

C. LOCATION CONSISTENCY GUIDE

D. STORY-SPECIFIC VISUAL GUIDE

E. TECHNOLOGY / UI VISUAL GUIDE if relevant

F. CAMERA LANGUAGE

G. NEGATIVE PROMPT MASTER

H. HERO SHOTS FOR CINEMATIC PREVIEW


Keep everything realistic and production-friendly.

Return ONLY the complete VIDEO PROMPT PACKAGE.
"""

    return _generate(prompt)


# ============================================================
# 7. CINEMATIC PREVIEW AGENT
# ============================================================

def cinepilot_preview_agent(video_prompt_package):

    prompt = f"""
You are the CinePilot AI Cinematic Preview Director.

Create a concise cinematic preview specification for the exact
film represented by this VIDEO PROMPT PACKAGE.

============================================================
VIDEO PROMPT PACKAGE
============================================================

{video_prompt_package}


============================================================
RULE
============================================================

The supplied video prompt package is the SOURCE OF TRUTH.

Do NOT change:

- film identity
- protagonist
- characters
- setting
- profession
- conflict
- genre
- technology
- visual style

Do NOT inject handloom/weaving.

Do NOT inject agriculture.

Do NOT inject AI.

Do NOT inject crime.

Do NOT inject supernatural elements.

unless already present.


============================================================
CREATE
============================================================

1. PREVIEW TITLE

2. MASTER VISUAL PROMPT

3. HERO FRAME 1

4. HERO FRAME 2

5. HERO FRAME 3

6. CHARACTER CONSISTENCY

7. LOCATION / ENVIRONMENT

8. LIGHTING

9. CAMERA / LENS

10. COLOR / MOOD

11. TECHNOLOGY / VFX VISUALIZATION if relevant

12. NEGATIVE PROMPT

13. CONTINUITY NOTES


The preview should feel like a professional film pitch /
director's visual board.

Return ONLY the cinematic preview specification.
"""

    return _generate(prompt)


# ============================================================
# 8. ORCHESTRATOR
# ============================================================

def cinepilot_orchestrator(film_idea):

    film_idea = film_idea.strip()

    if not film_idea:

        raise ValueError(
            "Film idea cannot be empty."
        )


    print("=" * 70)
    print("🎬 CINEPILOT — AUTONOMOUS FILM FACTORY")
    print("=" * 70)

    print(
        f"\n💡 USER IDEA:\n{film_idea}"
    )


    # --------------------------------------------------------
    # 1 DIRECTOR + PARALLEL
    # --------------------------------------------------------

    print(
        "\n1️⃣ Director Agent → "
        "Dynamic Parallel Research + Film Concept"
    )

    research_context, film_concept = (
        cinepilot_director_agent(
            film_idea
        )
    )

    print(
        "   ✅ Film Concept generated"
    )


    # --------------------------------------------------------
    # 2 SCREENPLAY
    # --------------------------------------------------------

    print(
        "\n2️⃣ Screenplay Agent"
    )

    screenplay = cinepilot_script_agent(
        film_concept
    )

    print(
        "   ✅ Screenplay generated"
    )


    # --------------------------------------------------------
    # 3 SCENES
    # --------------------------------------------------------

    print(
        "\n3️⃣ Scene Breakdown Agent"
    )

    scene_breakdown = cinepilot_scene_agent(
        screenplay
    )

    print(
        "   ✅ Scene Breakdown generated"
    )


    # --------------------------------------------------------
    # 4 SHOTS
    # --------------------------------------------------------

    print(
        "\n4️⃣ Shot Design Agent"
    )

    shot_breakdown = cinepilot_shot_agent(
        scene_breakdown
    )

    print(
        "   ✅ Shot Breakdown generated"
    )


    # --------------------------------------------------------
    # 5 PRODUCTION
    # --------------------------------------------------------

    print(
        "\n5️⃣ Production Plan Agent"
    )

    production_plan = (
        cinepilot_production_plan_agent(
            scene_breakdown,
            shot_breakdown
        )
    )

    print(
        "   ✅ Production Plan generated"
    )


    # --------------------------------------------------------
    # 6 VIDEO PROMPTS
    # --------------------------------------------------------

    print(
        "\n6️⃣ Video Prompt Agent"
    )

    video_prompt_package = (
        cinepilot_video_prompt_agent(
            scene_breakdown,
            shot_breakdown,
            production_plan
        )
    )

    print(
        "   ✅ Video Prompt Package generated"
    )


    # --------------------------------------------------------
    # 7 PREVIEW
    # --------------------------------------------------------

    print(
        "\n7️⃣ Cinematic Preview Agent"
    )

    cinematic_preview = (
        cinepilot_preview_agent(
            video_prompt_package
        )
    )

    print(
        "   ✅ Cinematic Preview generated"
    )


    # ========================================================
    # FINAL RESULT
    # ========================================================

    autonomous_result = {

        "film_idea":
            film_idea,

        "research_context":
            research_context,

        "film_concept":
            film_concept,

        "screenplay":
            screenplay,

        "scene_breakdown":
            scene_breakdown,

        "shot_breakdown":
            shot_breakdown,

        "production_plan":
            production_plan,

        "video_prompt_package":
            video_prompt_package,

        "cinematic_preview":
            cinematic_preview
    }


    result_path = (
        Path(__file__).resolve().parent
        / "cinepilot_result.json"
    )


    with open(
        result_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            autonomous_result,
            f,
            ensure_ascii=False,
            indent=2
        )


    print(
        "\n" + "=" * 70
    )

    print(
        "🎉 CINEPILOT ORCHESTRATOR COMPLETED"
    )

    print(
        "=" * 70
    )

    print(
        f"\n💾 Complete result saved:\n"
        f"{result_path}"
    )


    return autonomous_result


# ============================================================
# 9. FILM FACTORY ENTRY POINT
# ============================================================

def cinepilot_film_factory(film_idea):

    print(
        "\n🚀 CINEPILOT FILM FACTORY STARTING..."
    )

    print(
        f"💡 User Idea: {film_idea}"
    )


    if not film_idea or not film_idea.strip():

        raise ValueError(
            "Film idea cannot be empty."
        )


    result = cinepilot_orchestrator(
        film_idea.strip()
    )


    print(
        "\n" + "=" * 70
    )

    print(
        "🎬 CINEPILOT FILM FACTORY — COMPLETE"
    )

    print(
        "=" * 70
    )


    return result