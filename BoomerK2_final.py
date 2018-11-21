def boomerKuwanger(file, pieces=1, prefix="", replace='\x00', offset=0):
    #file is the path to the file you want to mess with  -if you want to just use filename, put it in the same folder
    #pieces is how many pieces you want the file to be broken into          -default= 1
    #prefix is whatever you want to go at the beginning of the filenames    -default= nothing
    #replace is whatever you want put into the place of each section        -default= all zeroes
    #offset is how many bytes into the file you want the sections to start  -default= 0
    with open(file, 'rb') as inF:   #open the input file
        data = inF.read()       #data is the entire file as a string
    secLen = int((len(data))/pieces)    #secLen is the int length of each section
    rePiece = replace * secLen          #rePiece is what we're going to put in each section
    work = []               #initialize the list of section boundaries
    for i in range(offset, len(data), secLen):
        work.append(i)                  #generate the list of section boundaries
    for i in work:
        end = i+secLen
        if data[i:end]!=rePiece:
            save = open(prefix+"-"+str(secLen).zfill(5)+"-"+str(i).zfill(12)+"-"+file, 'wb')  #open the file
            data2 = data[:i]+rePiece+data[end:]
            save.write(data2)                       #save string to file
            save.close()                            #close file
