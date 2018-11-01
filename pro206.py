"""Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit."""

def concelaed(num):


    pass



i = 10**9
while i < 10**10:
    if concelaed(i**2):
        print(i)
        break
    i += 10
