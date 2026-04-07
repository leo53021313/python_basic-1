# 計算幾次方
def pow(x, y):
    return x**y


def discount(total):
    if total >= 2000:
        total -= 200 * (total // 2000)
    return total


# 簡單斷句

print(f"myModule 的 __name__: {__name__}")


# 測試模組
if __name__ == "__main__":  # 測試時記得加入這個防止實際運行時這個也會print出來
    print(f"myModule.py - function pow 的結果: {pow(2,3)}")
    print(f"myModule.py - function discount 的結果: {discount(6000)} 元")
