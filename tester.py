from geo.utils import calculate_circle_properties

def main():
    radius = 10  
    c, area = calculate_circle_properties(radius)

    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()
