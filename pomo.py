import click
import time

@click.group()
def cli():
    """A simple Pomodoro timer CLI."""
    pass

@cli.command()
@click.option('--minutes', '-m', default=25, help='The duration of the pomodoro session in minutes.')
def start(minutes):
    """Starts a new Pomodoro session."""
    
    duration = minutes * 60 
    
    click.echo(f"Starting a {minutes}-minute Pomodoro session. Time to focus! 🧘")

    for i in range(duration, 0, -1):
        mins, secs = divmod(i, 60)
        time_string = f"{mins:02d}:{secs:02d}"
        click.echo(f"  ⏳ Time remaining: {time_string}", nl=False)
        click.echo('\r', nl=False)
        time.sleep(1)
        
    click.echo(f"\n🎉 {minutes}-minute session finished! Time for a short break. 🎉")


@cli.command(name='break')
@click.option('--minutes', '-m', default=0, help='The duration of the break in minutes.')
@click.option('--long', '-l', is_flag=True, help='Flag to start a long break (15 minutes).')
def break_timer(minutes, long):
    """Starts a break session."""
    
    duration_minutes = 0
    break_type = "break"

    if minutes:
        # If user provides --minutes, it takes top priority
        duration_minutes = minutes
    elif long:
        # If --long flag is used, it's a 15 min long break
        duration_minutes = 15
        break_type = "long break"
    else:
        # Otherwise, it's a default 5 min short break
        duration_minutes = 5
        break_type = "short break"
        
    duration_seconds = duration_minutes * 60
    
    click.echo(f"Starting a {duration_minutes}-minute {break_type}. Time to relax! ☕")
    
    for i in range(duration_seconds, 0, -1):
        mins, secs = divmod(i, 60)
        time_string = f"{mins:02d}:{secs:02d}"
        click.echo(f"  ⏳ Time remaining: {time_string}", nl=False)
        click.echo('\r', nl=False)
        time.sleep(1)
        
    click.echo("\n🎉 Break is over! Time to get back to it. 🎉")


if __name__ == '__main__':
    cli()