import streamlit as st
from datetime import date, datetime

# ── 페이지 설정 ──────────────────────────────────────────────
st.set_page_config(
    page_title="My To-Do",
    page_icon="🌸",
    layout="wide",
)

# ── 커스텀 CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --brand:     #FFD3E7;
    --brand-mid: #FFB8D4;
    --brand-deep:#FF85B3;
    --brand-dark:#C7456A;
    --bg:        #FFF7FB;
    --surface:   #FFFFFF;
    --text:      #3D1A28;
    --muted:     #B08090;
    --radius:    18px;
    --shadow:    0 4px 24px rgba(199,69,106,0.08);
}

/* 전체 배경 */
.stApp { background: var(--bg); font-family: 'DM Sans', sans-serif; }
.block-container { padding: 2rem 3rem 4rem !important; max-width: 1100px !important; }

/* 헤더 */
h1 {
    font-family: 'DM Serif Display', serif !important;
    color: var(--text) !important;
    font-size: 2.8rem !important;
    line-height: 1.15 !important;
    margin-bottom: 0 !important;
}
h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: var(--text) !important;
}

/* 섹션 타이틀 */
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    color: var(--brand-dark);
    letter-spacing: 0.5px;
    margin: 0 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* 카드 */
.card {
    background: var(--surface);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 22px 26px;
    margin-bottom: 16px;
    border: 1.5px solid #FFE8F2;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.card:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(199,69,106,0.13); }

/* 할일 아이템 */
.todo-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 14px 18px;
    border-radius: 12px;
    background: #FFF7FB;
    margin-bottom: 8px;
    border: 1.5px solid #FFE8F2;
    transition: background 0.15s;
}
.todo-item.done { background: #F5F5F5; border-color: #E0E0E0; }
.todo-item .todo-text { font-size: 0.95rem; color: var(--text); line-height: 1.4; }
.todo-item .todo-text.done-text { text-decoration: line-through; color: var(--muted); }
.todo-item .meta { font-size: 0.75rem; color: var(--muted); margin-top: 3px; }

/* 배지 */
.badge {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.badge-high   { background: #FFD3E7; color: #C7456A; }
.badge-medium { background: #FFE8C6; color: #B06A00; }
.badge-low    { background: #D8F5E5; color: #1A7A45; }

/* 통계 박스 */
.stat-box {
    background: var(--surface);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    border: 1.5px solid #FFE8F2;
    padding: 20px 22px;
    text-align: center;
}
.stat-number {
    font-family: 'DM Serif Display', serif;
    font-size: 2.4rem;
    color: var(--brand-dark);
    line-height: 1;
}
.stat-label {
    font-size: 0.78rem;
    color: var(--muted);
    margin-top: 4px;
    font-weight: 500;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* 진행바 */
.progress-wrap { background: #FFE8F2; border-radius: 100px; height: 10px; margin-top: 8px; overflow: hidden; }
.progress-fill { background: linear-gradient(90deg, var(--brand-mid), var(--brand-deep)); border-radius: 100px; height: 100%; transition: width 0.4s ease; }

/* 입력 필드 */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stDateInput > div > div > input {
    border: 1.5px solid #FFD3E7 !important;
    border-radius: 10px !important;
    background: #FFF7FB !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus { border-color: var(--brand-deep) !important; box-shadow: 0 0 0 3px rgba(255,133,179,0.15) !important; }

/* 버튼 */
.stButton > button {
    background: linear-gradient(135deg, var(--brand-mid), var(--brand-deep)) !important;
    border: none !important;
    color: white !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    padding: 8px 20px !important;
    transition: opacity 0.2s, transform 0.15s !important;
    box-shadow: 0 2px 12px rgba(255,133,179,0.3) !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }

/* 체크박스 */
.stCheckbox > label { font-family: 'DM Sans', sans-serif !important; color: var(--text) !important; }

/* 구분선 */
hr { border-color: #FFE8F2 !important; }

/* 날짜 표시 */
.today-date {
    font-size: 0.85rem;
    color: var(--muted);
    font-style: italic;
    margin-top: -4px;
    margin-bottom: 20px;
}

/* 빈 상태 */
.empty-state {
    text-align: center;
    padding: 32px 16px;
    color: var(--muted);
    font-size: 0.9rem;
}
.empty-state .icon { font-size: 2.5rem; margin-bottom: 8px; }

/* expander */
.streamlit-expanderHeader {
    background: #FFF7FB !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1.5px solid #FFE8F2 !important;
}
section[data-testid="stSidebar"] .stMarkdown { color: var(--text) !important; }
</style>
""", unsafe_allow_html=True)

# ── 세션 상태 초기화 ─────────────────────────────────────────
if "todos" not in st.session_state:
    st.session_state.todos = [
        {"id": 1, "task": "프로젝트 기획서 작성", "priority": "높음", "category": "업무", "due": "2026-03-15", "done": False, "created": "2026-03-10"},
        {"id": 2, "task": "팀 미팅 자료 준비",   "priority": "높음", "category": "업무", "due": "2026-03-12", "done": False, "created": "2026-03-10"},
        {"id": 3, "task": "독서 — 원씽 2장",      "priority": "낮음", "category": "개인", "due": "2026-03-20", "done": True,  "created": "2026-03-09"},
        {"id": 4, "task": "운동 루틴 정리하기",   "priority": "중간", "category": "건강", "due": "2026-03-14", "done": False, "created": "2026-03-09"},
        {"id": 5, "task": "장보기 목록 만들기",   "priority": "낮음", "category": "개인", "due": "2026-03-11", "done": True,  "created": "2026-03-08"},
    ]
if "next_id" not in st.session_state:
    st.session_state.next_id = 6

PRIORITY_MAP = {"높음": "badge-high", "중간": "badge-medium", "낮음": "badge-low"}
PRIORITY_EMOJI = {"높음": "🔴", "중간": "🟡", "낮음": "🟢"}
CATEGORIES = ["업무", "개인", "건강", "학습", "기타"]

# ── 헤더 ────────────────────────────────────────────────────
st.markdown("# 🌸 My To-Do")
st.markdown(f'<div class="today-date">{datetime.now().strftime("%Y년 %m월 %d일 %A")}</div>', unsafe_allow_html=True)

# ── 통계 ────────────────────────────────────────────────────
todos = st.session_state.todos
total   = len(todos)
done    = sum(1 for t in todos if t["done"])
pending = total - done
high_prio = sum(1 for t in todos if not t["done"] and t["priority"] == "높음")
pct = int((done / total * 100) if total else 0)

c1, c2, c3, c4 = st.columns(4)
for col, num, label, icon in [
    (c1, total,     "전체 할일",   "📋"),
    (c2, pending,   "남은 할일",   "⏳"),
    (c3, done,      "완료",        "✅"),
    (c4, high_prio, "긴급",        "🔴"),
]:
    with col:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{num}</div>
            <div class="stat-label">{icon} {label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("")
st.markdown(f"""
<div style="background:white;border-radius:14px;padding:16px 22px;border:1.5px solid #FFE8F2;box-shadow:0 4px 24px rgba(199,69,106,0.08);margin-bottom:8px;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
        <span style="font-family:'DM Serif Display',serif;color:#3D1A28;font-size:1rem;">오늘의 달성률</span>
        <span style="font-weight:700;color:#C7456A;font-size:1.1rem;">{pct}%</span>
    </div>
    <div class="progress-wrap"><div class="progress-fill" style="width:{pct}%"></div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── 레이아웃: 왼쪽(할일 목록) + 오른쪽(추가 폼) ────────────
left, right = st.columns([2, 1], gap="large")

# ── 오른쪽: 새 할일 추가 ─────────────────────────────────────
with right:
    st.markdown('<div class="section-title">✏️ 새 할일 추가</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        new_task     = st.text_input("할일 내용", placeholder="무엇을 해야 하나요?")
        new_priority = st.selectbox("우선순위", ["높음", "중간", "낮음"])
        new_category = st.selectbox("카테고리", CATEGORIES)
        new_due      = st.date_input("마감일", value=date.today())

        if st.button("➕ 추가하기", use_container_width=True):
            if new_task.strip():
                st.session_state.todos.append({
                    "id":       st.session_state.next_id,
                    "task":     new_task.strip(),
                    "priority": new_priority,
                    "category": new_category,
                    "due":      str(new_due),
                    "done":     False,
                    "created":  str(date.today()),
                })
                st.session_state.next_id += 1
                st.success("할일이 추가됐어요! 🌸")
                st.rerun()
            else:
                st.warning("내용을 입력해 주세요.")
        st.markdown('</div>', unsafe_allow_html=True)

    # 카테고리 필터
    st.markdown('<div class="section-title" style="margin-top:20px;">🗂️ 필터</div>', unsafe_allow_html=True)
    filter_cat  = st.multiselect("카테고리", CATEGORIES, default=CATEGORIES)
    filter_prio = st.multiselect("우선순위", ["높음", "중간", "낮음"], default=["높음", "중간", "낮음"])
    show_done   = st.checkbox("완료된 항목 보기", value=True)

# ── 왼쪽: 할일 목록 ─────────────────────────────────────────
with left:
    # 필터 적용
    filtered = [
        t for t in st.session_state.todos
        if t["category"] in filter_cat
        and t["priority"] in filter_prio
        and (show_done or not t["done"])
    ]
    # 정렬: 미완료 먼저, 우선순위 순
    prio_order = {"높음": 0, "중간": 1, "낮음": 2}
    filtered.sort(key=lambda t: (t["done"], prio_order[t["priority"]], t["due"]))

    # ── 미완료 ──
    st.markdown('<div class="section-title">⏳ 진행 중</div>', unsafe_allow_html=True)
    pending_list = [t for t in filtered if not t["done"]]
    if not pending_list:
        st.markdown('<div class="empty-state"><div class="icon">🎉</div>모든 할일을 완료했어요!</div>', unsafe_allow_html=True)
    for t in pending_list:
        badge_cls = PRIORITY_MAP[t["priority"]]
        col_check, col_content, col_del = st.columns([0.5, 5, 0.5])
        with col_check:
            if st.checkbox("", key=f"chk_{t['id']}"):
                t["done"] = True
                st.rerun()
        with col_content:
            st.markdown(f"""
            <div class="todo-item">
                <div style="flex:1">
                    <div class="todo-text">{t['task']}</div>
                    <div class="meta">
                        <span class="badge {badge_cls}">{PRIORITY_EMOJI[t['priority']]} {t['priority']}</span>
                        &nbsp;{t['category']}&nbsp;·&nbsp;📅 {t['due']}
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)
        with col_del:
            if st.button("🗑", key=f"del_{t['id']}"):
                st.session_state.todos = [x for x in st.session_state.todos if x["id"] != t["id"]]
                st.rerun()

    # ── 완료 ──
    if show_done:
        done_list = [t for t in filtered if t["done"]]
        if done_list:
            st.markdown('<div class="section-title" style="margin-top:24px;">✅ 완료됨</div>', unsafe_allow_html=True)
            for t in done_list:
                col_check, col_content, col_del = st.columns([0.5, 5, 0.5])
                with col_check:
                    if st.checkbox("", value=True, key=f"chk_{t['id']}"):
                        pass
                    else:
                        t["done"] = False
                        st.rerun()
                with col_content:
                    st.markdown(f"""
                    <div class="todo-item done">
                        <div style="flex:1">
                            <div class="todo-text done-text">{t['task']}</div>
                            <div class="meta">{t['category']} · {t['due']}</div>
                        </div>
                    </div>""", unsafe_allow_html=True)
                with col_del:
                    if st.button("🗑", key=f"del_{t['id']}"):
                        st.session_state.todos = [x for x in st.session_state.todos if x["id"] != t["id"]]
                        st.rerun()

    # ── 전체 삭제 ──
    if done and st.button("🧹 완료 항목 전체 삭제", use_container_width=True):
        st.session_state.todos = [t for t in st.session_state.todos if not t["done"]]
        st.rerun()