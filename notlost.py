import math

samples = []
sample = []
line = raw_input()
while line != "":
        if line != "*" and line[0:2] != "--":
                sample.append(line)
        elif line == "*":
                samples.append(sample)
                sample = []
        line = raw_input()
results = []

for s_index in range(0, len(samples)):
        degrees = []
        distance = []
        for st in samples[s_index]:
                r = st.split(" ")
                degrees.append(int(r[0]))
                distance.append(int(r[1]))
        vector = [0, 0]
        i = 0
	while(i < len(degrees)):
                disx = round(distance[i] * math.sin(math.radians(degrees[i])))
                disy = round(distance[i] * math.cos(math.radians(degrees[i])))
                vector[0] += disx
                vector[1] += disy
                i += 1
        print(vector)
        answer1 = round(math.sqrt(vector[0]**2 + vector[1]**2))
        if vector[1] == 0 and vector[0] > 0:
                answer2 = 270
        elif vector[1] == 0 and vector[0] < 0:
                answer2 = 90
        elif vector[1] > 0 and vector[0] == 0:
                answer2 = 180
        elif vector[1] < 0 and vector[0] == 0:
                answer2 = 0
        elif vector[0] > 0 and vector[1] > 0:
                answer2 = 270 - round(math.degrees(math.atan(vector[1]/vector[0])))
        elif vector[0] > 0 and vector[1] < 0:
                answer2 = 360 + round(math.degrees(math.atan(vector[1]/vector[0])))
        elif vector[0] < 0 and vector[1] < 0:
                answer2 = 90 - round(math.degrees(math.atan(vector[1]/vector[0])))
        elif vector[0] < 0 and vector [1] > 0:
                answer2 = 180 + round(math.degrees(math.atan(vector[1]/vector[0])))
        result = str(int(answer2)) + " " + str(int(answer1))
        print("-- SAMPLE "+str(s_index+1)+" --")
        print(result)