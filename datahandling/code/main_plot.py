import matplotlib.pyplot as plt
import random
from collections import Counter

if __name__ == "__main__":

    # scatter plot
    random.seed(666)
    x = [random.randint(0,100) for _ in range(100)]
    y = [random.randint(0,100) for _ in range(100)]
    plt.scatter(x, y)
    plt.show()

    # line plot
    x = [random.randint(0, 100) for _ in range(100)]
    plt.plot([i for i in range(100)], x)
    plt.show()

    # bar plot
    data = [3, 3, 4, 1, 5, 4, 2, 1, 5, 4, 4, 4, 5, 3, 2, 1, 4, 5, 5]
    counter = Counter(data)
    x = [point[0] for point in counter.most_common()]
    y = [point[1] for point in counter.most_common()]
    plt.bar(x, y)
    plt.show()

    # histogram
    data = [random.randint(1, 100) for _ in range(1000)]
    plt.hist(data, rwidth = 0.8, bins = 5, density = True)
    plt.show()

    # boxplot
    data = [random.randint(1, 100) for _ in range(1000)]
    data.append(200)
    data.append(-200)
    plt.boxplot(data)
    plt.show()

    data1 = [random.randint(66, 166) for _ in range(200)]
    data2 = [random.randint(60, 120) for _ in range(200)]
    plt.boxplot([data1, data2])
    plt.show()



