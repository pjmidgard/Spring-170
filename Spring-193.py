import os  
from time import time
import binascii
import math
import os.path

enter_name_of_file = input("New computer code: c and old computer code: e: ")

#@Author Jurijus pacalovas

class compression:

    def cryptograpy_compression(self):

                self.name = "Created: Jurijus pacalovas price Software 1000 000 Euro cost"

                if enter_name_of_file=="c":


                    corridors=0


                    corridors_2=7


                    name = input("What is name of file? ")


                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"

                    e5=0


                    e1=""


                    e6=0


                    e7=255

                    INFO3=""

                    INFO4=""

                    INFO5=""

                    reverse_bin=0

                    block_2=5

                    block_21=4

                    name_1=name

                    name_of_file=len(name_1)

                    name_1=name+".bin"

                    name_of_file=len(name_1)

                    count_numbers=0

                    counts_1=2


                    counts_11=0





                    s=""





                    e2=0





                    e3=2





                    e4=""





                    c=2





                    select_words=2





                    elements_words=0





                 





                    INFO3=""





                    INFO_OR_DATA_TO_BINARY=""











                    size_of_size_cosscounts_1=0





                    





                    binary_to_data=0











                    block=1





                    r=""











                    x=0





                    x1=0





                    x2=0





                    x = time()











                    with open(name_1, "w") as f4:





                            f4.write(s)





                    with open(name_1, "a") as f3:





                            f3.write(s)





                    with open(name, "rb") as binary_file:



                       # Read the whole file at once

                   
                        data = binary_file.read()
                     
                      


                        s=str(data)



                        long1=len(data)





                        long5=len(data)


                        times_numbers_reapits=0


                        binary_to_data_1=0




                        while times_numbers_reapits<10:





                            aas1=0


                            a1=0


                            counts_1=counts_1+1



                            count_numbers=count_numbers+1



                            with open(name_1, "ab") as f2:





                                if count_numbers==1:





                                    INFO=bin(int(binascii.hexlify(data),16))[2:]





                                    long=len(INFO)





                                    long1=len(data)




                                    times_7=(long1*8)-long





                                    z=0





                                    if times_7!=0:





                                        while z<times_7:



                                            if counts_11==0:

                                                INFO="0"+INFO





                                            z=z+1



                                    INFO=INFO


                                    if count_numbers==1:

                                     INFO_OR_DATA_TO_BINARY=INFO
                                     c=1
                                     
                                     if c==1:
                                         while counts_11!=10:
                                             long2=len(INFO_OR_DATA_TO_BINARY)
                                             block=0
                                             X=0
                                             X1=0
                                             INFOS=""
                                             
                                             while block<long2:
                                                xyz1=INFO_OR_DATA_TO_BINARY[block:block+4]
                                                xyz=xyz1[0:4]
                                                xyzg1=xyz1[0:2]
                                                xyzg2=xyz1[2:4]
                                                if len(xyz1)==4:
                                                    A=int(xyz1[0:2],2)
                                                    B=int(xyz1[2:4],2)
                                                    B1=int(xyz1[2:4],2)
                                                    B2=xyz1[2:4]
                                                    B3=int(xyz1[2:3],2)
                                                #print(X1)
                                                if     len(xyz1)!=4:
                                                        X1=1
                                                else:
                                                     AB=int(xyz,2)
                                                X+=1
                                                if X>1:
                                                    X=0
                                                D=format(X,"01b")
                                                E=format(X+1,"01b")
                                                F=format(X+2,"01b")
                                                
                                                if A==X and B3==X and X==0:
                                                    
                                                    C=xyzg1+"1"+xyz1[3:4]
                                                    #print(xyz1)
                                                    #print(C)                                           
                                                
                                                elif A==X and B3==X and X==1:
                                                    
                                                    C=xyzg1+"0"+xyz1[3:4]
                                                    #print(xyz1)
                                                    #print(C)   
                                                
                                                elif A==X and B==X and X==1:
                                                    
                                                    C=xyzg1+"1"
                                                    #print(xyz1)
                                                    #print(C)   
                                                    
                                                elif A==X and B==X and X==0:
                                                    
                                                    C=xyzg1+"00"
                                                    #print(xyz1)
                                                    #print(C)   
                                                    
                                                                                                
                                             
                                                else:
                               
                                                         
                                                    if xyz1[2:3]=="0" and X==0:
                                                         C=xyzg1+"1"+xyz1[3:4]
                                                         
                                                    elif xyz1[2:3]=="1" and X==1:
                                                         C=xyzg1+"0"+xyz1[3:4]
                                                         
                                                         

                                                    else:
                                                         #print(X)
                                                         C=xyz1
                                                         #print(C)
                                                         
                                                                                                             
                                                 
                                                 
                                                 
                                                 
       
                                                   
                                                #print(C)
                                                INFOS+=C
                                                block+=4
                                                #print(block)
                                          
                                             counts_11+=1
                                             INFO_OR_DATA_TO_BINARY=INFOS
                                             #print(INFOS)
                                             
                                         if counts_11==10:
                                    

                                              INFO_OR_DATA_TO_BINARY=INFOS

                                    long=len(INFO_OR_DATA_TO_BINARY)
                                long1=len(INFO_OR_DATA_TO_BINARY)
                                times_7=8-long%8
                                z=0
                               
                                if times_7!=0:





                                        while z<times_7:





                                            INFO_OR_DATA_TO_BINARY="0"+INFO_OR_DATA_TO_BINARY





                                            z=z+1                                        
                                    
                                        
                                        n = int(INFO_OR_DATA_TO_BINARY, 2)


                                        binary_data=len(INFO_OR_DATA_TO_BINARY)
                                        #print(binary_data)





                                        binary_data=(binary_data/8)*2





                                        binary_data=str(binary_data)





                                        binary_data="%0"+binary_data+"x"


                                        jl=binascii.unhexlify(binary_data % n)

                                        binary_to_data_2=len(jl)

                                        data=jl

                                        binary_to_data_1=binary_to_data_1+1



                                        binary_to_data_3=""


                                        size_x=""



                                        reverse_bin=reverse_bin+1
                                        if reverse_bin==1:

                                                times_numbers_reapits=10


                                                if times_numbers_reapits==10:


                                                    f2.write(jl)


                                                    x2 = time()



                                                    x3=x2-x

                                                    return print(x3)







    def cryptograpy_unpack(self):                                 





                 if enter_name_of_file=="e":





                    corridors=0





                    corridors_2=7





                    name=input("What is name of file? ")





                    name_new="file.Secret"





                    name_2=""





                    name_2_clear="?"





                    e1=""











                    e5=0





                    e6=0





                    e7=255











                    INFO3=""





                    INFO4=""





                    INFO5=""





                    INFO8=""











                 





                    reverse_bin=0





                    block_2=5





                    block_21=4





                    name_1=name





                    name_of_file=len(name_1)





                    name_1=name[:name_of_file-4]





                    name_of_file=len(name_1)





                    





                    count_numbers=0





                    counts_1=2





                    counts_11=0





                    s=""





                    e2=0





                    e3=2





                    e4=""





                    c=2





                    select_words=2





                    elements_words=0





                    cr=0





                 





                    INFO3=""





                    INFO_OR_DATA_TO_BINARY=""











                    size_of_size_cosscounts_1=0





                    





                    binary_to_data=0











                    block=1





                    counts_11=0











                    x=0





                    x1=0





                    x2=0





                    x = time()











                    with open(name_1, "w") as f4:





                            f4.write(s)





                    with open(name_1, "a") as f3:





                            f3.write(s)





                    with open(name, "rb") as binary_file:











                        # Read the whole file at once





                        data = binary_file.read()





                        s=str(data)





                        





                        long1=len(data)





                        long5=len(data)





                        





                        times_numbers_reapits=0





                        binary_to_data_1=0





                       





                        while times_numbers_reapits<10:





                       





                            aas1=0





                            a1=0











                            counts_1=counts_1+1





                            





                            count_numbers=count_numbers+1











                            with open(name_1, "ab") as f2:





                                if count_numbers==1:





                                    INFO=bin(int(binascii.hexlify(data),16))[2:]





                                    long=len(INFO)





                                    long1=len(data)





                                





                                    times_7=(long1*8)-long





                                    z=0





                                    if times_7!=0:





                                        while z<times_7:





                                            INFO="0"+INFO





                                            z=z+1





                                            





                                    INFO=INFO+INFO_OR_DATA_TO_BINARY











                                    if count_numbers==1:





                                        INFO_OR_DATA_TO_BINARY=INFO





                            





                                    n = int(INFO_OR_DATA_TO_BINARY, 2)





                                





                                    binary_data=len(INFO_OR_DATA_TO_BINARY)





                                    binary_data=(binary_data/8)*2





                                    binary_data=str(binary_data)





                                    binary_data="%0"+binary_data+"x"





                             





                                    jl=binascii.unhexlify(binary_data % n)





                                    binary_to_data_2=len(jl)





                                    





                                    data=jl





                                    binary_to_data_1=binary_to_data_1+1





                                   





                                    if count_numbers==1:











                                        long5=len(data)











                                    INFO=bin(int(binascii.hexlify(data),16))[2:]





                                    long=len(INFO)











                                    long1=len(data)





                                





                                    times_7=(long1*8)-long





                                    z=0





                                    if times_7!=0:





                                        while z<times_7:





                                            INFO="0"+INFO





                                            z=z+1











                                    INFO_OR_DATA_TO_BINARY=INFO











                                    long3=len(INFO_OR_DATA_TO_BINARY)





                                long2=len(INFO_OR_DATA_TO_BINARY)





                                c=1











                                if c==1:











                                    block=0


                                    X=0
                                    X1=0
                                    INFOS=""








                                    
                                    while block<long2:
                                        xyz1=INFO[0:9]
                                        xyz=INFO[0:8]
                                        xyzg1=INFO[0:4]
                                        xyzg2=INFO[4:8]
                                        if len(xyz1)==9:
                                            A=int(INFO[0:4],2)
                                            B=int(INFO[4:9],2)
                                            B1=int(INFO[4:8],2)
                                            X1=1
                                        else:
                                             A=int(INFO,2)
                                        X+=1
                                        if X>3:
                                            X=0
                                        D=format(X,"04b")
                                        E=format(X+1,"04b")
                                        F=format(X+2,"04b")
                                        
                                        if xyzg1==X and xyzg2==X:
                                            
                                            C=xyzg1+D
                                        
                                        elif xyzg1==X+1 and xyzg2==X+1:
                                            
                                            C=xyzg1+E
                                        else:
                                            if X1==1:
                                                G=B1+(X+2)
                                                if B1>15:
                                                    G=0+(X+2)
                                                F1=format(G,"04b")
                                                C=xyzg1+F1+INFO[8:9]
                                            else:
                                                C=xyz
                                        INFOS+=C
                                        block+=9
                                        #print(block)
                                        
                                    counts_11+=1
                                    #print(counts_11)                      

                                    if counts_11==1:







                           





                                    















                                                   





                                        





                                        



                                       

                                        INFO_OR_DATA_TO_BINARY=INFOS
                                        n = int(INFO_OR_DATA_TO_BINARY, 2)





                                        





                                        binary_data=len(INFO_OR_DATA_TO_BINARY)





                                        binary_data=(binary_data/8)*2





                                        binary_data=str(binary_data)





                                        binary_data="%0"+binary_data+"x"





                                     





                                        jl=binascii.unhexlify(binary_data % n)





                                        binary_to_data_2=len(jl)





                                        data=jl





                                        binary_to_data_1=binary_to_data_1+1





                                        binary_to_data_3=""





                                        size_x=""





                                    





                                        reverse_bin=reverse_bin+1





                                        if reverse_bin==1:





                                                times_numbers_reapits=10





                                                if times_numbers_reapits==10:





                                                





                                                    f2.write(jl)





                                                    x2 = time()





                                                    x3=x2-x





                                                    return print(x3)





                     











                                





               











d=compression()











xw=d.cryptograpy_compression()





print(xw)











xw1=d.cryptograpy_unpack()





print(xw1)