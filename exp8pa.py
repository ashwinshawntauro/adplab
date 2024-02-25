def display_handshake(people):
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            print(people[i],' shakes hand with ',people[j])

people=['sarosh','jaden','jacob']
display_handshake(people)