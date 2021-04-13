from Name import Name

original = Name("Freddy","George","Mercury")

aliases = [
    ("Freddy Mercury",1923),
    ("Freddy Mercury",1974),
    ("Freddy G. Jones",2007),
    ("Freddy George Jones",2007),
    ("Freddy G Mercury",1997),
    ("Freddy G. Mercury",1992),
    ("Freddy Granola Mercury",1988),
    ("Freddy George Jones",1990)
]

score_map = {}
for alias,year in aliases:
    score = original.compare(alias)
    
    if score not in score_map:
        score_map[score]=[]
    score_map[score].append(year)
    
    print(f"Comparing {original} to {alias} gives a score {score}.")

score, years = sorted(list(score_map.items()))[0]
minimum_dob = min(years)
maximum_dob = max(years)
print(f"Best score is {score}")
print(f"The minimum date of birth is {minimum_dob} and a maxiumum dob is {maximum_dob}.")
