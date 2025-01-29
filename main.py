import itertools 
 
def magic_trick(positions):
    # 第一步：筷子跟左边的东西互换 
    index = positions.index('筷子')
    if index != 0:
        positions = list(positions)
        positions[index], positions[index - 1] = positions[index - 1], positions[index]
        positions = tuple(positions)
    
    # 第二步：杯子跟右边的东西互换 
    index = positions.index('杯子')
    if index != 2:
        positions = list(positions)
        positions[index], positions[index + 1] = positions[index + 1], positions[index]
        positions = tuple(positions)
    
    # 第三步：勺子跟左边的东西互换 
    index = positions.index('勺子')
    if index != 0:
        positions = list(positions)
        positions[index], positions[index - 1] = positions[index - 1], positions[index]
        positions = tuple(positions)
    
    return positions 
 
items = ['筷子', '勺子', '杯子']
all_permutations = list(itertools.permutations(items)) 
 
# 记录不符合条件的排列 
failed_cases = []
 
print(f"总共有 {len(all_permutations)} 种排列组合。")
print("-----------------------------------------")
 
for idx, initial in enumerate(all_permutations, start=1):
    print(f"排列组合 {idx}：{initial}")
    
    current = initial 
    print(f"初始排列：{current}")
    
    # 第一步 
    step1 = list(current)
    index = step1.index('筷子')
    if index != 0:
        step1[index], step1[index - 1] = step1[index - 1], step1[index]
    print(f"第一步后：{tuple(step1)}")
    
    # 第二步 
    step2 = list(step1)
    index = step2.index('杯子')
    if index != 2:
        step2[index], step2[index + 1] = step2[index + 1], step2[index]
    print(f"第二步后：{tuple(step2)}")
    
    # 第三步 
    step3 = list(step2)
    index = step3.index('勺子')
    if index != 0:
        step3[index], step3[index - 1] = step3[index - 1], step3[index]
    print(f"第三步后：{tuple(step3)}")
    
    # 检查结果 
    if step3[2] == '杯子':
        print("最右边的是杯子")
    else:
        print("最右边的不是杯子")
        failed_cases.append(initial) 
    
    print("------------------------")
 
# 输出最终结果 
if failed_cases:
    print("以下排列组合在执行魔术后，最右边的不是杯子：")
    for case in failed_cases:
        print(case)
else:
    print("所有情况均已验证，最右边的都是杯子。")