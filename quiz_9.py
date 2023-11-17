class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

# 객체 생성
coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

while True:
    # 첫 번째 사용자 입력
    selected_beverage = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")

    # 선택된 음료에 따라 객체 할당 및 calculate 함수 호출
    if selected_beverage == "커피":
        selected_object = coffee
    elif selected_beverage == "녹차":
        selected_object = green_tea
    elif selected_beverage == "아이스티":
        selected_object = ice_tea
    else:
        print("올바른 음료를 선택하세요.")
        continue

    # 두 번째 사용자 입력
    quantity = int(input(f"{selected_beverage}의 수량을 입력하세요: "))

    # calculate 함수 호출 및 결과 출력
    total_price = selected_object.calculate(quantity)
    print(f"{selected_beverage} {quantity}잔의 총 가격은 {total_price}원 입니다.")

    # 추가 주문 여부 확인
    additional_order = input("추가 주문을 하시겠습니까? (예/아니오): ").lower()
    if additional_order != "예":
        break
