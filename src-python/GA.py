import numpy as np
# 遗传算法
class GA:
    def __init__(self, population, fitness, cross_rate, mutation_rate, max_iter):
        self.population = population
        self.fitness = fitness
        self.cross_rate = cross_rate
        self.mutation_rate = mutation_rate
        self.max_iter = max_iter

    def run(self):
        # 初始化种群
        population = self.init_population()
        # 计算初始种群的适应度
        fitness_value = self.fitness(population)
        # 循环遗传
        for i in range(self.max_iter):
            # 选择
            population = self.select(population, fitness_value)
            # 交叉
            population = self.cross(population)
            # 变异
            population = self.mutate(population)
            # 计算新一代种群的适应度
            fitness_value = self.fitness(population)
        # 返回最好的种群
        return population[np.argmax(fitness_value)]

    def init_population(self):
        return np.random.randint(0, 2, size=(self.population, self.fitness.dim))

    def select(self, population, fitness_value):
        # 轮盘赌选择
        fitness_value = fitness_value / np.sum(fitness_value)
        # 按概率选择
        return np.random.choice(population, size=self.population, p=fitness_value)

    def cross(self, population):
        # 交叉
        new_population = np.empty(population.shape, dtype=np.int)
        for i in range(self.population):
            # 交叉概率
            if np.random.rand() < self.cross_rate:
                # 随机选择交叉点
                cross_point = np.random.randint(0, self.fitness.dim)
                # 交叉
                new_population[i, 0:cross_point] = population[i, 0:cross_point]
                new_population[i, cross_point:] = population[i, cross_point:]
            else:
                new_population[i, :] = population[i, :]
        return new_population
