tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

total_fee = tuition_fee + lab_fee + library_fee + exam_fee
fee_after_discount = max(0.0, total_fee - discount)
annual_fee = fee_after_discount * 2
monthly_installment = annual_fee / 12

print(f"Tuition Fee: {tuition_fee:.2f}")
print(f"Lab Fee: {lab_fee:.2f}")
print(f"Library Fee: {library_fee:.2f}")
print(f"Exam Fee: {exam_fee:.2f}")
print(f"Total Fee: {total_fee:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Fee after Discount: {fee_after_discount:.2f}")
print(f"Annual Fee: {annual_fee:.2f}")
print(f"Monthly Installment: {monthly_installment:.2f}")