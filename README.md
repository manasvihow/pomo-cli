# 🍅 Pomo CLI

A simple Pomodoro timer for your command line. 

---

## ✨ Features

* Intuitive `start`, `break`, `log`, and `repeat` commands.
* Specify time in various formats like `30s`, `5m`, or `22m30s`.
* Add comma-separated tags to your sessions for better organization (e.g., `--tags writing,blog`).
* Automatically logs all completed sessions to a local `pomo_log.json` file.
* View your completed Pomodoros with the `log` command.
* Quickly restart a previous task using the `repeat` command.
* **Cross-Platform**: Works on macOS, Windows, and Linux.

### Live Timer Display

When you start a session, you'll see a live progress bar that fills up with tomatoes as you go:

```

# At the start

⏳ 25:00 [────────────────────] Writing the first draft

# A few minutes later...

⏳ 18:45 [🍅🍅🍅🍅🍅─────────────] Writing the first draft

# Almost done!

⏳ 01:15 [🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅─] Writing the first draft

````

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
pomo start "Writing the first draft" --tags writing,blog
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

Start a custom break:

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
