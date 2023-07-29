# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    # remain [i] = gas[i] - cost[i]
    remaining_gas = [gas_of_i_th - cost_of_i_th for gas_of_i_th, cost_of_i_th in zip(gas, cost)]
    if sum(remaining_gas) >= 0:
        for i in range(len(remaining_gas)):
            if remaining_gas[i] > 0:
                return i
    return -1
