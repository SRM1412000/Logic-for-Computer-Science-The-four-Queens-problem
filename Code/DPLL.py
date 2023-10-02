# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 07:08:41 2020

@author: David
"""


def complemento(i):
    if len(i)==1 or len(i)==2:
        if  i[0]=='-' and i[1]!='-':
            return i[1]
        elif(i[0]!='-' and len(i)==1):
            return '-'+i[0]
        
def clausula_unitaria(S):
    for i in range(0,len(S)):
        if(len(S[i])==1):
            return S[i][0]
        
def unitPropagate(u,p):
    while(([] not in u) and (clausula_unitaria(u))):
        i=0
        l=clausula_unitaria(u)
        if(len(l)==1):
            p[l]=1
        elif(len(l)==2):
            p[l[1]]=0
        while(i<len(u)):
            if(len(u)>0 and l in u[i]):
                u.pop(i)
                i-=1
            if(len(u)>0 and complemento(l) in u[i]):
                u[i].remove(complemento(l))
            i+=1
    return u,p




def DPLL(S,i):
    S,i=unitPropagate(S, i)
    if([] in S):
        return "Insatisfacible",[]
    if(len(S)==0):
        return "Satisfacible",i
    c=0
    l=""
    while(c<len(S) and len(l)==0):
        if(S[c][0] not in i.keys()):
            l=S[c][0]
        c+=1;
    c=0
    s2=S[:]
    new_dict=i.copy()
    if(len(l)==1):
        new_dict[l]=1
    elif(len(l)==2):
        new_dict[l[1]]=0
    while(c<len(s2)):
        if(len(s2)>0 and l in s2[c]):
            s2.pop(c)
            c-=1
        c+=1
    s2=[[t for t in sub if t!=complemento(l)]for sub in s2]
    c=0
    z,w=DPLL(s2,new_dict)
    if(z=="Satisfacible" and w):
        return "Satisfacible",w
    else:
        s3=S[:]
        l=complemento(l)
        while(c<len(s3)):
            if(len(s3)>0 and l in s3[c]):
                s3.pop(c)
                c-=1
            c+=1
        s3=[[b for b in sub if b!=complemento(l)]for sub in s3]
        new_dict2=i.copy()
        if(len(l)==1):
            new_dict2[l]=1
        elif(len(l))==2:
            new_dict2[l[1]]=0
        return DPLL(s3,new_dict2)





    

        
        
 
        
        
        
        
    
    
    
    
    
        
    
            
        

        
    
    

                    
               
        
                
    
                
       
            
            
    
                
                

    