# Instructions
Run the `randomizer.py` script.

# Explanation
The `randomizer.py` script generates pairs for all students for a lab, writing its output to `lab_pairs.txt`. the script pulls the list of students in each section from `student_list.txt`. Once the lab pairs are generated, they are added to `previous_pairs.txt`. This file contains a list of all pairs previously generated this semester. The randomizer attempts to generate pairs that are not present in the previous pairs, in order to prevent duplicate teams. 

# New Semester
When a new semester starts, `student_list.txt` and `previous_pairs.txt` need to be updated. The contents of `previous_pairs.txt` must be deleted. `student_list.txt` needs to have each section updated to match the new rosters.