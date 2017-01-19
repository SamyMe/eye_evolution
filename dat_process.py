from bisect import bisect_left
import decimal

def load_dat_file(file):
    dat_data = []
    with open(file) as f:
        next(f)
        for row in f:
            row = row.strip().split()
            dat_data.append((float(row[0]), float(row[1])))

    dat_data = sorted(dat_data, reverse=True)
    n0_vals = [ i[1] for i in dat_data]
    return dat_data, n0_vals


def find_r(t, n0):
    dat_data, n0_vals = t
    i = bisect_left(n0_vals, n0)
    print(dat_data[i][0], dat_data[i-1][0])
    print(dat_data[i][1], dat_data[i-1][1])
    
    return (dat_data[i-1][0] - dat_data[i][0])*(n0 - dat_data[i][1])/(dat_data[i-1][1] - dat_data[i][1]) + dat_data[i][0]
    
if __name__=="__main__":
    table = load_dat_file("indice_refraction_facile.dat")
    n0 = 1.3615223
    print(n0)
    print(find_r(table, n0))
