import numpy as np
import matplotlib.pyplot as plot
from numbers import Number
from collections import Counter
from math import ceil,floor


def checker(data: tuple or list)-> None:
    """
    This function help to check data set
    :param data:
    :return: None
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError('Data set must be list or tuple.')
    if len(data) == 0:
        raise ValueError('Data set should have some data')


def mean(data: tuple or list)->float:
    """
    This function calculate mean value
    :param data: data set
    :return: float -- mean value
    """
    checker(data)
    return sum(data)/len(data)


def variance(data: list or tuple)-> float:
    """
    Function which calculate variance
    :param data: data set
    :return: float -- variance
    """
    if len(data) == 1:
        raise ValueError('Data set should have minimum two elements for this function')
    checker(data)
    m = mean(data)
    d = [item**2 for item in data]
    m2 = mean(d)
    return m2 - m**2


def std(data: list or tuple)-> float:
    """
    Function which calculate standart deviation
    :param data: data set
    :return: float -- std deviation
    """
    return variance(data)**0.5


def mode(data: list or tuple)->tuple:
    """
    Function which calculate mode
    :param data:
    :return:
    """
    checker(data)
    item_with_value = Counter(data).most_common()
    max_fr_value = item_with_value[0][1]
    return tuple(item for item, value in item_with_value if value == max_fr_value)


def median(data: list or tuple)-> float:
    """
    Function which calculate median
    :param data:
    :return:
    """
    checker(data)
    sort_data = sorted(data)
    if len(data) % 2 == 1:
        return sort_data[len(data)//2]
    else:
        return (sort_data[len(data)//2] + sort_data[len(data)//2 - 1])/2


def quantile(data: list or tuple, p: float)->float:
    """
    This function calculates quantile
    :param data:
    :return:
    """
    checker(data)
    if not isinstance(p, Number):
        raise TypeError('Propability should be a number')
    if not 0 <= p <= 1:
        raise ValueError('Propability should be in range of 0;1')
    p = float(p)

    return sorted(data)[ceil(p*len(data))]

def data_range(data: list or tuple)-> float:
    """

    :param data:
    :return:
    """
    checker(data)
    return max(data)-min(data)


def covariation(set1: list or tuple, set2: list or tuple)->float:
    """
    Function which calculate covariation
    :param set1:
    :param set2:
    :return:
    """
    checker(set1)
    checker(set2)

    if len(set1) != len(set2):
        raise ValueError('Sets should have equal sizes')
    if len(set1) <= 1:
        raise ValueError('Sets should have more than 1 item')

    set1_dev = [item - mean(set1) for item in set1]
    set2_dev = [item - mean(set2) for item in set2]
    return sum([item1 * item2 for item1, item2 in zip(set1_dev, set2_dev)])/(len(set1)-1)

def corrilation(set1: list or tuple, set2: list or tuple)->float:
    """
    Function which calculate corrilation
    :param set1:
    :param set2:
    :return:
    """
    if std(set1) > 0 and std(set2) > 0:
        return covariation(set1, set2)/(std(set1)*std(set2))
    return 0


def make_buckets(data: tuple or list, size: int)->dict:
    """

    :param data:
    :param size:
    :return:
    """
    checker(data)
    if size <= 0:
        raise ValueError('Size should be more than 0')
    return Counter([size * floor(i / size) for i in data])


def cdf(data: list or tuple)->list:
    """

    :param data:
    :param plot:
    :return:
    """
    checker(data)
    step = data_range(data)/(len(data)-1)
    values = np.arange(min(data), max(data) + 2*step, step)
    prob = [sum([num for key, num in Counter(data).items()
                 if key < value]) / (len(data)) for value in values]
    plot.title('CDF')
    plot.plot(values, prob)
    plot.show()
    return values.tolist(), prob


def pdf(data: list or tuple, size: int)->list:
    """

    :param data:
    :return:
    """
    checker(data)
    bucket_data = make_buckets(data, size)
    sort_buck_data = sorted(bucket_data.keys())
    prob = [bucket_data[key]/len(data) for key in sort_buck_data]
    plot.plot(sort_buck_data, prob)
    plot.title('PDF')
    plot.show()
    return sort_buck_data, prob


def box_plot(data: tuple or list) -> None:
    """
    Box plot for data set
    :return: None
    """
    plot.boxplot(data)
    plot.show()


def hist(data, size, title="", label_x="", label_y="")-> None:
    """

    :param data: data set
    :param size: size of buckets
    :param title: title
    :param label_x: x label
    :param label_y: y label
    :return: None
    """

    hist_data = make_buckets(data, size)
    plot.bar(hist_data.keys(), hist_data.values(), width=size)
    plot.xlabel(label_x)
    plot.ylabel(label_y)
    plot.title(title)
    plot.show()



if __name__ == '__main__':
    print(mode([1,1,1,1,1,2,2,3,3,3,3,3]))
    cdf([1,1,1,1,1,2,2,3,3,3,3,3])
    pdf([1,1,1,1,1,2,2,3,3,3,3,3])




