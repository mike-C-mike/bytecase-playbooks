"""Tkinter GUI for ByteCase Playbooks."""
import json
import os
import random
import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from bytecase_theme import apply_theme, configure_toplevel, get_current_theme, style_text_widget
from playbook_data import (
    APP_ATTRIBUTION,
    APP_DOMAIN,
    APP_NAME,
    APP_SUBTITLE,
    APP_VERSION,
    GLOSSARY,
    ARTIFACT_AREAS,
    INVESTIGATIVE_QUESTIONS,
    CONTROL_CONTEXT_PROMPTS,
    SCENARIO_CARDS,
    SCENARIO_COACHING_QUESTIONS,
    DECISION_PATHS,
    PLAYBOOKS,
    PLAYBOOK_BOUNDARY,
    categories,
    get_playbook,
    search_glossary,
    search_playbooks,
    search_artifact_areas,
    search_investigative_questions,
    search_scenario_cards,
    search_scenario_coaching_questions,
)
from coach_questions import (
    BUILT_IN_PACK_NAME,
    import_question_pack,
    load_coach_questions,
    question_pack_directory,
    question_pack_records,
    search_coach_questions,
    set_question_pack_enabled,
    validate_question_pack_file,
)
from session_core import create_session, load_session, save_session_outputs, session_summary
from settings_service import DEFAULT_OUTPUT_ROOT, get_output_root, load_settings, save_settings
from validators import validate_session


class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, colors, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.colors = colors
        self.canvas = tk.Canvas(self, highlightthickness=0, bg=colors["app_background"])
        self.v_scroll = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame = ttk.Frame(self.canvas)
        self.window_id = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.v_scroll.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.v_scroll.grid(row=0, column=1, sticky="ns")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, _event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.window_id, width=event.width)

    def _on_mousewheel(self, event):
        try:
            target = self.winfo_containing(event.x_root, event.y_root)
        except Exception:
            return
        if target is None:
            return
        try:
            widget = target
            while widget is not None:
                if widget in (self, self.canvas, self.frame):
                    self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
                    return
                widget = getattr(widget, "master", None)
        except Exception:
            return


class PlaybooksApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.settings = load_settings()
        self.colors = apply_theme(root, self.settings)
        self.root.title(f"{APP_NAME} v{APP_VERSION}")
        self.root.geometry("1180x760")
        self.root.minsize(1060, 680)
        self.session = create_session(PLAYBOOKS[0]["id"], self.settings.get("defaults", {}).get("mode", "Field Reference"))
        self.current_step_index = 1
        self.last_export_folder = None
        self.step_check_vars = {}
        self.step_note_widgets = {}
        self.coach_questions = load_coach_questions()
        self.coach_visible_questions = list(self.coach_questions)
        self.current_coach_index = 0
        self.coach_answer_var = tk.IntVar(value=-1)
        self.coach_attempted = 0
        self.coach_correct = 0
        self.coach_results = {}
        self.coach_set_label = "All Questions"
        self._build_ui()
        self.refresh_all()

    def _build_ui(self):
        header = ttk.Frame(self.root)
        header.pack(fill="x", padx=14, pady=(12, 6))
        ttk.Label(header, text=APP_NAME, style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text=APP_SUBTITLE, style="Muted.TLabel").pack(anchor="w")
        ttk.Label(header, text=APP_ATTRIBUTION, style="Muted.TLabel").pack(anchor="w")


        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=14, pady=(0, 12))

        self.start_tab = ScrollableFrame(self.notebook, self.colors)
        self.workbench_tab = ttk.Frame(self.notebook)
        self.library_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.start_tab, text="Home")
        self.notebook.add(self.workbench_tab, text="Workbench")
        self.notebook.add(self.library_tab, text="Library")

        self.workbench_notebook = ttk.Notebook(self.workbench_tab)
        self.workbench_notebook.pack(fill="both", expand=True)
        self.decision_tab = ScrollableFrame(self.workbench_notebook, self.colors)
        self.playbook_tab = ScrollableFrame(self.workbench_notebook, self.colors)
        self.artifact_tab = ScrollableFrame(self.workbench_notebook, self.colors)
        self.scenario_tab = ScrollableFrame(self.workbench_notebook, self.colors)
        self.coach_tab = ScrollableFrame(self.workbench_notebook, self.colors)
        self.workbench_notebook.add(self.decision_tab, text="Guide")
        self.workbench_notebook.add(self.playbook_tab, text="Playbook")
        self.workbench_notebook.add(self.artifact_tab, text="Artifacts")
        self.workbench_notebook.add(self.scenario_tab, text="Coaching")
        self.workbench_notebook.add(self.coach_tab, text="Drills")

        self.library_notebook = ttk.Notebook(self.library_tab)
        self.library_notebook.pack(fill="both", expand=True)
        self.session_tab = ScrollableFrame(self.library_notebook, self.colors)
        self.reference_tab = ScrollableFrame(self.library_notebook, self.colors)
        self.question_packs_tab = ScrollableFrame(self.library_notebook, self.colors)
        self.settings_tab = ScrollableFrame(self.library_notebook, self.colors)
        self.library_notebook.add(self.session_tab, text="Save / Export")
        self.library_notebook.add(self.reference_tab, text="Search")
        self.library_notebook.add(self.question_packs_tab, text="Question Packs")
        self.library_notebook.add(self.settings_tab, text="Settings")

        self._build_start_tab(self.start_tab.frame)
        self._build_decision_tab(self.decision_tab.frame)
        self._build_playbook_tab(self.playbook_tab.frame)
        self._build_session_tab(self.session_tab.frame)
        self._build_artifact_tab(self.artifact_tab.frame)
        self._build_scenario_tab(self.scenario_tab.frame)
        self._build_coach_tab(self.coach_tab.frame)
        self._build_question_packs_tab(self.question_packs_tab.frame)
        self._build_reference_tab(self.reference_tab.frame)
        self._build_settings_tab(self.settings_tab.frame)

    def _panel(self, parent, title=None):
        panel = ttk.LabelFrame(parent, text=title) if title else ttk.Frame(parent, style="Panel.TFrame")
        panel.pack(fill="x", padx=10, pady=8)
        return panel

    def show_start_page(self):
        self.notebook.select(self.start_tab)

    def show_guide_page(self):
        self.notebook.select(self.workbench_tab)
        self.workbench_notebook.select(self.decision_tab)

    def show_playbook_page(self):
        self.notebook.select(self.workbench_tab)
        self.workbench_notebook.select(self.playbook_tab)

    def show_artifact_page(self):
        self.notebook.select(self.workbench_tab)
        self.workbench_notebook.select(self.artifact_tab)

    def show_scenario_page(self):
        self.notebook.select(self.workbench_tab)
        self.workbench_notebook.select(self.scenario_tab)

    def show_coach_page(self):
        self.notebook.select(self.workbench_tab)
        self.workbench_notebook.select(self.coach_tab)

    def show_question_packs_page(self):
        self.notebook.select(self.library_tab)
        self.library_notebook.select(self.question_packs_tab)

    def show_session_page(self):
        self.notebook.select(self.library_tab)
        self.library_notebook.select(self.session_tab)

    def show_reference_page(self):
        self.notebook.select(self.library_tab)
        self.library_notebook.select(self.reference_tab)

    def show_settings_page(self):
        self.notebook.select(self.library_tab)
        self.library_notebook.select(self.settings_tab)

    def _build_start_tab(self, parent):
        intro = self._panel(parent, "What do you need help with?")
        intro.columnconfigure(1, weight=1)
        ttk.Label(intro, text="Mode:").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.mode_var = tk.StringVar(value=self.session.get("mode", "Field Reference"))
        mode = ttk.Combobox(intro, textvariable=self.mode_var, values=["Field Reference", "Learning / Refresher"], state="readonly", width=24)
        mode.grid(row=0, column=1, sticky="w", padx=10, pady=8)
        mode.bind("<<ComboboxSelected>>", lambda _e: self.set_mode())
        ttk.Button(intro, text="Boundary", command=self.show_boundary).grid(row=0, column=2, padx=10, pady=8)
        ttk.Button(intro, text="Guide Me", style="Accent.TButton", command=self.show_guide_page).grid(row=0, column=3, padx=10, pady=8)
        ttk.Button(intro, text="Search Reference", command=self.show_reference_page).grid(row=0, column=4, padx=10, pady=8)

        lanes = self._panel(parent, "Main paths")
        lanes.columnconfigure(0, weight=1)
        lanes.columnconfigure(1, weight=1)
        lanes.columnconfigure(2, weight=1)
        path_items = [
            ("Workbench", "Use Guide, Playbooks, Artifacts, Coaching, and Drills from one focused work area.", self.show_guide_page),
            ("Practice Drills", "Run Coach drills, review missed questions, and strengthen examiner judgment.", self.show_coach_page),
            ("Library", "Save/export sessions, search reference content, manage question packs, or adjust settings.", self.show_session_page),
        ]
        for idx, (title, desc, command) in enumerate(path_items):
            card = ttk.Frame(lanes, style="Panel.TFrame")
            card.grid(row=0, column=idx, sticky="nsew", padx=8, pady=10)
            ttk.Label(card, text=title, style="Header.TLabel", wraplength=230).pack(anchor="w", padx=10, pady=(10, 4))
            ttk.Label(card, text=desc, style="Muted.TLabel", wraplength=230).pack(anchor="w", padx=10, pady=(0, 8))
            ttk.Button(card, text="Open", command=command).pack(anchor="w", padx=10, pady=(0, 10))

        selector = self._panel(parent, "Select a playbook")
        selector.columnconfigure(0, weight=1)
        selector.columnconfigure(1, weight=1)
        ttk.Label(selector, text="Category").grid(row=0, column=0, sticky="w", padx=10, pady=(8, 2))
        ttk.Label(selector, text="Playbooks").grid(row=0, column=1, sticky="w", padx=10, pady=(8, 2))
        self.category_var = tk.StringVar(value="All")
        self.category_box = ttk.Combobox(selector, textvariable=self.category_var, values=["All"] + categories(), state="readonly")
        self.category_box.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 8))
        self.category_box.bind("<<ComboboxSelected>>", lambda _e: self.populate_playbook_list())
        self.playbook_list = tk.Listbox(selector, height=8, exportselection=False)
        self.playbook_list.grid(row=1, column=1, sticky="nsew", padx=10, pady=(0, 8))
        self.playbook_list.bind("<<ListboxSelect>>", lambda _e: self.preview_selected_playbook())
        selector.rowconfigure(1, weight=1)
        buttons = ttk.Frame(selector)
        buttons.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 8))
        ttk.Button(buttons, text="Open Playbook", style="Accent.TButton", command=self.open_selected_playbook).pack(side="left", padx=(0, 8))
        ttk.Button(buttons, text="Learning View", command=lambda: self.quick_mode("Learning / Refresher")).pack(side="left", padx=(0, 8))
        ttk.Button(buttons, text="Field View", command=lambda: self.quick_mode("Field Reference")).pack(side="left", padx=(0, 8))

        preview = self._panel(parent, "Preview")
        self.preview_text = tk.Text(preview, height=12)
        self.preview_text.pack(fill="x", padx=10, pady=10)
        style_text_widget(self.preview_text, self.colors)
        self.preview_text.configure(state="disabled")

        quick = self._panel(parent, "Current playbook session")
        self.start_summary_var = tk.StringVar()
        ttk.Label(quick, textvariable=self.start_summary_var).pack(anchor="w", padx=10, pady=8)
        actions = ttk.Frame(quick)
        actions.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Button(actions, text="Continue", command=self.show_playbook_page).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Guide Me", command=self.show_guide_page).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Open JSON", command=self.open_session_json).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Save / Export", command=self.show_session_page).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Artifacts", command=self.show_artifact_page).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Coaching", command=self.show_scenario_page).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Drills", command=self.show_coach_page).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Search", command=self.show_reference_page).pack(side="left", padx=(0, 8))

    def _build_decision_tab(self, parent):
        intro = self._panel(parent, "Guide Me")
        ttk.Label(
            intro,
            text="Pick the situation closest to what you are doing. Playbooks will suggest the best built-in reference and explain why.",
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 4))
        ttk.Label(
            intro,
            text="This is not a case workflow tracker. It is a learning/reference shortcut into the right playbook.",
            wraplength=1040,
            style="Muted.TLabel",
        ).pack(anchor="w", padx=10, pady=(0, 8))

        chooser = self._panel(parent, "What are you working on?")
        chooser.columnconfigure(0, weight=1)
        chooser.columnconfigure(1, weight=1)
        self.decision_path_var = tk.StringVar(value=DECISION_PATHS[0]["label"] if DECISION_PATHS else "")
        self.decision_box = ttk.Combobox(
            chooser,
            textvariable=self.decision_path_var,
            values=[path["label"] for path in DECISION_PATHS],
            state="readonly",
        )
        self.decision_box.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.decision_box.bind("<<ComboboxSelected>>", lambda _e: self.refresh_decision_detail())
        ttk.Button(chooser, text="Show Recommendation", style="Accent.TButton", command=self.refresh_decision_detail).grid(row=0, column=1, sticky="w", padx=10, pady=10)

        detail = self._panel(parent, "Recommended reference path")
        self.decision_detail_text = tk.Text(detail, height=20)
        self.decision_detail_text.pack(fill="both", expand=True, padx=10, pady=10)
        style_text_widget(self.decision_detail_text, self.colors)
        self.decision_detail_text.configure(state="disabled")
        actions = ttk.Frame(detail)
        actions.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Button(actions, text="Open Recommended Playbook", style="Accent.TButton", command=self.open_recommended_playbook).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Use Learning Mode", command=lambda: self.open_recommended_playbook(force_mode="Learning / Refresher")).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Use Field Mode", command=lambda: self.open_recommended_playbook(force_mode="Field Reference")).pack(side="left", padx=(0, 8))

        reminder = self._panel(parent, "How to use this")
        ttk.Label(
            reminder,
            text=(
                "Use Field Reference when you are actively working and need concise order-of-operations reminders. "
                "Use Learning / Refresher when you have time to slow down and read the deeper explanation layer. "
                "Neither mode creates case notes or performs analysis."
            ),
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=10)
        self.refresh_decision_detail()

    def _build_playbook_tab(self, parent):
        top = self._panel(parent, "Current playbook")
        top.columnconfigure(0, weight=1)
        self.playbook_title_var = tk.StringVar()
        self.playbook_meta_var = tk.StringVar()
        ttk.Label(top, textvariable=self.playbook_title_var, font=("Segoe UI", 13, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=(8, 2))
        ttk.Label(top, textvariable=self.playbook_meta_var, style="Muted.TLabel").grid(row=1, column=0, sticky="w", padx=10, pady=(0, 8))
        ttk.Button(top, text="Use When", command=lambda: self.show_list_popup("Use When", self.current_playbook().get("use_when", []))).grid(row=0, column=1, padx=5, pady=8)
        ttk.Button(top, text="Pause When", command=lambda: self.show_list_popup("Avoid / Pause When", self.current_playbook().get("avoid_when", []))).grid(row=0, column=2, padx=5, pady=8)

        nav = self._panel(parent, "Steps")
        nav.columnconfigure(0, weight=1)
        self.steps_tree = ttk.Treeview(nav, columns=("status", "title"), show="headings", height=8)
        self.steps_tree.heading("status", text="Done")
        self.steps_tree.heading("title", text="Step")
        self.steps_tree.column("status", width=70, stretch=False)
        self.steps_tree.column("title", width=760)
        self.steps_tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.steps_tree.bind("<<TreeviewSelect>>", lambda _e: self.select_tree_step())
        nav_buttons = ttk.Frame(nav)
        nav_buttons.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
        ttk.Button(nav_buttons, text="Previous", command=self.previous_step).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Next", command=self.next_step).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Why?", command=lambda: self.show_step_panel("why")).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Tools", command=lambda: self.show_step_panel("tools")).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Artifacts", command=lambda: self.show_step_panel("artifacts")).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Cautions", command=lambda: self.show_step_panel("cautions")).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Document", command=lambda: self.show_step_panel("document")).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Commands", command=self.show_command_examples).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Does Not Prove", command=self.show_does_not_prove).pack(side="left", padx=(0, 8))
        ttk.Button(nav_buttons, text="Use Context", command=self.show_use_context).pack(side="left", padx=(0, 8))

        card = self._panel(parent, "Step card")
        card.columnconfigure(0, weight=1)
        self.step_header_var = tk.StringVar()
        self.step_focus_var = tk.StringVar()
        ttk.Label(card, textvariable=self.step_header_var, font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=(8, 2))
        self.step_check_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(card, text="Mark as reviewed", variable=self.step_check_var, command=self.update_step_checked).grid(row=0, column=1, sticky="e", padx=10, pady=8)
        ttk.Label(card, textvariable=self.step_focus_var, wraplength=980).grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=(0, 6))
        self.step_context_var = tk.StringVar()
        ttk.Label(card, textvariable=self.step_context_var, style="Muted.TLabel", wraplength=980).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=(0, 8))
        card_actions = ttk.Frame(card)
        card_actions.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ttk.Button(card_actions, text="Pop Out Reading", command=self.pop_out_current_reading).pack(side="left", padx=(0, 8))
        ttk.Button(card_actions, text="Deep Dive", command=self.show_deep_dive).pack(side="left", padx=(0, 8))
        ttk.Button(card_actions, text="Copy Summary", command=self.copy_step_summary).pack(side="left", padx=(0, 8))
        ttk.Button(card_actions, text="Copy Document List", command=self.copy_document_reminders).pack(side="left", padx=(0, 8))
        ttk.Button(card_actions, text="Copy Commands", command=self.copy_command_examples).pack(side="left", padx=(0, 8))

        detail = self._panel(parent, "Read this first")
        ttk.Label(
            detail,
            text="Read the guidance for the selected step first. Use the buttons above for focused explanations when you need more context.",
            style="Muted.TLabel",
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 0))
        self.detail_text = tk.Text(detail, height=16)
        self.detail_text.pack(fill="both", expand=True, padx=10, pady=10)
        style_text_widget(self.detail_text, self.colors)
        self.detail_text.configure(state="disabled")

        notes = self._panel(parent, "Your notes for this step")
        ttk.Label(
            notes,
            text="Optional reference notes for your own learning or session continuity. This is not a case notes area.",
            style="Muted.TLabel",
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 0))
        self.step_notes_text = tk.Text(notes, height=5)
        self.step_notes_text.pack(fill="x", padx=10, pady=10)
        style_text_widget(self.step_notes_text, self.colors)
        self.step_notes_text.bind("<FocusOut>", lambda _e: self.save_current_step_notes())
        self.step_notes_text.bind("<KeyRelease>", lambda _e: self.mark_dirty_step_notes())

    def _build_session_tab(self, parent):
        summary_panel = self._panel(parent, "Playbook progress")
        summary_panel.columnconfigure(0, weight=1)
        ttk.Label(
            summary_panel,
            text="This saves the current playbook, selected mode, current step, reviewed steps, and step reference notes. It does not create case notes or write under a case folder.",
            wraplength=1040,
            style="Muted.TLabel",
        ).grid(row=0, column=0, sticky="w", padx=10, pady=(8, 4))
        self.progress_summary_var = tk.StringVar()
        ttk.Label(summary_panel, textvariable=self.progress_summary_var).grid(row=1, column=0, sticky="w", padx=10, pady=(0, 8))

        review = self._panel(parent, "Review / export")
        self.review_text = tk.Text(review, height=14)
        self.review_text.pack(fill="x", padx=10, pady=10)
        style_text_widget(self.review_text, self.colors)
        self.review_text.configure(state="disabled")
        actions = ttk.Frame(review)
        actions.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Button(actions, text="Review", command=self.refresh_review).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Save Session", style="Accent.TButton", command=self.export_session).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Save + Open", command=lambda: self.export_session(open_after=True)).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Open Last", command=self.open_last_folder).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="New Session", command=self.new_session).pack(side="right", padx=(8, 0))

    def _build_artifact_tab(self, parent):
        intro = self._panel(parent, "Artifact Decision Helper")
        ttk.Label(
            intro,
            text=(
                "Start with the question you are trying to answer. Select the situation and the examiner question, "
                "then review artifact areas that may help, where those artifacts may be found, and common tools or methods used to collect or examine them."
            ),
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 4))
        ttk.Label(
            intro,
            text=(
                "Tool names are examples of commonly used industry tools or methods, not endorsements, recommendations, "
                "or validation statements. Validate tools locally and follow agency policy."
            ),
            wraplength=1040,
            style="Muted.TLabel",
        ).pack(anchor="w", padx=10, pady=(0, 8))

        helper = self._panel(parent, "What are you trying to understand?")
        helper.columnconfigure(1, weight=1)
        ttk.Label(helper, text="Situation").grid(row=0, column=0, sticky="w", padx=10, pady=(10, 4))
        self.artifact_situation_var = tk.StringVar(value="Dead-box laptop exam")
        situations = self.artifact_situation_values()
        self.artifact_situation_box = ttk.Combobox(helper, textvariable=self.artifact_situation_var, values=situations, state="readonly", width=36)
        self.artifact_situation_box.grid(row=0, column=1, sticky="ew", padx=10, pady=(10, 4))
        self.artifact_situation_box.bind("<<ComboboxSelected>>", lambda _e: self.refresh_artifact_questions())

        ttk.Label(helper, text="Question").grid(row=1, column=0, sticky="w", padx=10, pady=(4, 10))
        self.question_var = tk.StringVar()
        self.question_box = ttk.Combobox(helper, textvariable=self.question_var, values=[], state="readonly")
        self.question_box.grid(row=1, column=1, sticky="ew", padx=10, pady=(4, 10))
        self.question_box.bind("<<ComboboxSelected>>", lambda _e: self.show_question_detail())

        self.question_detail_text = tk.Text(helper, height=20)
        self.question_detail_text.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 10))
        style_text_widget(self.question_detail_text, self.colors)
        self.question_detail_text.configure(state="disabled")
        helper.rowconfigure(2, weight=1)
        q_actions = ttk.Frame(helper)
        q_actions.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ttk.Button(q_actions, text="Copy Guidance", command=self.copy_question_guidance).pack(side="left", padx=(0, 8))
        ttk.Button(q_actions, text="Use / Access Context", command=self.show_use_context).pack(side="left", padx=(0, 8))

        detail = self._panel(parent, "Artifact area detail")
        detail.columnconfigure(0, weight=1)
        detail.columnconfigure(1, weight=2)
        self.artifact_area_list = tk.Listbox(detail, height=8, exportselection=False)
        self.artifact_area_list.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.artifact_area_list.bind("<<ListboxSelect>>", lambda _e: self.show_artifact_area_detail())
        self.artifact_detail_text = tk.Text(detail, height=16)
        self.artifact_detail_text.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        style_text_widget(self.artifact_detail_text, self.colors)
        self.artifact_detail_text.configure(state="disabled")
        detail.rowconfigure(0, weight=1)
        actions = ttk.Frame(detail)
        actions.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ttk.Button(actions, text="Copy Artifact Detail", command=self.copy_artifact_guidance).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Search This", command=self.search_selected_artifact_area).pack(side="left", padx=(0, 8))

        self.refresh_artifact_questions()

    def _build_scenario_tab(self, parent):
        intro = self._panel(parent, "Coaching")
        ttk.Label(
            intro,
            text=(
                "Use Coaching when you want a mentoring-examiner style question path. "
                "Answer each step without seeing the result, then review the full path at the end. "
                "The goal is examiner mindset, not trivia."
            ),
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 4))
        ttk.Label(
            intro,
            text="This is not a tabletop exercise, certification test, finding generator, or substitute for agency policy. It is a structured coaching aid for careful forensic thinking.",
            wraplength=1040,
            style="Muted.TLabel",
        ).pack(anchor="w", padx=10, pady=(0, 8))

        selector = self._panel(parent, "Coaching path")
        selector.columnconfigure(1, weight=1)
        ttk.Label(selector, text="Path").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.coaching_prompt_var = tk.StringVar(value=SCENARIO_COACHING_QUESTIONS[0]["title"] if SCENARIO_COACHING_QUESTIONS else "")
        self.coaching_prompt_box = ttk.Combobox(selector, textvariable=self.coaching_prompt_var, values=[item["title"] for item in SCENARIO_COACHING_QUESTIONS], state="readonly")
        self.coaching_prompt_box.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.coaching_prompt_box.bind("<<ComboboxSelected>>", lambda _e: self.begin_coaching_path())
        ttk.Button(selector, text="Start / Reset Path", command=self.begin_coaching_path).grid(row=0, column=2, padx=10, pady=10)
        ttk.Button(selector, text="Next Path", command=self.next_coaching_prompt).grid(row=0, column=3, padx=10, pady=10)

        context = self._panel(parent, "Scenario context")
        self.coaching_context_var = tk.StringVar()
        ttk.Label(context, textvariable=self.coaching_context_var, wraplength=1040).pack(anchor="w", padx=10, pady=10)

        qpanel = self._panel(parent, "Mentor question")
        qpanel.columnconfigure(0, weight=1)
        self.coaching_progress_var = tk.StringVar(value="Question 1")
        ttk.Label(qpanel, textvariable=self.coaching_progress_var, style="Muted.TLabel").grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        self.coaching_question_var = tk.StringVar()
        ttk.Label(qpanel, textvariable=self.coaching_question_var, wraplength=1040, font=("Segoe UI", 11, "bold")).grid(row=1, column=0, sticky="w", padx=10, pady=(2, 6))
        self.coaching_answer_var = tk.IntVar(value=-1)
        self.coaching_choice_frame = ttk.Frame(qpanel)
        self.coaching_choice_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 6))

        actions = ttk.Frame(qpanel)
        actions.grid(row=3, column=0, sticky="ew", padx=10, pady=(2, 10))
        ttk.Button(actions, text="Previous", command=self.previous_coaching_step).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Record / Next", style="Accent.TButton", command=self.check_coaching_answer).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Finish & Review", command=self.show_coaching_answer).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Copy Review", command=self.copy_coaching_guidance).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Open Related Playbook", command=self.open_coaching_playbook).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Search Terms", command=self.search_coaching_terms).pack(side="left", padx=(0, 8))

        detail = self._panel(parent, "Path status / final review")
        self.coaching_feedback_text = tk.Text(detail, height=22)
        self.coaching_feedback_text.pack(fill="both", expand=True, padx=10, pady=10)
        style_text_widget(self.coaching_feedback_text, self.colors)
        self.coaching_feedback_text.configure(state="disabled")

        mindset = self._panel(parent, "Core mindset")
        ttk.Label(
            mindset,
            text=(
                "During a coaching path, the app records your choices without revealing the best answer. "
                "At the end, review the full chain: what the artifact supports, what context is missing, what alternatives exist, and what language avoids overclaiming."
            ),
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=10)
        self.begin_coaching_path()

    def _build_coach_tab(self, parent):
        intro = self._panel(parent, "Coach Mode")
        ttk.Label(
            intro,
            text=(
                "Use Coach Mode for quick examiner-thinking practice. It is designed as a refresher and learning aid: "
                "read the prompt, choose the safest answer, then review the explanation and follow-up questions."
            ),
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 4))
        ttk.Label(
            intro,
            text="This is not a certification test and it does not score case work. It reinforces guardrails, attribution caution, documentation habits, and examiner judgment.",
            wraplength=1040,
            style="Muted.TLabel",
        ).pack(anchor="w", padx=10, pady=(0, 8))

        controls = self._panel(parent, "Practice set")
        controls.columnconfigure(1, weight=1)
        pack_names = ["All"] + sorted({item.get("pack_name", BUILT_IN_PACK_NAME) for item in self.coach_questions})
        topics = ["All"] + sorted({item.get("topic", "General") for item in self.coach_questions})
        difficulties = ["All", "Novice", "Experienced", "Expert"]
        counts = ["All", "5", "10", "15", "20"]
        orders = ["In order", "Shuffle"]

        ttk.Label(controls, text="Pack").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.coach_pack_var = tk.StringVar(value="All")
        self.coach_pack_box = ttk.Combobox(controls, textvariable=self.coach_pack_var, values=pack_names, state="readonly", width=34)
        self.coach_pack_box.grid(row=0, column=1, sticky="w", padx=10, pady=8)
        self.coach_pack_box.bind("<<ComboboxSelected>>", lambda _e: self.start_coach_set())

        ttk.Label(controls, text="Topic").grid(row=1, column=0, sticky="w", padx=10, pady=(0, 8))
        self.coach_topic_var = tk.StringVar(value="All")
        self.coach_topic_box = ttk.Combobox(controls, textvariable=self.coach_topic_var, values=topics, state="readonly", width=34)
        self.coach_topic_box.grid(row=1, column=1, sticky="w", padx=10, pady=(0, 8))
        self.coach_topic_box.bind("<<ComboboxSelected>>", lambda _e: self.start_coach_set())

        ttk.Label(controls, text="Difficulty").grid(row=0, column=2, sticky="w", padx=(10, 2), pady=8)
        self.coach_difficulty_var = tk.StringVar(value="All")
        difficulty_box = ttk.Combobox(controls, textvariable=self.coach_difficulty_var, values=difficulties, state="readonly", width=18)
        difficulty_box.grid(row=0, column=3, sticky="w", padx=6, pady=8)
        difficulty_box.bind("<<ComboboxSelected>>", lambda _e: self.start_coach_set())

        ttk.Label(controls, text="Count").grid(row=1, column=2, sticky="w", padx=(10, 2), pady=(0, 8))
        self.coach_count_var = tk.StringVar(value="10")
        count_box = ttk.Combobox(controls, textvariable=self.coach_count_var, values=counts, state="readonly", width=10)
        count_box.grid(row=1, column=3, sticky="w", padx=6, pady=(0, 8))
        count_box.bind("<<ComboboxSelected>>", lambda _e: self.start_coach_set())

        ttk.Label(controls, text="Order").grid(row=2, column=0, sticky="w", padx=10, pady=(0, 8))
        self.coach_order_var = tk.StringVar(value="Shuffle")
        order_box = ttk.Combobox(controls, textvariable=self.coach_order_var, values=orders, state="readonly", width=18)
        order_box.grid(row=2, column=1, sticky="w", padx=10, pady=(0, 8))
        order_box.bind("<<ComboboxSelected>>", lambda _e: self.start_coach_set())

        ttk.Button(controls, text="Start / Reset", style="Accent.TButton", command=self.start_coach_set).grid(row=0, column=4, padx=10, pady=8)
        ttk.Button(controls, text="Next Question", command=self.next_coach_question).grid(row=0, column=5, padx=10, pady=8)
        ttk.Button(controls, text="Review Missed", command=self.review_missed_coach_questions).grid(row=1, column=4, padx=10, pady=(0, 8))
        ttk.Button(controls, text="Summary", command=self.show_coach_summary).grid(row=1, column=5, padx=10, pady=(0, 8))
        ttk.Button(controls, text="Open Coaching", command=self.open_coach_scenario).grid(row=2, column=4, padx=10, pady=(0, 8))
        ttk.Button(controls, text="Copy Missed", command=self.copy_missed_coach_review).grid(row=2, column=5, padx=10, pady=(0, 8))
        self.coach_score_var = tk.StringVar(value="Score: 0/0")
        ttk.Label(controls, textvariable=self.coach_score_var, style="Muted.TLabel").grid(row=2, column=2, columnspan=2, sticky="w", padx=10, pady=(0, 8))

        qpanel = self._panel(parent, "Question")
        qpanel.columnconfigure(0, weight=1)
        self.coach_question_var = tk.StringVar()
        ttk.Label(qpanel, textvariable=self.coach_question_var, wraplength=1040, font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 6))
        self.coach_choice_frame = ttk.Frame(qpanel)
        self.coach_choice_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 6))
        actions = ttk.Frame(qpanel)
        actions.grid(row=2, column=0, sticky="ew", padx=10, pady=(2, 10))
        ttk.Button(actions, text="Check Answer", style="Accent.TButton", command=self.check_coach_answer).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Show Answer", command=self.show_coach_answer).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Copy Explanation", command=self.copy_coach_explanation).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Search Terms", command=self.search_coach_terms).pack(side="left", padx=(0, 8))

        detail = self._panel(parent, "Answer review")
        self.coach_feedback_text = tk.Text(detail, height=18)
        self.coach_feedback_text.pack(fill="x", padx=10, pady=10)
        style_text_widget(self.coach_feedback_text, self.colors)
        self.coach_feedback_text.configure(state="disabled")
        self.refresh_coach_question()


    def get_coach_questions(self):
        if not getattr(self, "coach_questions", None):
            self.coach_questions = load_coach_questions()
        return self.coach_questions

    def refresh_coach_question_sources(self):
        self.coach_questions = load_coach_questions()
        if hasattr(self, "coach_pack_box"):
            current_pack = self.coach_pack_var.get() if hasattr(self, "coach_pack_var") else "All"
            current_topic = self.coach_topic_var.get() if hasattr(self, "coach_topic_var") else "All"
            pack_values = ["All"] + sorted({item.get("pack_name", BUILT_IN_PACK_NAME) for item in self.coach_questions})
            topic_values = ["All"] + sorted({item.get("topic", "General") for item in self.coach_questions})
            self.coach_pack_box.configure(values=pack_values)
            self.coach_topic_box.configure(values=topic_values)
            if current_pack not in pack_values:
                self.coach_pack_var.set("All")
            if current_topic not in topic_values:
                self.coach_topic_var.set("All")
        self.start_coach_set()

    def _build_question_packs_tab(self, parent):
        intro = self._panel(parent, "Question Packs")
        ttk.Label(
            intro,
            text=(
                "Import downloadable Coach Mode question packs here. Built-in ByteCase questions remain available, "
                "and imported packs stay local under the ByteCase playbooks question_packs folder."
            ),
            wraplength=1040,
        ).pack(anchor="w", padx=10, pady=(8, 4))
        ttk.Label(
            intro,
            text="Only import question packs from sources you trust. Packs are educational content and do not replace agency policy, legal authority, formal training, or examiner judgment.",
            wraplength=1040,
            style="Muted.TLabel",
        ).pack(anchor="w", padx=10, pady=(0, 8))

        actions = self._panel(parent, "Pack actions")
        ttk.Button(actions, text="Import Question Pack", style="Accent.TButton", command=self.import_question_pack_file).pack(side="left", padx=10, pady=10)
        ttk.Button(actions, text="Validate Pack File", command=self.validate_question_pack_file_dialog).pack(side="left", padx=(0, 10), pady=10)
        ttk.Button(actions, text="Enable Selected", command=lambda: self.set_selected_question_pack_enabled(True)).pack(side="left", padx=(0, 10), pady=10)
        ttk.Button(actions, text="Disable Selected", command=lambda: self.set_selected_question_pack_enabled(False)).pack(side="left", padx=(0, 10), pady=10)
        ttk.Button(actions, text="Open Pack Folder", command=self.open_question_pack_folder).pack(side="left", padx=(0, 10), pady=10)
        ttk.Button(actions, text="Refresh", command=self.refresh_question_pack_list).pack(side="left", padx=(0, 10), pady=10)

        body = self._panel(parent, "Installed packs")
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        self.question_pack_records = []
        self.question_pack_tree = ttk.Treeview(body, columns=("enabled", "pack", "version", "questions"), show="headings", height=10)
        self.question_pack_tree.heading("enabled", text="Enabled")
        self.question_pack_tree.heading("pack", text="Pack")
        self.question_pack_tree.heading("version", text="Version")
        self.question_pack_tree.heading("questions", text="Questions")
        self.question_pack_tree.column("enabled", width=80, stretch=False)
        self.question_pack_tree.column("pack", width=360)
        self.question_pack_tree.column("version", width=110, stretch=False)
        self.question_pack_tree.column("questions", width=90, stretch=False)
        self.question_pack_tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.question_pack_tree.bind("<<TreeviewSelect>>", lambda _e: self.show_question_pack_detail())
        self.question_pack_detail_text = tk.Text(body, height=14)
        self.question_pack_detail_text.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        style_text_widget(self.question_pack_detail_text, self.colors)
        self.question_pack_detail_text.configure(state="disabled")

        footer = self._panel(parent, "Pack folder")
        self.question_pack_folder_var = tk.StringVar(value=str(question_pack_directory()))
        ttk.Label(footer, textvariable=self.question_pack_folder_var, wraplength=1040, style="Muted.TLabel").pack(anchor="w", padx=10, pady=8)
        self.refresh_question_pack_list()

    def _build_reference_tab(self, parent):
        search_panel = self._panel(parent, "Search playbooks and glossary")
        search_panel.columnconfigure(1, weight=1)
        ttk.Label(search_panel, text="Search").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.reference_query_var = tk.StringVar()
        entry = ttk.Entry(search_panel, textvariable=self.reference_query_var)
        entry.grid(row=0, column=1, sticky="ew", padx=10, pady=8)
        entry.bind("<Return>", lambda _e: self.run_reference_search())
        ttk.Button(search_panel, text="Search", style="Accent.TButton", command=self.run_reference_search).grid(row=0, column=2, padx=10, pady=8)
        ttk.Button(search_panel, text="Clear", command=self.clear_reference_search).grid(row=0, column=3, padx=10, pady=8)
        ttk.Label(search_panel, text="Search examples: RAM, hash, write blocker, browser, Volatility, USB, password, actor, command, attribution", style="Muted.TLabel").grid(row=1, column=1, columnspan=3, sticky="w", padx=10, pady=(0, 8))

        body = self._panel(parent, "Reference results")
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=2)
        body.rowconfigure(0, weight=1)
        self.reference_results = []
        self.reference_tree = ttk.Treeview(body, columns=("type", "title"), show="headings", height=12)
        self.reference_tree.heading("type", text="Type")
        self.reference_tree.heading("title", text="Result")
        self.reference_tree.column("type", width=120, stretch=False)
        self.reference_tree.column("title", width=360)
        self.reference_tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.reference_tree.bind("<<TreeviewSelect>>", lambda _e: self.show_reference_result())
        self.reference_detail_text = tk.Text(body, height=18)
        self.reference_detail_text.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        style_text_widget(self.reference_detail_text, self.colors)
        self.reference_detail_text.configure(state="disabled")
        actions = ttk.Frame(body)
        actions.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ttk.Button(actions, text="Open Playbook", command=self.open_reference_playbook).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Show Glossary", command=self.show_all_glossary).pack(side="left", padx=(0, 8))

        starter = self._panel(parent, "What Playbooks is for")
        text = (
            "ByteCase Playbooks is the explainer layer. It helps new examiners, occasional examiners, or anyone needing a refresher understand why steps matter, what order to think in, what tools may apply, what artifacts are common, and what to document.\n\n"
            "ByteCase Workflow will track case progress. Playbooks explains the work."
        )
        ttk.Label(starter, text=text, wraplength=1040).pack(anchor="w", padx=10, pady=10)
        self.show_all_glossary()

    def _build_settings_tab(self, parent):
        output = self._panel(parent, "Output")
        output.columnconfigure(1, weight=1)
        ttk.Label(output, text="ByteCase Output Root").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.output_root_var = tk.StringVar(value=self.settings.get("output", {}).get("output_root", ""))
        ttk.Entry(output, textvariable=self.output_root_var).grid(row=0, column=1, sticky="ew", padx=10, pady=8)
        ttk.Button(output, text="Browse", command=self.browse_output_root).grid(row=0, column=2, padx=10, pady=8)
        ttk.Label(output, text=f"Leave blank to use {DEFAULT_OUTPUT_ROOT}", style="Muted.TLabel").grid(row=1, column=1, sticky="w", padx=10, pady=(0, 8))
        self.export_txt_var = tk.BooleanVar(value=self.settings.get("output", {}).get("export_txt", True))
        self.export_docx_var = tk.BooleanVar(value=self.settings.get("output", {}).get("export_docx", True))
        ttk.Checkbutton(output, text="Export TXT", variable=self.export_txt_var).grid(row=2, column=1, sticky="w", padx=10, pady=4)
        ttk.Checkbutton(output, text="Export DOCX", variable=self.export_docx_var).grid(row=3, column=1, sticky="w", padx=10, pady=4)

        appearance = self._panel(parent, "Appearance")
        ttk.Label(appearance, text="Theme").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.theme_var = tk.StringVar(value=self.settings.get("appearance", {}).get("theme", "system"))
        ttk.Combobox(appearance, textvariable=self.theme_var, values=["system", "dark", "light"], state="readonly", width=20).grid(row=0, column=1, sticky="w", padx=10, pady=8)
        ttk.Button(parent, text="Save Settings", style="Accent.TButton", command=self.save_settings_action).pack(anchor="w", padx=10, pady=10)

    def populate_playbook_list(self):
        selected_category = self.category_var.get()
        self.playbook_list.delete(0, tk.END)
        for pb in PLAYBOOKS:
            if selected_category == "All" or pb["category"] == selected_category:
                self.playbook_list.insert(tk.END, pb["title"])
        if self.playbook_list.size() > 0:
            self.playbook_list.selection_set(0)
            self.preview_selected_playbook()

    def selected_playbook_from_list(self):
        selection = self.playbook_list.curselection()
        if not selection:
            return None
        title = self.playbook_list.get(selection[0])
        for pb in PLAYBOOKS:
            if pb["title"] == title:
                return pb
        return None

    def preview_selected_playbook(self):
        pb = self.selected_playbook_from_list()
        if not pb:
            return
        text = [pb["title"], f"Category: {pb['category']}", f"Level: {pb['level']}", "", pb["summary"], "", "Use when:"]
        text.extend(f"- {item}" for item in pb.get("use_when", []))
        text.append("")
        text.append("Pause when:")
        text.extend(f"- {item}" for item in pb.get("avoid_when", []))
        text.append("")
        text.append(f"Steps: {len(pb.get('steps', []))}")
        self.set_text(self.preview_text, "\n".join(text))

    def open_selected_playbook(self):
        pb = self.selected_playbook_from_list()
        if not pb:
            messagebox.showwarning("No playbook selected", "Select a playbook first.")
            return
        self.save_current_step_notes()
        self.session = create_session(pb["id"], self.mode_var.get())
        self.current_step_index = 1
        self.sync_current_step_index()
        self.refresh_all()
        self.show_playbook_page()

    def quick_mode(self, mode):
        self.mode_var.set(mode)
        self.set_mode()
        self.show_playbook_page()

    def set_mode(self):
        self.session["mode"] = self.mode_var.get()
        self.refresh_current_step()
        self.refresh_start_summary()

    def current_playbook(self):
        return get_playbook(self.session.get("playbook_id")) or PLAYBOOKS[0]

    def refresh_all(self):
        self.mode_var.set(self.session.get("mode", "Field Reference"))
        self.populate_playbook_list()
        self.refresh_playbook_header()
        self.refresh_steps_tree()
        self.refresh_current_step()
        try:
            self.current_step_index = int(self.session.get("current_step_index", self.current_step_index))
        except (TypeError, ValueError):
            self.current_step_index = 1
        self.sync_current_step_index()
        self.refresh_start_summary()
        self.refresh_review()
        if hasattr(self, "decision_detail_text"):
            self.refresh_decision_detail()
        if hasattr(self, "coach_question_var"):
            self.refresh_coach_question()

    def refresh_playbook_header(self):
        pb = self.current_playbook()
        self.playbook_title_var.set(pb["title"])
        self.playbook_meta_var.set(f"{pb['category']} | {pb['level']} | {len(pb.get('steps', []))} guidance steps | Mode: {self.session.get('mode')}")

    def refresh_steps_tree(self):
        for item in self.steps_tree.get_children():
            self.steps_tree.delete(item)
        for item in self.session.get("step_state", []):
            status = "Yes" if item.get("checked") else ""
            self.steps_tree.insert("", "end", iid=str(item["index"]), values=(status, f"{item['index']}. {item['title']}"))
        if self.session.get("step_state"):
            self.steps_tree.selection_set(str(self.current_step_index))
            self.steps_tree.see(str(self.current_step_index))

    def select_tree_step(self):
        selection = self.steps_tree.selection()
        if not selection:
            return
        self.save_current_step_notes()
        self.current_step_index = int(selection[0])
        self.sync_current_step_index()
        self.refresh_current_step()

    def get_step(self):
        pb = self.current_playbook()
        index = max(1, min(self.current_step_index, len(pb.get("steps", []))))
        return pb["steps"][index - 1]

    def get_step_state(self):
        for item in self.session.get("step_state", []):
            if item.get("index") == self.current_step_index:
                return item
        return {}

    def refresh_current_step(self):
        pb = self.current_playbook()
        if not pb.get("steps"):
            return
        step = self.get_step()
        state = self.get_step_state()
        self.step_header_var.set(f"Step {self.current_step_index}: {step.get('title', '')}")
        self.step_focus_var.set(step.get("field_focus", ""))
        if hasattr(self, "step_context_var"):
            self.step_context_var.set(self.format_step_context())
        self.step_check_var.set(bool(state.get("checked")))
        self.set_text(self.step_notes_text, state.get("notes", ""), readonly=False)
        mode = self.session.get("mode", "Field Reference")
        if mode == "Learning / Refresher":
            detail = self.format_step_full(step)
        else:
            detail = self.format_step_field(step)
        self.set_text(self.detail_text, detail)
        self.refresh_playbook_header()

    def format_step_field(self, step):
        lines = ["Field Reference", "", step.get("field_focus", ""), "", "Why this order matters:", step.get("why", ""), "", "Document:"]
        lines.extend(f"- {item}" for item in step.get("document", []))
        lines.append("")
        lines.append("Cautions:")
        lines.extend(f"- {item}" for item in step.get("cautions", []))
        if step.get("does_not_prove"):
            lines.append("")
            lines.append("Does not prove:")
            lines.extend(f"- {item}" for item in step.get("does_not_prove", []))
        if step.get("command_examples"):
            lines.append("")
            lines.append("Command examples available. Use Commands for sample syntax and guardrails.")
        return "\n".join(lines)

    def format_step_full(self, step):
        lines = ["Learning / Refresher", "", step.get("learning_detail", ""), "", "Why:", step.get("why", ""), "", "Possible tools:"]
        lines.extend(f"- {item}" for item in step.get("tools", []))
        lines.append("")
        lines.append("Common artifacts / outputs:")
        lines.extend(f"- {item}" for item in step.get("artifacts", []))
        lines.append("")
        lines.append("Cautions:")
        lines.extend(f"- {item}" for item in step.get("cautions", []))
        if step.get("does_not_prove"):
            lines.append("")
            lines.append("Does not prove:")
            lines.extend(f"- {item}" for item in step.get("does_not_prove", []))
        if step.get("command_examples"):
            lines.append("")
            lines.append("Command examples:")
            lines.append(self.format_command_examples(step))
        lines.append("")
        lines.append("Document:")
        lines.extend(f"- {item}" for item in step.get("document", []))
        return "\n".join(lines)


    def format_step_context(self):
        pb = self.current_playbook()
        steps = pb.get("steps", [])
        total = len(steps)
        current = max(1, min(self.current_step_index, total or 1))
        parts = [f"Step {current} of {total}."]
        if current > 1:
            parts.append("Previous: " + steps[current - 2].get("title", ""))
        if current < total:
            parts.append("Next: " + steps[current].get("title", ""))
        parts.append("Use Pop Out Reading during a live reference session, or Deep Dive when studying the step.")
        return " ".join(parts)

    def current_reading_text(self):
        step = self.get_step()
        mode = self.session.get("mode", "Field Reference")
        if mode == "Learning / Refresher":
            return self.format_step_full(step)
        return self.format_step_field(step)

    def pop_out_current_reading(self):
        step = self.get_step()
        title = f"Step {self.current_step_index}: {step.get('title', '')}"
        self.show_text_popup(title, self.current_reading_text())

    def show_deep_dive(self):
        step = self.get_step()
        title = f"Deep Dive - Step {self.current_step_index}: {step.get('title', '')}"
        self.show_text_popup(title, self.format_step_full(step))

    def build_step_summary_text(self):
        step = self.get_step()
        lines = [
            f"Step {self.current_step_index}: {step.get('title', '')}",
            "",
            "Field focus:",
            step.get("field_focus", ""),
            "",
            "Why this matters:",
            step.get("why", ""),
            "",
            "Document:",
        ]
        lines.extend(f"- {item}" for item in step.get("document", []))
        lines.append("")
        lines.append("Cautions:")
        lines.extend(f"- {item}" for item in step.get("cautions", []))
        return "\n".join(lines)

    def copy_to_clipboard(self, text, label="Text"):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()
        messagebox.showinfo("Copied", f"{label} copied to clipboard.")

    def copy_step_summary(self):
        self.copy_to_clipboard(self.build_step_summary_text(), "Step summary")

    def copy_document_reminders(self):
        step = self.get_step()
        lines = [f"Step {self.current_step_index}: {step.get('title', '')}", "", "What to document:"]
        lines.extend(f"- {item}" for item in step.get("document", []))
        self.copy_to_clipboard("\n".join(lines), "Document reminder list")

    def format_command_examples(self, step):
        commands = step.get("command_examples", [])
        if not commands:
            return "No command examples are built into this step. Use the tool documentation, agency SOP, and your validated local process."
        lines = []
        for item in commands:
            lines.append(item.get("label", "Command example"))
            lines.append(item.get("example", ""))
            lines.append("Purpose: " + item.get("purpose", ""))
            lines.append("Does not prove: " + item.get("does_not_prove", ""))
            lines.append("")
        lines.append("Reminder: Command examples are learning prompts. Adjust paths, filenames, options, tool locations, and scope for your environment.")
        return "\n".join(lines).strip()

    def format_does_not_prove(self, step):
        values = step.get("does_not_prove", [])
        if not values:
            values = [
                "This step supports examiner understanding, but it does not produce a conclusion by itself.",
                "Tool output must be reviewed in context and corroborated when it matters.",
            ]
        lines = ["Does not prove / overclaim guardrails", ""]
        lines.extend(f"- {item}" for item in values)
        return "\n".join(lines)

    def show_command_examples(self):
        step = self.get_step()
        self.show_text_popup("Command Examples", self.format_command_examples(step))

    def show_does_not_prove(self):
        step = self.get_step()
        self.show_text_popup("Does Not Prove", self.format_does_not_prove(step))

    def copy_command_examples(self):
        self.copy_to_clipboard(self.format_command_examples(self.get_step()), "Command examples")

    def show_step_panel(self, key):
        step = self.get_step()
        title_map = {"why": "Why this matters", "tools": "Possible tools", "artifacts": "Common artifacts / outputs", "cautions": "Cautions", "document": "What to document"}
        if key == "why":
            body = step.get("why", "") + "\n\n" + step.get("learning_detail", "")
        else:
            body = "\n".join(f"- {item}" for item in step.get(key, []))
        self.show_text_popup(title_map.get(key, key.title()), body)

    def show_list_popup(self, title, values):
        self.show_text_popup(title, "\n".join(f"- {item}" for item in values))

    def show_boundary(self):
        self.show_text_popup("Boundary Notice", PLAYBOOK_BOUNDARY)

    def show_text_popup(self, title, body):
        win = tk.Toplevel(self.root)
        configure_toplevel(win, self.colors)
        win.title(title)
        win.geometry("720x480")
        ttk.Label(win, text=title, font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=12, pady=(12, 4))
        text = tk.Text(win, height=20)
        text.pack(fill="both", expand=True, padx=12, pady=8)
        style_text_widget(text, self.colors)
        text.insert("1.0", body)
        text.configure(state="disabled")
        ttk.Button(win, text="Close", command=win.destroy).pack(anchor="e", padx=12, pady=(0, 12))

    def update_step_checked(self):
        state = self.get_step_state()
        state["checked"] = self.step_check_var.get()
        self.refresh_steps_tree()
        self.refresh_start_summary()

    def mark_dirty_step_notes(self):
        pass

    def sync_current_step_index(self):
        self.session["current_step_index"] = self.current_step_index

    def save_current_step_notes(self):
        try:
            state = self.get_step_state()
            if state is not None:
                state["notes"] = self.step_notes_text.get("1.0", "end-1c")
        except tk.TclError:
            pass

    def previous_step(self):
        self.save_current_step_notes()
        self.current_step_index = max(1, self.current_step_index - 1)
        self.sync_current_step_index()
        self.refresh_steps_tree()
        self.refresh_current_step()

    def next_step(self):
        self.save_current_step_notes()
        max_step = len(self.session.get("step_state", []))
        self.current_step_index = min(max_step, self.current_step_index + 1)
        self.sync_current_step_index()
        self.refresh_steps_tree()
        self.refresh_current_step()

    def update_session_details(self):
        self.refresh_start_summary()
        self.refresh_review()

    def refresh_start_summary(self):
        self.sync_current_step_index()
        summary = session_summary(self.session)
        text = (
            f"Current: {summary['playbook_title']} | Mode: {summary['mode']} | "
            f"Step: {summary['current_step_index']} of {summary['total_steps']} | "
            f"Reviewed: {summary['checked_steps']} of {summary['total_steps']} | "
            f"Steps with notes: {summary['steps_with_notes']}"
        )
        self.start_summary_var.set(text)
        if hasattr(self, "progress_summary_var"):
            self.progress_summary_var.set(text)

    def refresh_review(self):
        self.save_current_step_notes()
        self.sync_current_step_index()
        summary = session_summary(self.session)
        warnings = validate_session(self.session)
        lines = [
            f"Playbook: {summary['playbook_title']}",
            f"Mode: {summary['mode']}",
            f"Current Step: {summary['current_step_index']} of {summary['total_steps']}",
            f"Reviewed Steps: {summary['checked_steps']} of {summary['total_steps']}",
            f"Steps With Notes: {summary['steps_with_notes']}",
            "",
            "Saved Session Includes:",
            "- Selected playbook",
            "- Selected mode",
            "- Current step",
            "- Reviewed step checkboxes",
            "- Step reference notes",
            "",
            "Saved Session Does Not Include:",
            "- Case notes",
            "- Case number",
            "- Examiner name",
            "- Evidence files",
            "",
            "Warnings:" if warnings else "Warnings: None",
        ]
        lines.extend(f"- {warning}" for warning in warnings)
        lines.append("")
        lines.append(f"Output Folder: {get_output_root(self.settings)}\\playbooks\\sessions")
        self.set_text(self.review_text, "\n".join(lines))
        self.refresh_start_summary()

    def export_session(self, open_after=False):
        self.save_current_step_notes()
        self.sync_current_step_index()
        self.refresh_review()
        try:
            json_path, txt_path, docx_path = save_session_outputs(self.settings, self.session)
        except Exception as exc:
            messagebox.showerror("Export failed", str(exc))
            return
        self.last_export_folder = json_path.parent
        created = [str(json_path), str(txt_path)]
        if docx_path:
            created.append(str(docx_path))
        messagebox.showinfo("Export complete", "Created:\n" + "\n".join(created))
        if open_after:
            self.open_folder(self.last_export_folder)

    def open_last_folder(self):
        if self.last_export_folder and Path(self.last_export_folder).exists():
            self.open_folder(self.last_export_folder)
        else:
            messagebox.showinfo("No folder yet", "Export a session first.")

    def open_folder(self, path):
        path = str(path)
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", path], check=False)
        else:
            subprocess.run(["xdg-open", path], check=False)

    def open_session_json(self):
        path = filedialog.askopenfilename(title="Open ByteCase Playbooks session JSON", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not path:
            return
        try:
            self.session = load_session(path)
            self.current_step_index = int(self.session.get("current_step_index", 1))
            self.refresh_all()
            self.show_playbook_page()
        except Exception as exc:
            messagebox.showerror("Could not open session", str(exc))

    def new_session(self):
        pb = self.current_playbook()
        if not messagebox.askyesno("New session", "Start a new session with the current playbook?"):
            return
        self.session = create_session(pb["id"], self.mode_var.get())
        self.current_step_index = 1
        self.sync_current_step_index()
        self.refresh_all()

    def artifact_situation_values(self):
        preferred_order = [
            "Dead-box laptop exam",
            "Powered-on computer / live system",
            "BitLocker-enabled laptop",
            "Memory/RAM review",
            "Mobile device review",
            "External media review",
            "Browser/download review",
            "Shared device or shared account",
            "Cloud sync review",
            "Possible remote access or automation",
            "File movement question",
        ]
        values = []
        for value in preferred_order:
            if any(value in item.get("situations", []) for item in INVESTIGATIVE_QUESTIONS):
                values.append(value)
        for item in INVESTIGATIVE_QUESTIONS:
            for value in item.get("situations", []):
                if value != "Any situation" and value not in values:
                    values.append(value)
        return values or ["General review"]

    def questions_for_situation(self, situation):
        exact_matches = [
            item for item in INVESTIGATIVE_QUESTIONS
            if situation in item.get("situations", [])
        ]
        if exact_matches:
            return exact_matches
        any_matches = [
            item for item in INVESTIGATIVE_QUESTIONS
            if "Any situation" in item.get("situations", [])
        ]
        return any_matches or list(INVESTIGATIVE_QUESTIONS)

    def refresh_artifact_questions(self):
        if not hasattr(self, "question_box"):
            return
        situation = self.artifact_situation_var.get() if hasattr(self, "artifact_situation_var") else ""
        questions = self.questions_for_situation(situation)
        labels = [item.get("question", "") for item in questions]
        self.visible_investigative_questions = questions
        self.question_box.configure(values=labels)
        if labels and self.question_var.get() not in labels:
            self.question_var.set(labels[0])
        elif not labels:
            self.question_var.set("")
        self.show_question_detail()

    def artifact_area_by_id(self, artifact_id):
        for item in ARTIFACT_AREAS:
            if item.get("id") == artifact_id:
                return item
        return None

    def artifact_areas_for_question(self, question):
        if not question:
            return []
        areas = []
        seen = set()
        for artifact_id in question.get("related_artifact_ids", []):
            area = self.artifact_area_by_id(artifact_id)
            if area and area.get("id") not in seen:
                areas.append(area)
                seen.add(area.get("id"))
        if areas:
            return areas
        related = [value.lower() for value in question.get("related_artifacts", [])]
        for area in ARTIFACT_AREAS:
            label = f"{area.get('category', '')} - {area.get('title', '')}".lower()
            if any(value in label or area.get("title", "").lower() in value for value in related):
                areas.append(area)
        return areas or list(ARTIFACT_AREAS)

    def populate_artifact_area_list(self):
        if not hasattr(self, "artifact_area_list"):
            return
        self.artifact_area_list.delete(0, tk.END)
        self.visible_artifact_areas = self.artifact_areas_for_question(self.selected_question())
        for item in self.visible_artifact_areas:
            self.artifact_area_list.insert(tk.END, f"{item.get('category', '')} - {item.get('title', '')}")
        if self.visible_artifact_areas:
            self.artifact_area_list.selection_set(0)
            self.show_artifact_area_detail()
        elif hasattr(self, "artifact_detail_text"):
            self.set_text(self.artifact_detail_text, "No artifact areas mapped for this question yet.")

    def selected_artifact_area(self):
        if not hasattr(self, "artifact_area_list"):
            return None
        selection = self.artifact_area_list.curselection()
        if not selection:
            return None
        try:
            return self.visible_artifact_areas[selection[0]]
        except (AttributeError, IndexError):
            return None

    def format_artifact_area(self, item):
        if not item:
            return "No artifact area selected."
        lines = [
            item.get("title", ""),
            f"Category: {item.get('category', '')}",
            "",
            "What this may help answer:",
            item.get("helps_answer", ""),
            "",
            "Where to look:",
        ]
        lines.extend(f"- {value}" for value in item.get("where_to_look", []))
        lines.append("")
        lines.append("Common tools / methods:")
        lines.extend(f"- {value}" for value in item.get("tools", []))
        lines.append("")
        lines.append("Reminder:")
        lines.append("- Tool names are common examples only, not endorsements, recommendations, or validation statements.")
        lines.append("")
        lines.append("Guardrails / does not prove:")
        lines.extend(f"- {value}" for value in item.get("cautions", []))
        lines.append("")
        lines.append("Document:")
        lines.extend(f"- {value}" for value in item.get("document", []))
        lines.append("")
        lines.append("Related playbooks:")
        lines.extend(f"- {value}" for value in item.get("related_playbooks", []))
        return "\n".join(lines)

    def show_artifact_area_detail(self):
        if hasattr(self, "artifact_detail_text"):
            self.set_text(self.artifact_detail_text, self.format_artifact_area(self.selected_artifact_area()))

    def copy_artifact_guidance(self):
        self.copy_to_clipboard(self.format_artifact_area(self.selected_artifact_area()), "Artifact guidance")

    def search_selected_artifact_area(self):
        item = self.selected_artifact_area()
        if not item:
            return
        self.reference_query_var.set(item.get("title", ""))
        self.show_reference_page()
        self.run_reference_search()

    def selected_question(self):
        text = self.question_var.get() if hasattr(self, "question_var") else ""
        candidates = getattr(self, "visible_investigative_questions", None) or INVESTIGATIVE_QUESTIONS
        for item in candidates:
            if item.get("question") == text:
                return item
        for item in INVESTIGATIVE_QUESTIONS:
            if item.get("question") == text:
                return item
        return candidates[0] if candidates else (INVESTIGATIVE_QUESTIONS[0] if INVESTIGATIVE_QUESTIONS else None)

    def format_question_guidance(self, item):
        if not item:
            return "No question selected."
        situation = self.artifact_situation_var.get() if hasattr(self, "artifact_situation_var") else "Any situation"
        areas = self.artifact_areas_for_question(item)
        lines = [
            f"Situation: {situation}",
            f"Question: {item.get('question', '')}",
            "",
            "Examiner mindset:",
            item.get("mindset", ""),
            "",
            "Decision factors / look at:",
        ]
        lines.extend(f"- {value}" for value in item.get("look_at", []))
        lines.append("")
        lines.append("Mapped artifact areas:")
        for area in areas:
            lines.append(f"- {area.get('category', '')} - {area.get('title', '')}")
            lines.append(f"  May help answer: {area.get('helps_answer', '')}")
            if area.get("where_to_look"):
                lines.append("  Where to look: " + "; ".join(area.get("where_to_look", [])[:4]))
            if area.get("tools"):
                lines.append("  Common tools/methods: " + "; ".join(area.get("tools", [])[:4]))
        lines.append("")
        lines.append("Guardrails:")
        lines.extend(f"- {value}" for value in item.get("guardrails", []))
        lines.append("")
        lines.append("Tool note:")
        lines.append("- Tool names are examples of commonly used industry tools or methods, not endorsements, recommendations, or validation statements.")
        return "\n".join(lines)

    def show_question_detail(self):
        if hasattr(self, "question_detail_text"):
            self.set_text(self.question_detail_text, self.format_question_guidance(self.selected_question()))
        self.populate_artifact_area_list()

    def copy_question_guidance(self):
        self.copy_to_clipboard(self.format_question_guidance(self.selected_question()), "Question guidance")

    def selected_coaching_prompt(self):
        title = self.coaching_prompt_var.get() if hasattr(self, "coaching_prompt_var") else ""
        for item in SCENARIO_COACHING_QUESTIONS:
            if item.get("title") == title:
                return item
        return SCENARIO_COACHING_QUESTIONS[0] if SCENARIO_COACHING_QUESTIONS else None

    def coaching_steps(self):
        item = self.selected_coaching_prompt() or {}
        return item.get("steps", []) or []

    def begin_coaching_path(self):
        self.coaching_step_index = 0
        self.coaching_answers = {}
        self.coaching_review_complete = False
        self.refresh_coaching_step()

    def refresh_coaching_prompt(self):
        self.begin_coaching_path()

    def refresh_coaching_step(self):
        item = self.selected_coaching_prompt()
        steps = self.coaching_steps()
        if not item or not steps or not hasattr(self, "coaching_choice_frame"):
            return
        if not hasattr(self, "coaching_step_index"):
            self.coaching_step_index = 0
        self.coaching_step_index = max(0, min(self.coaching_step_index, len(steps) - 1))
        step = steps[self.coaching_step_index]
        self.coaching_context_var.set(item.get("opening_context", item.get("summary", "")))
        self.coaching_progress_var.set(f"Question {self.coaching_step_index + 1} of {len(steps)}")
        self.coaching_question_var.set(step.get("prompt", ""))
        selected = getattr(self, "coaching_answers", {}).get(step.get("id", str(self.coaching_step_index)), -1)
        self.coaching_answer_var.set(selected)
        for child in self.coaching_choice_frame.winfo_children():
            child.destroy()
        for idx, choice in enumerate(step.get("choices", [])):
            rb = ttk.Radiobutton(self.coaching_choice_frame, text=choice, value=idx, variable=self.coaching_answer_var)
            rb.pack(anchor="w", padx=2, pady=2)
        remaining = len(steps) - len(getattr(self, "coaching_answers", {}))
        self.set_text(
            self.coaching_feedback_text,
            (
                "Answer this question, then click Record / Next. The best answer and coaching explanation will stay hidden until Finish & Review.\n\n"
                f"Path: {item.get('title', '')}\n"
                f"Category: {item.get('category', '')}\n"
                f"Recorded answers: {len(getattr(self, 'coaching_answers', {}))} of {len(steps)}\n"
                f"Remaining: {max(0, remaining)}"
            ),
        )

    def next_coaching_prompt(self):
        if not SCENARIO_COACHING_QUESTIONS:
            return
        current = self.selected_coaching_prompt()
        idx = SCENARIO_COACHING_QUESTIONS.index(current) if current in SCENARIO_COACHING_QUESTIONS else 0
        idx = (idx + 1) % len(SCENARIO_COACHING_QUESTIONS)
        self.coaching_prompt_var.set(SCENARIO_COACHING_QUESTIONS[idx].get("title", ""))
        self.begin_coaching_path()

    def previous_coaching_step(self):
        steps = self.coaching_steps()
        if not steps:
            return
        if not hasattr(self, "coaching_step_index"):
            self.coaching_step_index = 0
        self.coaching_step_index = max(0, self.coaching_step_index - 1)
        self.refresh_coaching_step()

    def check_coaching_answer(self):
        item = self.selected_coaching_prompt()
        steps = self.coaching_steps()
        selected = self.coaching_answer_var.get() if hasattr(self, "coaching_answer_var") else -1
        if not item or not steps:
            return
        if selected < 0:
            messagebox.showinfo("Choose a response", "Select the best response first.")
            return
        if not hasattr(self, "coaching_step_index"):
            self.coaching_step_index = 0
        step = steps[self.coaching_step_index]
        if not hasattr(self, "coaching_answers"):
            self.coaching_answers = {}
        step_id = step.get("id", str(self.coaching_step_index))
        self.coaching_answers[step_id] = selected
        if self.coaching_step_index < len(steps) - 1:
            self.coaching_step_index += 1
            self.refresh_coaching_step()
        else:
            self.set_text(
                self.coaching_feedback_text,
                "Last answer recorded. Click Finish & Review to see the full coaching review."
            )

    def format_coaching_guidance(self, item=None, selected_index=None, reveal_only=False):
        # Compatibility wrapper used by older copy/open handlers.
        return self.format_coaching_review()

    def format_coaching_review(self):
        item = self.selected_coaching_prompt()
        steps = self.coaching_steps()
        if not item or not steps:
            return "No coaching path selected."
        answers = getattr(self, "coaching_answers", {})
        lines = [
            item.get("title", ""),
            f"Category: {item.get('category', '')}",
            "",
            "Scenario context:",
            item.get("opening_context", item.get("summary", "")),
            "",
            "Coaching review:",
        ]
        correct = 0
        for idx, step in enumerate(steps):
            step_id = step.get("id", str(idx))
            selected = answers.get(step_id, -1)
            best = int(step.get("best_index", 0))
            choices = step.get("choices", [])
            if selected == best:
                correct += 1
            lines.append("")
            lines.append(f"Question {idx + 1}: {step.get('prompt', '')}")
            lines.append("Your response: " + (choices[selected] if 0 <= selected < len(choices) else "No response recorded"))
            lines.append("Best response: " + (choices[best] if 0 <= best < len(choices) else "Not specified"))
            lines.append("Result: " + ("Aligned with the safer response" if selected == best else "Review the coaching note"))
            lines.append("Why: " + step.get("explanation", ""))
            if step.get("coaching_note"):
                lines.append("Mentor note: " + step.get("coaching_note", ""))
        lines.append("")
        lines.append(f"Path score: {correct} of {len(steps)} safer responses")
        lines.append("")
        lines.append("Bigger-picture debrief:")
        lines.append(item.get("debrief", item.get("bigger_picture", "")))
        lines.append("")
        lines.append("Reference terms:")
        lines.extend(f"- {value}" for value in item.get("related_reference_terms", []))
        lines.append("")
        lines.append("Boundary reminder:")
        lines.append("- Coaching paths are readiness prompts. They do not produce findings, replace policy, or prove investigative conclusions.")
        return "\n".join(lines)

    def show_coaching_answer(self):
        self.coaching_review_complete = True
        self.set_text(self.coaching_feedback_text, self.format_coaching_review())

    def copy_coaching_guidance(self):
        self.copy_to_clipboard(self.format_coaching_review(), "Coaching review")

    def open_coaching_playbook(self):
        item = self.selected_coaching_prompt()
        if not item:
            return
        playbook_id = item.get("related_playbook_id", "")
        try:
            self.save_current_step_notes()
            self.session = create_session(playbook_id, self.mode_var.get())
            self.current_step_index = 1
            self.sync_current_step_index()
            self.refresh_all()
            self.show_playbook_page()
        except Exception as exc:
            messagebox.showerror("Could not open playbook", str(exc))

    def search_coaching_terms(self):
        item = self.selected_coaching_prompt()
        if not item:
            return
        terms = item.get("related_reference_terms", [])
        query = terms[0] if terms else item.get("title", "")
        self.reference_query_var.set(query)
        self.show_reference_page()
        self.run_reference_search()

    def format_use_context_prompts(self):
        lines = [
            "Use / Access Context Mindset",
            "",
            "A device artifact can show activity, but it does not automatically identify the person who performed the action. When attribution matters, separate the artifact from the human actor and look for supporting context.",
            "",
        ]
        for item in CONTROL_CONTEXT_PROMPTS:
            lines.append(item.get("title", ""))
            lines.append(item.get("prompt", ""))
            lines.append("Examples:")
            lines.extend(f"- {value}" for value in item.get("examples", []))
            lines.append("Caution: " + item.get("caution", ""))
            lines.append("")
        lines.append("Practical reminder: admissions such as being the only person who knows a device password can support access/control context, but should still be documented accurately and weighed with possession, account, session, and corroborating evidence.")
        return "\n".join(lines).strip()

    def show_use_context(self):
        self.show_text_popup("Use / Access Context", self.format_use_context_prompts())

    def run_reference_search(self):
        query = self.reference_query_var.get().strip()
        self.reference_results = []
        for item in search_glossary(query):
            self.reference_results.append({"type": "Glossary", "title": item.get("term", ""), "data": item})
        for playbook in search_playbooks(query):
            self.reference_results.append({"type": "Playbook", "title": playbook.get("title", ""), "data": playbook})
        for area in search_artifact_areas(query):
            self.reference_results.append({"type": "Artifact", "title": area.get("title", ""), "data": area})
        for question in search_investigative_questions(query):
            self.reference_results.append({"type": "Question", "title": question.get("question", ""), "data": question})
        for scenario in search_scenario_cards(query):
            self.reference_results.append({"type": "Scenario", "title": scenario.get("title", ""), "data": scenario})
        for coaching in search_scenario_coaching_questions(query):
            self.reference_results.append({"type": "Coaching", "title": coaching.get("title", ""), "data": coaching})
        for question in search_coach_questions(query, self.coach_questions):
            self.reference_results.append({"type": "Coach", "title": question.get("question", ""), "data": question})
        self.populate_reference_tree()
        if self.reference_results:
            self.reference_tree.selection_set("0")
            self.show_reference_result()
        else:
            self.set_text(self.reference_detail_text, "No reference results found. Try a broader term such as RAM, hash, browser, live, imaging, write blocker, USB, command, password, control, actor, attribution, scenario, coach, drill, or artifact.")

    def clear_reference_search(self):
        self.reference_query_var.set("")
        self.show_all_glossary()

    def show_all_glossary(self):
        self.reference_results = [{"type": "Glossary", "title": item.get("term", ""), "data": item} for item in GLOSSARY]
        self.populate_reference_tree()
        if self.reference_results:
            self.reference_tree.selection_set("0")
            self.show_reference_result()

    def populate_reference_tree(self):
        for item in self.reference_tree.get_children():
            self.reference_tree.delete(item)
        for idx, result in enumerate(self.reference_results):
            self.reference_tree.insert("", "end", iid=str(idx), values=(result.get("type", ""), result.get("title", "")))

    def selected_reference_result(self):
        selection = self.reference_tree.selection()
        if not selection:
            return None
        try:
            idx = int(selection[0])
            return self.reference_results[idx]
        except (ValueError, IndexError):
            return None

    def show_reference_result(self):
        result = self.selected_reference_result()
        if not result:
            return
        data = result.get("data", {})
        result_type = result.get("type")
        if result_type == "Glossary":
            lines = [data.get("term", ""), f"Category: {data.get('category', '')}", ""]
            definition = data.get("plain_language") or data.get("definition", "")
            lines.append(definition)
            if data.get("why_it_matters"):
                lines.extend(["", "Why it matters:", data.get("why_it_matters", "")])
            if data.get("common_examples"):
                lines.extend(["", "Common examples:"])
                lines.extend(f"- {item}" for item in data.get("common_examples", []))
            if data.get("guardrail"):
                lines.extend(["", "Guardrail:", data.get("guardrail", "")])
            if data.get("related"):
                lines.extend(["", "Related terms:"])
                lines.extend(f"- {item}" for item in data.get("related", []))
            if data.get("related_playbooks"):
                lines.extend(["", "Related playbooks:"])
                lines.extend(f"- {item}" for item in data.get("related_playbooks", []))
        elif result_type == "Coach":
            lines = [
                "Coach Question",
                f"Pack: {data.get('pack_name', '')}",
                f"Publisher: {data.get('pack_publisher', '')}",
                f"Topic: {data.get('topic', '')}",
                f"Difficulty: {data.get('difficulty', '')}",
                "",
                data.get("question", ""),
                "",
                "Choices:",
            ]
            for idx, choice in enumerate(data.get("choices", []), start=1):
                prefix = "*" if idx - 1 == data.get("answer_index", 0) else " "
                lines.append(f"{prefix} {idx}. {choice}")
            lines.append("")
            lines.append("Explanation:")
            lines.append(data.get("explanation", ""))
            lines.append("")
            lines.append("Guardrail:")
            lines.append(data.get("guardrail", ""))
            lines.append("")
            lines.append("Follow-up questions:")
            lines.extend(f"- {item}" for item in data.get("follow_up", []))
        elif result_type == "Artifact":
            lines = [
                data.get("title", ""),
                f"Category: {data.get('category', '')}",
                "",
                "What this may help answer:",
                data.get("helps_answer", ""),
                "",
                "Guardrails:",
            ]
            lines.extend(f"- {item}" for item in data.get("cautions", []))
        elif result_type == "Question":
            lines = [data.get("question", ""), "", "Mindset:", data.get("mindset", ""), "", "Look at:"]
            lines.extend(f"- {item}" for item in data.get("look_at", []))
            lines.append("")
            lines.append("Guardrails:")
            lines.extend(f"- {item}" for item in data.get("guardrails", []))
        elif result_type == "Scenario":
            lines = [
                data.get("title", ""),
                f"Category: {data.get('category', '')}",
                "",
                "Situation:",
                data.get("situation", ""),
                "",
                "Plain-language takeaway:",
                data.get("plain_language", ""),
                "",
                "Guardrails:",
            ]
            lines.extend(f"- {item}" for item in data.get("guardrails", []))
        elif result_type == "Coaching":
            lines = [
                data.get("title", ""),
                f"Category: {data.get('category', '')}",
                "",
                "Scenario context:",
                data.get("opening_context", data.get("summary", "")),
                "",
                "Question path:",
            ]
            for idx, step in enumerate(data.get("steps", []), start=1):
                lines.append(f"{idx}. {step.get('prompt', '')}")
            lines.extend(["", "Bigger-picture debrief:", data.get("debrief", "")])
        else:
            lines = [data.get("title", ""), f"Category: {data.get('category', '')}", f"Level: {data.get('level', '')}", "", data.get("summary", ""), "", "Use when:"]
            lines.extend(f"- {item}" for item in data.get("use_when", []))
            lines.append("")
            lines.append("Pause when:")
            lines.extend(f"- {item}" for item in data.get("avoid_when", []))
            lines.append("")
            lines.append("Steps:")
            for idx, step in enumerate(data.get("steps", []), start=1):
                suffix = ""
                if step.get("command_examples"):
                    suffix = "  [command examples]"
                lines.append(f"{idx}. {step.get('title', '')}{suffix}")
        self.set_text(self.reference_detail_text, "\n".join(lines))

    def open_reference_playbook(self):
        result = self.selected_reference_result()
        if not result or result.get("type") != "Playbook":
            messagebox.showinfo("No playbook selected", "Select a Playbook result first. Artifact, Question, Scenario, Coaching, and Coach results are reference-only here.")
            return
        playbook = result.get("data", {})
        self.save_current_step_notes()
        self.session = create_session(playbook.get("id"), self.mode_var.get())
        self.current_step_index = 1
        self.sync_current_step_index()
        self.refresh_all()
        self.show_playbook_page()

    def populate_scenario_list(self):
        if not hasattr(self, "scenario_list"):
            return
        self.scenario_list.delete(0, tk.END)
        for item in SCENARIO_CARDS:
            self.scenario_list.insert(tk.END, f"{item.get('category', '')} - {item.get('title', '')}")
        if SCENARIO_CARDS:
            self.scenario_list.selection_set(0)
            self.show_scenario_detail()

    def selected_scenario(self):
        if not hasattr(self, "scenario_list"):
            return None
        selection = self.scenario_list.curselection()
        if not selection:
            return None
        try:
            return SCENARIO_CARDS[selection[0]]
        except (IndexError, TypeError):
            return None

    def format_scenario_guidance(self, item):
        if not item:
            return "No scenario selected."
        lines = [
            item.get("title", ""),
            f"Category: {item.get('category', '')}",
            "",
            "Situation:",
            item.get("situation", ""),
            "",
            "How to think about it:",
        ]
        lines.extend(f"- {value}" for value in item.get("what_to_think", []))
        lines.append("")
        lines.append("Helpful supporting context:")
        lines.extend(f"- {value}" for value in item.get("supporting_context", []))
        lines.append("")
        lines.append("Guardrails / does not prove:")
        lines.extend(f"- {value}" for value in item.get("guardrails", []))
        lines.append("")
        lines.append("Plain-language takeaway:")
        lines.append(item.get("plain_language", ""))
        lines.append("")
        lines.append("Related playbook:")
        lines.append(f"- {item.get('related_playbook_title', '')}")
        lines.append("")
        lines.append("Reference terms:")
        lines.extend(f"- {value}" for value in item.get("related_reference_terms", []))
        return "\n".join(lines)

    def show_scenario_detail(self):
        if hasattr(self, "scenario_detail_text"):
            self.set_text(self.scenario_detail_text, self.format_scenario_guidance(self.selected_scenario()))

    def copy_scenario_guidance(self):
        self.copy_to_clipboard(self.format_scenario_guidance(self.selected_scenario()), "Scenario guidance")

    def open_scenario_playbook(self):
        scenario = self.selected_scenario()
        if not scenario:
            return
        playbook_id = scenario.get("related_playbook_id", "")
        try:
            self.save_current_step_notes()
            self.session = create_session(playbook_id, self.mode_var.get())
            self.current_step_index = 1
            self.sync_current_step_index()
            self.refresh_all()
            self.show_playbook_page()
        except Exception as exc:
            messagebox.showerror("Could not open playbook", str(exc))

    def search_scenario_terms(self):
        scenario = self.selected_scenario()
        if not scenario:
            return
        terms = scenario.get("related_reference_terms", [])
        query = terms[0] if terms else scenario.get("title", "")
        self.reference_query_var.set(query)
        self.show_reference_page()
        self.run_reference_search()


    def refresh_question_pack_list(self):
        if not hasattr(self, "question_pack_tree"):
            return
        self.question_pack_records = question_pack_records(include_disabled=True)
        for item in self.question_pack_tree.get_children():
            self.question_pack_tree.delete(item)
        for idx, record in enumerate(self.question_pack_records):
            enabled = "Yes" if record.get("enabled") else "No"
            if record.get("errors"):
                enabled = "Error"
            self.question_pack_tree.insert(
                "",
                "end",
                iid=str(idx),
                values=(enabled, record.get("pack_name", ""), record.get("version", ""), record.get("question_count", 0)),
            )
        if self.question_pack_records:
            self.question_pack_tree.selection_set("0")
            self.show_question_pack_detail()

    def selected_question_pack_record(self):
        if not hasattr(self, "question_pack_tree"):
            return None
        selection = self.question_pack_tree.selection()
        if not selection:
            return None
        try:
            return self.question_pack_records[int(selection[0])]
        except (ValueError, IndexError):
            return None

    def show_question_pack_detail(self):
        record = self.selected_question_pack_record()
        if not record:
            return
        lines = [
            record.get("pack_name", ""),
            f"Pack ID: {record.get('pack_id', '')}",
            f"Version: {record.get('version', '')}",
            f"Publisher: {record.get('publisher', '')}",
            f"Enabled: {'Yes' if record.get('enabled') else 'No'}",
            f"Questions: {record.get('question_count', 0)}",
            "",
            "Description:",
            record.get("description", ""),
            "",
            "License:",
            record.get("license", ""),
        ]
        if record.get("path"):
            lines.extend(["", "Local file:", record.get("path", "")])
        if record.get("warnings"):
            lines.extend(["", "Warnings:"])
            lines.extend(f"- {item}" for item in record.get("warnings", []))
        if record.get("errors"):
            lines.extend(["", "Errors:"])
            lines.extend(f"- {item}" for item in record.get("errors", []))
        self.set_text(self.question_pack_detail_text, "\n".join(lines))

    def import_question_pack_file(self):
        path = filedialog.askopenfilename(
            title="Import ByteCase question pack",
            filetypes=[("JSON question packs", "*.json"), ("All files", "*.*")],
        )
        if not path:
            return
        result = import_question_pack(Path(path))
        if not result.get("ok"):
            messagebox.showerror("Question pack rejected", "\n".join(result.get("errors", ["Unknown validation error."])))
            return
        pack = result.get("pack") or {}
        warning_text = ""
        if result.get("warnings"):
            warning_text = "\n\nWarnings:\n" + "\n".join(result.get("warnings", []))
        messagebox.showinfo(
            "Question pack imported",
            f"Imported {pack.get('pack_name', 'question pack')} with {len(result.get('questions', []))} question(s).\n\nSaved to:\n{result.get('destination', '')}{warning_text}",
        )
        self.refresh_question_pack_list()
        self.refresh_coach_question_sources()

    def validate_question_pack_file_dialog(self):
        path = filedialog.askopenfilename(
            title="Validate ByteCase question pack",
            filetypes=[("JSON question packs", "*.json"), ("All files", "*.*")],
        )
        if not path:
            return
        result = validate_question_pack_file(Path(path))
        pack = result.get("pack") or {}
        lines = [
            "Question Pack Validation",
            "",
            f"File: {path}",
            f"Status: {'OK' if result.get('ok') else 'Rejected'}",
            f"Pack: {pack.get('pack_name', '')}",
            f"Version: {pack.get('version', '')}",
            f"Publisher: {pack.get('publisher', '')}",
            f"Questions: {len(result.get('questions', []))}",
        ]
        if result.get("errors"):
            lines.extend(["", "Errors:"])
            lines.extend(f"- {item}" for item in result.get("errors", []))
        if result.get("warnings"):
            lines.extend(["", "Warnings:"])
            lines.extend(f"- {item}" for item in result.get("warnings", []))
        self.show_text_popup("Question Pack Validation", "\n".join(lines))

    def set_selected_question_pack_enabled(self, enabled):
        record = self.selected_question_pack_record()
        if not record:
            return
        if record.get("built_in"):
            messagebox.showinfo("Built-in pack", "Built-in ByteCase questions cannot be disabled from this screen.")
            return
        if record.get("errors"):
            messagebox.showerror("Pack has errors", "This pack has validation errors and cannot be enabled until the file is corrected.")
            return
        set_question_pack_enabled(record.get("pack_id", ""), enabled)
        self.refresh_question_pack_list()
        self.refresh_coach_question_sources()

    def open_question_pack_folder(self):
        folder = question_pack_directory()
        folder.mkdir(parents=True, exist_ok=True)
        self.open_folder(folder)

    def start_coach_set(self):
        pack = self.coach_pack_var.get() if hasattr(self, "coach_pack_var") else "All"
        topic = self.coach_topic_var.get() if hasattr(self, "coach_topic_var") else "All"
        difficulty = self.coach_difficulty_var.get() if hasattr(self, "coach_difficulty_var") else "All"
        count_value = self.coach_count_var.get() if hasattr(self, "coach_count_var") else "All"
        order_value = self.coach_order_var.get() if hasattr(self, "coach_order_var") else "In order"

        questions = list(self.coach_questions)
        if pack != "All":
            questions = [item for item in questions if item.get("pack_name", BUILT_IN_PACK_NAME) == pack]
        if topic != "All":
            questions = [item for item in questions if item.get("topic") == topic]
        if difficulty != "All":
            questions = [item for item in questions if item.get("difficulty") == difficulty]

        if order_value == "Shuffle":
            questions = list(questions)
            random.shuffle(questions)

        if count_value != "All":
            try:
                limit = int(count_value)
                questions = questions[:limit]
            except (TypeError, ValueError):
                pass

        self.coach_visible_questions = questions or list(self.coach_questions)
        self.current_coach_index = 0
        self.coach_answer_var.set(-1)
        self.coach_attempted = 0
        self.coach_correct = 0
        self.coach_results = {}
        self.coach_set_label = f"Pack: {pack} | Topic: {topic} | Difficulty: {difficulty} | Count: {count_value} | Order: {order_value}"
        self.refresh_coach_question()

    def selected_coach_question(self):
        if not getattr(self, "coach_visible_questions", None):
            self.coach_visible_questions = list(self.coach_questions)
        if not self.coach_visible_questions:
            return None
        self.current_coach_index = max(0, min(self.current_coach_index, len(self.coach_visible_questions) - 1))
        return self.coach_visible_questions[self.current_coach_index]

    def refresh_coach_question(self):
        if not hasattr(self, "coach_question_var"):
            return
        item = self.selected_coach_question()
        for child in self.coach_choice_frame.winfo_children():
            child.destroy()
        if not item:
            self.coach_question_var.set("No coach questions are available.")
            self.set_text(self.coach_feedback_text, "")
            return
        self.coach_answer_var.set(-1)
        total = len(self.coach_visible_questions)
        question_id = item.get("id", f"index_{self.current_coach_index}")
        prior = self.coach_results.get(question_id)
        prior_text = ""
        if prior:
            prior_text = " | Prior: " + ("Correct" if prior.get("correct") else "Missed")
        self.coach_question_var.set(
            f"Question {self.current_coach_index + 1} of {total} | {item.get('pack_name', '')} | {item.get('topic', '')} | {item.get('difficulty', '')}{prior_text}\n{item.get('question', '')}"
        )
        for idx, choice in enumerate(item.get("choices", [])):
            ttk.Radiobutton(
                self.coach_choice_frame,
                text=choice,
                variable=self.coach_answer_var,
                value=idx,
            ).pack(anchor="w", padx=4, pady=3)
        self.set_text(
            self.coach_feedback_text,
            "Choose the safest answer, then select Check Answer. Use Show Answer when studying without scoring.",
        )
        self.update_coach_score()

    def update_coach_score(self):
        if hasattr(self, "coach_score_var"):
            total = len(getattr(self, "coach_visible_questions", []))
            missed = sum(1 for result in getattr(self, "coach_results", {}).values() if not result.get("correct"))
            self.coach_score_var.set(f"Score: {self.coach_correct}/{self.coach_attempted} checked | Missed: {missed} | Set size: {total}")

    def format_coach_answer(self, item, selected_index=None, reveal_only=False):
        if not item:
            return "No question selected."
        answer_index = item.get("answer_index", 0)
        choices = item.get("choices", [])
        correct_answer = choices[answer_index] if 0 <= answer_index < len(choices) else ""
        lines = [
            item.get("question", ""),
            "",
            f"Pack: {item.get('pack_name', '')} ({item.get('pack_publisher', '')})",
            "",
            "Best answer:",
            f"{answer_index + 1}. {correct_answer}",
            "",
            "Why:",
            item.get("explanation", ""),
            "",
            "Follow-up questions a senior examiner might ask:",
        ]
        lines.extend(f"- {value}" for value in item.get("follow_up", []))
        lines.append("")
        lines.append("Guardrail:")
        lines.append(item.get("guardrail", ""))
        lines.append("")
        lines.append("Related search terms:")
        lines.extend(f"- {value}" for value in item.get("search_terms", []))
        if selected_index is not None and selected_index >= 0 and not reveal_only:
            lines.insert(2, "Result: " + ("Correct" if selected_index == answer_index else "Not quite"))
        return "\n".join(lines)

    def check_coach_answer(self):
        item = self.selected_coach_question()
        if not item:
            return
        selected = self.coach_answer_var.get()
        if selected < 0:
            messagebox.showinfo("Choose an answer", "Select an answer first, or use Show Answer for study mode.")
            return
        question_id = item.get("id", f"index_{self.current_coach_index}")
        was_checked_before = question_id in self.coach_results
        correct = selected == item.get("answer_index", 0)
        self.coach_results[question_id] = {
            "id": question_id,
            "topic": item.get("topic", ""),
            "difficulty": item.get("difficulty", ""),
            "question": item.get("question", ""),
            "selected_index": selected,
            "answer_index": item.get("answer_index", 0),
            "correct": correct,
        }
        if not was_checked_before:
            self.coach_attempted += 1
            if correct:
                self.coach_correct += 1
        else:
            self.coach_correct = sum(1 for result in self.coach_results.values() if result.get("correct"))
            self.coach_attempted = len(self.coach_results)
        self.set_text(self.coach_feedback_text, self.format_coach_answer(item, selected_index=selected))
        self.update_coach_score()

    def build_coach_summary_text(self):
        total = len(getattr(self, "coach_visible_questions", []))
        attempted = len(getattr(self, "coach_results", {}))
        correct = sum(1 for result in self.coach_results.values() if result.get("correct"))
        missed = attempted - correct
        percent = round((correct / attempted) * 100, 1) if attempted else 0
        lines = [
            "Coach Mode Drill Summary",
            "",
            getattr(self, "coach_set_label", "Current question set"),
            f"Questions in set: {total}",
            f"Checked: {attempted}",
            f"Correct: {correct}",
            f"Missed: {missed}",
            f"Score: {percent}%" if attempted else "Score: Not started",
            "",
            "Missed / review items:",
        ]
        missed_items = self.get_missed_coach_questions()
        if missed_items:
            for item in missed_items:
                lines.append(f"- {item.get('pack_name', '')} / {item.get('topic', '')} / {item.get('difficulty', '')}: {item.get('question', '')}")
        else:
            lines.append("- No missed questions in the current checked set.")
        lines.append("")
        lines.append("Reminder: Coach Mode is for refresher training and examiner-thinking practice. It is not a certification test and it does not score case work.")
        return "\n".join(lines)

    def get_missed_coach_questions(self):
        missed_ids = {qid for qid, result in getattr(self, "coach_results", {}).items() if not result.get("correct")}
        if not missed_ids:
            return []
        lookup = {item.get("id", f"index_{idx}"): item for idx, item in enumerate(self.coach_questions)}
        return [lookup[qid] for qid in missed_ids if qid in lookup]

    def show_coach_summary(self):
        self.show_text_popup("Coach Drill Summary", self.build_coach_summary_text())

    def review_missed_coach_questions(self):
        missed = self.get_missed_coach_questions()
        if not missed:
            messagebox.showinfo("Review Missed", "No missed questions are available for review in the current drill.")
            return
        self.coach_visible_questions = missed
        self.current_coach_index = 0
        self.coach_answer_var.set(-1)
        self.coach_set_label = "Missed-question review"
        self.refresh_coach_question()
        messagebox.showinfo("Review Missed", f"Loaded {len(missed)} missed question(s) for review.")

    def copy_missed_coach_review(self):
        self.copy_to_clipboard(self.build_coach_summary_text(), "Coach drill summary")

    def show_coach_answer(self):
        item = self.selected_coach_question()
        self.set_text(self.coach_feedback_text, self.format_coach_answer(item, reveal_only=True))

    def next_coach_question(self):
        if not getattr(self, "coach_visible_questions", None):
            return
        self.current_coach_index = (self.current_coach_index + 1) % len(self.coach_visible_questions)
        self.refresh_coach_question()

    def copy_coach_explanation(self):
        self.copy_to_clipboard(self.format_coach_answer(self.selected_coach_question(), reveal_only=True), "Coach explanation")

    def search_coach_terms(self):
        item = self.selected_coach_question()
        if not item:
            return
        terms = item.get("search_terms", [])
        query = terms[0] if terms else item.get("topic", "")
        self.reference_query_var.set(query)
        self.show_reference_page()
        self.run_reference_search()

    def open_coach_scenario(self):
        item = self.selected_coach_question()
        if not item:
            return
        # Coach Mode questions may link to older scenario-card IDs or newer coaching prompts.
        scenario_id = item.get("related_scenario_id", "")
        for coaching in SCENARIO_COACHING_QUESTIONS:
            if coaching.get("id") == scenario_id or coaching.get("category") == item.get("topic"):
                self.show_scenario_page()
                if hasattr(self, "coaching_prompt_var"):
                    self.coaching_prompt_var.set(coaching.get("title", ""))
                    self.refresh_coaching_prompt()
                return
        self.show_scenario_page()
        messagebox.showinfo("Coaching", "Opened the Coaching lane. This question does not have a one-to-one coaching prompt yet.")


    def selected_decision_path(self):
        label = self.decision_path_var.get() if hasattr(self, "decision_path_var") else ""
        for path in DECISION_PATHS:
            if path.get("label") == label:
                return path
        return DECISION_PATHS[0] if DECISION_PATHS else None

    def refresh_decision_detail(self):
        path = self.selected_decision_path()
        if not path:
            return
        playbook = get_playbook(path.get("playbook_id", "")) or {}
        lines = [
            path.get("label", ""),
            "",
            "Recommended playbook:",
            f"- {playbook.get('title', path.get('playbook_id', ''))}",
            "",
            "Recommended mode:",
            f"- {path.get('recommended_mode', 'Field Reference')}",
            "",
            "Why this path fits:",
            path.get("why", ""),
            "",
            "Quick questions before you continue:",
        ]
        lines.extend(f"- {item}" for item in path.get("questions", []))
        lines.append("")
        lines.append("First steps this playbook will emphasize:")
        lines.extend(f"- {item}" for item in path.get("first_steps", []))
        lines.append("")
        lines.append("Boundary reminder:")
        lines.append("Playbooks explains the work. It does not track the case, collect evidence, parse artifacts, or make conclusions.")
        self.set_text(self.decision_detail_text, "\n".join(lines))

    def open_recommended_playbook(self, force_mode=None):
        path = self.selected_decision_path()
        if not path:
            messagebox.showinfo("No recommendation", "Select a situation first.")
            return
        playbook_id = path.get("playbook_id", "")
        mode = force_mode or path.get("recommended_mode", "Field Reference")
        try:
            self.save_current_step_notes()
            self.session = create_session(playbook_id, mode)
            self.current_step_index = 1
            self.mode_var.set(mode)
            self.sync_current_step_index()
            self.refresh_all()
            self.show_playbook_page()
        except Exception as exc:
            messagebox.showerror("Could not open playbook", str(exc))

    def browse_output_root(self):
        folder = filedialog.askdirectory(title="Select ByteCase output root")
        if folder:
            self.output_root_var.set(folder)

    def save_settings_action(self):
        self.settings.setdefault("output", {})["output_root"] = self.output_root_var.get().strip()
        self.settings["output"]["export_txt"] = self.export_txt_var.get()
        self.settings["output"]["export_docx"] = self.export_docx_var.get()
        self.settings.setdefault("appearance", {})["theme"] = self.theme_var.get()
        self.settings.setdefault("defaults", {})["mode"] = self.mode_var.get()
        save_settings(self.settings)
        self.colors = apply_theme(self.root, self.settings)
        messagebox.showinfo("Settings saved", "Settings saved. Restart the app if any visual element does not refresh immediately.")

    def set_text(self, widget, text, readonly=True):
        widget.configure(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert("1.0", text or "")
        if readonly:
            widget.configure(state="disabled")

