import csv

def convert_to_csv(input_file, output_file):
    """Convert a text file to CSV format with dynamic headers."""
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        first_line = infile.readline().strip()
        headers = first_line.split(", ")  
        
        writer.writerow(headers)
        
        writer.writerow(first_line.split(", "))  
        for line in infile:
            data = line.strip().split(", ")
            writer.writerow(data)

if __name__ == "__main__":
    input_file = 'data.txt'  
    output_file = 'output.csv' 

    convert_to_csv(input_file, output_file)
    print(f"Data has been converted from {input_file} to {output_file}.")
