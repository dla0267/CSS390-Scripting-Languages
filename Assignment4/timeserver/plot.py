import subprocess

with open('output.tsv', 'r') as infile, open('comp.txt', 'w') as outfile:
    prevLine = infile.next().split("\t")
    for i, line in enumerate(infile, 1):
        if i % 6 == 0:
            thisLine = line.split("\t")
            firstCode = (int(thisLine[1]) - int(prevLine[1])) / 60
            secondCode = (int(thisLine[2]) - int(prevLine[2])) / 60
            thirdCode = (int(thisLine[3]) - int(prevLine[3])) / 60
            outfile.write(str(thisLine[0]) + "\t" + str(firstCode) + "\t" + str(secondCode) + "\t" + str(thirdCode) + "\n")
            prevLine = thisLine
subprocess.call("./plot.sh")


