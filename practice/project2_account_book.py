import json

try:
    with open('records.json', 'r') as f:
        records = json.load(f)
except FileNotFoundError:
    records = [] # 파일이 없으면 빈 리스트로 시작

def add_record(record_type):
    desc = input("설명을 입력하세요: ")
    amount = int(input("금액을 입력하세요: "))
    records.append({"type": record_type, "desc": desc, "amount": amount})
    with open("records.json", "w") as f:
        json.dump(records, f)
    print(f"{record_type}이 저장되었습니다.")

while True:
    print("=== 가계부 프로그램 ===")
    print("1. 수입 추가")
    print("2. 지출 추가")
    print("3. 전체 내역 조회")
    print("4. 잔액 조회")
    print("5. 내역 삭제")
    print("6. 종료")

    choice = input("번호를 입력하세요")

    # 사용할 때
    if choice == "1":
        add_record("수입")

    elif choice == "2":
        add_record("지출")

    elif choice == "3":
        if not records:
            print("내역이 없습니다.")
        
        else:
            for record in records:
                print(f"[{record['type']}] {record['desc']}: {record['amount']:,}원")
            
    elif choice == "4":
        balance = 0 # 현재 잔액
        total_in = 0 # 총 수입
        total_out = 0 # 총 지출
        for record in records:
            if record['type'] == "수입":
                total_in += record['amount']
            
            elif record['type'] == "지출":
                total_out += record['amount']
        
        balance = total_in - total_out

        print(f"총 수입: {total_in:,}원")
        print(f"총 지출: {total_out:,}원")
        print(f"현재 잔액 : {balance:,}원")
        if balance < 0:
            print("잔액이 마이너스입니다!")


    elif choice == "5":
        if not records:
            print("내역이 없습니다.")
        else:
            for i, record in enumerate(records, 1):
                print(f"{i}. [{record['type']}] {record['desc']}: {record['amount']:,}원")

            index = int(input("삭제할 번호를 입력하세요: "))
 
            records.pop(index - 1) # 해당 인덱스의 항목 삭제 

            with open("records.json", "w") as f:
                json.dump(records, f)
            print(f"{index}번이 삭제되었습니다.") 
            
        
    elif choice == "6":
        print("프로그램을 종료합니다.")
        break