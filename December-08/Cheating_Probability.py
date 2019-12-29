"""Given an RxC Matrix in which each element represents the Department of a student seated in that row and column in
an examination hall, write a code to calculate the probability of each student copying if a person from the same
department sits: In front of him = 0.3 Behind him = 0.2 To his left or right = 0.2 In any of his 4 closest diagonals
= 0.025

Set of row, col adjustments:
[-1, -1] [-1, 0] [-1, 1]
[0, -1]  [0, 0]  [0, 1]
[1, -1]  [1, 0]  [1, 1]

Set of probabilities based on location:
[.025] [.3] [.025]
[.2]   [0]  [.2]
[.025] [.2] [.025]

"""


def cheating_matrix(seating_chart):
    """
    Calculate and return the probabilities of cheating for each position in a rxc grid
    :param seating_chart: A nested list representing a rxc grid
    :return: A nested list, the same size as seating_chart, with each element representing that
            position's cheating probability
    """

    # Create matrix of probabilities by location
    prob_matrix = [[.025, .3, .025],
                   [.2, 0, .2],
                   [.025, .2, .025]]

    # Create blank nested list for saving calculated probabilities (same size as seating_chart)
    calc_prob = []
    for ch_row in range(len(seating_chart)):
        new_row = []
        for ch_col in range(len(seating_chart[ch_row])):
            new_row.append(seating_chart[ch_row][ch_col])
        calc_prob.append(new_row)

    # calculate probabilities for each spot in seating_chart, store in calc_prob
    for row in range(len(seating_chart)):
        for col in range(len(seating_chart[row])):
            calc_prob[row][col] = 0
            for r_adj in range(-1, 2):
                for c_adj in range(-1, 2):
                    if 0 <= row + r_adj < len(seating_chart):
                        if 0 <= col + c_adj < len(seating_chart[row]):
                            if seating_chart[row][col] == seating_chart[row + r_adj][col + c_adj]:
                                calc_prob[row][col] += prob_matrix[1 + r_adj][1 + c_adj]
    return calc_prob


seats = [['a', 'b', 'a'],
         ['b', 'b', 'a']]

seats_b = [['a', 'b', 'c', 'd', 'a'],
           ['b', 'c', 'd', 'a', 'b'],
           ['c', 'd', 'a', 'b', 'c']]

ch_mx = cheating_matrix(seats_b)
for r in ch_mx:
    print(r)
