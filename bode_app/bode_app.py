import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

st.title("伝達関数のボード線図表示アプリ")

st.markdown("""
### 伝達関数の係数を入力してください
例: 分子 = 1, 分母 = 1, 2, 1 は \( \frac{1}{s^2 + 2s + 1} \) に対応します。
""")

# 入力フォーム
num_input = st.text_input("分子係数（カンマ区切り）", "1")
den_input = st.text_input("分母係数（カンマ区切り）", "1, 2, 1")

# 実行ボタン
if st.button("描画する"):

    try:
        num = [float(x.strip()) for x in num_input.split(",")]
        den = [float(x.strip()) for x in den_input.split(",")]

        # 伝達関数作成
        P = ctrl.tf(num, den)

        # 周波数軸（0.1〜100 rad/s）
        w = np.logspace(-1, 2, 500)

        # Bode応答
        mag, phase, omega = ctrl.bode(P, w, dB=True, deg=True, plot=False)

        # プロット
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

        ax1.semilogx(omega, 20 * np.log10(mag))
        ax1.set_ylabel("Gain [dB]")
        ax1.grid(True, which="both")

        ax2.semilogx(omega, phase)
        ax2.set_ylabel("Phase [deg]")
        ax2.set_xlabel("Frequency [rad/s]")
        ax2.grid(True, which="both")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
