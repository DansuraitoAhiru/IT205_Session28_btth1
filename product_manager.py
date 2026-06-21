from tabulate import tabulate
from product import Product


class  ProductManager:
    def __init__(self):
        self.products = [
            Product("SP001", "Laptop Dell", 15000000, 3, 2000000),
            Product("SP002", "Chuột Logitech", 350000, 20, 500000),
            Product("SP003", "Bàn phím cơ AKKO", 1200000, 10, 1000000),
            Product("SP004", "Màn hình Samsung", 4500000, 5, 0),
            Product("SP005", "Tai nghe Sony", 2500000, 1, 0)
        ]

    def check_space(self, message):
        while True:
            info = input(message).strip()

            if info == "":
                print("Không được để rỗng")
                continue
            return info


    def find_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def input_positive_number(self, message):
        while True:
            try:
                number = float(input(message).strip())

                if number < 0:
                    print("Giá trị phải lớn hơn hoặc bằng 0")
                    continue
                return number

            except ValueError:
                print("Vui lòng nhập số")

    def input_quantity(self, message):
        while True:
            try:
                number = int(input(message).strip())

                if number < 0 or number > 10000:
                    print("Số lượng đã bán phải là số nguyên từ 0 đến 10,000")
                    continue
                return number

            except ValueError:
                print("Vui lòng nhập số")

    def add_product(self):
        while True:
            new_id = self.check_space("Nhập mã sản phẩm mới: ").upper()

            if self.find_id(new_id):
                print("Mã sản phẩm đã tồn tại")
                continue
            break

        name = self.check_space("Nhập tên sản phẩm: ").title()
        price = self.input_positive_number("Nhập giá bán: ")
        quantity = self.input_quantity("Nhập số lượng đã bán: ")
        discount = self.input_positive_number("Nhập số tiền giảm giá: ")

        new_product = Product(new_id, name, price, quantity, discount)
        self.products.append(new_product)
        print(f"Đã sản phẩm mã {new_id} thành công")

    
    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm hiện đang rỗng!")
            return
        
        table = []
        for product in self.products:
            table.append([
                product.id,
                product.name,
                f"{product.price:,.0f}",
                product.quantity_sold,
                f"{product.discount:,.0f}",
                f"{product.total_revenue:,.0f} VND",
                product.revenue_type
            ])

        display = tabulate(table, 
                        headers= ["Mã SP", "Tên SP", "Giá bán", "Số lượng đã bán", "Giảm giá", "Tổng doanh thu", "Loại doanh thu"],
                        tablefmt= "github")
    
        print(display)

    def update_product(self):
        if not self.products:
            print("Danh sách sản phẩm hiện đang rỗng!")
            return
        
        update_id = self.check_space("Nhập mã sản phẩm cần cập nhật: ").upper()

        found = self.find_id(update_id)
        if not found:
            print("Không tìm thấy sản phẩm cần cập nhật!")
            return
        
        new_price = self.input_positive_number("Nhập giá bán mới: ")
        new_quantity = self.input_quantity("Nhập số lượng đã bán mới: ")
        new_discount = self.input_positive_number("Nhập số tiền giảm giá mới: ")

        found.price = new_price
        found.quantity_sold = new_quantity
        found.discount = new_discount
        found.calculate_revenue()
        found.classify_revenue()
        print(f"Cập nhật sản phẩm mã {update_id} thành công!")

    def delete_product(self):
        if not self.products:
            print("Danh sách sản phẩm hiện đang rỗng!")
            return
        
        delete_id = self.check_space("Nhập mã sản phẩm cần xóa: ").upper()

        found = self.find_id(delete_id)
        if not found:
            print("Không tìm thấy sản phẩm cần xóa!")
            return
        
        while True:
            is_confirmed = self.check_space(" Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ").upper()

            if is_confirmed == "Y":
                self.products.remove(found)
                print("Xóa sản phẩm thành công!")
                break
            elif is_confirmed == "N":
                print("Đã hủy thao tác xóa!")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập Y hoặc N!")


    def search_product(self):
        if not self.products:
            print("Danh sách sản phẩm hiện đang rỗng!")
            return
        
        keyword = self.check_space("Nhập tên sản phẩm muốn tìm: ").lower()

        results = []
        for product in self.products:
            if keyword in product.name.lower():
                results.append(product)

        if not results:
            print("Không tìm thấy sản phẩm phù hợp!")
            return

        table = []
        for product in results:
            table.append([
                product.id,
                product.name,
                f"{product.price:,.0f}",
                product.quantity_sold,
                f"{product.discount:,.0f}",
                f"{product.total_revenue:,.0f} VND",
                product.revenue_type
            ])

        display = tabulate(table, 
                        headers= ["Mã SP", "Tên SP", "Giá bán", "Số lượng đã bán", "Giảm giá", "Tổng doanh thu", "Loại doanh thu"],
                        tablefmt= "github")
    
        print(display)


    def statistics(self):
        if not self.products:
            print("Chưa có dữ liệu để thống kê!")
            return
        
        low = 0
        mid = 0
        good = 0
        high = 0

        for product in self.products:
            if product.revenue_type == "Thấp":
                low += 1
            elif product.revenue_type == "Trung bình":
                mid += 1
            elif product.revenue_type == "Khá":
                good += 1
            else:
                high += 1    
        table = [
            ["Thấp", low],
            ["Trung bình", mid],
            ["Khá", good],
            ["Cao", high]
        ]

        display = tabulate(table,
                           headers= ["Phân loại doanh thu", "Số lượng sản phẩm"],
                           tablefmt= "grid",
                           numalign="left")
        print(display)