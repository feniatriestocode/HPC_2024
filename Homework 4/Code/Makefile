# Compiler and flags
CC = gcc
CFLAGS = -O3 -Wall -std=c99
LDFLAGS = -g

# CUDA setup for later transition (optional for now)
NVCC = nvcc
CUDAFLAGS = -O3 -arch=sm_70 # Change architecture as per your GPU

# Source and object files
SRC = contrast-enhancement.c histogram-equalization.c main.c
OBJ = $(SRC:.c=.o)

# Output binary
TARGET = main

# Default rule
all: $(TARGET)

# Compile and link
$(TARGET): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

# Object files
%.o: %.c hist-equ.h
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f $(OBJ) $(TARGET)

# Optional rule for CUDA compilation later
cuda:
	$(NVCC) $(CUDAFLAGS) -o $(TARGET) $(SRC)

# Phony targets
.PHONY: all clean cuda
