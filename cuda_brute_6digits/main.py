import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy as np
import time

# Simulate the correct pin (known beforehand)
correct_pin = "236472"
correct_pin_int = int(correct_pin)

# CUDA Kernel to perform brute-force cracking of PINs
mod = SourceModule("""
__global__ void brute_force_kernel(int target_pin, int *found)
{
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    
    if (*found) return; // Exit if PIN is already found

    int pin = idx;  // Assign each thread a unique PIN
    
    if (pin == target_pin) {
        atomicExch(found, 1);  // Use atomicExch to safely update found
    }
}
""")

# Function to brute force using CUDA
def brute_force_with_gpu():
    num_pins = 1000000  # Number of possible PIN combinations (from 000000 to 999999)
    block_size = 256  # Number of threads per block
    grid_size = (num_pins + block_size - 1) // block_size  # Grid size to cover all PINs

    target_pin = np.array([correct_pin_int], dtype=np.int32)
    found = np.array([0], dtype=np.int32)  # Use 0 for False, 1 for True

    # Allocate memory on the GPU for target_pin and found
    target_pin_gpu = cuda.mem_alloc(target_pin.nbytes)
    found_gpu = cuda.mem_alloc(found.nbytes)

    # Copy data from CPU to GPU
    cuda.memcpy_htod(target_pin_gpu, target_pin)
    cuda.memcpy_htod(found_gpu, found)

    # Launch the kernel
    func = mod.get_function("brute_force_kernel")
    func(target_pin_gpu, found_gpu, block=(block_size, 1, 1), grid=(grid_size, 1))

    # Copy the result back to the CPU
    cuda.memcpy_dtoh(found, found_gpu)

    if found[0] == 1:  # If found is set to 1 (True)
        print(f"Found correct PIN: {correct_pin}")
    else:
        print("PIN not found.")

if __name__ == "__main__":
    start_time = time.time()
    brute_force_with_gpu()
    end_time = time.time()

    print(f"Brute-force finished in {end_time - start_time:.4f} seconds")
