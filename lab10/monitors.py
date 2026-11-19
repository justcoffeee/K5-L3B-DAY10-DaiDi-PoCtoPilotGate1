"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def llm_fallback_rate(trials):
    """Tỉ lệ ticket mà trợ lý phải chạy tiếp khi LLM không trả lời (sự kiện llm_fallback).
    Không cần nhãn: tăng vọt nghĩa là nhà cung cấp LLM đang nghẽn, quyết định đang dựa vào đường dự phòng."""
    return sum(any(e.get("type") == "llm_fallback" for e in t["events"]) for t in trials) / max(1, len(trials))


def peak_hour_review_load(trials):
    """Số ca vào hàng chờ người duyệt trong giờ đông nhất (theo arrive_min), lấy mức cao nhất qua các ngày/seed.
    So với công suất một người duyệt (6 ca/giờ) để biết lúc nào phải gọi thêm người."""
    buckets = {}
    for t in trials:
        if t.get("review_kind") and t.get("arrive_min") is not None:
            key = (t.get("seed"), t.get("day"), int(t["arrive_min"]) // 60)
            buckets[key] = buckets.get(key, 0) + 1
    return max(buckets.values(), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "llm_fallback_rate": llm_fallback_rate,
    "peak_hour_review_load": peak_hour_review_load,
}
STARTER_MONITORS = ("escalation_rate",)
