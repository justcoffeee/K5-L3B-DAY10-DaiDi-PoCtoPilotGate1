# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): DaiDi
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-DaiDi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S4

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phạm Hoàng Huy | 2A202603836 | Kỹ sư cổng (vòng 2: sửa theo thẻ sự cố, `monitors.py`) · gom bài nộp | ✓ |
|   2 | Lê Thanh Tùng | 2A202603819 | Kỹ sư cổng (vòng 1: eval, trace, `guards.py`, câu 2.6–2.8) |             |
|   3 | Cấn Xuân Nghĩa | 2A202603805 | Sản phẩm và kinh doanh |             |
|   4 | Nguyễn Mạnh Hùng | 2A202603852 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## CanXuanNghia-2A202603805

### Phần việc phụ trách

Sản phẩm và kinh doanh; câu 2.3, Phiếu B mục B3: bản đồ dữ liệu và ví dụ drift chính sách REFUND-v3 → v4 từ 2026-12-01; câu 2.9, mục B7.4 và nhóm `business` trong `config/operating_gates.json`.

### Đóng góp cụ thể

Điền bản đồ nguồn dữ liệu, trường quyết định tiền/lỗi hãng, nguồn sự thật và điểm lệch; phân tích thay đổi hạn mức tự động và quy tắc FORCE_MAJEURE, chỉ số chịu ảnh hưởng và cách phát hiện đề xuất. Sau khi đồng bộ phần Hùng đã push, đặt bốn cổng kinh doanh và giải thích từng giá trị từ `ops_limits`/`ops_facts`; giữ nguyên `operations` và `legal` của Hùng. Có dùng Codex hỗ trợ đọc code/dữ liệu và soạn, soát câu chữ theo `RULES.md`. Không chạy eval; mọi lần chạy thực hiện trên máy Huy. Không sửa tiêu chí đã ký.

### Bằng chứng

`templates/form-b-evaluation-gates.md`, mục B3; căn cứ `data/world.json`, `lab10/agent.py`, `lab10/helpers.py` và `lab10/tools.py`. Đây là phân tích và đề xuất, không phải kết quả chạy mới.

## LeThanhTung-2A202603819

### Phần việc phụ trách

Kỹ sư cổng (vòng 1 & hỗ trợ vòng 2):
- Phiếu A: Câu 1.3 (thiết kế offline metric cho bước ghi lỗi hãng `file_carrier_fault`).
- Phiếu B: Mục B0 (dòng 1 baseline), B1 (Câu 2.1 - đọc phân tích report mốc base & khuyến nghị cổng kết hợp), B2 (Câu 2.2 - mổ xẻ lỗi chìm T-002@55 qua 3 phần), B7.1–B7.3 (Câu 2.6 cổng phòng ngừa trong `guards.py`, Câu 2.7 tránh rò rỉ dữ liệu, Câu 2.8 behavioral test).
- Codebase: Trực tiếp xây dựng các cổng phòng ngừa trong `lab10/guards.py` (`write_gate` cho `issue_refund`, `file_carrier_fault`, `notify_carrier`).
- Phiếu C (Thẻ S4): Mục C0 (nhật ký chạy vòng 2), C1 (mốc prepared và đối chiếu pre-mortem B6), C5 (Specification & Giả định môi trường), C6 (Fault tree TRƯỚC sửa), C9 (Fault tree SAU sửa và phân tích rủi ro mới về ROI).

### Đóng góp cụ thể

- Triển khai thành công 3 cổng bảo vệ code cứng trong `lab10/guards.py` đối chiếu nguồn sự thật Database và chính sách hiệu lực: chặn đứng hoàn sai tiền quỹ, triệt tiêu 100% rủi ro phạt oan hãng vận chuyển (loại bỏ lỗi do shop `MERCHANT_HANDOVER`), và làm sạch dữ liệu nhạy cảm PII (`customer_note`) gửi đối tác.
- Phân tích chi tiết trace $T\text{-}002@55$ chỉ ra bản chất lỗi chìm (Silent Error) do xung đột thứ bậc giữa `model_override` và DB nội bộ.
- Xây dựng 2 ca kiểm thử hành vi độc lập (Behavioral test ad-hoc) chứng minh tính bất biến của cổng phòng ngừa khi khách khai khống hoặc gửi thông tin cá nhân.
- Phân tích cây lỗi (Fault tree) 3 nhánh chuẩn xác cho sự cố thẻ S4 (đêm 11.11 ticket gấp ba, nghẽn LLM, hàng chờ vỡ SLA 60 phút) trước và sau sửa; chỉ ra trade-off phát sinh khi tăng người trực giúp hết ùn nhưng kéo giảm ROI ngày thường từ 1.34 xuống 0.72.
- Tuân thủ nghiêm ngặt nguyên tắc nhóm: Không chạy lệnh eval trên máy cá nhân (mọi lần chạy chuẩn hóa trên máy trưởng nhóm Huy), không sửa tiêu chí đã ký, phối hợp chặt chẽ với các thành viên.

### Bằng chứng

- Code cổng phòng ngừa: `lab10/guards.py`, `lab10/guards_round1.py`.
- Các commit trên GitHub: `0246edc`, `3890a0e`, `dd6452a`, `e9f6b1c`, `4d0bec7`, `c9f54e5`.
- Mã lần chạy trỏ tới: `R-base-before-20261119-143424-b45eeb` (base), `R-base-after-20261119-143751-a7034b`, `R-S4-before-20261119-170619-a42b10`, `R-S4-prepared-20261119-170619-a42b10`, `R-S4-after-20261119-171317-3de02d`.
- Các mục đã điền hoàn chỉnh: Phiếu A (A2), Phiếu B (B0, B1, B2, B7.1–B7.3), Phiếu C (C0, C1, C5, C6, C9).

### Exit ticket

- **Một điều học được:** Hiểu sâu sắc về cơ chế phòng thủ nhiều lớp (Defense in Depth) và tầm quan trọng sống còn của việc đặt cổng kiểm tra bằng code (Hard Gate) đối chiếu nguồn sự thật Database (Single Source of Truth) thay vì ngây thơ tin tưởng vào output hay prompt của LLM khi tích hợp vào quy trình tài chính - vận hành.
- **Một điều còn chưa chắc:** Cách thiết kế cơ chế co giãn linh hoạt (Dynamic auto-scaling) tối ưu nhất cho nhân sự trực ca duyệt thủ công giữa các khung giờ bình thường và giờ siêu sale cao điểm để vừa không bao giờ vỡ SLA 60 phút, vừa giữ vững trần hiệu quả kinh tế (ROI ≥ 1.0).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
