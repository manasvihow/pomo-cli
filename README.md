# 🍅 Pomo CLI - A Simple Pomodoro Timer

A simple, elegant, and powerful Pomodoro timer for your command line. Boost your productivity and track your work sessions without ever leaving the terminal.

---

## ✨ Features

* **Simple Commands**: Intuitive `start`, `break`, `log`, and `repeat` commands.
* **Flexible Durations**: Specify time in various formats like `30s`, `5m`, or `22m30s`.
* **Categorize with Tags**: Add comma-separated tags to your sessions for better organization (e.g., `--tags writing,blog` or `-t writing, blog`).
* **Task Logging**: Automatically logs all completed sessions to a local `pomo_log.json` file.
* **Session History**: View your completed Pomodoros with the `log` command.
* **Repeat Tasks**: Quickly restart a previous task using the `repeat` command.
* **Visual Progress Bar**: A clean, emoji-powered progress bar shows your time remaining.
* **Cross-Platform**: Works on macOS, Windows, and Linux.

---

## 💾 Installation

Install `pomo-cli` directly from PyPI using pip:

```bash
pip install pomo-cli
````

-----

## 🚀 Usage

Once installed, you can use the `pomo` command from anywhere in your terminal.

### Starting a Session

Start a default 25-minute work session:

```bash
pomo start "Writing the first draft" --t writing,blog
```

Start a quick 30-second session:

```bash
pomo start "Reviewing PR" -d 5m
```

### Taking a Break

Start a default 5-minute break:

```bash
pomo break
```

Start a custom duration break:

```bash
pomo break -d 15m
```

### Viewing Your History

See the last 10 sessions you completed:

```bash
pomo log
```

See the last 3 sessions:

```bash
pomo log -n 3
```

See all logged sessions:

```bash
pomo log --all
```

### Repeating a Session

Repeat the last session that had the tag "writing":

```bash
pomo repeat writing
```

-----

## 📄 License

This project is licensed under the MIT License.
