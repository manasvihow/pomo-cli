import click
import time
import os
import platform
import json
import re

try:
    import winsound
except ImportError:
    winsound = None

# --- Global Variables ---
log_file = "pomo_log.json"

# --- Helper Functions ---

def parse_duration(duration_str):
    if duration_str.isdigit():
        return int(duration_str) * 60
    parts = re.findall(r'(\d+)([ms])', duration_str)
    if not parts:
        click.echo(f"Warning: Invalid duration format '{duration_str}'. Defaulting to 25 minutes.")
        return 25 * 60
    total_seconds = 0
    for value, unit in parts:
        value = int(value)
        if unit == 'm':
            total_seconds += value * 60
        elif unit == 's':
            total_seconds += value
    return total_seconds

def play_alert_sound():
    sound_file = 'ding.mp3'
    if not os.path.exists(sound_file):
        # Acknowledging the warning you saw in your output
        click.echo(f"\nWarning: Sound file '{sound_file}' not found. Place a .wav file here for alerts.")
        return
    system = platform.system()
    try:
        if system == 'Darwin':
            os.system(f'afplay {sound_file} &')
        elif system == 'Windows':
            if winsound:
                winsound.PlaySound(sound_file, winsound.SND_FILENAME)
        elif system == 'Linux':
            os.system(f'aplay -q {sound_file} &')
    except Exception as e:
        click.echo(f"\nWarning: Could not play sound. Error: {e}")

# --- CHANGED: Now logs duration in seconds ---
def log_session(duration_seconds, description, tags):
    """Appends a completed session to the JSON log file."""
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
    logs.append({
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'duration_seconds': duration_seconds,
        'description': description,
        'tags': tags
    })
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=4)


# --- Main CLI Group ---
@click.group()
def cli():
    """A simple Pomodoro timer CLI."""
    pass


# --- CLI Commands ---

@cli.command()
@click.argument('description', required=False, default="Work")
@click.option('--duration', '-d', default="25", type=str, help='Duration in format like "30", "15s", "22m30s".')
@click.option('--tags', '-t', default="", help='Comma-separated tags for the session.')
def start(duration, description, tags):
    """Starts a new Pomodoro session."""
    duration_seconds = parse_duration(duration)
    minutes_for_display = round(duration_seconds / 60.0, 2)
    
    click.echo(f"Starting a {minutes_for_display}-minute session for: '{description}' 🧘")
    end_time = time.time() + duration_seconds
    last_displayed_time = ""
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        remaining_seconds = max(0, remaining_seconds)
        mins, secs = divmod(remaining_seconds, 60)
        time_string = f"{mins:02d}:{secs:02d}"
        if time_string != last_displayed_time:
            click.echo(f"  ⏳ Time remaining: {time_string}", nl=False)
            click.echo('\r', nl=False)
            last_displayed_time = time_string
        time.sleep(0.1)
    
    click.echo("  ⏳ Time remaining: 00:00")
    final_message = f"🎉 Session '{description}' finished! Time for a short break. 🎉"
    click.echo(final_message)
    play_alert_sound()
    # --- CHANGED: Pass seconds to the log function ---
    log_session(duration_seconds, description, tags)


@cli.command(name='break')
@click.option('--minutes', '-m', default=5, type=float, help='The duration of the break in minutes.')
@click.option('--long', '-l', is_flag=True, help='Flag to start a long break (15 minutes).')
def break_timer(minutes, long):
    """Starts a break session."""
    if long:
        minutes = 15
    duration_seconds = int(minutes * 60)
    
    click.echo(f"Starting a {minutes}-minute break. Time to relax! ☕")
    for i in range(duration_seconds, -1, -1):
        mins, secs = divmod(i, 60)
        time_string = f"{mins:02d}:{secs:02d}"
        click.echo(f"  ⏳ Time remaining: {time_string}", nl=False)
        click.echo('\r', nl=False)
        time.sleep(1)
        
    final_message = "🎉 Break is over! Time to get back to it. 🎉"
    click.echo(f"\n{final_message}")
    play_alert_sound()


# --- Replace your existing 'repeat' command with this one ---

@cli.command()
@click.argument('query') # This line tells click to expect an argument like "fixing"
@click.pass_context
def repeat(ctx, query):
    """Repeats the last session matching the query in description or tags."""
    if not os.path.exists(log_file):
        click.echo("Log file not found. No sessions to repeat.")
        return

    with open(log_file, 'r') as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    
    # Search in reverse to find the most recent match
    for session in reversed(logs):
        if query.lower() in session.get('description', '').lower() or \
           query.lower() in session.get('tags', '').lower():
            
            click.echo(f"Found last session: '{session['description']}' with tags '{session['tags']}'. Repeating.")
            
            seconds = session['duration_seconds']
            duration_str = f"{seconds}s" # e.g., "10s"
            
            # Use ctx.invoke to call the 'start' command with the found parameters
            ctx.invoke(
                start,
                duration=duration_str,
                description=session['description'],
                tags=session['tags']
            )
            return # Exit after finding and running the first match

    click.echo(f"No past session found matching '{query}'.")
    
if __name__ == '__main__':
    cli()

