from observer import Observer

class UINotifier(Observer):
    def update(self, event):
        print(f"[UI] Updating UI with message : {event}")
