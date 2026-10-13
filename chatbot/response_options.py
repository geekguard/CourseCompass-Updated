"""Guided answer choices for the Course Compass chatbot.

Each option has:
  - label: short student-friendly text shown on the clickable chip
  - value: text sent to the keyword parser (must match existing keywords)

Multi-select questions (interests, subjects, skills, personality) let students
tap several chips then press "Use selected answers".
Single-select questions (career_goal) send the answer as soon as a chip is tapped.

Only the first few chips are shown; "Show more options" reveals the rest.
Students can still type their own answer in the text box if none of the chips fit.
"""

RESPONSE_OPTIONS = {
    # ------------------------------------------------------------------
    # INTERESTS  (multi-select)
    # ------------------------------------------------------------------
    "interests": [
        {"label": "Technology and digital tools", "value": "technology"},
        {"label": "Computers, software and networks", "value": "computing"},
        {"label": "Engineering and technical problem-solving", "value": "engineering"},
        {"label": "Building, construction and structures", "value": "construction"},
        {"label": "Healthcare and medicine", "value": "health"},
        {"label": "Science, experiments and research", "value": "science"},
        {"label": "Agriculture, crops and farming", "value": "agriculture"},
        {"label": "Animals and animal care", "value": "animals"},
        {"label": "Business, finance and entrepreneurship", "value": "business"},
        {"label": "Art and creative work", "value": "art"},
        {"label": "Design and product ideas", "value": "design"},
        {"label": "Education, teaching and training", "value": "education"},
        {"label": "Helping people and communities", "value": "community"},
        {"label": "Environment, land and sustainability", "value": "environment"},
        {"label": "Property, housing and real estate", "value": "property"},
        {"label": "Information, records and library work", "value": "information"},
        {"label": "Practical and hands-on work", "value": "practical"},
        {"label": "Society and social issues", "value": "social sciences"},
    ],

    # ------------------------------------------------------------------
    # SUBJECTS  (multi-select)
    # ------------------------------------------------------------------
    "subjects": [
        {"label": "Mathematics", "value": "mathematics"},
        {"label": "Biology", "value": "biology"},
        {"label": "Chemistry", "value": "chemistry"},
        {"label": "Physics", "value": "physics"},
        {"label": "Computer Science / ICT", "value": "computer science"},
        {"label": "English Language", "value": "english"},
        {"label": "Economics", "value": "economics"},
        {"label": "Geography", "value": "geography"},
        {"label": "Art", "value": "art"},
        {"label": "Technical Drawing", "value": "technical drawing"},
    ],

    # ------------------------------------------------------------------
    # SKILLS  (multi-select)
    # ------------------------------------------------------------------
    "skills": [
        {"label": "Analysis — examining information carefully", "value": "analysis"},
        {"label": "Analytical thinking — working things out", "value": "analytical"},
        {"label": "Problem-solving", "value": "problem-solving"},
        {"label": "Communication — explaining ideas clearly", "value": "communication"},
        {"label": "Creativity — coming up with new ideas", "value": "creativity"},
        {"label": "Organisation and planning", "value": "organization"},
        {"label": "Practical / hands-on skills", "value": "practical"},
        {"label": "Coding and programming", "value": "coding"},
        {"label": "Teaching or explaining things", "value": "teaching"},
        {"label": "Attention to detail", "value": "detail-oriented"},
    ],

    # ------------------------------------------------------------------
    # PERSONALITY  (multi-select)
    # ------------------------------------------------------------------
    "personality": [
        {"label": "Analytical — I like working things out", "value": "analytical"},
        {"label": "Creative — I enjoy new ideas", "value": "creative"},
        {"label": "Curious — I like learning how things work", "value": "curious"},
        {"label": "Detail-oriented — I notice small details", "value": "detail-oriented"},
        {"label": "Observant — I pay attention to what is happening", "value": "observant"},
        {"label": "Organised — I like planning", "value": "organized"},
        {"label": "Patient — I can take my time with tasks", "value": "patient"},
        {"label": "Practical — I enjoy applying what I learn", "value": "practical"},
        {"label": "Social — I enjoy working with people", "value": "social"},
        {"label": "Caring", "value": "caring"},
        {"label": "Helpful — I enjoy supporting others", "value": "helpful"},
        {"label": "Empathetic — I consider other people's feelings", "value": "empathetic"},
        {"label": "Responsible — people can rely on me", "value": "responsible"},
        {"label": "Adaptable — I can adjust to change", "value": "adaptable"},
        {"label": "Precise — I value accuracy", "value": "precise"},
        {"label": "Visual — I understand things through diagrams", "value": "visual"},
    ],

    # ------------------------------------------------------------------
    # CAREER GOAL  (single-select — job titles, not programme names)
    # ------------------------------------------------------------------
    "career_goal": [
        # Computing & IT
        {"label": "Software Engineer", "value": "I want to become a software engineer"},
        {"label": "Computer Engineer", "value": "I want to become a computer engineer"},
        {"label": "Network Engineer", "value": "I want to become a network engineer"},
        {"label": "Data Analyst", "value": "I want to become a data analyst"},
        # Engineering
        {"label": "Agricultural Engineer", "value": "I want to become an agricultural engineer"},
        {"label": "Bio-resource Engineer", "value": "I want to become a bio-resource engineer"},
        {"label": "Communication Engineer", "value": "I want to become a communication engineer"},
        {"label": "Engineer (general)", "value": "I want to become an engineer"},
        # Health & medicine
        {"label": "Doctor", "value": "I want to become a doctor"},
        {"label": "Nurse", "value": "I want to become a nurse"},
        {"label": "Public Health Officer", "value": "I want to become a public health officer"},
        {"label": "Laboratory Scientist", "value": "I want to become a laboratory scientist"},
        {"label": "Pharmacologist", "value": "I want to become a pharmacologist"},
        {"label": "Anatomist", "value": "I want to become an anatomist"},
        {"label": "Physiologist", "value": "I want to become a physiologist"},
        {"label": "Medical Microbiologist", "value": "I want to become a medical microbiologist"},
        {"label": "Chemical Pathologist", "value": "I want to become a chemical pathologist"},
        {"label": "Haematologist", "value": "I want to become a haematologist"},
        {"label": "Histopathologist", "value": "I want to become a histopathologist"},
        {"label": "Veterinarian", "value": "I want to become a veterinary doctor"},
        # Agriculture
        {"label": "Agricultural Economist", "value": "I want to become an agricultural economist"},
        {"label": "Agronomist", "value": "I want to become an agronomist"},
        {"label": "Animal Scientist", "value": "I want to become an animal scientist"},
        {"label": "Soil Scientist", "value": "I want to become a soil scientist"},
        {"label": "Extension Officer", "value": "I want to become an extension officer"},
        # Built environment
        {"label": "Architect", "value": "I want to become an architect"},
        {"label": "Quantity Surveyor", "value": "I want to become a quantity surveyor"},
        {"label": "Urban Planner", "value": "I want to become an urban planner"},
        {"label": "Estate Manager", "value": "I want to become an estate manager"},
        {"label": "Property Manager", "value": "I want to become a property manager"},
        {"label": "Surveyor", "value": "I want to become a surveyor"},
        {"label": "Building Technologist", "value": "I want to become a building technologist"},
        {"label": "Construction Technology Teacher", "value": "I want to become a construction technology teacher"},
        {"label": "Electrical Technology Teacher", "value": "I want to become an electrical technology teacher"},
        {"label": "Mechanical Technology Teacher", "value": "I want to become a mechanical technology teacher"},
        {"label": "GIS Specialist", "value": "I want to become a gis specialist"},
        {"label": "Construction Manager", "value": "I want to become a construction manager"},
        {"label": "Environmental Officer", "value": "I want to become an environmental management officer"},
        # Design
        {"label": "Industrial Designer", "value": "I want to become an industrial designer"},
        {"label": "Product Designer", "value": "I want to become a product designer"},
        # Science
        {"label": "Chemist", "value": "I want to become a chemist"},
        {"label": "Scientist", "value": "I want to become a scientist"},
        # Business
        {"label": "Accountant", "value": "I want to become an accountant"},
        # Education & information
        {"label": "Science Teacher", "value": "I want to become a science teacher"},
        {"label": "Vocational Teacher", "value": "I want to become a vocational teacher"},
        {"label": "School Counsellor", "value": "I want to become a school counsellor"},
        {"label": "Educational Psychologist", "value": "I want to become an educational psychologist"},
        {"label": "Education Officer", "value": "I want to become an education officer"},
        {"label": "Educational Administrator", "value": "I want to become an educational administrator"},
        {"label": "Training Officer", "value": "I want to become a training officer"},
        {"label": "Librarian", "value": "I want to become a librarian"},
        {"label": "Information Specialist", "value": "I want to become an information specialist"},
        {"label": "Technical Instructor", "value": "I want to become a technical instructor"},
        # Fallback
        {"label": "I am still exploring my options", "value": "skip"},
    ],
}

# Questions where the student can pick more than one chip before submitting
MULTI_SELECT_QUESTIONS = {"interests", "subjects", "skills", "personality"}
