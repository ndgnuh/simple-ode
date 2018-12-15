# simple-ode
Các gói giải phương trình IVP và BVP (chủ yếu là IVP)

## Những gói chính
- Các phương pháp RK:
  - Euler (ẩn, hiện)
  - Hình thang
  - RK3, RK4 (hiện)
- Các phương pháp Adams - Bashforth (với s bất kì)


## Thư viện yêu cầu:
- Numpy (bản bất kì)
- Matplotlib (chỉ dùng cho việc vẽ đồ thị, nếu chỉ tính toán thì không cần)

## Cách sử dụng:
### Chạy bằng menu (chưa khả dụng)
- Khai báo đầu vào trong hàm `inputs.py`. Bắt buộc phải có hàm `f`, điểm ban đầu `x0`, giá trị ban đầu `y0`. Sau đó chạy chương trình.
### Chạy chay bằng file `main.py`
- Khai báo đầu vào, import các module tương ứng với các phương pháp trong thư mục `ode`. Muốn biết trong mỗi module này có những gói nhỏ nào thì mở file ra xem (xem mấy cái `def` ấy).
```python
from ode import euler, rk, ...vân vân
```
- Import 2 hàm là `implicit` và `explicit` từ `ode/schemes.py`, những hàm này dùng để chạy các module ở trên. 
- Để chạy phương pháp hiện dùng hàm `explicit`:
```python
[x,y] = explicit(f, x0, y0, x, stepnum, <Module giải pt>)
# y' = 1 - y, y(0) = 0, tìm y(5) với 10 bước nhảy, dùng rk4
f = lambda x,y: 1 - y
[x,y] = explicit(f, 0, 0, 5, 10, rk.erk4)
```
- Để chạy phương pháp ẩn dùng hàm `implicit`, ở đây dùng nguyên lý điểm bất động nên phương pháp ẩn sẽ tương đương với dự đoán hiệu chỉnh. Mặc định của module phương pháp hiện là RK4, mặc định số lần hiệu chỉnh là 50.
```python
[x,y] = implicit(f, x0, y0, x, stepnum, <Module pp ẩn>, [module pp hiện], [số lần hiệu chỉnh])
```
**Lưu ý**: Các module ở trên chỉ thực hiện tính toán chứ KHÔNG in kết quả. 
### In ra kết quả

- Import module `rprint` từ trong thư mục `misc`
- Chạy chương trình ra kết quả, gán vào 2 biến như ở trên.
```python
[x,y] = implicit(...)
```
- Dùng `result` của `rprint` để in ra kết quả
```python
rprint.result(x, y)
```

## Báo lỗi
Nếu tìm thấy lỗi thì tốt nhất báo trong mục issue của github, quăng lên messenger hay nói mồm thì vài ngày nó trôi mất. Với lại nếu là lỗi syntax khi khai báo do chưa biết dùng `python` thì đưa lên đây mọi người có thể đọc lại và học luôn.