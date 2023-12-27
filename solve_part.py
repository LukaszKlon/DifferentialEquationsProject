import numpy as np
import scipy.integrate as integrate

class solver():
    def __init__(self,n):
        self.elements_number = n
        self.h = 2 / n #odleglość pomiędzy kolejnymi punktami
    
    def e_iFunction(self,i,x):
        if x < self.h * (i-1) and x > self.h * (i+1):
            return 0
        if x < self.h * i:
            return x/self.h - i + 1
        return -x/self.h + i + 1
    
    def e_iPrim(self,i,x):
        if x < self.h * (i-1) and x > self.h * (i+1):
            return 0
        if x < self.h * i:
            return 1/self.h
        return -1/self.h 
    
    def integralB(self,i,j,l,r):
        q = 0
        if i == self.elements_number and j == self.elements_number:
            q = self.e_iFunction(i,2)*self.e_iFunction(j,2)
        return q - integrate.quad(lambda x: self.e_iPrim(i,x)*self.e_iPrim(j,x),l,r)[0] + integrate.quad(lambda x: self.e_iFunction(i,x)*self.e_iFunction(j,x),l,r)[0]
    
    def integralL(self,i,l,r):
        return -integrate.quad(lambda x: self.e_iFunction(i,x)*np.sin(x),l,r)[0]
    
    def Prepare_Left_Matrix(self):
        Result = []
        for i in range(1,self.elements_number+1):
            row = []
            for j in range(1,self.elements_number+1):
                if abs(i - j) > 1:
                    k = 0
                elif abs(i-j) == 1:
                    left = 2 * max(0,min(i,j)/self.elements_number)
                    right = 2 * min(1,max(i,j)/self.elements_number)
                    k = self.integralB(i,j,left,right)
                else:
                    left = 2 * max(0,(i-1)/self.elements_number)
                    right = 2 * min(1,(i+1)/self.elements_number)
                    k = self.integralB(i,j,left,right)
                row.append(k)
            Result.append(row)
        
        return Result

    def Prepare_Right_Matrix(self):
        Result = []
        for i in range(1,self.elements_number+1):
            left = 2 * max(0,(i-1)/self.elements_number)
            right = 2 * min(1,(i+1)/self.elements_number)
            Result.append(self.integralL(i,left,right))
        return Result
    
    def solve(self):

        B = np.array(self.Prepare_Left_Matrix())
        L = np.array(self.Prepare_Right_Matrix())
        # print(B)
        # print(L)

        return ([i*self.h for i in range(self.elements_number+1)],np.insert(np.linalg.solve(B,L),0,0))
    


x = solver(5)
print(x.solve())
