import camelot
import pandas as pd


def main():
    pd.set_option('display.max_rows', 1000)
    # tables = camelot.read_pdf('AA200504.pdf', pages="8,9,10, 11, 12", flavor="stream")
    tables = camelot.read_pdf('AA200504.pdf', pages="8,9,10", flavor="stream")
    # print(tables[0].df)

    company = []
    kurs = []
    kursTarget = []
    anbefaling = []
    valuta = []


    parsedList = []
    


    for table in tables:
        data = table.df
        for row in data.index:
            if (row >= 2) and (data.loc[row,6] == "NOK") :
                diff = 0
                try:
                    diff = float(data.loc[row,4])-float(data.loc[row,2])
                    try:
                        diffPerAksje = diff/float(data.loc[row,2])*100
                    except:
                        diffPerAksje = 0
                except:
                    diff = 0
            

                
                # print(float(data.loc[row, 4]))
                parsedList.append(
                    {
                        'navn':data.loc[row,0],
                        'kurs':data.loc[row,2],
                        'kursTarget':data.loc[row,4],
                        'ticker':data.loc[row, 1],
                        'anbefaling':data.loc[row,3],
                        'valuta':data.loc[row,6],
                        'diff': diff,
                        'per aksje':diffPerAksje
                    }
                )
            
    a = pd.DataFrame.from_dict(parsedList)
    a = a.sort_values('per aksje', ascending=False)
    print(a)



if __name__ == "__main__":
    main()