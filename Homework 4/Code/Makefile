# Compiler and flags
NVCC = nvcc
CFLAGS = -O2

# Source files and output executable
SRC = contrast_enhancement.cu histogram_equalization.cu main.cu
OUT = hist_eq

# Default target
all: $(OUT)

# Compile the source files and create the executable
$(OUT): $(SRC)
	$(NVCC) $(CFLAGS) $(SRC) -o $(OUT)

# Clean up build files
clean:
	rm -f $(OUT)

# Phony targets
.PHONY: all clean
