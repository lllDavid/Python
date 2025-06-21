# Atomically update a file and a database record with rollback on failure
class AtomicTransaction:
    def __init__(self):
        self._rollback_actions = []
        self._committed = False

    def add_rollback(self, action):
        self._rollback_actions.append(action)

    def commit(self):
        self._committed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._committed or exc_type:
            for action in reversed(self._rollback_actions):
                try:
                    action()
                except Exception:
                    pass  