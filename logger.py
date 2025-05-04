from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] {message}"
        self.logs.append(entry)
        return entry

    def get_logs(self):
        return self.logs
