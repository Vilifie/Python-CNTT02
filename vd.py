# a=float(input("nhap vao so thu 1:"))
# b=float(input("nhap vao so thu 2:"))
# c=a+b

# #b1
# chuyencan=float(input("nhap vao diem chuyen can:"))
# kiemtra=float(input("nhap vao diem kiem tra:"))
# baitap=float(input("nhap vao diem bai tap:"))
# thi=float(input("nhap vao diem thi:"))
# tongket=chuyencan*0.1+kiemtra*0.2+baitap*0.2+thi*0.5
# print("tong ket:",tongket)

# #b2
# import math
# a=float(input("nhap vao he so a:"))
# b=float(input("nhap vao he so b:"))
# c=float(input("nhap vao he so c:"))
# delta=b*b-4*a*c
# if delta>0:
#     x1=(-b-math.sqrt(delta))/(2*a)
#     x2=(+b+math.sqrt(delta))/(2*a)
#     print("x1=",x1)
#     print("x2=",x2)
# elif delta==0:
#     x=-b/(2*a)
#     print("nghiem kep:",x)
# else:
#     print("chuong trinh vo nghiem")

# # Ax+b=0
# a=float(input("Nhap a:"))
# b=float(input("Nhap b"))

# if a !=0:
#     x=-b/a
#     print("Nghiem x=", x)
# elif b == 0:
#     print("Phuong trinh vo so nghiem")
# else:
#     print("Phuong trinh vo nghiem")

# # Tinh thanh tien va giam gia
# so_luong = int(input("Nhap so luong:"))
# don_gia = float(input("Nhap don gia"))

# thanh_tien = so_luong * don_gia

# if thanh_tien >= 5000000:
#     giam_gia = 3
# if thanh_tien >= 2000000:
#     giam_gia = 2
# if thanh_tien>= 1000000:
#     giam_gia = 1
# else:
#     giam_gia = 0

# tien_giam = thanh_tien * giam_gia / 100
# phai_tra = thanh_tien - tien_giam

# print("Thanh tien:", thanh_tien)
# print("Giam gia:", giam_gia, "%")
# print("Tien giam:", tien_giam)
# print("So tien phai tra", phai_tra)

# if a>b:
#     a=a-b
# else:
#     b=b-a
# print("uoc:",a)

# Tim uoc so chung
# a=[1,2,3,4,9]
# for i in range(0,len(a)-1):
#     tong=tong+a[i]
# print("tong:",tong)


# chiều 2
# def tinh_tong(a, b):
#     """trả về tổng a + b"""
#     ket_qua= a + b
#     return ket_qua
# tong=tinh_tong(10,5)
# print(tong)
 

#vd1
# def chao(ten, loi="xin chào"):
#     print(f"{loi}, {ten}!")

# chao("an")
# chao("binh", "hello")
#vd2
def thong_ke(ds):
    tb = sum(ds) / len(ds)
    return min(ds), max(ds), tb
nho, lon, tb = thong_ke({7, 9, 6, 8})
print(nho, lon, tb)