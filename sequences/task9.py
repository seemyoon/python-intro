# 1. Create two variables and assign them the same sequences of type set. Do not copy one variable to another
# 2. Compare two created variables using comparison operator. Print result to the terminal. Explain the result
# 3. Compare two objects using the is operator, explain the result
# 4. Check if there are certain elements in the set using the in operator

sequencesSet1 = {
    "asd",
    True,
    None,
    (999, 7878, "Oleksandr"),
}

sequencesSet2 = {
    "asd",
    True,
    None,
    (999, 7878, "Oleksandr"),
}

print(
    sequencesSet1 == sequencesSet2
)  # explain: because inside sets we have built-in magic method __eq__, so that's why we have result true
print(sequencesSet1.__eq__(sequencesSet2))
print(
    id(sequencesSet1) == id(sequencesSet2)
)  # explain: because even though the values of the sets are the same, they are different objects in memory (created independently). therefore, their ids are different, and the comparison result is False.
print(
    sequencesSet1 is sequencesSet2
)  # explain: the is operator compares object references, that is, it checks whether both variables point to the same object. since you have created two independent sets, their references are different, and the result is False.

print("asd" in sequencesSet1)
print("dsa" in sequencesSet1)
print(False in sequencesSet1)
print((999, 7878, "Masha") in sequencesSet2)
