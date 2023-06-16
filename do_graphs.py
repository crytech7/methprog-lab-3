from matplotlib import pyplot
from scipy.interpolate import make_interp_spline
import numpy as np
def main():
    """Генерируем графики"""

    size = [10, 100, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    meta_simple_hash_times = [1.8401579423384234e-05, 4.204836758700284e-06, 1.1075626720081676e-05, 1.2115998701615768e-05, 2.11975791237571e-05, 2.863190390846946e-05, 1.89651142467152e-05, 2.215125344016335e-05, 1.9767067649147727e-05, 1.9420276988636363e-05, 2.8891996903852984e-05, 2.0655718716708098e-05]
    meta_complex_hash_times = [0.004247340289029208, 0.004142327742143111, 0.0040828748182816935, 0.004192200574007901, 0.004110206257213245, 0.004081531004472213, 0.004004001617431641, 0.00409609621221369, 0.004780856045809659, 0.004007664593783292, 0.004165952855890448, 0.004086494445800781]
    meta_simple_collisions = [3, 1, 2, 1, 10, 5, 2, 5, 2, 1, 9, 2]
    meta_complex_collisions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    size_np = np.array(size)

    meta_simple_collisions_np = np.array(meta_simple_collisions)
    meta_complex_collisions_np = np.array(meta_complex_collisions)

    X_Y_Spline = make_interp_spline(size, meta_simple_collisions_np)
    X_ = np.linspace(size_np.min(), size_np.max(), 500)
    Y_ = X_Y_Spline(X_)
    pyplot.plot(X_, Y_, label="simple hash")

    X_Y_Spline = make_interp_spline(size_np, meta_complex_collisions_np)
    X_ = np.linspace(size_np.min(), size_np.max(), 500)
    Y_ = X_Y_Spline(X_)
    pyplot.plot(X_, Y_, label="complex hash")
    
    pyplot.xlabel("Количество элементов, штук")
    pyplot.ylabel("Коллизии, штуки")
    pyplot.legend()
    pyplot.savefig("Collisions")

    # meta_simple_hash_times_np = np.array(meta_simple_hash_times)
    # meta_complex_hash_times_np = np.array(meta_complex_hash_times)
    
    # X_Y_Spline = make_interp_spline(size, meta_simple_hash_times_np)
    # X_ = np.linspace(size_np.min(), size_np.max(), 500)
    # Y_ = X_Y_Spline(X_)
    # pyplot.plot(X_, Y_, label="simple hash")
    
    # X_Y_Spline = make_interp_spline(size_np, meta_complex_hash_times_np)
    # X_ = np.linspace(size_np.min(), size_np.max(), 500)
    # Y_ = X_Y_Spline(X_)
    # pyplot.plot(X_, Y_, label="complex hash")
    # # pyplot.plot(size, times_sel_sort, label="selection sort")
    # pyplot.xlabel("Количество элементов, штук")
    # pyplot.ylabel("Время, секунды")
    # pyplot.legend()
    # pyplot.savefig("Find hash tables times")


if __name__ == "__main__":
    main()
