import csv

def read_csv(filename):
    """
    读取 CSV 文件并返回其中的数据。
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # 跳过标题行
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    """
    处理数据并返回冠军和他们赢得的次数以及冠军国家。
    """
    champions = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)
    return champions, countries

def display_champions(champions):
    """
    显示冠军和他们赢得的次数。
    """
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")

def display_countries(countries):
    """
    显示冠军国家。
    """
    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_str = ", ".join(sorted(countries))
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)
    champions, countries = process_data(data)
    display_champions(champions)
    display_countries(countries)

if __name__ == "__main__":
    main()