# 📦 Changelog

## [v1.0] - Earlier
### Initial Release
- 📝 Add notes with timestamp and default status ("Pending")
- 📋 View all notes with serial number, creation time, and status
- 🔍 Search notes by keyword (case-insensitive)
- ❌ Delete notes by serial number
- 📊 Statistics module:
  - Total note count
  - Longest note
  - Total word count across all notes
- 💾 Persistent storage using `tasks.json`
- 🧠 Input via keyboard (CLI interface)
- 🗂️ Structured class-based design using Python

---

## [v1.1] - 27-Oct-2025
### Feature Upgrade
- 🎤 Voice input added for all core functions (add, view, search, delete, statistics, exit)
- 🌐 Multilingual command mapping (English + Hindi phrases)
- 🧠 Intelligent command routing using `command_map`
- 🗣️ Voice fallback: if speech input fails, user can type instead
- 🔁 Unified interface for both voice and text control
- 📦 Improved CLI flow with dynamic prompts and execution feedback

---

## 🧭 Planned Features (v1.2 and beyond)
- ✅ Ability to change status of notes/tasks (e.g., mark as Done)
- 🕶️ Background availability: app runs silently and activates on voice trigger
- 🔊 Voice output using text-to-speech
- 🖼️ GUI interface using Tkinter
- 📤 Export notes to CSV/PDF
- 📴 Offline voice model (no Google dependency)
