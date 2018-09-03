t = int(input().strip())
for i in range(t):
    no_of_finger = int(input().strip())
    finger_l= input()
    type(finger_l)
    finger_lengths = [int(n) for n in finger_l.split()]
    glove_l = input()
    glove_lengths = [int(n) for n in glove_l.split()]
    rev_glove_lengths= glove_lengths[::-1]
    front = True
    back = True
    for i in range(no_of_finger):
        if not (glove_lengths[i]>= finger_lengths[i]):
            front = False
    for i in range(no_of_finger):
        if not (rev_glove_lengths[i]>= finger_lengths[i]):
            back = False
    if (front == True and back == True):
        print("both")
    elif (front == False and back == False):
        print("none")
    elif (front == True):
        print("front")
    else:
        print("back")
