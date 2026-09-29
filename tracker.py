"""
Pydoro Analytics: Tracks daily study sessions and generates performance reports.
"""
study_log = {}
sessions = []
def log_session(subject, minutes):
    study_log[subject] = study_log.get(subject, 0) + minutes
    sessions.append((subject, minutes))
def find_top_subject():
    top_subject, top_time = "None", 0
    for s, t in study_log.items():
        if t > top_time:
            top_subject, top_time = s, t
    return top_subject, top_time
def build_report_text():
    if not sessions:
        return "No sessions logged yet today."
    total = sum(m for _, m in sessions)
    lines = [f"Sessions done   : {len(sessions)}", f"Total study time: {total} min", "", "Time by subject:"]
    for s, m in study_log.items():
        lines.append(f"  - {s} : {m} min")
    top, top_time = find_top_subject()
    lines.extend(["", f"Most studied: {top} ({top_time} min)"])
    if total >= 120:
        msg = "Okay that's serious focus, well done!"
    elif total >= 60:
        msg = "Solid day. Keep going!"
    else:
        msg = "Good start. Even a little counts."
    lines.append("\n" + msg)
    return "\n".join(lines)