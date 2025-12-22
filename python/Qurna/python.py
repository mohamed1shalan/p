import json
import re

class TajweedAnalysisEngine:
    def __init__(self):
        # Define the letters and conditions for each rule
        self.rules_definition = {
            "Al-Izhar Al-Halqi": {
                "letters": ['ء', 'ه', 'ع', 'ح', 'غ', 'خ']
            },
            "Idgham with Ghunnah": {
                "letters": ['ي', 'ن', 'م', 'و']
            },
            "Idgham without Ghunnah": {
                "letters": ['ل', 'ر']
            },
            "Al-Iqlab": {
                "letters": ['ب']
            },
            "Al-Ikhfa' Al-Haqiqi": {
                "letters": ['ص', 'ذ', 'ث', 'ك', 'ج', 'ش', 'ق', 'س', 'د', 'ط', 'ز', 'ف', 'ت', 'ض', 'ظ']
            },
            "Al-Ikhfa' Ash-Shafawi": {
                "letters": ['ب']
            },
            "Idgham Shafawi": {
                "letters": ['م']
            },
            "Al-Izhar Ash-Shafawi": {
                "excluded_letters": ['ب', 'م']
            },
            "Ghunnah": {
                "letters": ['نّ', 'مّ']
            },
            "Al-Qalqalah": {
                "letters": ['ق', 'ط', 'ب', 'ج', 'د']
            }
            # Other rules can be added here
        }

    def analyze_text(self, rule_name, quranic_text):
        """
        Analyzes the given Quranic text for a specific Tajweed rule.

        Args:
            rule_name (str): The name of the Tajweed rule to search for.
            quranic_text (str): The Quranic text to analyze.

        Returns:
            str: A JSON string representing the findings.
        """
        findings = []
        verses = self._split_into_verses(quranic_text)

        for verse_num, verse_text in verses.items():
            words = verse_text.split()
            for i, word in enumerate(words):
                # Logic for Rules of Noon Sakinah and Tanween
                if rule_name in ["Al-Izhar Al-Halqi", "Idgham with Ghunnah", "Idgham without Ghunnah", "Al-Iqlab", "Al-Ikhfa' Al-Haqiqi"]:
                    if 'نْ' in word or re.search(r'[اًٌٍ]', word):
                        next_word = words[i + 1] if i + 1 < len(words) else ""
                        next_letter = next_word[0] if next_word else ""

                        if rule_name == "Al-Izhar Al-Halqi" and next_letter in self.rules_definition[rule_name]["letters"]:
                            findings.append(self._create_finding(rule_name, verse_num, [word, next_word], [word[-1], next_letter], f"Noon Sakinah or Tanween in '{word}' followed by '{next_letter}'."))
                        # ... Implement other Noon Sakinah rules similarly

                # Logic for Rules of Meem Sakinah
                elif rule_name in ["Al-Ikhfa' Ash-Shafawi", "Idgham Shafawi", "Al-Izhar Ash-Shafawi"]:
                    if 'مْ' in word:
                        next_word = words[i + 1] if i + 1 < len(words) else ""
                        next_letter = next_word[0] if next_word else ""

                        if rule_name == "Al-Ikhfa' Ash-Shafawi" and next_letter == 'ب':
                            findings.append(self._create_finding(rule_name, verse_num, [word, next_word], ['مْ', 'ب'], f"Meem Sakinah in '{word}' followed by 'ب'."))
                        elif rule_name == "Idgham Shafawi" and next_letter == 'م':
                            findings.append(self._create_finding(rule_name, verse_num, [word, next_word], ['مْ', 'م'], f"Meem Sakinah in '{word}' followed by 'م'."))
                        elif rule_name == "Al-Izhar Ash-Shafawi" and next_letter not in self.rules_definition[rule_name]["excluded_letters"] and next_letter:
                             findings.append(self._create_finding(rule_name, verse_num, [word, next_word], ['مْ', next_letter], f"Meem Sakinah in '{word}' followed by '{next_letter}'."))

                # Logic for Ghunnah
                elif rule_name == "Ghunnah":
                    if 'نّ' in word or 'مّ' in word:
                        trigger = 'نّ' if 'نّ' in word else 'مّ'
                        findings.append(self._create_finding(rule_name, verse_num, [word], [trigger], f"Ghunnah on a Mushaddadah letter in '{word}'."))

                # Logic for Qalqalah
                elif rule_name == "Al-Qalqalah":
                    for letter in self.rules_definition[rule_name]["letters"]:
                        if f"{letter}ْ" in word or (word.endswith(letter) and i == len(words) - 1):
                             findings.append(self._create_finding(rule_name, verse_num, [word], [letter], f"Qalqalah on the letter '{letter}' in '{word}'."))


        return json.dumps(findings, ensure_ascii=False, indent=2)

    def _split_into_verses(self, text):
        """
        Splits the text into a dictionary of verses.
        This is a simplified implementation. A more robust solution
        would handle various verse numbering styles.
        """
        verses = {}
        # This regex looks for a sequence of Arabic text followed by (number)
        matches = re.findall(r'([\s\S]+?)\((\d+)\)', text)
        for match in matches:
            verse_text = match[0].strip()
            verse_num = int(match[1])
            verses[verse_num] = verse_text
        return verses

    def _create_finding(self, rule, verse, words, triggers, details):
        """Helper function to create a finding dictionary."""
        return {
            "rule": rule,
            "verse": verse,
            "location_words": words,
            "trigger_letters": triggers,
            "details": details
        }

# --- Example Usage ---

engine = TajweedAnalysisEngine()

# Example 1: Al-Izhar Al-Halqi
quranic_text_izhar = "قُلْ هُوَ اللَّهُ أَحَدٌ (1) اللَّهُ الصَّمَدُ (2)"
# Note: The following is a conceptual example. A sophisticated engine would need to handle cross-verse analysis.
# For this example, let's assume the analysis is within a continuous text stream.
# A more advanced implementation would need to look ahead to the next verse.
print("--- Testing Al-Izhar Al-Halqi ---")
# This is a conceptual test as the provided text doesn't contain a clear example within a single verse processing loop.
# The logic would need to be enhanced to consider the start of the next verse.
# A hypothetical adjusted text for demonstration: "أَحَدٌ هُوَ"
quranic_text_izhar_demo = "مِنْ خَيْرٍ (1)"
# Let's adjust for a more direct test case
quranic_text_izhar_direct = "مِنْهُ"
# The example below will be simplified as the current engine processes verse by verse.
# The logic would need to be expanded to consider the beginning of the next verse.

# Example 2: Ikhfa' Ash-Shafawi
quranic_text_ikhfa_shafawi = "تَرْمِيهِم بِحِجَارَةٍ (3)"
print("\n--- Testing Al-Ikhfa' Ash-Shafawi ---")
result_ikhfa_shafawi = engine.analyze_text("Al-Ikhfa' Ash-Shafawi", quranic_text_ikhfa_shafawi)
print(result_ikhfa_shafawi)

# Example 3: Ghunnah
quranic_text_ghunnah = "مِنَ الْجِنَّةِ وَالنَّاسِ (6)"
print("\n--- Testing Ghunnah ---")
result_ghunnah = engine.analyze_text("Ghunnah", quranic_text_ghunnah)
print(result_ghunnah)

# Example 4: Qalqalah
quranic_text_qalqalah = "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ (1)"
print("\n--- Testing Al-Qalqalah ---")
result_qalqalah = engine.analyze_text("Al-Qalqalah", quranic_text_qalqalah)
print(result_qalqalah)