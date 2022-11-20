import pandas as pd


xls = pd.ExcelFile('dados.xlsx')
file1 = open("myfile.txt","a")#append mode
for i in xls.sheet_names:
    df = pd.read_excel('dados.xlsx', sheet_name=i)
    print(df)

    

    p = df.values.tolist()


    for l in p:
        base = f"INSERT INTO {i} VALUES ("
        for j in l:
            print(j, type(j))
            if type(j) in [int , float]:
                if not pd.isna(j):
                    base += f"{round(j)} , "
            else:
                base += f"'{j}' , "
    
        base = base[:-3] +");\n"

        print(base)
        file1.write(base)
# Append-adds at last


file1.close()