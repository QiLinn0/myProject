from pulp import *

prob = LpProblem('Z',LpMaximize)

X1 = LpVariable('X1', 0.0, cat = 'LpContinuous')
X2 = LpVariable('X2', 0.0, cat = 'LpContinuous')
X3 = LpVariable('X3', 0.0, cat = 'LpContinuous')

prob += X1 + 0.8 * X2 + 1.2 * X3

prob += X1 - X2 + X3 <= 30
prob += 3 * X1 + 2 * X2 +4 * X3 <= 42
prob += 3 * X1 + 2 * X2 <= 30

prob.solve()

print(LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("最小Z为", -1 * value(prob.objective))