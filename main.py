""" Pydoro
A Python-based Pomodoro timer featuring terminal controls, session analytics, and a floating GUI countdown.
"""
import tracker
from timer_window import TimerHUD
hud = TimerHUD()
def prompt_positive_int(prompt, default_val):
    val = input(f"{prompt} [{default_val}]: ").strip()
    return int(val) if val.isdigit() and int(val) > 0 else default_val
def main():
    print("\nPydoro: Python-based Pomodoro ")
    while True:
        print("\n1. Start Work Session\n2. View Study Report\n3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            subject = input("Subject [General]: ").strip().title() or "General"
            work_mins = prompt_positive_int("Work duration in minutes", 25)
            break_mins = prompt_positive_int("Break duration in minutes", 5)
            # 1. Work Session
            print(f"\n[Focus] {subject} for {work_mins} min... (Check floating timer)")
            hud.run_countdown(work_mins * 60, f"Focusing on: {subject}")
            tracker.log_session(subject, work_mins)
            print(f"[Done] Logged {work_mins} min of {subject}!")
            # 2. Break Session
            print(f"[Break] Resting for {break_mins} min... (Check floating timer)")
            hud.run_countdown(break_mins * 60, "Break time! Step away and rest.")
            print("[Break's over! Ready for the next run.]")
        elif choice == "2":
            print("\n Today's Report :-")
            print(tracker.build_report_text())
        elif choice == "3":
            print("\n Final Day Summary :-")
            print(tracker.build_report_text())
            print("\nGoodbye!")
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")
if __name__ == "__main__":
    main()