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
- Khai báo đầu vào trong hàm `input.py`. Bắt buộc phải có hàm `f`, điểm ban đầu `x0`, giá trị ban đầu `y0`
### Chạy chay bằng file `main.py`
