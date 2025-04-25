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
- After confirming the design, the system generates both a task summary and individual detailed task files:
  - A summary table in `docs/task.md` with all tasks in a concise format
  - Individual task files in `docs/tasks/` directory (e.g., `task_T001.md`, `task_T002.md`) with detailed information

#### Enhanced Task Management System

The project implements a task management system inspired by Task Master with these key features:

1. **Dual-layer Documentation**: Summary table in `task.md` and detailed files in `tasks/` directory
   
2. **Task Metadata**: ID, title, description, status, dependencies (with visual indicators ✅⏱️), priority, and estimated time

3. **Dependency Tracking**: Accurate status indicators prevent work on incomplete prerequisites

4. **Task Information**: Implementation details, acceptance criteria, and test strategies

5. **Status Workflow**: TO-DO → IN-PROGRESS → REVIEW → DONE

This system helps teams manage complex projects with interdependent components, maintain visibility into task status, ensure consistent implementation, and scale across larger teams.


## Project Design Focus

This project is intentionally designed to be small and simple, but includes various considerations found in actual development:

- **Plan Mode**: Using `plan.md` for detailed planning, explaining project goals and implementation steps
- **Rule Implementation**: Using Project Rules in `.cursor/rules/` to systematize team standards:
  - Business logic rules (`business_logic.mdc`)
  - Python code style rules (`python_linting.mdc`)
  - Flask best practices (`flask_best_practice.mdc`)
  - Task generation automation (`generate_tasks_from_plan.mdc`) - Automatically converts product requirements into structured tasks
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
│   ├── task.md         # Task summary table with all tasks
│   └── tasks/          # Directory containing detailed individual task files
└── README.md           # This readme file
```



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


## About Vibe Coding

Vibe Coding is not just using AI to assist programming, but a development philosophy that treats AI as a team member, focusing on:

1. The transition from **personal productivity** to **team knowledge**
2. Systematizing tacit knowledge through rules
3. Enabling AI to understand and follow the team's business logic and technical standards

## Task Management References

This project references the concept of the following tools

1. **Task Master** ([github.com/eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master)): We've integrated its comprehensive task tracking and management concepts to enable handling of complex project requirements:
   - Dual-layer task documentation (summary + detailed files)
   - Dependency status tracking with visual indicators
   - Comprehensive test strategy documentation
   - Detailed acceptance criteria

2. **Features for Complex Projects**: The enhanced task management system supports complex project requirements through:
   - Precise dependency tracking that prevents work on tasks with incomplete prerequisites
   - Detailed implementation instructions that maintain consistency across developers
   - Strict status consistency rules to prevent misrepresentation of progress
   - Scalable task ID system supporting parent-child relationships for task hierarchies

To use this enhanced task management system for your own complex projects:
1. Adapt the `.cursor/rules/generate_tasks_from_plan.mdc` file to match your project's needs
2. Create your product requirements document in `docs/prd_*.md`
3. Let the system generate your plan and tasks
4. Iterate through task implementation following the defined workflow

---

*This project is for demonstration and educational purposes only.* 