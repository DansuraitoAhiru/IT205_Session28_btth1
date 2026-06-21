from product_manager import ProductManager


def main():
    manager = ProductManager()

    while True:
        choice = input('''
================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
Nhập lựa chọn của bạn: ''').strip()
        
        match choice:
            case "1":
                manager.show_all()

            case "2":
                manager.add_product()

            case "3":
                manager.update_product()

            case "4":
                manager.delete_product()

            case "5":
                manager.search_product()

            case "6":
                manager.statistics()

            case "7":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập 1-7!")

if __name__ == "__main__":
    main()