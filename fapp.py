# Q1: How would you store the number of votes for each candidate?
# A1:
# You can use a dictionary to store candidate names as keys and their votes as values.
votes = {"Alice": 5000, "Bob": 4500, "Charlie": 3200}  # Dictionary
# Q2: How would you store the names of all the candidates in the election?
# A2:
# You can use a list to store all candidate names.
# candidates = ["Alice", "Bob", "Charlie"]  List
# Q11: Use a while loop to count down from the total number of votes.
# python
# Copy
# Edit
total_votes = 10000
while total_votes > 0:
    print(total_votes)
    total_votes -= 1000