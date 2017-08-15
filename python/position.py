positionA=0
positionB=102
t=0
while((positionB-positionA)!=0):
    t+=1
    positionA=2*t
    positionB=102-(1*t)
    distanceB=102 - positionB

print("The walker A meets walker B at his " + str(positionA) + " mile")

print("The walker B meets walker A at his " + str(distanceB) + " mile")
