# Vibe Coding Demo Project: AI Article Sharer

This is a demonstration project showcasing the "Vibe Coding" development process. The project implements a simple Flask website that allows users to click a button and randomly receive three article links about AI and Vibe Coding.

## Project Background

This project originates from my experience shared in [From "Writing Code" to "Dancing with AI" - My Experience Promoting Vibe Coding in My Company](https://medium.com/p/015e28909290). The article explores how to elevate AI assistants (like Cursor) from personal productivity tools to a part of team knowledge sharing and collaboration.

## The Four Levels of Vibe Coding

The demo project showcases the four levels of Vibe Coding mentioned in the article:

1. **Level 1 (Generate)**: Using AI to generate basic code and structure
2. **Level 2 (Enhance)**: Having AI assist with refactoring and optimizing code
3. **Level 3 (Systematize)**: Systematizing team knowledge and standards through Project Rules
4. **Level 4 (Automate)**: Integration into workflows (not covered in this demo project)

## Project Design Focus

This project is intentionally designed to be small and simple, but includes various considerations found in actual development:

- **Plan Mode**: Using `plan.md` for detailed planning, explaining project goals and implementation steps
- **Rule Implementation**: Using Project Rules in `.cursor/rules/` to systematize team standards:
  - Business logic rules (`business_logic.mdc`)
  - Python code style rules (`python_linting.mdc`)
  - Flask best practices (`flask_best_practice.mdc`)
- **Act Mode**: Implementing specific functionality according to the plan and rules

## Project Structure

```
.
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Frontend page template
├── static/             # (Optional) CSS/JS files
├── .cursor/rules/      # Cursor Project Rules directory
│   ├── business_logic.mdc
│   ├── python_linting.mdc
│   ├── flask_best_practice.mdc
│   └── generate_tasks_from_plan.mdc
├── requirements.txt    # Python dependency list
├── docs/               # Project documentation directory
│   ├── prd_*.md        # Product requirement documents
│   ├── plan.md         # System design and implementation strategy
│   └── task.md         # Breakdown task list
└── README.md           # This readme file
```

## Development Process

This project uses a two-stage development process, from requirement documents to executable tasks:

### 1. From PRD to System Design

- When a product requirement document with the prefix "prd_" exists, the system automatically analyzes the document and generates a system design plan
- All designs and strategies are written to `docs/plan.md`, including:
  - System design summary
  - Implementation strategy
  - Key technical considerations

### 2. From System Design to Task List

- Team members review the system design in `docs/plan.md`
- After confirming the design, the system generates specific tasks based on the plan, written to `docs/task.md`
- Tasks are presented in table format, including:
  - Task ID
  - Title
  - Estimated time
  - Dependencies
  - Status (TO-DO, IN-PROGRESS, REVIEW, DONE)
  - Acceptance criteria
- Task status reflects development progress and review status:
  - **TO-DO**: Task waiting to be started
  - **IN-PROGRESS**: Task in development
  - **REVIEW**: Task development completed, waiting for review
  - **DONE**: Review passed, can be committed to git

This two-stage approach ensures a smooth transition from high-level design to specific implementation, and allows team members to participate in design discussions before task breakdown.

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   flask run
   ```

3. Access in browser:
   ```
   http://localhost:5000
   ```

## How to Use This Demo

As a teaching example demonstrating Vibe Coding, you can focus on the following points:

1. Read `plan.md` to understand the project planning approach
2. Check the `.cursor/rules/` directory to understand how team knowledge is systematized
3. Study how `app.py` and `templates/index.html` follow these rules
4. Try modifying or extending functionality yourself to experience how AI assists development based on existing rules

## Extension Suggestions

To extend this demo project into a more complete application, you might consider:

1. Integrating a search API to dynamically fetch articles instead of using a hardcoded list
2. Adding article preview functionality
3. Implementing user bookmark functionality
4. Adding category filtering

## About Vibe Coding

Vibe Coding is not just using AI to assist programming, but a development philosophy that treats AI as a team member, focusing on:

1. The transition from **personal productivity** to **team knowledge**
2. Systematizing tacit knowledge through rules
3. Enabling AI to understand and follow the team's business logic and technical standards

## Task Management References

This project references the following open-source tools and concepts for task management:

1. **Task Master** ([github.com/eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master)): We've integrated its task tracking and management concepts to better fit this project's development process.

2. **Extension Possibilities**: Features in Task Master such as Test Strategy and Sub Tasks for each task can also be implemented in this project through custom Cursor rules (see `.cursor/rules/generate_tasks_from_plan.mdc`), but for simplicity, this demo project does not fully implement these features.

---

*This project is for demonstration and educational purposes only.* 