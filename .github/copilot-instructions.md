### 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports** (prefer relative imports within packages).
- **If user request is lacking clarity, always use brave search to search for more context**
- **Always use sequential thinking, memory, context7 for coding tasks**
- **Always use the most up-to-date coding style appropriate given the context7 documentation**

### 🧪 Testing & Reliability
- **Always create unit tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case

### ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.
- **At the end of a completion of a task, always update the progress of the project through the Jira/Atlassian MCP and always provide a direct link for tracking.

### 📎 Style & Conventions
- **Use Python** as the primary language.
- **Follow PEP8**, use type hints, and format with `black`.
- **Use `pydantic` for data validation**.
- Use `FastAPI` for APIs and `SQLAlchemy` or `SQLModel` for ORM if applicable.
- Write **docstrings for every function** using the Google style:
  ```python
  def example():
      """
      Brief summary.

      Args:
          param1 (type): Description.

      Returns:
          type: Description.
      """
  ```

### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.

you are to always use appropriate MCP tools for the task. List of tools:

# Enhanced MCP Tool Usage Guidelines

## 🔧 General MCP Tool Principles

- **Understand tool capabilities** before invoking them - each tool has specific strengths and use cases.
- **Respect token efficiency** - only retrieve what's needed and process large datasets incrementally.
- **Validate inputs and outputs** for each tool to ensure reliable operation.
- **Handle errors gracefully** with informative error messages and recovery strategies.
- **Maintain context** between tool interactions to build on previous results.

## 📚 Context7 Documentation Tool

### When to Use:
- When implementing features that depend on third-party libraries or frameworks.
- When needing up-to-date API documentation that might have changed since training data.
- To verify correct usage patterns, parameters, or return types for external libraries.
- When exploring alternative libraries for a specific functionality.

### Best Practices:
- **Always use two-step process**: First resolve the library ID, then fetch documentation.
- **Be specific with topics** to get targeted documentation instead of general overviews.
- **Request appropriate token limits** based on the complexity of the documentation needed.
- **Cache documentation results** when working extensively with a particular library.
- **Extract and highlight key information** rather than pasting full documentation.

## 🔍 Brave Search Tool

### When to Use:
- When needing information beyond training cutoff date (currently October 2024).
- When researching library-specific best practices or common issues.
- When looking for reference implementations or code examples.
- When investigating compatibility issues between libraries or versions.
- When researching performance considerations for specific technologies.

### Best Practices:
- **Construct precise queries** using technical terms and specific version numbers when applicable.
- **Search in iterations**, starting with broad queries and then refining based on initial results.
- **Combine search terms** with framework names to get context-specific results.
- **Prioritize official documentation** sources over forum posts or blogs.
- **Verify recency of information** when dealing with rapidly evolving frameworks.
- **Cite sources** in code comments when implementing solutions found through search.

## 📂 Filesystem Tool

### When to Use:
- When analyzing project structure at the beginning of tasks.
- When locating relevant files for modification.
- When verifying existence of files or directories before operations.
- When reading file content to understand implementation details.
- When creating new files or updating existing ones.
- When executing batch operations across multiple files.

### Best Practices:
- **Always check file existence** before attempting to read or modify.
- **Use directory_tree** for initial project exploration to understand structure.
- **Leverage search_files** with appropriate patterns to locate relevant files.
- **Get file metadata** before performing large operations to understand size constraints.
- **Use incremental edits** for large files rather than full rewrites.
- **Create directory structures** before writing files to avoid path errors.
- **Maintain backups** of existing content before making significant changes.
- **Follow project conventions** for file naming and directory organization.

## 📊 GitHub Tool

### When to Use:
- When forking repositories for reference or customization.
- When searching for example implementations across multiple repositories.
- When retrieving code from public repositories that demonstrate patterns.
- When creating or updating repositories to share project code.
- When managing issues and pull requests for collaborative development.

### Best Practices:
- **Search repositories** with specific technical terms to find relevant examples.
- **Examine file contents** before incorporating to ensure compatibility with current project.
- **Create focused pull requests** with clear titles and descriptions.
- **Use issue search** to find similar problems that may have been resolved previously.
- **Reference specific commits** when discussing code evolution.
- **Create branches** for feature development to maintain clean project history.
- **Provide detailed commit messages** that explain purpose and implementation details.
- **Review code changes** before finalizing pull requests.

## 📝 Atlassian (Jira/Confluence) Tool

### When to Use:
- When retrieving project requirements or specifications.
- When accessing knowledge base articles for implementation guidance.
- When creating or updating tickets for task tracking.
- When documenting implementation decisions or technical approaches.
- When checking acceptance criteria for features.

### Best Practices:
- **Use specific JQL queries** to retrieve relevant issues efficiently.
- **Search Confluence** with specific terms to locate technical documentation.
- **Link related issues** when creating new tickets.
- **Update issue status** as tasks progress.
- **Include implementation details** in issue comments for future reference.
- **Add testing notes** to issues when completing development work.
- **Reference issue keys** in commit messages and code comments.
- **Create or update documentation** in Confluence when completing significant features.

## 🔄 Tool Integration Patterns

- **Chain results** between tools for comprehensive solutions (e.g., search → GitHub → filesystem).
- **Verify information** from one tool with another when accuracy is critical.
- **Combine file analysis** with documentation lookup to ensure correct implementation.
- **Use search results** to inform GitHub repository selection or code retrieval.
- **Reference Jira requirements** while performing filesystem operations to ensure alignment.
- **Document search and GitHub findings** in Confluence for team knowledge sharing.

## 🚀 Performance Optimization

- **Limit search scope** to retrieve only essential information.
- **Process large files in chunks** rather than loading entirely into context.
- **Cache frequently accessed documentation** to reduce repetitive lookups.
- **Prioritize local file operations** over network requests when possible.
- **Use efficient search patterns** to locate relevant content quickly.

These guidelines should help maximize the effectiveness of MCP tools while maintaining project efficiency and quality standards.

# Enhanced MCP Tool Usage Guidelines

## 🔧 General MCP Tool Principles

- **Understand tool capabilities** before invoking them - each tool has specific strengths and use cases.
- **Respect token efficiency** - only retrieve what's needed and process large datasets incrementally.
- **Validate inputs and outputs** for each tool to ensure reliable operation.
- **Handle errors gracefully** with informative error messages and recovery strategies.
- **Maintain context** between tool interactions to build on previous results.

## 📚 Context7 Documentation Tool

### When to Use:
- When implementing features that depend on third-party libraries or frameworks.
- When needing up-to-date API documentation that might have changed since training data.
- To verify correct usage patterns, parameters, or return types for external libraries.
- When exploring alternative libraries for a specific functionality.

### Best Practices:
- **Always use two-step process**: First resolve the library ID, then fetch documentation.
- **Be specific with topics** to get targeted documentation instead of general overviews.
- **Request appropriate token limits** based on the complexity of the documentation needed.
- **Cache documentation results** when working extensively with a particular library.
- **Extract and highlight key information** rather than pasting full documentation.

## 🔍 Brave Search Tool

### When to Use:
- When needing information beyond training cutoff date (currently October 2024).
- When researching library-specific best practices or common issues.
- When looking for reference implementations or code examples.
- When investigating compatibility issues between libraries or versions.
- When researching performance considerations for specific technologies.

### Best Practices:
- **Construct precise queries** using technical terms and specific version numbers when applicable.
- **Search in iterations**, starting with broad queries and then refining based on initial results.
- **Combine search terms** with framework names to get context-specific results.
- **Prioritize official documentation** sources over forum posts or blogs.
- **Verify recency of information** when dealing with rapidly evolving frameworks.
- **Cite sources** in code comments when implementing solutions found through search.

## 📂 Filesystem Tool

### When to Use:
- When analyzing project structure at the beginning of tasks.
- When locating relevant files for modification.
- When verifying existence of files or directories before operations.
- When reading file content to understand implementation details.
- When creating new files or updating existing ones.
- When executing batch operations across multiple files.

### Best Practices:
- **Always check file existence** before attempting to read or modify.
- **Use directory_tree** for initial project exploration to understand structure.
- **Leverage search_files** with appropriate patterns to locate relevant files.
- **Get file metadata** before performing large operations to understand size constraints.
- **Use incremental edits** for large files rather than full rewrites.
- **Create directory structures** before writing files to avoid path errors.
- **Maintain backups** of existing content before making significant changes.
- **Follow project conventions** for file naming and directory organization.

## 📊 GitHub Tool

### When to Use:
- When forking repositories for reference or customization.
- When searching for example implementations across multiple repositories.
- When retrieving code from public repositories that demonstrate patterns.
- When creating or updating repositories to share project code.
- When managing issues and pull requests for collaborative development.

### Best Practices:
- **Search repositories** with specific technical terms to find relevant examples.
- **Examine file contents** before incorporating to ensure compatibility with current project.
- **Create focused pull requests** with clear titles and descriptions.
- **Use issue search** to find similar problems that may have been resolved previously.
- **Reference specific commits** when discussing code evolution.
- **Create branches** for feature development to maintain clean project history.
- **Provide detailed commit messages** that explain purpose and implementation details.
- **Review code changes** before finalizing pull requests.

## 📝 Atlassian (Jira/Confluence) Tool

### When to Use:
- When retrieving project requirements or specifications.
- When accessing knowledge base articles for implementation guidance.
- When creating or updating tickets for task tracking.
- When documenting implementation decisions or technical approaches.
- When checking acceptance criteria for features.

### Best Practices:
- **Use specific JQL queries** to retrieve relevant issues efficiently.
- **Search Confluence** with specific terms to locate technical documentation.
- **Link related issues** when creating new tickets.
- **Update issue status** as tasks progress.
- **Include implementation details** in issue comments for future reference.
- **Add testing notes** to issues when completing development work.
- **Reference issue keys** in commit messages and code comments.
- **Create or update documentation** in Confluence when completing significant features.

## 🔄 Tool Integration Patterns

- **Chain results** between tools for comprehensive solutions (e.g., search → GitHub → filesystem).
- **Verify information** from one tool with another when accuracy is critical.
- **Combine file analysis** with documentation lookup to ensure correct implementation.
- **Use search results** to inform GitHub repository selection or code retrieval.
- **Reference Jira requirements** while performing filesystem operations to ensure alignment.
- **Document search and GitHub findings** in Confluence for team knowledge sharing.

## 🚀 Performance Optimization

- **Limit search scope** to retrieve only essential information.
- **Process large files in chunks** rather than loading entirely into context.
- **Cache frequently accessed documentation** to reduce repetitive lookups.
- **Prioritize local file operations** over network requests when possible.
- **Use efficient search patterns** to locate relevant content quickly.

These guidelines should help maximize the effectiveness of MCP tools while maintaining project efficiency and quality standards.
