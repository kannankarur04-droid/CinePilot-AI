# 🎬 CinePilot AI

## One Idea → Production-Ready Film Plan

CinePilot AI is an AI-powered film pre-production system that transforms a simple film idea into a structured, production-ready cinematic plan.

Instead of stopping at a story idea or screenplay, CinePilot takes the concept through multiple stages of filmmaking — from research and director vision to screenplay, scene design, camera planning, production planning, AI video prompts, and cinematic preview.

---

## 🚀 What CinePilot AI Does

Give CinePilot a simple film idea.

For example:

> A middle-aged man loses his business, faces humiliation while taking whatever work he can find, learns AI, and eventually becomes the owner of a startup.

CinePilot transforms that idea into a complete filmmaking pipeline:

```text
Film Idea
    ↓
Real-World Research
    ↓
Film Concept
    ↓
Director Vision
    ↓
Screenplay
    ↓
Scene Breakdown
    ↓
Camera & Shot Breakdown
    ↓
Production Plan
    ↓
AI Video Prompt Package
    ↓
Cinematic Preview
```

The goal is to bridge the gap between **creative storytelling** and **practical film production planning**.

---

# 🎯 Core Objective

CinePilot AI is designed to demonstrate how AI can function as an integrated film-production assistant.

The system can transform an arbitrary user-provided film idea into structured production information covering:

* Story development
* Research
* Screenwriting
* Scene planning
* Camera planning
* Lighting
* Production requirements
* AI video generation prompts
* Cinematic visual direction

---

# 🧠 Key Features

## 1. Any-Idea Film Generation

CinePilot is not locked to a single predefined story.

The user can provide a new film idea and the pipeline dynamically generates the downstream production stages from that idea.

Example tested ideas included:

* A fisherman in coastal Tamil Nadu discovering an abandoned lighthouse connected to his missing father.
* A young woman in Madurai discovering a secret underground library beneath her family's old house.
* A young woman discovering a hidden room containing her grandfather's old 16mm film camera and a mysterious family recording.

This demonstrates that the pipeline can work with different genres, locations, characters, and story premises.

---

## 2. Real Parallel Web Research

CinePilot performs real web research as part of the film-development workflow.

Research is used to provide contextual information that can influence the creative development of the film.

The research stage can provide:

* Relevant references
* Cultural context
* Location-related information
* Story inspiration
* Supporting research sources

Research results are incorporated into the film-development pipeline rather than being treated as a completely separate activity.

---

## 3. AI Director Vision

CinePilot develops a director-oriented creative vision for the story.

This includes:

* Genre
* Tone
* Visual identity
* Character direction
* Emotional arc
* Cinematic approach
* Production considerations

---

## 4. AI Screenplay Generation

The system converts the film concept into a structured screenplay.

The screenplay includes:

* Scene structure
* Characters
* Locations
* Actions
* Dialogue
* Visual direction
* Scene duration

---

## 5. Scene Breakdown

Each screenplay scene is converted into production-oriented information.

The scene breakdown can include:

* Location
* Characters
* Props
* Set design
* Costume
* Lighting
* Visual mood
* Camera direction
* Sound
* VFX requirements
* Continuity
* Production difficulty
* Low-budget alternatives

---

## 6. Camera & Shot Planning

CinePilot converts scenes into a cinematic camera plan.

The system can specify:

* Shot type
* Camera angle
* Lens
* Camera movement
* Composition
* Lighting
* Sound
* Visual purpose
* Hero shots
* Low-budget shooting strategies

This allows the creative idea to move closer to an actual shooting plan.

---

## 7. Production Planning

CinePilot generates a practical production plan covering areas such as:

* Cast
* Locations
* Props
* Costumes
* Camera equipment
* Lighting
* Sound
* VFX
* AI/video generation requirements
* Shooting schedule
* Call sheet considerations
* Production risks
* Post-production
* Low-budget alternatives

---

## 8. AI Video Prompt Package

CinePilot converts selected cinematic shots into detailed AI video-generation prompts.

Each prompt can contain:

* Character
* Action
* Environment
* Camera
* Lens
* Camera movement
* Lighting
* Colour/mood
* Sound
* Duration
* Continuity
* Negative prompts

This makes the output suitable as a bridge between film planning and AI-generated video workflows.

---

## 9. Cinematic Preview

The final stage creates a visual blueprint for the film.

The Cinematic Preview includes:

* Master visual prompt
* Hero frames
* Character consistency
* Location consistency
* Lighting progression
* Camera/lens language
* Colour and mood progression
* VFX direction
* Negative prompts
* Continuity notes

---

# 🏗️ CinePilot Pipeline

The complete pipeline is:

```text
┌───────────────────────────┐
│       USER FILM IDEA      │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│    REAL WEB RESEARCH      │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│      FILM CONCEPT         │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│      DIRECTOR VISION      │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│        SCREENPLAY         │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│     SCENE BREAKDOWN       │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│     CAMERA & SHOTS        │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│     PRODUCTION PLAN       │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│   VIDEO PROMPT PACKAGE    │
└─────────────┬─────────────┘
              ↓
┌───────────────────────────┐
│    CINEMATIC PREVIEW      │
└───────────────────────────┘
```

---

# 🎬 Demonstration Film

## THE LEGACY CAMERA

One of the final CinePilot QA demonstrations generated the following film concept.

### Premise

A young woman in Madurai discovers a secret room beneath her family's old house.

Inside, she finds an old 16mm film camera and a mysterious recording connected to her grandfather and the family's hidden past.

### Generated Film Title

**THE LEGACY CAMERA**

### Visual Arc

```text
Sterile / Desaturated
        ↓
Warm Discovery
        ↓
High-Contrast B&W Truth
        ↓
Hopeful Morning Resolve
```

The final cinematic preview maintains this visual progression across the production stages.

---

# 🧪 Phase 5 QA

CinePilot Phase 5 was tested with multiple independent film ideas to verify that the system was not dependent on a single hard-coded story.

### Pipeline QA

| Stage                | Result |
| -------------------- | ------ |
| Real Research        | ✅ PASS |
| Film Concept         | ✅ PASS |
| Director Vision      | ✅ PASS |
| Screenplay           | ✅ PASS |
| Scene Breakdown      | ✅ PASS |
| Camera & Shots       | ✅ PASS |
| Production Plan      | ✅ PASS |
| Video Prompt Package | ✅ PASS |
| Cinematic Preview    | ✅ PASS |

### Runtime QA

The final runtime and JSON output were also validated.

```text
RUNTIME: PASS
JSON: PASS
```

All major generated output stages were confirmed to be present and non-empty.

---

# 🔄 Any-Idea Validation

The dynamic pipeline was tested using different story premises.

### Test 1 — Fisherman

```text
Fisherman
+
Coastal Tamil Nadu
+
Abandoned Lighthouse
+
Missing Father
```

Result:

```text
All major CinePilot stages generated successfully.
```

### Test 2 — Madurai Mystery

```text
Young Woman
+
Madurai
+
Old Family House
+
Underground Secret Room
+
Grandfather
+
16mm Film Camera
```

Result:

```text
All major CinePilot stages generated successfully.
```

These tests demonstrated that the production pipeline responds to the supplied film idea rather than relying on a single fixed story.

---

# 🛠️ Technology Stack

CinePilot AI uses a lightweight Python-based application architecture.

### Core Technologies

* Python
* Streamlit
* Google Gemini
* Google GenAI SDK
* Parallel Web Research
* python-dotenv
* JSON-based result storage

### AI Model

The current application uses:

```text
gemini-3.1-flash-lite
```

---

# 📁 Project Structure

The core working project contains:

```text
cinipilot/
│
├── app_cinematic_v2.py
├── cinepilot_runtime.py
├── cinepilot_result.json
├── .env
│
├── CinePilot_PHASE5_FULL_BACKUP_2026-09-07.zip
│
└── CinePilot_PHASE5_UI_WORKING_BACKUP_2026-09-08/
    ├── app_cinematic_v2.py
    └── cinepilot_runtime.py
```

### Main Application

`app_cinematic_v2.py`

Responsible for:

* Streamlit interface
* User film idea input
* Pipeline execution
* Results display
* Tab-based cinematic output
* Result download

### Runtime

`cinepilot_runtime.py`

Responsible for:

* Film factory pipeline
* Research integration
* AI generation stages
* Dynamic film-idea propagation
* Final structured result generation

---

# ⚙️ Installation

## 1. Clone or copy the project

Place the CinePilot project in a local directory.

Example:

```text
C:\Users\<USERNAME>\Desktop\cinipilot
```

## 2. Install Python

Recommended Python version used during development:

```text
Python 3.14.0
```

## 3. Install dependencies

```bash
pip install streamlit google-genai parallel-web python-dotenv
```

---

# 🔑 Environment Variables

Create a `.env` file in the project directory.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
PARALLEL_API_KEY=your_parallel_api_key
```

Do not commit API keys to GitHub or include them in the public repository.

---

# ▶️ Running CinePilot

From the project directory:

```bash
streamlit run app_cinematic_v2.py
```

Streamlit will start the CinePilot interface.

Enter a film idea and run the Film Factory pipeline.

---

# 🖥️ User Workflow

The basic workflow is:

### Step 1

Enter any film idea.

### Step 2

Run CinePilot.

### Step 3

The system performs the production pipeline.

### Step 4

Explore the generated stages through the application tabs:

```text
Research
Director
Screenplay
Scenes
Camera & Shots
Lighting
Production
Video Prompts
Cinematic Preview
```

### Step 5

Download the complete CinePilot result as a JSON file.

---

# 💡 Example Input

```text
A middle-aged man suffers a major business loss.
After years of taking whatever work he can find and facing humiliation,
he decides to learn AI.
Eventually, he builds an AI startup and becomes a successful entrepreneur.
```

CinePilot can transform this simple premise into a structured film-development workflow.

---

# 🎥 Why CinePilot?

Traditional AI story generation often stops at:

```text
Idea → Story
```

CinePilot attempts to extend that workflow:

```text
Idea
 ↓
Research
 ↓
Story
 ↓
Screenplay
 ↓
Scenes
 ↓
Shots
 ↓
Production
 ↓
AI Video Prompts
 ↓
Cinematic Visual Plan
```

The focus is therefore not only **"What is the story?"**

It is also:

> **"How can this story be prepared for production?"**

---

# 🌟 Key Innovation

CinePilot combines several filmmaking workflows into one AI-assisted pipeline.

### Creative Intelligence

AI helps develop:

* Story
* Characters
* Conflict
* Emotional arc
* Director vision

### Production Intelligence

AI helps plan:

* Scenes
* Shots
* Camera
* Lighting
* Props
* Locations
* Production requirements

### Generative Video Readiness

The system then converts cinematic decisions into structured prompts suitable for AI video generation workflows.

---

# 🎯 Current Status

## Phase 5 — COMPLETE

The current CinePilot prototype has completed its planned Phase 5 development and QA workflow.

```text
Core Pipeline        ✅
Dynamic Any-Idea     ✅
Real Research        ✅
Film Development     ✅
Production Planning  ✅
AI Video Prompts     ✅
Cinematic Preview    ✅
UI QA                 ✅
Backup                ✅
```

---

# 🔮 Future Improvements

Potential future development areas include:

* Tamil and multilingual output
* More language controls
* Advanced screenplay formatting
* Improved research relevance filtering
* Automatic shot-count validation
* Character image consistency
* AI-generated storyboard frames
* Direct AI video generation integration
* Automatic production budget estimation
* Location intelligence
* Advanced scheduling
* PDF screenplay export
* Production-ready call sheets
* Character and costume continuity tracking

---

# ⚠️ Known QA Note

During final Phase 5 QA, the Camera & Shots output contained a minor counting discrepancy:

```text
Listed shots: 14
Master shot count: 16
```

The underlying camera-planning output was successfully generated and the discrepancy does not prevent the core pipeline from functioning.

This can be addressed in a future QA refinement.

---

# 🔐 Security Note

Never commit secrets to source control.

The following should remain private:

```text
GEMINI_API_KEY
PARALLEL_API_KEY
```

Use environment variables or a secure secrets manager.

---

# 📜 Disclaimer

CinePilot AI is an experimental AI-assisted filmmaking and pre-production system.

Generated research, creative content, screenplay material, production recommendations, and AI prompts should be reviewed by human filmmakers before real-world production.

Research sources should also be independently verified when factual accuracy is important.

---

# 👨‍💻 Project

**CinePilot AI**

### Vision

> **One Idea → Production-Ready Film Plan**

CinePilot explores how AI can become a creative and production partner for independent filmmakers, creators, and storytellers.

---

## 🎬 From Idea to Production

```text
                     CINEPILOT AI

                       ONE IDEA
                          │
                          ▼
                    🔎 RESEARCH
                          │
                          ▼
                  🎬 FILM CONCEPT
                          │
                          ▼
                  🎭 DIRECTOR VISION
                          │
                          ▼
                    ✍️ SCREENPLAY
                          │
                          ▼
                   🎞️ SCENE PLAN
                          │
                          ▼
                    📷 SHOT PLAN
                          │
                          ▼
                   🏭 PRODUCTION
                          │
                          ▼
                  🎥 VIDEO PROMPTS
                          │
                          ▼
                 ✨ CINEMATIC PREVIEW
                          │
                          ▼
                 🎬 PRODUCTION-READY
                    FILM BLUEPRINT
```

---

**CinePilot AI — Turning a simple idea into a cinematic production blueprint.** 🎬
