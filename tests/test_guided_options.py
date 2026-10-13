import unittest

from chatbot.response_options import RESPONSE_OPTIONS, MULTI_SELECT_QUESTIONS
from data.courses import COURSES
from chatbot.parser import (
    extract_interests, extract_subjects, extract_skills,
    extract_personality, extract_career_goals,
)
from chatbot.recommender import RecommendationEngine
from models.student_profile import StudentProfile


class GuidedResponseOptionTests(unittest.TestCase):
    def test_each_guided_value_is_recognised_by_its_existing_parser(self):
        extractors = {
            "interests": extract_interests,
            "subjects": extract_subjects,
            "skills": extract_skills,
            "personality": extract_personality,
            "career_goal": extract_career_goals,
        }
        for question_id, options in RESPONSE_OPTIONS.items():
            for option in options:
                with self.subTest(question=question_id, option=option["label"]):
                    if option["value"] == "skip":
                        continue
                    self.assertTrue(extractors[question_id](option["value"]))

    def test_guided_options_cover_every_catalogue_tag(self):
        extractors = {
            "interests": (extract_interests, "interests"),
            "subjects": (extract_subjects, "subjects"),
            "skills": (extract_skills, "skills"),
            "personality": (extract_personality, "personality_traits"),
            "career_goal": (extract_career_goals, "careers"),
        }
        for question_id, (extractor, attribute) in extractors.items():
            with self.subTest(question=question_id):
                catalogue_tags = {
                    value.lower()
                    for course in COURSES
                    for value in getattr(course, attribute, [])
                }
                covered_tags = set()
                for option in RESPONSE_OPTIONS[question_id]:
                    if option["value"] == "skip":
                        continue
                    covered_tags.update(extractor(option["value"]))
                self.assertTrue(
                    catalogue_tags.issubset(covered_tags),
                    msg=f"Tags without guided choices: {sorted(catalogue_tags - covered_tags)}",
                )

    def test_multi_select_is_enabled_for_profile_list_questions(self):
        self.assertEqual(
            MULTI_SELECT_QUESTIONS,
            {"interests", "subjects", "skills", "personality"},
        )

    def test_multiple_interest_options_can_be_parsed_together(self):
        matches = extract_interests("technology, health, agriculture")
        self.assertIn("technology", matches)
        self.assertIn("health", matches)
        self.assertIn("agriculture", matches)

    def test_career_options_keep_career_goal_separate_from_interest(self):
        career = extract_career_goals("I want to become a doctor")
        interests = extract_interests("I want to become a doctor")
        self.assertIn("doctor", career)
        self.assertNotIn("health", interests)

    def test_guided_profile_choices_link_to_existing_course_tags(self):
        extractors = {
            "interests": (extract_interests, "interests"),
            "subjects": (extract_subjects, "subjects"),
            "skills": (extract_skills, "skills"),
            "personality": (extract_personality, "personality_traits"),
            "career_goal": (extract_career_goals, "careers"),
        }
        for question_id, options in RESPONSE_OPTIONS.items():
            extractor, attribute = extractors[question_id]
            catalogue_tags = {
                value.lower()
                for course in COURSES
                for value in getattr(course, attribute, [])
            }
            for option in options:
                if option["value"] == "skip":
                    continue
                extracted = extractor(option["value"])
                generic_career_match = (
                    question_id == "career_goal"
                    and any(value in {"teacher", "engineer", "scientist", "data analyst", "farmer"} for value in extracted)
                )
                self.assertTrue(
                    any(value in catalogue_tags for value in extracted) or generic_career_match,
                    msg=f"{question_id} option {option['label']!r} has no matching course tag: {extracted}",
                )


    def test_personality_trait_adds_points_and_explanation_to_recommendation(self):
        engine = RecommendationEngine()
        course = next(course for course in COURSES if course.personality_traits)
        trait = course.personality_traits[0]

        without_trait, _ = engine._calculate_score(StudentProfile(), course)
        with_trait, reasons = engine._calculate_score(
            StudentProfile(personality_traits=[trait]), course
        )

        self.assertEqual(with_trait - without_trait, 5)
        self.assertTrue(any("personality match" in reason for reason in reasons))

    def test_personality_scoring_is_capped_at_ten_points(self):
        engine = RecommendationEngine()
        course = next(
            course for course in COURSES
            if len(course.personality_traits) >= 2
        )
        profile = StudentProfile(personality_traits=course.personality_traits[:2])

        score, reasons = engine._calculate_score(profile, course)

        self.assertEqual(score, 10)
        self.assertTrue(any("personality match" in reason for reason in reasons))


if __name__ == "__main__":
    unittest.main()
