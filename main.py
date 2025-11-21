from pro_runner.generator import get_late_excuse, get_homework_excuse
import time

print("=== 변명만들기 레쓰고 ===")
print("...")
time.sleep(1) 

print("\n 교수님, 제가 오늘 늦은 이유는요")
print(f" {get_late_excuse()}")

print("\n 아 과제요? 과제는")
print(f" {get_homework_excuse()}")
print(" 진짜 그래서 못했어요")

print("\n===========================================")
