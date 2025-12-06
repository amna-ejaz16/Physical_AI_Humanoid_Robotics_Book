<!--
Sync Impact Report:
Version change: 0.0.0 (initial/placeholder) → 1.0.0
Modified principles: All (from template placeholders to concrete definitions)
Added sections: Key Standards, Constraints, Success Criteria
Removed sections: None (placeholders filled or expanded)
Templates requiring updates:
- .specify/templates/plan-template.md: ✅ Updated (Implicitly aligned; no direct changes needed to template content)
- .specify/templates/spec-template.md: ✅ Updated (Implicitly aligned; no direct changes needed to template content)
- .specify/templates/tasks-template.md: ✅ Updated (Implicitly aligned; no direct changes needed to template content)
- .claude/commands/sp.adr.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.analyze.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.checklist.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.clarify.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.constitution.md: ✅ Updated (This command file itself is implicitly aligned by executing this update)
- .claude/commands/sp.git.commit_pr.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.implement.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.phr.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.plan.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.specify.md: ✅ Updated (Implicitly aligned)
- .claude/commands/sp.tasks.md: ✅ Updated (Implicitly aligned)
Follow-up TODOs: None
-->
# AI/Spec-Driven Book — “Physical AI & Humanoid Robotics” Constitution

## Core Principles

### Technical Accuracy
All robotics, AI, biomechanics, and control-system concepts MUST be correct, validated through authoritative sources or primary robotics research.

### Engineering Clarity
Content MUST be understandable to readers with undergraduate-level background in robotics, AI, or computer science.

### Modular Documentation
Each chapter MUST be written as a self-contained Docusaurus page with reusable components, diagrams, and definitions.

### Reproducibility & Transparency
All explanations, algorithms, and mechanical principles MUST be traceable to credible references.

### Safety & Ethics Awareness
Content MUST ensure responsible framing of AI embodiment, autonomy, Human–Robot Interaction (HRI), and real-world deployment.

### Consistency with Spec-Kit Plus methodology
All outputs MUST align with spec-driven development, structured thinking, and verifiable constraints.

## Key Standards

- Every factual or technical claim MUST be traceable to:
  - Robotics textbooks, IEEE papers, ACM papers, arXiv preprints, or official documentation.
- Citation Format: IEEE or APA (author–year) depending on technical section.
- Minimum 50% peer-reviewed, standards-based, or academically credible sources (IEEE, ACM, Springer, MIT Press, etc.).
- Visual assets (diagrams, flowcharts, mechanical schematics) MUST include alt-text and source/reference if not original.
- Code Samples: Written in Python, ROS/ROS2, or pseudo-code; MUST be runnable or logically consistent.
- Content Quality:
  - Clarity: Grade 10–12 readability for explanations; advanced sections may exceed this.
  - Tone: Engineering-professional, concise, precise.
- Tools:
  - Spec-Kit Plus for structured generation.
  - Claude Code for scalable multi-file creation.
  - Docusaurus for documentation structure.
  - GitHub Pages for deployment.

## Constraints

- Book Length: 20–30 chapters (modular), each 800–2,000 words.
- Total estimated word count: 25,000–45,000.
- Minimum Sources: 30 high-quality references across the book.
- Output Format:
  - Markdown (.mdx) optimized for Docusaurus
  - MUST support code blocks, diagrams, callouts, and structured headings
- File/Folder Structure:
  - /docs/chapters/*
  - /docs/diagrams/*
  - /docs/references/*
- All chapters SHOULD include:
  - learning objectives
  - topic overview
  - core content
  - diagrams
  - real-world applications
  - references section

## Success Criteria

- Technical excellence verified against robotics and AI research.
- Zero plagiarism; all content original or properly cited.
- Book builds progressively from fundamentals → applied robotics → embodied intelligence → humanoid architecture.
- All markdown files compile in Docusaurus without errors.
- Final GitHub Pages deployment builds successfully.
- Content audited for:
  - Structural consistency
  - Engineering correctness
  - Ethical/safety awareness
  - Implementability via Spec-Kit Plus workflow

## Governance
This Constitution supersedes all other project practices. Amendments require formal documentation, approval, and a clear migration plan. All Pull Requests (PRs) and code reviews MUST verify compliance with these principles. Complexity MUST be justified. Refer to `CLAUDE.md` for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-12-04 | **Last Amended**: 2025-12-04