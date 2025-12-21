# Real-Time Attendance System with Face Recognition

## Project Overview
A Python-based real-time attendance system using face recognition. The application provides a user-friendly GUI for managing students, capturing attendance, and training face data. It uses OpenCV for face detection/recognition, Tkinter for the GUI, SQLite for the database, and is designed for easy portability and setup.

## Features
- Student management (add, update, delete student info)
- Real-time face recognition for attendance marking
- Attendance record export (CSV)
- Model training from captured face samples
- Developer and helpdesk info sections
- Clean, modern Tkinter GUI
- Portable: No MySQL or external DB required (uses SQLite)
- Data privacy: Local storage, no cloud upload

## Requirements
- Python 3.8+
- Windows (recommended; Linux/Mac may require minor tweaks)
- Webcam

## Installation & Setup
1. **Clone the repository:**
	```
	git clone https://github.com/sajid1495/Real-Time-Attendance-SQLite.git
	cd Real-Time-Attendance-SQLite
	```
2. **Create a virtual environment (recommended):**
	```
	python -m venv .venv
	# Activate (Windows):
	.venv\Scripts\activate
	# Activate (Linux/Mac):
	source .venv/bin/activate
	```
3. **Install dependencies:**
	```
	pip install -r requirements.txt
	```

4. **Create required folders and files:**
	- Manually create a folder named `data` in the project root. This will store all captured face images.
	- Manually create an empty file named `attendance.csv` in the project root. This will store attendance records.
	- **No need to create the SQLite database file (`attendance.db`) manually. It will be generated automatically on first run.**

5. **Run the application:**
	```
	python main.py
	```

## Usage
- **Add Students:** Fill in student info and take photo samples (at least 10-20 per student recommended).
- **Train Model:** After adding students, click "Train Model" to update the face recognizer.
- **Mark Attendance:** Use "Face Detector" to recognize faces and mark attendance.
- **View Attendance:** Attendance is saved in `attendance.csv`.
- **Data Folder:** All face images are stored locally in the `data/` folder (excluded from git).

## Notes for Developers
- Do not commit `.venv/`, `data/`, `attendance.db`, or other large/binary files (see `.gitignore`).
- If you add new dependencies, update `requirements.txt`.
- The project is modular: see `student.py`, `face_recognition.py`, `train.py`, etc.
- For packaging as an executable, use PyInstaller:
  ```
  pyinstaller --onefile --noconsole main.py
  ```

## Troubleshooting
- If the camera does not open, ensure no other app is using it.
- If you see errors about missing DLLs or packages, re-check your Python environment and dependencies.
- For large file warnings on GitHub, ensure `.gitignore` is present and correct.

## License
This project is for educational use. For commercial use, please contact the author.

## Author
- Sajid (https://github.com/sajid1495)
