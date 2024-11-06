"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1      # The number the user inputs to stop entering new scores


def main():
    """
    program calculates separately class max,mini & average
    """

    b = 'SC001'   #設b,b1,b2,b3為SC001班級
    b1 = 'Sc001'
    b2 = 'sc001'
    b3 = 'sC001'
    c = 'SC101'   #設c,c1,c2,c3為SC101班級
    c1 = 'Sc101'
    c2 = 'sc101'
    c3 = 'sC101'
    n001 = 0      #n001為SC001幾筆成績
    n101 = 0      #n101為SC101幾筆成績

    # 先定義變數
    max_sc001 = 0
    max_sc101 = 0
    min_sc001 = 10000
    min_sc101 = 10000
    total_sc001 = 0
    total_sc101 = 0
    while True:
        a = str(input('Which class ? '))
        if a == str(EXIT):
            break
        else:
            if a == b or a == b1 or a == b2 or a == b3:
                score1 = int(input('Score: '))
                if score1 > max_sc001:
                    max_sc001 = score1
                if score1 < min_sc001:
                    min_sc001 = score1
                n001 += 1
                total_sc001 += score1

            if a == c or a == c1 or a == c2 or a == c3:
                score101 = int(input('Score: '))
                if score101 > max_sc101:
                    max_sc101 = score101
                if score101 < min_sc101:
                    min_sc101 = score101
                n101 += 1
                total_sc101 += score101
    # Show the results
    if n001 == 0 & n101 == 0:
        print('No class scores were entered')
    else:
        if n001 == 0 & n101 != 0:
            print('=' * 13 + str(b) + '=' * 13)
            print("No score for 001")
        else:
            print('='*13 + str(b) + '='*13)
            print('Max(001) = ' + str(max_sc001))
            print('Min(001) = ' + str(min_sc001))
            print('Avg(001) = ' + str(total_sc001/n001))
        if n101 == 0 & n001 != 0:
            print('=' * 13 + str(c) + '=' * 13)
            print("No score for 101")
        else:
            print('='*13 + str(c) + '='*13)
            print('Max(101) = ' + str(max_sc101))
            print('Min(101) = ' + str(min_sc101))
            print('Avg(101) = ' + str(total_sc101/n101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
