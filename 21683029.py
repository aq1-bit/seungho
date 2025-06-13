import streamlit as st
import streamlit.components.v1 as components

profile_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <title>조승호 프로필</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #fafafa;
      margin: 0;
      padding: 0;
    }

    .page {
      max-width: 800px;
      margin: 50px auto;
      padding: 40px;
      background-color: #ffffff;
      border-radius: 10px;
      box-shadow: 0 0 12px rgba(0, 0, 0, 0.08);
      page-break-after: always;
    }

    .header {
      text-align: center;
      margin-bottom: 30px;
    }

    .header img {
      width: 140px;
      height: 140px;
      border-radius: 50%;
      border: 3px solid #d32f2f;
      object-fit: cover;
    }

    h1 {
      font-size: 28px;
      margin: 10px 0 5px;
      color: #d32f2f;
    }

    .subinfo {
      font-size: 16px;
      color: #555;
    }

    .section-title {
      font-size: 20px;
      color: #d32f2f;
      border-bottom: 2px solid #f8bbd0;
      margin-bottom: 20px;
      padding-bottom: 5px;
    }

    p, li {
      font-size: 16px;
      line-height: 1.8;
      color: #333;
    }

    ul {
      padding-left: 20px;
    }

    .info-list p {
      margin: 6px 0;
    }

    .tag-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
    }

    .tag {
      background-color: #fce4ec;
      color: #d32f2f;
      padding: 5px 12px;
      border-radius: 15px;
      font-size: 14px;
    }

    .contact-info {
      font-size: 16px;
      margin-top: 15px;
    }
  </style>
</head>
<body>

<!-- PAGE 1: 기본 정보 -->
<div class="page">
  <div class="header">
  <h1>조승호</h1>
    <p class="subinfo">건양대학교 재난안전소방학과 | 3학년</p>
  </div>
  <h2 class="section-title">👤 기본 정보</h2>
  <div class="info-list">
    <p><strong>🎂 생년월일:</strong> 2002.08.28</p>
  <p><strong>👨 성별:</strong> 남자</p>
 <p><strong>🏠 거주지:</strong> 대전 광역시</p>
    <p><strong>📌 간단한 인사:</strong> 안녕하세요, 재난안전소방학과 재학중인 21학번 조승호입니다.</p>
  </div>
</div>

<!-- PAGE 2: 학력 -->
<div class="page">
  <h2 class="section-title">🎓 학력</h2>
  <p><strong>건양대학교 재난안전소방학과</strong> (2021.03 ~ 현재)</p>
  <p>재난 대응에 필요한 이론과 실무를 균형 있게 배우며 소방 분야 전문가로 성장하고 있습니다.</p>
  <p><strong>주요 수강 과목:</strong></p>
  <div class="tag-list">
    <span class="tag">소방경보시스템</span>
    <span class="tag">화재조사론</span>
    <span class="tag">구급 및 응급처치</span>
    <span class="tag">방재영상처리</span>
    <span class="tag">캡스톤 디자인</span>
  </div>
</div>

<!-- PAGE 3: 취미 및 롤모델 -->
<div class="page">
  <h2 class="section-title">📂 취미 및 롤모델 </h2>
  <ul>
   <li><strong>취미:</strong> 헬스, 축구, 큐브</li> 
   <li><strong>롤모델:</strong> 손흥민</li>
  </ul>
</div>

<!-- PAGE 4: 자격증 및 수상 --> 
<div class="page">
  <h2 class="section-title">📜 자격증 및 수상</h2>
  <ul>
    <li>위험물산업기사 (보유)</li>
    <li>토익 스피킹 (준비중)</li>
    <li>컴활 1급 (준비 중)</li>
    <li>소방전기,기계 (준비중)</li>
  </ul>
</div>

<!-- PAGE 5: 연락처 -->
<div class="page">
  <h2 class="section-title">📞 연락처 & 기타</h2>
  <div class="contact-info">
    <p><strong>📧 이메일:</strong> jsh21901838@GMAIL.COM</p>
    <p><strong>📱 전화번호:</strong> 010-2990-2190</p>
  </div>
  <h2 class="section-title">✨ 한 줄 소개</h2>
  <p>긍정적인 사고를 갖자 입니다다.</p>
</div>

</body>
</html>
"""

# Streamlit에서 렌더링
components.html(profile_html, height=3200, scrolling=True)

