import multiprocessing as mp #library to allow multivore processing(built in to python)

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']

from algorithm import algorithm as al #imports a file that contains the hashing algorithm that takes an input and return a string

print ("this will work for only letters and numbers no other punctuation upto 10 chars long passwords.\nDisclaimer: It may take a while & shorter codes will be faster!")

hashed = input("hashed code:\n")#text that has been hashed by the algorithm


def catch(a):#catches where text is hashed and matches the hashed code includes catch cat car caut
    p3.terminate()
    p2.terminate()#kill other processes
    p4.terminate()
    print ("\nPassword is\n '{0}'".format(a))
    
def cat(a):
    p1.terminate()
    p3.terminate()
    p4.terminate()
    print ("\nPassword is\n '{0}'".format(a))
    exit()
 
def car(a):
    p1.terminate()
    p2.terminate()
    p4.terminate()
    print ("\nPassword is\n '{0}'".format(a))
    exit()
    
 
def caut(a):
    p1.terminate()
    p3.terminate()
    p2.terminate()
    print ("\nPassword is\n '{0}'".format(a))
    exit()
    

def ap():#names represent letter combos thaey try eg ap is a-p
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']\#all chars it tests after the first char
    start = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']#set of chars the forst char can be
    
    # loops through everysingle combo until correct one found
    for a in start:
        z = al(a)
        if z == hashed:
            catch(a)
        else:
            print (a,'\n')
            pass
    del a#deletes variables used to free memory so ram doesnt fill up
    # at yhis point skip to the end as the rest of the funcs are the same but with different first characters
    for a in start:
        for b in chars:
            x = a+b
            z = al(x)
            if z == hashed:
                catch(x)
            else:
                print (x,'\n')
                pass            
    del a
    del b
    del x
    for a in start:
        for b in chars:
            for c in chars:
                x = a+b+c
                z = al(x)
                if z == hashed:
                    catch(x)
                else:
                    print (x,'\n')
                    pass
    del a
    del b
    del c
    del x
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    x = a+b+c+d
                    z = al(x)
                    if z == hashed:
                        catch(x)
                    else:
                        print (x,'\n')
                        pass
                    
    del a
    del b
    del c
    del d
    del x
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        x = a+b+c+d+e
                        z = al(x)
                        if z == hashed:
                            catch (x)
                
                            exit()
                        else:
                            print (x,'\n')
                            pass
                        
    del a
    del b
    del c
    del d
    del e
    del x
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        for f in chars:
                            x  = a+b+c+d+e+f
                            z = al(x)
                            if z == hashed:
                                catch(x)
                            else:
                                print (x,'\n')
                                pass
    del a
    del b
    del c
    del d
    del e
    del f
    del x
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars: 
                        for f in chars:
                            for g in chars:
                                x = a+b+c+d+e+f+g
                                z = al(x)
                                if z == hashed:
                                    catch(x)
                                else:
                                    print (x,'\n')
                                    pass
    del a
    del b
    del c
    del d
    del e
    del f
    del g 
    del x                       
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        for f in chars:
                            for g in chars:
                                for h in chars:
                                    x = a+b+c+d+e+f+g+h
                                    z = al(x)
                                    if z == hashed:
                                        catch(x)
                                    else:
                                        print (x,'\n')
                                        pass
    del a
    del b
    del c
    del d
    del e
    del f
    del g
    del h
    del x                                 
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        for f in chars:
                            for g in chars:
                                for h in chars:
                                    for i in chars:
                                        x = a+b+c+d+e+f+g+h+i
                                        z = al(x)
                                        if z == hashed:
                                            catch(x)
                                        else:
                                            print (x,'\n')
                                            pass
    del a
    del b
    del c
    del d
    del e
    del f
    del g
    del h
    del i
    del x
    for a in start:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        for f in chars:
                            for g in chars:
                                for h in chars:
                                    for i in chars:
                                        for j in chars:
                                            x = a+b+c+d+e+f+g+h+i+j
                                            z = al(x)
                                            if z == hashed:
                                                catch(x)
                                            else:
                                                print (x,'\n')
                                                pass
    del a
    del b
    del c
    del d
    del e
    del f
    del g
    del h
    del i
    del j
    del x


def qE():
   #imagine above but with starting chars q-E
    
def FV():
   
def W0():
   
    
   
# the following just runs each func in seperate cpu cores so as im aware it will be done 4x faster then by a single core

p1 = mp.Process(target=ap)
p2 = mp.Process(target=qE)
p3 = mp.Process(target=FV)
p4 = mp.Process(target=W0)

p1.start()
p2.start()
p3.start()
p4.start()
 
p1.join()
p2.join()
p3.join()
p4.join()

