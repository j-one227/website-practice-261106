import streamlit as st

st.set_page_config(page_title="나를 소개합니다", page_icon=":seedling:", layout="wide")

NAME = "김재원"
INTRO = "좋아하는 것을 깊이 들여다보고, 새로운 경험을 기록하며 나만의 방향을 찾아갑니다."
AFFILIATION = "소속 또는 학교를 입력하세요"
DREAM = "나의 꿈을 한 문장으로 적어보세요."
HOMETOWN = "나의 고향을 입력하세요"
HERO_IMAGE_URL = (
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e"
    "?auto=format&fit=crop&w=1400&q=85"
)
TRIPS = [
    ("여행지 이름", "도시 · 국가 · 방문 연도", "여행에서 오래 기억하고 싶은 장면을 적어보세요."),
    ("여행지 이름", "도시 · 국가 · 방문 연도", "그곳에서 만난 풍경이나 사람을 기록해 보세요."),
    ("여행지 이름", "도시 · 국가 · 방문 연도", "다시 가고 싶은 이유를 짧게 남겨보세요."),
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');

    :root {
        --paper: #F5F2EA;
        --ink: #203A35;
        --moss: #788B7A;
        --clay: #B76E50;
        --stone: #D8D1C2;
    }
    .stApp {
        background: radial-gradient(ellipse at 85% 0%, rgba(120, 139, 122, 0.13), transparent 30%), var(--paper);
        color: var(--ink);
        font-family: 'Noto Sans KR', sans-serif;
    }
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(ellipse at 85% 0%, rgba(120, 139, 122, 0.13), transparent 30%), var(--paper);
    }
    [data-testid="stHeader"] {
        background: var(--paper);
    }
    [data-testid="stMain"] {
        background: transparent;
    }
    .block-container {
        max-width: 1120px;
        padding: 2rem 2.5rem 4rem;
    }
    h1, h2, h3, p, a, span, div { font-family: 'Noto Sans KR', sans-serif; }
    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--stone);
        padding: 0.5rem 0 1.1rem;
        margin-bottom: 3.2rem;
        color: var(--ink);
        font-size: 0.78rem;
        letter-spacing: 0.08em;
    }
    .topbar .mark { font-weight: 700; }
    .topbar nav { display: flex; gap: 1.6rem; }
    .topbar a { color: var(--ink); text-decoration: none; }
    .topbar a:hover { color: var(--clay); }
    .hero-kicker, .section-kicker, .fact-label {
        color: var(--clay);
        font-size: 0.76rem;
        font-weight: 600;
        letter-spacing: 0.12em;
    }
    .hero-title {
        color: var(--ink);
        font-family: 'Gowun Batang', serif;
        font-size: 3.6rem;
        font-weight: 700;
        line-height: 1.28;
        margin: 1rem 0 1.25rem;
        word-break: keep-all;
    }
    .hero-title span { color: var(--clay); font-family: 'Gowun Batang', serif; }
    .hero-copy {
        color: var(--ink);
        font-size: 1.02rem;
        line-height: 1.9;
        max-width: 32rem;
        word-break: keep-all;
    }
    .hero-affiliation { color: var(--moss); font-size: 0.9rem; margin-top: 1.6rem; }
    .stImage img { aspect-ratio: 4 / 5; object-fit: cover; border-radius: 3px; }
    .stImage figcaption { color: var(--moss); font-size: 0.78rem; }
    .section-heading {
        border-top: 1px solid var(--stone);
        padding-top: 1rem;
        margin: 5rem 0 2rem;
    }
    .section-heading .section-kicker { margin-bottom: 0.4rem; }
    .section-title {
        color: var(--ink);
        font-family: 'Gowun Batang', serif;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    .section-note { color: var(--moss); font-size: 0.9rem; margin-top: 0.5rem; }
    .about-copy {
        color: var(--ink);
        font-family: 'Gowun Batang', serif;
        font-size: 1.35rem;
        line-height: 1.9;
        word-break: keep-all;
    }
    .fact {
        border-bottom: 1px solid var(--stone);
        padding: 0.9rem 0 1.1rem;
    }
    .fact-value { color: var(--ink); font-size: 1.05rem; margin-top: 0.4rem; }
    .dream-band {
        background: var(--ink);
        color: var(--paper);
        margin-top: 2rem;
        padding: 2.3rem 2.5rem;
    }
    .dream-band .fact-label { color: var(--stone); }
    .dream-text {
        color: var(--paper);
        font-family: 'Gowun Batang', serif;
        font-size: 1.65rem;
        line-height: 1.65;
        margin: 0.7rem 0 0;
        word-break: keep-all;
    }
    .trip-row {
        display: grid;
        grid-template-columns: 3.5rem minmax(10rem, 0.8fr) 1.2fr;
        gap: 1rem;
        align-items: start;
        border-bottom: 1px solid var(--stone);
        padding: 1.35rem 0;
    }
    .trip-number { color: var(--clay); font-size: 0.82rem; padding-top: 0.2rem; }
    .trip-name { color: var(--ink); font-family: 'Gowun Batang', serif; font-size: 1.2rem; }
    .trip-meta { color: var(--moss); font-size: 0.78rem; margin-top: 0.3rem; }
    .trip-note { color: var(--ink); font-size: 0.9rem; line-height: 1.7; }
    .footer {
        border-top: 1px solid var(--stone);
        color: var(--moss);
        font-size: 0.78rem;
        margin-top: 5rem;
        padding-top: 1.1rem;
    }
    @keyframes arrive {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .topbar, .hero-kicker, .hero-title, .hero-copy, .section-heading { animation: arrive 650ms ease-out both; }
    @media (max-width: 700px) {
        .block-container { padding: 1.2rem 1.1rem 3rem; }
        .topbar { margin-bottom: 2rem; }
        .topbar nav { gap: 0.7rem; font-size: 0.68rem; }
        .hero-title { font-size: 2.65rem; }
        .section-heading { margin-top: 3.5rem; }
        .trip-row { grid-template-columns: 2rem 1fr; gap: 0.65rem; }
        .trip-note { grid-column: 2; }
        .dream-band { padding: 1.7rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
        <span class="mark">PROFILE / 01</span>
        <nav>
            <a href="#about">소개</a>
            <a href="#dream">꿈</a>
            <a href="#travel">여행</a>
        </nav>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_text, hero_photo = st.columns([1.15, 0.85], gap="large", vertical_alignment="center")
with hero_text:
    st.markdown(
        f"""
        <p class="hero-kicker">안녕하세요, 반갑습니다</p>
        <h1 class="hero-title">저는 {NAME}<span>입니다.</span></h1>
        <p class="hero-copy">{INTRO}</p>
        <p class="hero-affiliation">{AFFILIATION}</p>
        """,
        unsafe_allow_html=True,
    )
with hero_photo:
    st.image(HERO_IMAGE_URL, caption="여행의 한 장면", use_container_width=True)

st.markdown(
    """
    <div class="section-heading" id="about">
        <p class="section-kicker">01 / ABOUT</p>
        <h2 class="section-title">나를 소개합니다</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

about, details = st.columns([1.1, 0.9], gap="large")
with about:
    st.markdown(f'<p class="about-copy">{INTRO}</p>', unsafe_allow_html=True)
with details:
    st.markdown(
        f"""
        <div class="fact">
            <div class="fact-label">소속</div>
            <div class="fact-value">{AFFILIATION}</div>
        </div>
        <div class="fact">
            <div class="fact-label">고향</div>
            <div class="fact-value">{HOMETOWN}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <div class="dream-band" id="dream">
        <div class="fact-label">02 / MY DREAM</div>
        <p class="dream-text">{DREAM}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-heading" id="travel">
        <p class="section-kicker">03 / JOURNEY</p>
        <h2 class="section-title">기억에 남는 여행</h2>
        <p class="section-note">마음에 남은 장소와 그곳의 이야기를 모았습니다.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

for index, (place, details, note) in enumerate(TRIPS, start=1):
    st.markdown(
        f"""
        <div class="trip-row">
            <div class="trip-number">{index:02}</div>
            <div>
                <div class="trip-name">{place}</div>
                <div class="trip-meta">{details}</div>
            </div>
            <div class="trip-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="footer">나의 기록 · 이름과 내용을 자유롭게 바꾸어 보세요.</div>', unsafe_allow_html=True)
