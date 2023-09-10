# dictionary comprehension

incorrect_score_dict = {
    "Tom": 80,
    "Lisa": 75,
    "Sarah": 90
}

correct_score_dict = {name: score + 5 for (name, score) in incorrect_score_dict.items() if score < 80}

print(correct_score_dict)