#import the warning module
import warnings

with warnings.catch_warnings():
    #ignore warnings
    warnings.simplefilter("ignore")

    #import necessary packages
    import numpy as np

    #Function to find the count of vowels and consonants in a given input string
    def count_vowels_consonants(input_string):
        vowels_count=0
        consonant_count=0
        for i in input_string:
            i=i.lower() #convert sentence to lower case
            if i.isalpha(): #check if character is an alphabet
                if i in ['a','e','i','o','u']:
                    vowels_count=vowels_count+1 # if character is vowel increment vowel count 
                else:
                    consonant_count=consonant_count+1# else increment consonant count
        return vowels_count,consonant_count # return both count as a tuple

    #Function to perform matrix multiplication
    def matrix_multiplication(matrix1,matrix2):
        shape1=matrix1.shape
        shape2=matrix2.shape
        resultant_matrix=[[0 for i in range(shape1[0])] for j in range(shape2[1])]  #declare resultant matrix and initialise to zeros
        if shape1[1]!=shape2[0]: #if not multipliable exits function
            return False
        else:
            #perform matrix multiplication
            for i in range(shape1[0]):
                for j in range(shape2[1]):
                    for k in range(shape2[0]):
                        resultant_matrix[i][j]=resultant_matrix[i][j]+(matrix1[i][k]*matrix2[k][j])
            return resultant_matrix #return reultant matrix

    #Function to find common elements in 2 lists
    def find_common_elements(list1, list2):
        visited=[]
        count=0
        for i in list1:
            for j in list2:
                #if the element has already not been considered and is present in both lists count is incremented
                if i not in visited and i==j:
                    visited.append(i)
                    count=count+1
        return count #return count

    #Function to find the transpose of a matrix
    def convert_transpose(matrix):
        matrix=np.array(matrix)
        row=matrix.shape[0]
        column=matrix.shape[1]
        #Declare transpose matrix and initialise to zeros
        transpose=np.array([[0 for i in range(row)] for j in range(column)])
        for i in range(row):
            for j in range(column):
                transpose[j][i]=matrix[i][j]
        return transpose #return transpose matrix
                    

    #Q1
    print("Q1")
    input_string=input("Enter the input string:")
    count=count_vowels_consonants(input_string)#store returned value
    print("Number of vowels:",count[0])
    print("Number of consonants:",count[1])
    print()

    #Q2
    print("Q2")
    matrix1=eval(input("Enter the first matrix:"))
    matrix2=eval(input("Enter the second matrix:"))
    matrix1=np.array(matrix1)
    matrix2=np.array(matrix2)
    resultant_matrix=matrix_multiplication(matrix1,matrix2)#store returned value
    #if resultant matrix is not False then matrix is printed else appropriate error message is displayed
    if resultant_matrix:
        print("Resultant matrix:",resultant_matrix)
    else:
        print("The matrices are not multipliable")
    print()

    #Q3
    print("Q3")
    list1=eval(input("Enter the first list:"))
    list2=eval(input("Enter the second list:"))
    count=find_common_elements(list1,list2)#store returned value
    print("Count :",count)
    print()

    #Q4
    print("Q4")
    matrix=eval(input("Enter the matrix:"))
    transpose=convert_transpose(matrix)#store returned value
    print("Transpose :",transpose)
    
