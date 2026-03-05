# Lập Trình Hướng Đối Tượng (OOP) trong Python

## Khái niệm cơ bản
- **Class (Lớp):** Bản thiết kế để tạo ra các đối tượng. Tập hợp các thuộc tính và phương thức đặc trưng.
- **Object (Đối tượng):** Một thực thể (instance) của một lớp, có các giá trị cụ thể cho các thuộc tính.

## 4 Nguyên lý cơ bản

### 1. Encapsulation (Tính đóng gói)
- Gom nhóm dữ liệu và các phương thức liên quan vào một lớp.
- Che giấu thông tin qua các mức độ truy cập:
    - `Public`: Truy cập từ bất cứ đâu.
    - `Protected` (`_name`): Nên dùng trong class và subclass.
    - `Private` (`__name`): Chỉ dùng trong nội bộ class (Python dùng name mangling).

### 2. Inheritance (Tính kế thừa)
- Cho phép xây dựng lớp mới dựa trên lớp cũ.
- **Đơn kế thừa:** Kế thừa từ một lớp cha.
- **Đa kế thừa:** Một lớp con có thể kế thừa từ nhiều lớp cha (`class Child(Parent1, Parent2)`).
- Sử dụng `super()` để gọi phương thức từ lớp cha.

### 3. Abstraction (Tính trừu tượng)
- Tổng quát hóa các phương thức mà không cần quan tâm đến cách thực hiện chi tiết.
- Trong Python: Sử dụng module `abc` (Abstract Base Classes) và decorator `@abstractmethod`.

### 4. Polymorphism (Tính đa hình)
- Một phương thức có thể thực hiện theo nhiều cách khác nhau tùy thuộc vào đối tượng gọi nó.

## Các kỹ thuật khác
- **Magic Methods (Dunder Methods):** Các phương thức bắt đầu và kết thúc bằng `__` (như `__init__`, `__str__`, `__len__`, `__add__`).
- **Class vs Instance Attributes:** Thuộc tính dùng chung cho cả lớp vs thuộc tính riêng của từng đối tượng.

## Files
- [README.md](file:///Volumes/WorkSpace/Project/PFP/Lý%20thuyết/10-OOP/README.md) - Tóm tắt lý thuyết
- [demo.ipynb](file:///Volumes/WorkSpace/Project/PFP/Lý%20thuyết/10-OOP/demo.ipynb) - Code demo chi tiết
