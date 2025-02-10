import win32clipboard
import time
import threading
import re

class ClipboardManager:
    def __init__(self):
        self.last_clipboard_content = ""

    def get_clipboard_content(self):
        win32clipboard.OpenClipboard()
        try:
            data = win32clipboard.GetClipboardData()
        except TypeError:
            data = ""
        win32clipboard.CloseClipboard()
        return data

    def set_clipboard_content(self, content):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(content)
        win32clipboard.CloseClipboard()

    def clean_clipboard_content(self, content):
        # Remove extra spaces and new lines
        cleaned_content = re.sub(r'\s+', ' ', content).strip()
        return cleaned_content

    def manage_clipboard(self):
        while True:
            current_content = self.get_clipboard_content()
            if current_content != self.last_clipboard_content:
                print("New Clipboard Content Detected")
                cleaned_content = self.clean_clipboard_content(current_content)
                if cleaned_content != current_content:
                    print("Cleaning Clipboard Content")
                    self.set_clipboard_content(cleaned_content)
                self.last_clipboard_content = cleaned_content
            time.sleep(1)

def main():
    print("Starting AutoMate Clipboard Manager...")
    clipboard_manager = ClipboardManager()
    clipboard_thread = threading.Thread(target=clipboard_manager.manage_clipboard)
    clipboard_thread.daemon = True
    clipboard_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAutoMate Clipboard Manager stopped.")

if __name__ == "__main__":
    main()