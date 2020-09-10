import pandas as pd


def new_entry(navn, kommentarer, aktivitet, kurs):
    entry = {
        "navn": navn,
        "kommentarer": kommentarer, 
        "aktivitet": aktivitet,
        "kurs": kurs
    }
    return entry

def main():
    pd.set_option('display.max_rows', 3000)
    fp = open("shareville_full", "r")
    file = fp.read() 
    file = file.split("Kurs") 
    file = file[2].split("Bli med!")
    file = file[0].split("\n")
    parsed = []
    k = 0
    
    k = 1
    while(1):
        try: 
            percent = file[k+2]
            if(len(percent) > 1):
                percent = file[k+2][:-1]
                percent = percent.replace("+", "")
                percent = percent.replace(",", ".")
                percent = float(percent)
        except:
            percent = 0
        try:
            if file[k+3][-3:] == "NOK" and percent != (0 or "-"):
                parsed.append(new_entry(
                    file[k],
                    file[k+1],
                    percent,
                    file[k+3]
                ))
        except:
            break;
        k = k+4

    a = pd.DataFrame.from_dict(parsed)
    a['aktivitet'] = a['aktivitet'].astype('float')
    a = a.sort_values('aktivitet', ascending=False)
    print(a)



if __name__ == "__main__":
    main()