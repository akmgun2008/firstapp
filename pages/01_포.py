import streamlit as st

# 제목
st.title("포켓몬 소개: 피카츄")

# 이미지 (공식 이미지 링크 사용)
st.image(
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
    caption="피카츄",
    use_column_width=True
)

# 설명
st.write("""
피카츄는 전기 타입 포켓몬으로, 포켓몬 시리즈의 마스코트입니다.
귀엽고 노란색 몸에 번개 모양 꼬리가 특징이며,
볼에는 전기를 저장하여 적을 감전시키거나 전기를 방출할 수 있습니다.

- **타입:** 전기
- **진화:** 피츄 → 피카츄 → 라이츄
- **특징:** 귀엽고 친근한 외모 덕분에 세계적으로 가장 유명한 포켓몬입니다.
""")
