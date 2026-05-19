import reflex as rx
import csv
from pathlib import Path

# =========================
# RESEARCH DATA
# =========================

# FINANCE TEXTS
Finance_Insight = " The Insight :  Through my independent interviews with seasoned wealth managers, senior advisors emphasized that while portfolio tech is moving incredibly fast, clients still demand human empathy, trust, and macro-judgment during times of market volatility. They don't look to an algorithm for reassurance."
Finance_Shift = " The Career Shift :  Executives agree that the entry-level role is changing. Junior analysts must pivot away from manual calculations and data-crunching to become data-literate managers of AI systems, elevating them into high-level strategy roles much faster."

# LEGAL TEXTS
Legal_Insight = " The Insight :  My research with practicing attorneys and compliance officers reveals that while AI tools can instantly draft standard contracts and review thousands of discovery documents, technology cannot replicate courtroom strategy, ethical judgment, or deep client advocacy."
Legal_Shift = " The Career Shift:  The consensus among senior partners is that junior lawyers need to spend less time on rote document review and quickly learn how to use AI for case synthesis, allowing them to focus on high-level legal strategy earlier in their careers."

# HEALTHCARE TEXTS
Health_Insight = " The Insight :  Medical professionals and nursing leads I spoke with stress that even as AI accelerates diagnostics and administrative charting, patient care still relies entirely on human bedside manner, complex triage judgment, and personal trust."
Health_Shift = " The Career Shift:  For incoming medical assistants and administrators, the job is transitioning away from manual data entry. New professionals must learn to oversee AI-driven workflow tools so they can maximize face-to-face patient time."

# MARKETING TEXTS
Market_Insight = " The Insight :  Marketing executives and creative directors noted that while generative AI can produce copy and graphics at massive scale, it completely lacks true cultural nuance, emotional resonance, and deep brand intuition."
Market_Shift = " The Career Shift:  The entry-level execution role is fading. Junior marketers are moving away from basic content creation and must quickly become expert prompt engineers, creative directors, and data strategists who know how to guide AI tools."

FIELD_DATA = {
    "finance": {
        "label": "Finance",
        "index": "High",
        "risk": "Moderate (High for data entry, low for strategy).",
        "verdict": Finance_Insight,
        "shift": Finance_Shift,
    },
    "legal": {
        "label": "Legal",
        "index": "High",
        "risk": "Low for attorneys; High for document-review roles.",
        "verdict": Legal_Insight,
        "shift": Legal_Shift,
    },
    "healthcare": {
        "label": "Healthcare",
        "index": "Moderate",
        "risk": "Near Zero for clinical care; High for administration.",
        "verdict": Health_Insight,
        "shift": Health_Shift,
    },
    "marketing": {
        "label": "Marketing",
        "index": "High",
        "risk": "High for execution; Low for creative strategy.",
        "verdict": Market_Insight,
        "shift": Market_Shift,
    },
}


# =========================
# STATE
# =========================

class State(rx.State):
    user_feedback: str = ""
    current_field: str = ""
    user_name: str = ""
    user_title: str = ""

    def set_user_feedback(self, value):
        self.user_feedback = value

    def set_current_field(self, value):
        self.current_field = value

    def set_user_name(self, value):
        self.user_name = value

    def set_user_title(self, value):
        self.user_title = value

    ai_index: str = ""
    displacement_risk: str = ""
    professional_verdict: str = ""
    professional_shift: str = ""

    feedback_submitted: bool = False

    def process_field(self):

        field = self.current_field.lower().strip()

        print("FIELD ENTERED: ", field)

        self.feedback_submitted = False
        self.user_feedback = ""

        data = FIELD_DATA.get(field)

        if data:
            self.ai_index = data["index"]
            self.displacement_risk = data["risk"]
            self.professional_verdict = data["verdict"]
            self.professional_shift = data["shift"]
            self.current_field = data["label"]

        else:
            self.ai_index = "Unknown"
            self.displacement_risk = "Unknown"
            self.professional_verdict = (
                "Error: Field keyword not recognized. "
                "Please type Finance, Legal, Healthcare, or Marketing."
            )
            self.professional_shift = ""

    def submit_feedback(self):

        feedback = self.user_feedback.strip()

        if not feedback:
            return

        file_path = Path("feedback_log.csv")

        file_exists = file_path.exists()

        with open(file_path, "a", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            if not file_exists:
                writer.writerow([
                    "field",
                    "name",
                    "title",
                    "feedback"
                ])

            writer.writerow([
                self.current_field,
                self.user_name.strip() or "Anonymous",
                self.user_title.strip() or "Not Specified",
                feedback
            ])

        self.feedback_submitted = True


# =========================
# CARD COMPONENT
# =========================

def info_card(title: str, desc: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold",
            margin_bottom="0.25rem",
        ),

        rx.text(
            desc,
            font_size="0.85rem",
            color="#a3a3a3",
        ),

        border="1px solid #262626",
        padding="1.25rem",
        border_radius="0.375rem",
        background_color="#171717",
        width="100%",

        transition="a11 0.2s ease",
        cursor="pointer",

        _hover={
            "transform": "translateY(-3px)",
            "border_color": "#ffffff",
        },
    )


# =========================
# PAGE
# =========================

def index() -> rx.Component:
    return rx.box(

        rx.vstack(

            # ================= HEADER =================

            rx.flex(

                rx.text(
                    "Workforce Insights",
                    font_size="1.25rem",
                    font_weight="bold",
                    letter_spacing="0.05em",
                ),

                rx.spacer(),

                rx.link(
                    "Contact Researcher",
                    href="#contact",
                    color="#a3a3a3",
                    font_size="0.875rem",
                    _hover={"color": "#ffffff"},
                ),

                width="100%",
                padding_y="1.5rem",
                border_bottom="1px solid #262626",
            ),

            # ================= HERO =================

            rx.vstack(

                rx.text(
                    "Workforce Automation Research Dashboard",
                    font_size="2.25rem",
                    font_weight="bold",
                    text_align="center",
                    line_height="1.1",
                ),

                rx.text(
                    "Interview Based Industry Research Initiative",
                    font_size="1.125rem",
                    color="#a3a3a3",
                    text_align="center",
                ),

                align="center",
                margin_y="3rem",
            ),

            # ================= SYSTEM INFO =================

            rx.vstack(

                rx.text(
                    " Executive Summary and Insights ",
                    font_size="0.90rem",
                    font_weight="bold",
                    color="#a3a3a3",
                    letter_spacing="0.1em",
                    text_transform="uppercase",
                ),

                rx.text(

                    "• This dashboard serves as a high value informational foundation built on primary insights gathered from direct interviews with industry professionals right here in Rochester, New York. Rather than predicting the future with absolute certainty, it synthesizes local data to document recurring strategic patterns, operational shifts, and emerging workforce automation trends.",
                    color="#d4d4d4",
                    font_size="0.95rem",
                ),



                background_color="#171717",
                border="1px solid #262626",
                padding="2rem",
                border_radius="0.5rem",
                align_items="flex-start",
                box_shadow="0 0 20px rgba(255, 255, 255, 0.03)",
                width="100%",
                spacing="3",
            ),

            # ================= INDUSTRIES =================

            rx.grid(

                info_card(
                    "💼 Finance",
                    "Financial Advisors, Wealth Managers, Corporate Bankers",
                ),

                info_card(
                    "⚖️ Legal",
                    "Attorneys, Paralegals, Compliance Officers",
                ),

                info_card(
                    "🩺 Healthcare",
                    "Physicians, Nursing Leads, Medical Administrators",
                ),

                info_card(
                    "📣 Marketing",
                    "Creative Directors, Strategists, Media Executives",
                ),

                columns="2",
                spacing="4",
                width="100%",
                margin_y="2.5rem",
            ),

            # ================= INPUT =================

            rx.vstack(

                rx.text(
                    "Industry Query",
                    font_size="0.875rem",
                    font_weight="bold",
                    color="#a3a3a3",
                    align_self="flex-start",
                ),

                rx.flex(

                    rx.input(
                        placeholder="Type Finance, Legal, Healthcare, or Marketing...",
                        id="industry_query",
                        on_change=State.set_current_field,
                        width="100%",
                        background_color="#0a0a0a",
                        border="1px solid #404040",
                        color="#ffffff",
                        _focus={"border_color": "#ffffff"},
                    ),

                    rx.button(
                        "Generate Report",
                        on_click=State.process_field,
                        background_color="#ffffff",
                        color="#000000",
                        font_weight="bold",

                        border_radius="0.5rem",
                        padding_x="1.25rem",

                        transition="a11 0.2s ease",

                        _hover={
                            "background-color": "#d4d4d4",
                            "transform": "transformY(-1px)",
                        },
                    ),

                    width="100%",
                    spacing="3",
                ),

                width="100%",
                background_color="#171717",
                border="1px solid #262626",
                padding="2rem",
                border_radius="0.5rem",
                margin_bottom="2.5rem",
            ),

            # ================= RESULTS =================

            rx.cond(

                State.professional_verdict,

                rx.vstack(

                    rx.text(
                        State.current_field,
                        size="6",
                        width="100%",
                        border_bottom="2px solid #ffffff",
                        padding_bottom="0.5rem",

                    ),

                    rx.flex(
                        rx.text(
                            "AI Transformation Index:",
                            font_weight="bold",
                            color="#a3a3a3",
                        ),

                        rx.text(State.ai_index),

                        spacing="2",
                    ),

                    rx.flex(
                        rx.text(
                            "Displacement Risk:",
                            font_weight="bold",
                            color="#a3a3a3",
                        ),

                        rx.text(State.displacement_risk),

                        spacing="2",
                    ),

                    rx.vstack(

                        rx.text(
                            "Interview Synthesis",
                            font_weight="bold",
                            color="#a3a3a3",
                        ),

                        rx.vstack(
                            rx.text(
                                State.professional_verdict,
                                line_height="1.9",
                                color="#f5f5f5",
                            ),

                            rx.text(
                                State.professional_shift,
                                line_height="1.9",
                                color="#f5f5f5",
                            )
                        ),

                        align_items="flex-start",
                        spacing="2",
                    ),

                    background_color="#171717",
                    border="1px solid #262626",
                    padding="2rem",
                    border_radius="0.5rem",
                    width="100%",
                    align_items="flex-start",
                    spacing="4",
                    margin_bottom="2.5rem",
                ),
            ),

            # ================= FEEDBACK =================

            rx.cond(

                (State.ai_index != "") & (State.ai_index != "Unknown"),

                rx.vstack(

                    rx.text(
                        " Field Feedback ",
                        font_size="0.90rem",
                        font_weight="bold",
                        color="#a3a3a3",
                        letter_spacing="0.1em",
                        text_transform="none",
                    ),

                    rx.text(
                        "If you currently work in this industry, your perspective is valuable. "
                        "Does this research summary align with your real-world experience?",
                        font_size="0.95rem",
                        color="#d4d4d4",
                    ),

                    rx.cond(

                        ~State.feedback_submitted,

                        rx.vstack(

                            rx.text_area(
                                placeholder="Share your thoughts...",
                                value=State.user_feedback,
                                on_change=State.set_user_feedback,
                                width="100%",
                                background_color="#0a0a0a",
                                border="1px solid #262626",
                                color="#ffffff",
                            ),

                            rx.flex(

                                rx.input(
                                    placeholder="Your Name (Optional)",
                                    value=State.user_name,
                                    on_change=State.set_user_name,
                                    background_color="#0a0a0a",
                                    border="1px solid #262626",
                                    color="#ffffff",
                                    width="100%",
                                ),

                                rx.input(
                                    placeholder="Your Industry Title (Optional)",
                                    value=State.user_title,
                                    on_change=State.set_user_title,
                                    background_color="#0a0a0a",
                                    border="1px solid #262626",
                                    color="#ffffff",
                                    width="100%",
                                ),

                                width="100%",
                                spacing="3",
                            ),

                            rx.button(
                                "Submit Feedback",
                                on_click=State.submit_feedback,
                                background_color="#ffffff",
                                color="#000000",
                                font_weight="bold",
                                align_self="flex-end",
                                _hover={"background_color": "#e5e5e5"},
                            ),

                            width="100%",
                            spacing="3",
                        ),

                        rx.box(

                            rx.text(
                                "Thank you. Your response has been logged successfully.",
                                color="#22c55e",
                                font_weight="bold",
                            ),

                            padding="1rem",
                            border="1px dashed #22c55e",
                            border_radius="0.375rem",
                            width="100%",
                            text_align="center",
                        ),
                    ),

                    background_color="#171717",
                    border="1px solid #262626",
                    padding="2rem",
                    border_radius="0.5rem",
                    width="100%",
                    align_items="flex-start",
                    spacing="3",
                    margin_bottom="2.5rem",
                ),
            ),

            # ================= ABOUT =================

            rx.vstack(

                rx.text(
                    "About The Project and Creator",
                    font_size="1.25rem",
                    font_weight="bold",
                    width="100%",
                    border_bottom="1px solid #262626",
                    padding_bottom="0.5rem",
                ),

                rx.text(
                    "This independent research initiative and dashboard were developed to explore how AI technology is reshaping professions through workflow automation, strategic augmentation, and organizational restructuring. As my first major development project, this platform represents six months of intensive research, synthesizing primary data gathered from direct interviews with local industry professionals right here in Rochester, New York.",
                    line_height="1.6",
                    color="#f5f5f5",

                ),

                rx.text(
                    "By building and debugging this functional prototype, my goal was to bridge the gap between raw qualitative data and interactive software to showcase real-world workforce transformations. This is just the beginning for this platform, and I am looking forward to continuously improving it over time.",
                    line_height="1.6",
                    color="#f5f5f5",
                ),

                background_color="#111111",
                border="1px solid #262626",
                padding="2rem",
                border_radius="0.5rem",
                width="100%",
                align_items="flex-start",
                spacing="3",
                margin_bottom="2.5rem",
            ),

            # ================= CONTACT =================

            rx.vstack(

                rx.text(
                    "Professional Inquiries",
                    font_size="1.25rem",
                    font_weight="bold",
                    width="100%",
                    border_bottom="1px solid #262626",
                    padding_bottom="0.5rem",
                ),

                rx.text(
                    "For research collaborations, professional discussions, or to share your own industry insights regarding workforce automation, please connect through the channel below.",
                    line_height="1.9",
                    color="#f5f5f5",
                ),

                rx.link(

                    rx.button(
                        "Connect on LinkedIn",
                        background_color="transparent",
                        border="1px solid #ffffff",
                        color="#ffffff",
                        font_weight="bold",
                        _hover={
                            "background_color": "#ffffff",
                            "color": "#000000",
                        },
                    ),

                    href="https://www.linkedin.com",
                    is_external=True,
                ),

                id="contact",
                background_color="#111111",
                border="1px solid #262626",
                padding="2rem",
                border_radius="0.5rem",
                width="100%",
                align_items="flex-start",
                spacing="3",
                margin_bottom="5rem",
            ),

            max_width="48rem",
            width="100%",
            spacing="2",
        ),

        background_color="#0a0a0a",
        color="#ffffff",
        min_height="100vh",
        display="flex",
        justify_content="center",
        padding_x="1.5rem",
    )


# =========================
# APP
# =========================

app = rx.App()
app.add_page(index)