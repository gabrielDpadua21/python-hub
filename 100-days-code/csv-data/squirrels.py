import pandas


squirrels = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": []
}


if __name__ == '__main__':
    data = pandas.read_csv('squirrels.csv')
    gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
    red_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
    black_squirrels = data[data['Primary Fur Color'] == 'Black']
    
    squirrels["Count"] = [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
    
    df = pandas.DataFrame(squirrels)
    df.to_csv('report.csv')
