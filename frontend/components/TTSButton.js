"use client";

export default function TTSButton({ text }) {
  const speak = () => {
    if (!text) return;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1;
    utterance.pitch = 1;
    window.speechSynthesis.speak(utterance);
  };

  return (
    <button
      onClick={speak}
      style={{
        marginTop: "15px",
        padding: "10px 20px",
        borderRadius: "10px",
        border: "none",
        backgroundColor: "#16a34a",
        color: "white",
        fontWeight: "bold",
        cursor: "pointer",
      }}
    >
      🔊 Listen
    </button>
  );
}