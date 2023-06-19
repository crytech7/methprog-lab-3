from matplotlib import pyplot
from scipy.interpolate import make_interp_spline
import numpy as np
def main():
    """Генерируем графики"""

    size = [10, 100, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

    meta_simple_hash_times = [5.245208740234375e-06, 5.7220458984375e-06, 8.821487426757812e-06, 1.9788742065429688e-05, 2.002716064453125e-05, 2.47955322265625e-05, 8.726119995117188e-05, 2.3603439331054688e-05, 2.193450927734375e-05, 2.193450927734375e-05, 6.890296936035156e-05, 2.3365020751953125e-05]
    meta_complex_hash_times = [0.006956577301025391, 0.00577092170715332, 0.0037963390350341797, 0.0038619041442871094, 0.003961801528930664, 0.003917217254638672, 0.008816003799438477, 0.004555225372314453, 0.006234169006347656, 0.0038635730743408203, 0.005184173583984375, 0.00412750244140625]
    meta_simple_collisions = [0, 0, 0, 2, 0, 2, 1, 1, 0, 0, 0, 1]
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
