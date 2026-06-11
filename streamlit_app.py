# 1. 재료 정보를 저장할 리스트 초기화
materials_list = []

print("=== 건축물 비용 및 친환경 점수 측정 프로그램 ===")
print("재료 입력을 종료하려면 비용에 '0'을 입력하세요.\n")

# 2. 반복문: 0을 입력할 때까지 계속해서 재료 정보를 더함
while True:
    material_name = input("재료 이름을 입력하세요: ")
    
    try:
        cost = int(input(f"[{material_name}]의 비용을 입력하세요 (원): "))
        if cost == 0:
            print("입력을 종료합니다.\n")
            break
            
        score = int(input(f"[{material_name}]의 친환경 점수를 입력하세요 (0~100점): "))
    except ValueError:
        print("숫자로 정확히 입력해주세요. 다시 입력합니다.\n")
        continue

    # 입력받은 데이터를 딕셔너리 형태로 리스트에 저장
    materials_list.append({
        "name": material_name,
        "cost": cost,
        "score": score
    })
    print("-" * 30)

# 3. 총합 및 평균 계산 (반복문을 통해 리스트 내부 데이터 누적)
total_cost = 0
total_score = 0
count = len(materials_list)

for item in materials_list:
    total_cost += item["cost"]
    total_score += item["score"]

# 4. 조건문을 통한 건축물 등급 판정 및 결과 출력
if count > 0:
    average_score = total_score / count
    
    print("=" * 40)
    print("[ 최종 건축물 측정 결과 ]")
    print(f"• 등록된 총 자재 수: {count}개")
    print(f"• 총 예상 건축 비용: {total_cost:,}원")
    print(f"• 친환경 평균 점수: {average_score:.1f}점")
    print("-" * 40)
    
    # 조건문: 70점 이상 판정
    if average_score >= 70:
        print("결과: 🎉 [친환경 건축물] 인증 등급입니다.")
    else:
        print("결과: 🏢 [일반 건축물] 등급입니다.")
    print("=" * 40)
else:
    print("입력된 자재 데이터가 없어 결과를 산출할 수 없습니다.")
