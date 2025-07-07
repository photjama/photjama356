n = int(input())  # รับจำนวนตัวเลขทั้งหมด
bins = [0] * 21  # สร้างลิสต์ขนาด 21 เพื่อเก็บจำนวนของแต่ละ bin

# รับข้อมูลและนับจำนวนแต่ละ bin
for i in range(n):
    num = int(input())
    bins[num] += 1

# แสดงผลลัพธ์
for i in range(21):
    print(f"{i}:{'*' * bins[i]}")