from geo.utils import calculate_circle_properties

def main():
    radius = 10  # 반지름 값을 지정합니다.
    c, area = calculate_circle_properties(radius)

    # 기대 결과와 실제 결과를 출력합니다.
    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()

