import subprocess
import csv
import numpy as np

# List of input images to process
input_images = [
    '../Images/fort.pgm', 
    '../Images/planet_surface.pgm',
    '../Images/ship.pgm',
    '../Images/text.pgm',
    '../Images/x_ray.pgm',
    '../Images/uth.pgm',
    '../Images/gradient_1.pgm',
    '../Images/gradient_2.pgm',
    '../Images/galaxy_lowres.pgm',
    '../Images/galaxy.pgm',
    '../Images/galaxy_HD.pgm'
]

output_images = [
    '../Images/Results/res_fort.pgm',  
    '../Images/Results/res_planet_surface.pgm',
    '../Images/Results/res_ship.pgm',
    '../Images/Results/res_text.pgm',
    '../Images/Results/res_x_ray.pgm',
    '../Images/Results/res_uth.pgm',
    '../Images/Results/res_gradient_1.pgm',
    '../Images/Results/res_gradient_2.pgm',
    '../Images/Results/res_galaxy_lowres.pgm',
    '../Images/Results/res_galaxy.pgm',
    '../Images/Results/res_galaxy_HD.pgm'
]

# Number of times to run each image
iterations = 15

# Function to run the command and capture the execution time printed by the C program
def run_contrast_enhancement(image_path, output_path):
    # Run the C program and capture its output
    result = subprocess.Popen(
        ['./hist_eq', image_path, output_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Get the output from stdout
    stdout, stderr = result.communicate()

    # Extract the execution time from the program's output
    for line in stdout.splitlines():
        if "CPU contrast enhancement Execution Time" in line:
            # The line format is: "CPU contrast enhancement Execution Time: 5.838 milliseconds"
            exec_time_ms = float(line.split(":")[1].strip().split()[0])  # Get the float value before 'milliseconds'
            return exec_time_ms

    # If the execution time line is not found, raise an error
    raise ValueError("Execution time not found in output for image {}".format(image_path))

# Function to process all images and gather statistics
def process_images(input_images, iterations):
    results = []

    # Iterate over all input images
    for image, output in zip(input_images, output_images):
        times = []
        
        # Run the contrast enhancement program for each image multiple times
        for _ in range(iterations):
            try:
                exec_time = run_contrast_enhancement(image, output)
                times.append(exec_time)
            except ValueError as e:
                print(e)
        
        # Calculate average and standard deviation
        average_time = np.mean(times)
        std_deviation = np.std(times)
        
        # Save the result for the current image
        results.append([image, round(average_time,5), round(std_deviation,5)])
    
    return results

# Function to save the results to a CSV file
def save_results_to_csv(results, output_csv):
    # Write the results to a CSV file
    with open(output_csv, 'wb') as file:
        writer = csv.writer(file)
        writer.writerow(["Image", "Average CPU Time (ms)", "Standard Deviation (ms)"])  # Header row
        writer.writerows(results)

# Main function
if __name__ == "__main__":
    # Process the images and get the statistics
    results = process_images(input_images, iterations)
    
    # Output CSV file path
    output_csv = '../Images/Results/contrast_enhancement_results.csv'
    
    # Save the results to the CSV file
    save_results_to_csv(results, output_csv)
    
    # Python 2.x print statement (no f-strings)
    print("Results saved to {}".format(output_csv))
