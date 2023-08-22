import sys
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as before_file, open(sys.argv[2], "w", newline = "") as after_file:
            reader = csv.DictReader(before_file)
            writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                name, house = row["name"].split(", "), row["house"]
                first = name[1]
                last = name[0]
                writer.writerow({"first": first, "last": last, "house": house})


    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()