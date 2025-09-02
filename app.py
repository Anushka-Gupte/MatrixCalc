import streamlit as st
import numpy as np

st.title("Matrix Calculator")

operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Transpose"])

if(operation == "Transpose"):
    n = st.selectbox("Select number of matrices", [1])
    data1 = st.text_area("Enter number of rows")
    data2 = st.text_area("Enter number of columns")
    try:
        r = int(data1.strip())
        c= int(data2.strip())
    except ValueError:
        st.write("Enter correct number of rows and columns")
    data = st.text_area("Enter a 2D matrix (rows separated by newlines and columns by commas)")
    button_sub = st.button("Calculate")
    if(data):
            try:
                values = []
                for row in data.strip().split('\n'):
                    for item in row.strip().split(','):
                        values.append(int(item))
                arr = np.array(values)
                arr= arr.reshape(r,c)
                arr = arr.T
                if(button_sub and data):
                    st.success(arr,icon="✅")
            except ValueError:
                st.error("Wrong format entered",icon="🚨")

else:
    n = st.selectbox("Select number of matrices", [2])
    

    if operation == "Addition" or operation == "Subtraction":

        data1 = st.text_area("Enter number of rows of any matrix")
        data2 = st.text_area("Enter number of columns of any matrix")
        r,c = 0,0
        try:
            r = int(data1.strip())
            c= int(data2.strip())
        except ValueError:
            st.write("Enter correct number of rows and columns")
        
        mat1 = st.text_area("Enter a 2D matrix (rows separated by newlines and columns by commas)", key=1)
        if(mat1):
                try:
                    values1 = []
                    for row in mat1.strip().split('\n'):
                        for item in row.strip().split(','):
                            values1.append(int(item))
                    arr1 = np.array(values1)
                    arr1 = arr1.reshape(r,c)
                except ValueError:
                    st.error("Wrong format entered",icon="🚨")
                
        mat2 = st.text_area("Enter a 2D matrix (rows separated by newlines and columns by commas)", key=2)
        if(mat2):
            try: 
                values2 = []
                for row in mat2.strip().split('\n'):
                    for item in row.strip().split(','):
                        values2.append(int(item))
                arr2 = np.array(values2)
                arr2 = arr2.reshape(r,c)
            except ValueError:
                st.error("Wrong format entered",icon="🚨")
        button_sub = st.button("Calculate")
        if(button_sub and mat1 and mat2):
            if operation == "Addition":
                st.success(arr1+arr2,icon="✅")
            else:
                st.success(arr1-arr2,icon="✅")

    elif operation == "Multiplication":
        d1 = st.text_area("Enter number of rows of 1st matrix")
        d2 = st.text_area("Enter number of columns of 1st matrix")
        try:
            r1 = int(d1.strip())
            c1 = int(d2.strip())
        except ValueError:
            st.write("Enter correct number of rows and columns")
        mat1 = st.text_area("Enter a 2D matrix(rows separated by newlines and columns by commas)",key=3)
        if(mat1):
            try:
                values3 = []
                for row in mat1.strip().split('\n'):
                    for item in row.strip().split(','):
                        values3.append(int(item))
                arr1 = np.array(values3)
                arr1 = arr1.reshape(r1,c1)
            except ValueError:
                    st.error("Wrong format entered")
        d3 = st.text_area("Enter number of rows of 2nd matrix")
        d4 = st.text_area("Enter number of columns of 2nd matrix")
        try:
            r2 = int(d3.strip())
            c2 = int(d4.strip())
        except ValueError:
            st.write("Enter correct number of rows and columns")
        mat2 = st.text_area("Enter a 2D matrix(rows separated by newlines and columns by commas)",key=4)
        if(mat2):
            try: 
                values2 = []
                for row in mat2.strip().split('\n'):
                    for item in row.strip().split(','):
                        values2.append(int(item))
                arr2 = np.array(values2)
                arr2 = arr2.reshape(r2,c2)
            except ValueError:
                st.error("Wrong format entered",icon="🚨")

        button_sub = st.button("Calculate")
        if(button_sub and mat1 and mat2):
            try:
                arr = np.matmul(arr1,arr2)
                st.success(arr,icon="✅")
            except ValueError:
                st.error("Invalid dimensions for multiplication",icon="🚨")







    