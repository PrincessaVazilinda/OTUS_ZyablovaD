# приведение типа создает новый объект?
# операция приведения типа к объекту создает новый объект?
# Ответ: да, можно это проверить на примере ниже при помощи метода id()

# id() - это встроенная функция, которая возвращает нам
# уникальный идентификатор данного объекта, который присваивается
# при создании объекта. Следовательно, каждый раз при создании
# объекта идентификатор будет отличаться.
# Таким образом мы можем доказать, что создается новый объект.
sample = 5.0
print(id(sample))
print(id(sample))

sample = int(sample)
print(id(sample))
print(id(sample))
