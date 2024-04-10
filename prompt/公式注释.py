# 方差 = Σ((x - μ)²) / N
def calculate_variance(data):
    """计算并返回数据的方差。"""
    # 计算均值
    mean = sum(data) / len(data)
    # 计算方差
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

print(calculate_variance([1,100]))