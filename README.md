# Course Compass

Course Compass is a rules-based chatbot that gathers a student's interests, favourite subjects, skills, personality traits, career goals and JAMB score, then compares that profile with the programme data in `data/courses.py`.

## Run locally on Windows (recommended simple setup)

1. Extract this ZIP into a new folder.
2. Double-click `setup_windows.bat`. It creates a fresh `.venv` inside this project and installs the dependencies from `requirements.txt`. This avoids accidentally using the virtual environment from another Course Compass folder.
3. After setup finishes, double-click `run_windows.bat`.
4. Open the local address printed in the terminal, usually `http://127.0.0.1:5000`.
5. On the first question, type your name. A small note explains that clickable options start on the next question. The choices appear inside the chat after each question; six are shown at first, and **Show more options** reveals the rest.

### Run through PyCharm instead

1. Open the `CourseCompass` folder in PyCharm.
2. Choose this folder's interpreter: `.venv\Scripts\python.exe` (create it first by running `setup_windows.bat`).
3. Run `app.py` using that interpreter. Do not select the interpreter from `CourseCompass_Phase1_Fixes (3)`.

### Manual setup (PowerShell)

From this folder, you can also run:

```powershell
py -3 -m venv .venv
& ".\.venv\Scripts\python.exe" -m ensurepip --upgrade
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" app.py
```


1. Open the folder containing `app.py` and `requirements.txt` in PyCharm.
2. Choose a project Python interpreter. A new virtual environment is recommended.
3. Open **View → Tool Windows → Terminal**.
4. Install the web application's dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the app:

   ```powershell
   python app.py
   ```

6. Open the local address printed in the terminal, usually `http://127.0.0.1:5000`.

If PowerShell reports that the wrong Python is being used, run the install command with the exact interpreter path selected in **File → Settings → Project → Python Interpreter**, for example:

```powershell
& ".\.venv3\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv3\Scripts\python.exe" app.py
```

## Run regression tests

With the project dependencies installed, run:

```powershell
python -m unittest discover -s tests -v
```

The tests cover interview category separation, common parsing edge cases, additional information, recommendation matching, server-side session persistence, request validation and HTML escaping.

## Session and security notes

- Conversation history and chatbot progress are stored in a local SQLite database under `instance/`, not in the browser cookie. This lets the app restore progress between requests and app-process restarts.
- `instance/` is runtime data and should not be committed or shared between unrelated users.
- Set `COURSE_COMPASS_SECRET_KEY` to a long random value for a deployed environment. The local fallback is generated at startup for development.
- If the deployed site uses HTTPS, set `COURSE_COMPASS_HTTPS=1` so the session cookie is marked secure.
- Debug mode is off by default. Set `FLASK_DEBUG=1` only during local development.
- For a production deployment, use a production WSGI server and configure HTTPS, backups and the database path appropriately.

## Important data limitation

The recommendation rules are explainable, but their quality depends on the accuracy of `data/courses.py`. Course names, degree awards, programme duration, JAMB cut-offs and UTME subject combinations must be checked against current ATBU and JAMB IBASS information before the app is used as an official admissions guide. The interface already advises students to verify current JAMB requirements; do not describe the stored cut-offs as guaranteed admission cut-offs.

## Keyword parser evaluation

Course Compass includes a small synthetic evaluation set for its rules-based parser.
Run these commands from the project root after installing the requirements:

```powershell
python evaluation/run_evaluation.py
python -m unittest tests.test_keyword_evaluation -v
```

Read `EVALUATION_GUIDE.md` for a suggested real-student pilot and a simple way to record false positives, missed categories, task completion and recommendation usefulness. The synthetic score is not a claim of perfect real-world understanding; use real anonymised pilot examples to extend the tests.


## Guided answer coverage

The in-chat answer choices cover all tags currently used by the bundled course catalogue: 18 interest tags, 10 subject tags, 10 skill tags, 16 personality-trait tags, and 53 distinct career tags. Career button answers are resolved to the exact catalogue career label so a specific choice is not reduced to a generic label such as “engineer”. These choices reflect the current bundled dataset; they do not independently verify that every course or career label is an official current ATBU/JAMB offering.


## Guided chat options and typing answers

- The name question is free text; guided choices appear after the student submits a name.
- Interests, subjects, skills and personality allow multiple selections. Select one or more chips, then click **Use selected answers**. The button remains clickable and explains what to do if nothing is selected.
- Career goal uses a single choice and sends the answer when clicked.
- Only the first six choices are shown at first. Use **Show more options** to reveal the rest.
- Students can still type their own answer. If the answer does not match the current question, the bot gives an example relevant to that question instead of a vague error.
