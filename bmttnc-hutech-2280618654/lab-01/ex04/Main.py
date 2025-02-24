from QuanLySinhVien import QuanLySinhVien
    
qlsv = QuanLySinhVien()
while (1 == 1):
        print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("==========================MENU======================")
        print("== 1:THÊM SINH VIÊN ==")
        print("== 2:Cập nhật thông tin bởi ID ==")
        print("== 3:Xoá sinh viên bởi ID ==")
        print("== 4:Tìm kiếm sinh viên theo tên ==")
        print("== 5:Sắp xếp sinh viên theo điểm TB ==")
        print("== 6:Sắp xếp sinh viên theo điểm chuyên ngành ==")
        print("== 7:Hiển thị danh sách sinh viên ==")
        print("== 0:Thoat ==")
        print("====================================================")
        
        key = int (input("Nhập tuỳ chọn:"))
        if(key == 1):
            print("\n1:Thêm sinh viên.")
            qlsv.nhapSinhVien()
            print("\nThêm sinh viên thành công!")
        elif (key == 2):
            if (qlsv.soLuongSinhVien() > 0):
                print("\nCập nhật thông tin sinh viên. ")
                print("\nNhập ID: ")               
                ID = int (input())
                qlsv.updateSinhVien (ID)
            else:
                    print("\nDanh sách sinh viên trống!")
        elif (key == 3 ):
            if (qlsv.soLuongSinhVien ()> 0 ) :
                print("\n3: Xoá sinh vien.")
                print("\nNhập ID: ")
                ID = int (input())
                if (qlsv.deleteById(ID)):
                    print("\nSinh viên có ID = ", ID, " Đã bị xoá.")
                else:
                    print("\nSinh viên có ID = ", ID," Không tồn tại.")
            else:
                    print("\nDanh sách sinh viên trống!")
        elif (key == 4 ) :
                    if (qlsv.soLuongSinhVien ()> 0 ):
                        print("\n4:Tìm kiếm sinh viên theo tên: ")
                        print("\nNhập tên để tìm kiếm: ")
                        name = input ()
                        searchResult = qlsv.findByName(name) 
                        qlsv.showSinhVien(searchResult)
                    else:
                        print("\nDanh sách sinh viên trống!")
        elif (key == 5):                
                if (qlsv.soLuongSinhVien() > 0):
                        print("\n5: Sắp xếp sinh viên theo điểm trung bình (GPA).")
                        qlsv.sortByDiemTB ()
                        qlsv.showSinhVien(qlsv.getListSinhVien ())
                else:
                        print("\nDanh sách sinh viên trống!")
        elif (key == 6 ):
                    if (qlsv.soLuongSinhVien () > 0):
                        print("\n6: Sap xep sinh vien theo ten:")
                        qlsv.sortByName ()
                        qlsv.showSinhVien (qlsv.getListSinhVien())
                    else:
                        print("\nDanh sách sinh viên trống!!")
        elif (key == 7 ) :
                    if (qlsv.soLuongSinhVien() > 0):
                        print("\n7: Hien thi danh sach sinh vien.")
                        qlsv.showSinhVien(qlsv.getListSinhVien())
                    else:
                        print("\nDanh sách sinh viên trống!")
        elif (key == 0 ) :
                print("\nBạn đã chọn thoát chương trình!")
                break
        else:
                print("\nKhông có chức năng này!")
                print("\nHãy chọn chức năng trong MENU!")
                    
            
                
    